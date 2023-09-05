# GRAPH SCRUTINIZER - REST API

pip install fastapi redis uvicorn motor

## optional development dependency

pip install motor-types

## REST API backend execution
export PYTHONPATH=$PWD
python app/main.py

## Testing a request

    curl --request POST --header "Content-Type: application/json" --data '{"graph_path": "file:///input/graphs/use-case-graph.ttl", "depth":1, "support":0, "skip_singletons": false}'  http://0.0.0.0:8000/scrutinizer/requests/summarization


This returns JSON that looks something like

    {"data":[{"graph_processing_id":"82ee181c0f6028691786133d065e95d1"}],"code":200,"message":"Graph processing request registered!"}

Now, the graph_processing_id can be used to retrieve the status of the job (not working yet)

    curl --request GET http://0.0.0.0:8000/scrutinizer/requests/82ee181c0f6028691786133d065e95d1/status
