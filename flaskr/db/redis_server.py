import redis

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6380
REDIS_DB = 0


try:
    redis_server = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)
    redis_available = True
except redis.ConnectionError:
    redis_available = False