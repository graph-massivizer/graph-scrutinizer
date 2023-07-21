from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, File, UploadFile, Form
from fastapi import APIRouter, Body
from typing import Union
import hashlib
import json
from redis import Redis

from app.server.models.service_model import (
    GraphProcessingRequest,
    GraphProcessingTask,
    GraphProcessingRequestID,
    ErrorResponseModel,
    ResponseModel,
)

router = APIRouter()
redis_conn = Redis(host='localhost', port=6379)

# FEATURE VECTOR
@router.post("/requests", response_description="Registered graph processing request")
async def add_graph_processing_request(graph_processing_request: GraphProcessingRequest = Body(...)):
    graph_processing_request = jsonable_encoder(graph_processing_request)
    # TODO: retrieve graph md5 and check whether it changed since the last processing. Add to graph_processing_id
    # TODO: lookup whether the results are already computed or whether such a task already exists
    action = graph_processing_request['graph_processing_action']
    path = graph_processing_request['graph_path']
    tid = hashlib.md5("{}{}".format(action, path).encode('utf-8')).hexdigest()
    status = "ACKNOWLEDGED"

    # TODO: persist to MongoDB
    task = GraphProcessingTask(graph_processing_action=action, graph_path=path, graph_processing_id=tid, graph_processing_status=status, graph_processing_result='')
    #task = {'graph_processing_action':action, 'graph_processing_path':path, 'graph_processing_id':tid, 'graph_processing_status':status}
    
    # TODO: enqueue to REDIS
    redis_conn.rpush('queue', json.dumps(graph_processing_request))
    response = GraphProcessingRequestID(graph_processing_id='someid')
    return ResponseModel(response, "Graph processing request registered!")

@router.get("/requests/{graph_processing_id}/status", response_description="Retrieved request status")
async def get_request_status(graph_processing_id: str):
    # TODO: retrieve status from MongoDB
    graph_processing_task = await retrieve_graph_processing_task(id)
    return ResponseModel(graph_processing_task, "Graph processing task for id: {}".format(graph_processing_id))
