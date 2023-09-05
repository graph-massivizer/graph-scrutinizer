from multiprocessing import process
from pathlib import Path
from sys import executable
from typing import Optional
from redis import Redis
import json
import datetime
import subprocess

from inspect import getsourcefile

# TODO this seems rather hacky. There might be a better way to structure this code
sf: Optional[str] = getsourcefile(lambda:0) 
if sf is None:
    raise Exception("Could not determine executable location")
f = Path(sf).absolute()
directory = f.parent
executable = directory / "full_bisimulation"
assert executable.exists(), f"executable at {executable} not found"
executable_str = str(executable)

def consumer():
    redis_conn = Redis(host='localhost', port=6379)
    while True:
        processing_request = redis_conn.blpop('graph-summarization')[1].decode("utf-8")
        print("We just consumed: {}".format(processing_request))
        
        processing_request = json.loads(processing_request)
        # TODO: Now just from the file system, probably we need to encapsulate the file system and for sure make it more secure so only paths relative to a specific root are accessible.
        path = str(processing_request["graph_path"])
        #TODO these should come from the request
        k = int(processing_request["depth"])
        output = "output.txt"
        skip_singletons = bool(processing_request["skip_singletons"])
        support = int(processing_request["support"])
        # example command
        # full_bisimulation run_k_bisimulation_store_partition mappingbased-objects_lang\=en.ttl --k=3 --output=here.txt --skip_singletons --support=5

        command:list[str] = [executable_str, "run_k_bisimulation_store_partition", path, f"--k={k}", f"--output={output}", f"--support={support}"]
        
        if skip_singletons:
            command.append('--skip_singletons')
        subprocess.run(command , check=True, shell=False)

        print(type(processing_request['graph_processing_status_log']))
        processing_request['graph_processing_status_log']=processing_request['graph_processing_status_log']+[{'PROCESSING':str(datetime.datetime.now().isoformat())}]
        # TODO: persist into MongoDB
        print("We fired processing request and logged status: {}".format(processing_request))

if __name__ == '__main__':
    consumer()
