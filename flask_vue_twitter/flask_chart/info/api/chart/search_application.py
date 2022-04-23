from info import mongo_db
import pymongo
import json
from bson import ObjectId
from info import redis_store
import time
import datetime



class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


db0 = mongo_db['database']
db1 = mongo_db['twitter']
tweets = db0['tweets']
search = db0["search"]
origin = db1['origin']
origin_t = db1['origin_t']
origin_f = db1['origin_f']
quote = db1['quote']
quote_t = db1['quote_t']
quote_f = db1['quote_f']
retweet = db1['retweet']
retweet_t = db1['retweet_t']
retweet_f = db1['retweet_f']
quote_tagst = db1["quote_tagst"]
quote_tagsf = db1["quote_tagsf"]
origin_tagst = db1["origin_tagst"]
origin_tagsf = db1["origin_tagsf"]


def tags_search(tags):
    tags = tags.split("#")
    tags.remove(tags[0])
    tags = " ".join(tags)
    origin.searcht = origin_tagst.find({"$text": {"$search": tags}},  {'created_at':1,'id_str':1, 'user':{'name': 1}, 'text':1})
    origin.searchf=origin_tagsf.find({"$text": {"$search": tags}},  {'created_at':1,'id_str':1, 'user':{'name': 1}, 'text':1})
    quote.searcht=quote_tagst.find({"$text": {"$search": tags}},  {'created_at':1,'id_str':1, 'user':{'name': 1}, 'text':1})
    quote.searchf=quote_tagsf.find({"$text": {"$search": tags}},  {'created_at':1,'id_str':1, 'user':{'name': 1}, 'text':1})
    if (origin_tagst.count_documents({"$text": {"$search": tags}})>0):
        search.insert_many(origin.searcht)
    if (origin_tagsf.count_documents({"$text": {"$search": tags}})>0):
        search.insert_many(origin.searchf)
    if (quote_tagst.count_documents({"$text": {"$search": tags}})>0):
        search.insert_many(quote.searcht)
    if (quote_tagsf.count_documents({"$text": {"$search": tags}})>0):
        search.insert_many(quote.searchf)
    if (search.count_documents({})>0):
        cur = search.find().sort("created_at", pymongo.DESCENDING)
    else:
        cur = "Sorry, there are no such hashtags in our database"
    return cur

def fetch_by_hashtags(tags):
    results = tags_search(tags)
    print(results)
    if (type(results) == str):
        str0 = ''
        return str0
    else:
        lst_results = []
        for item in results:
            # item = JSONEncoder().encode(item)
            lst_results.append(str(item))
        make_str = ''.join(item for item in lst_results)
        redis_store.setex(tags, 25, make_str)
        return make_str

def get_by_hashtags(tags):
    if not tags:
        return 'no tags param'
    if (search.count_documents({}) > 0):
        search.drop()
    result = redis_store.get(tags)
    if not result:
        result = fetch_by_hashtags(tags)
    return result

## search by word
def words_search(words):
    origin_searcht=origin_t.find({"text": {"$regex": words}}, {'created_at':1,'id_str':1, 'user':{'name': 1}, 'text':1})
    origin_searchf=origin_f.find({"text": {"$regex": words}}, {'created_at':1,'id_str':1, 'user':{'name': 1}, 'text':1})
    quote_searcht=quote_t.find({"text": {"$regex": words}}, {'created_at':1,'id_str':1, 'user':{'name': 1}, 'text':1})
    quote_searchf=quote_f.find({"text": {"$regex": words}}, {'created_at':1,'id_str':1, 'user':{'name': 1}, 'text':1})
    if (origin_t.count_documents({"$text": {"$search": words}})>0):
        search.insert_many(origin_searcht)
    if (origin_f.count_documents({"$text": {"$search": words}})>0):
        search.insert_many(origin_searchf)
    if (quote_t.count_documents({"$text": {"$search": words}})>0):
        search.insert_many(quote_searcht)
    if (quote_f.count_documents({"$text": {"$search": words}})>0):
        search.insert_many(quote_searchf)
    if (search.count_documents({})>0):
        cur=search.find().sort("created_at", pymongo.DESCENDING)
    else:
        cur="Sorry, there are no such words in our database"
    return cur

def fetch_by_words(words):
    results = words_search(words)
    if (type(results) == str):
        str0 = ''
        return str0
    else:
        lst_results = []
        for item in results:
            # item = JSONEncoder().encode(item)
            lst_results.append(str(item))
        make_str = ''.join(item for item in lst_results)
        redis_store.setex(words, 60, make_str)
        return make_str

def get_by_words(words):
    if(search.count_documents({})>0):
        search.drop()
    result = redis_store.get(words)
    if not result:
        result = fetch_by_words(words)
    return result


def search_by_time(start, end):

    results = tweets.find({"timestamp": {"$gte": start, "$lte": end}}, {'created_at': 1, 'id_str': 1, 'user': {'name': 1}, 'text':1})
    if (tweets.count_documents({"timestamp": {"$gte": start, "$lte":end}})>0):
        pass
    else:
        results = "Out of time range"
    return results

def fetch_by_time(start, end):
    results = search_by_time(start, end)
    if(type(results)==str):
        str0 = ''
        return str0
    else:
        lst_results = []
        for item in results:
            # item = JSONEncoder().encode(item)
            lst_results.append(str(item))
        make_str = ''.join(item for item in lst_results)
        redis_store.setex(start, 60, make_str)
        return make_str


def get_by_time(start, end):
    if(search.count_documents({})>0):
        search.drop()
    start = time.mktime(datetime.datetime.strptime(start, "%m/%d/%Y").timetuple())
    end = time.mktime(datetime.datetime.strptime(end, "%m/%d/%Y").timetuple())
    result = redis_store.get(start)
    if not result:
        result = fetch_by_time(start, end)
    return result