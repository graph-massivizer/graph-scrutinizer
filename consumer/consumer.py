from redis import Redis

def consumer():
    redis_conn = Redis(host='localhost', port=6379)
    while True:
        val = redis_conn.blpop('queue')
        print("We just consumed: {}".format(val))

if __name__ == '__main__':
    consumer()
