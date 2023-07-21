from redis import Redis
import json
import datetime

def consumer():
    redis_conn = Redis(host='localhost', port=6379)
    while True:
        processing_request = redis_conn.blpop('graph-summarization')[1].decode("utf-8")
        print("We just consumed: {}".format(processing_request))
        
        processing_request = json.loads(processing_request)
        # TODO: fire processing request
        print(type(processing_request['graph_processing_status_log']))
        processing_request['graph_processing_status_log']=processing_request['graph_processing_status_log']+[{'PROCESSING':str(datetime.datetime.now().isoformat())}]
        # TODO: persist into MongoDB
        print("We fired processing request and logged status: {}".format(processing_request))

if __name__ == '__main__':
    consumer()
