# import redis
from redis import StrictRedis


class Config:
    DEBUG = None
    # set key
    SECRET_KEY = 'mMr88P+cvbxFXvcpX9PpiBTWMDLtGNkI7fwKhVv7GWuv9QZyRoyUsw=='

    # set connection with database
    # SQLALCHEMY_DATABASE_URI = 'mysql://python37_11:x864dxNPP2X4NnMk@149.129.106.112/python37_11'
    # SQLALCHEMY_DATABASE_URI = 'mysql://twitter:4H6JmFmcxFP4mLWp@121.4.48.74/twitter'
    SQLALCHEMY_DATABASE_URI = 'mysql://root@127.0.0.1/twitter'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
 
    # 配置状态保持session信息的存储
    SESSION_TYPE = 'redis'
    # 抽取redis的主机和端口
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # SESSION_REDIS = StrictRedis(host='149.129.106.112', port=6379)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400


# 定义开发环境的配置类
class DevelopmentConfig(Config):
    DEBUG = True


# 定义生产环境的配置类
class ProductionConfig(Config):
    DEBUG = False


# 实现不同环境下的配置类的字典映射
config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
