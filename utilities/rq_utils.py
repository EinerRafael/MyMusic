from rq import Queue
from redis import Redis
from mymusic.constants import *

redis_conn = Redis(host=REDIS_HOST, port=REDIS_PORT, db=1)