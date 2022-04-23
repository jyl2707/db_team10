import random

from flask import jsonify, request, current_app

from info import db
from info import redis_store
from info import mongo_db
from info import mongo_store
from info.models import Chart1, User
from info.utils.response_code import RET
from . import chart_print
import json
import time
from . import search_application

from sqlalchemy import func, and_

@chart_print.route('/chart', methods=['GET'])
def chart():
    if request.method == 'GET':
        text = request.args.get('text')
        hashtag = request.args.get('hashtag')
        if hashtag:
            hashtag = '#' + hashtag
        start_date = request.args.get('startDate')
        end_date = request.args.get('endDate')
        page_index = request.args.get('page') or 1
        page_size = request.args.get('size') or 10
        skip = int(page_size) * (int(page_index) - 1)
        if hashtag:
            res_data = search_application.get_by_hashtags(hashtag, skip, int(page_size))
        elif text:
            res_data = search_application.get_by_words(text)
        elif start_date and end_date:
            res_data = search_application.get_by_time(start_date, end_date)
        else:
            res_data = ''

        return jsonify(errno=RET.OK, errmsg='OK', data=res_data, counts=5000)

@chart_print.route('/chart', methods=['GET'])
def chart1():
    if request.method == 'GET':
        # redis ope
        redis_store.set('cache_data', '-')
        print('Redis data: ', redis_store.get('cache_data'))
        # mongo db ope: 
        twitter_info = mongo_db['twitter_info']
        twitter_info.insert_one({'text': 'twitter text', 'id': '1'})
        m_d = twitter_info.find_one({'id': '1'})
        print('Mongo db data:', m_d)


        text = request.args.get('text')
        tweet_id = request.args.get('id')
        start_date = request.args.get('startDate')
        end_date = request.args.get('endDate')
        page_index = request.args.get('page') or 1
        page_size = request.args.get('size') or 10

        # query = db.session.query(Chart1, User).outerjoin(User, Chart1.user_id == User.id).filter(
        #     Chart1.text.like('%' + (text if text else '') + '%'))
        # query = db.session.query(User).filter(User.id == user.id).filter(User.name == name)

        # if tweet_id:
        #     query = query.filter(Chart1.id == tweet_id)

        # if not start_date is None and not end_date is None:
        #     s_time_array = time.strptime(start_date, "%Y-%m-%d")
        #     s_time_stamp = int(time.mktime(s_time_array)) * 1000
        #     e_time_array = time.strptime(end_date, "%Y-%m-%d")
        #     e_time_stamp = int(time.mktime(e_time_array)) * 1000
        #     query = query.filter(Chart1.timestamp_ms > s_time_stamp).filter(Chart1.timestamp_ms < e_time_stamp)

        # counts = query.count()
        # charts = query.paginate(int(page_index), int(page_size), False)
        # list = [dict(zip(result.keys(), result)) for result in charts.items]
        # _l = []
        # for i in list:
        #     _d = i.get('Chart1').to_dict()
        #     if i.get('User'):
        #         _d['user'] = i.get('User').to_dict()
        #     _l.append(_d)
        # res_data = dict(charts=_l)

        # TODO: 1. 数据改为从mongodb查询, 分页(可选项)
        # return jsonify(errno=RET.OK, errmsg='OK', data=res_data, counts=counts)

    # TODO: 2. 增加新接口用户列表，用户查询接口

    # i


