# from datetime import datetime
# from elasticsearch import Elasticsearch
# es = Elasticsearch()

# doc = {
#     'author': 'limei',
#     'text': 'i can do this always in elvation time',
#     'timestamp': datetime.now(),
# }
# res = es.index(index="tweet_25", doc_type='tweet', id=1, body=doc)
# #print(res['created'])
# es.indices.refresh(index="tweet_25")

# for i in range(1,1000000):
#   res = es.get(index="tweet_1", doc_type='tweet')
#   print res

#es.indices.refresh(index="test-index")


# res1 = es.search(index="test-index", body={"query": {"match_phrase": {'text':'i can do this always in elvation time'}}})

#print res
# print res1
# print("Got %d Hits:" % res['hits']['total'])
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])



# es.put_template(id=1,body={
#     "template": "tweets_*",
#     "mappings": {
#         "tweet": {
#             "dynamic_templates": [
#                 {
#                     "notanalyzed": {
#                         "match": "*",
#                         "match_mapping_type": "string",
#                         "mapping": {
#                             "type": "string",
#                             "index": "not_analyzed"
#                         }
#                     }
#                 }
#             ],
#             "properties": {
#                 "timestamp": {
#                  "type": "date",
#                  "format": "strict_date_optional_time||epoch_millis"
#                 },
#                 "user": {
#                     "type": "string"
#                 },
#                 "message": {
#                     "type": "string",
#                     "fields": {
#                         "raw": {
#                             "type": "string",
#                             "index": "not_analyzed"
#                         }
#                     }
#                 }
#             }
#         }
#     }
# })


import redis

class RedisQueue(object):
    """Simple Queue with Redis Backend"""
    def __init__(self, name, namespace='queue', **redis_kwargs):
        """The default connection parameters are: host='localhost', port=6379, db=0"""
        self.__db= redis.Redis(**redis_kwargs)
        self.key = '%s:%s' %(namespace, name)

    def qsize(self):
        """Return the approximate size of the queue."""
        return self.__db.llen(self.key)

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.qsize() == 0

    def put(self, item):
        """Put item into the queue."""
        self.__db.rpush(self.key, item)

    def get(self, block=True, timeout=None):
        """Remove and return an item from the queue.

        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)
        else:
            item = self.__db.lpop(self.key)

        if isinstance(item,tuple):
            item = item[1]
        return item

    def get_nowait(self):
        """Equivalent to get(False)."""
        return self.get(False)

#from RedisQueue import RedisQueue
# q=RedisQueue('te')

# print q.get()






