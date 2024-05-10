from multiprocessing import process
from pathlib import Path
from sys import executable
from typing import Optional
from redis import Redis
import json
import datetime
import subprocess
from rdflib import Graph
import networkx as nx

def consumer():
    redis_conn = Redis(host='localhost', port=6379)
    while True:
        processing_request = redis_conn.blpop('graph-betweenness-centrality')[1].decode("utf-8")
        print("We just consumed: {}".format(processing_request))

        processing_request = json.loads(processing_request)
        # TODO: Now just from the file system, probably we need to encapsulate the file system and for sure make it more secure so only paths relative to a specific root are accessible.
        path = str(processing_request["graph_path"])

        # TODO: we agree to build a library of converters
        # TODO START: This conversion from turtle to a processable graph interface should be handled by Inceptor?
        g = Graph()
        g.parse(path)
        G = nx.Graph()
        for s, p, o in g:
            G.add_edge(str(s), str(o))
        # TODO END: This conversion from turtle to a processable graph interface should be handled by Inceptor?

        print(type(processing_request['graph_processing_status_log']))
        processing_request['graph_processing_status_log'] = processing_request['graph_processing_status_log'] + [
            {'PROCESSING': str(datetime.datetime.now().isoformat())}]
        centrality = nx.betweenness_centrality(G, normalized=True, endpoints=True, seed=0)
        most_cited = sorted([(k, v) for k, v in centrality.items()], key=lambda x: x[1], reverse=True)[0][0]
        # hardware config, how much it took, energy consumption?, ...
        # make this data collection generic by doing it through decorators

        print("TODO: We found most cited work: {}".format(most_cited))
        print("TODO: we need to persist somewhere!")
        # TODO: persist into MongoDB
        print("We fired processing request and logged status: {}".format(processing_request))


if __name__ == '__main__':
    consumer()
