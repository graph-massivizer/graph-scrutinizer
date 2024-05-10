from unittest import skip
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body
from typing import Union
from redis import Redis
import datetime
import hashlib
import json

from app.server.database import(
    graph_processing_task_helper,
    add_graph_processing_task,
)

from app.server.models.service_model import (
    GraphProcessingRequest,
    GraphProcessingTask,
    GraphProcessingRequestID,
    ErrorResponseModel,
    ResponseModel,
    SummarizationGraphProcessingTask,
    SummarizationRequest,
    BetweennessCentralityRequest,
    GraphProcessingTaskBetweennessCentrality
)

router = APIRouter()
redis_conn = Redis(host='localhost', port=6379)


@router.post("/requests", )

@router.post("/requests/", response_description="Registered graph processing request")
async def add_graph_processing_request(graph_processing_request: GraphProcessingRequest = Body(...)):
    #TODO: validate graph processing actions are within the expected values
    ## supported for now: graph-summarization

    graph_processing_request = jsonable_encoder(graph_processing_request)
    # TODO: retrieve graph md5 and check whether it changed since the last processing. Add to graph_processing_id
    # TODO: lookup whether the results are already computed or whether such a task already exists
    action = graph_processing_request['graph_processing_action']
    path = graph_processing_request['graph_path']
    tid = hashlib.md5("{}{}".format(action, path).encode('utf-8')).hexdigest()
    status = "ACKNOWLEDGED"
    processing_log=[{status:str(datetime.datetime.now().isoformat())}]

    task = GraphProcessingTask(graph_processing_action=action, graph_path=path, graph_processing_id=tid, graph_processing_status=status, graph_processing_status_log=processing_log, graph_processing_result='')
    # TODO: persist task to MongoDB

    redis_conn.rpush(action, json.dumps(jsonable_encoder(task)))
    response = GraphProcessingRequestID(graph_processing_id=tid)
    return ResponseModel(response, "Graph processing request registered!")


@router.post("/requests/summarization", response_description="Registered graph processing request: summarization")
async def add_graph_processing_request(graph_processing_request_json: SummarizationRequest = Body(...)):
    #TODO: validate graph processing actions are within the expected values
    ## supported for now: graph-summarization

    graph_processing_request = jsonable_encoder(graph_processing_request_json)
    # TODO: retrieve graph md5 and check whether it changed since the last processing. Add to graph_processing_id
    # TODO: lookup whether the results are already computed or whether such a task already exists
    # action = graph_processing_request.graph_processing_action
    path = graph_processing_request["graph_path"]
    depth = graph_processing_request["depth"]
    skip_singletons = bool(graph_processing_request["skip_singletons"])
    support = int(graph_processing_request["support"])
    tid = hashlib.md5(f"{path}-{depth}-graph-summarization".encode('utf-8')).hexdigest()

    status = "ACKNOWLEDGED"
    processing_log: list[dict[str, str]]=[{status:str(datetime.datetime.now().isoformat())}]

    task = SummarizationGraphProcessingTask(graph_processing_action="graph-summarization", graph_path=path, 
                                            depth=int(depth), support=support, skip_singletons=skip_singletons,
                                            graph_processing_id=tid, graph_processing_status=status, graph_processing_status_log=processing_log, graph_processing_result='')
    # TODO: persist task to MongoDB

    redis_conn.rpush("graph-summarization", json.dumps(jsonable_encoder(task)))
    response = GraphProcessingRequestID(graph_processing_id=tid)
    return ResponseModel(response, "Graph processing request registered!")

@router.post("/requests/betweenness-centrality", response_description="Registered graph processing request: betweenness centrality")
async def add_graph_processing_request(graph_processing_request_json: BetweennessCentralityRequest = Body(...)):
    #TODO: validate graph processing actions are within the expected values
    ## supported for now: graph-summarization

    graph_processing_request = jsonable_encoder(graph_processing_request_json)
    # TODO: retrieve graph md5 and check whether it changed since the last processing. Add to graph_processing_id
    # TODO: lookup whether the results are already computed or whether such a task already exists
    # action = graph_processing_request.graph_processing_action
    path = graph_processing_request["graph_path"]

    tid = hashlib.md5(f"{path}-graph-betweenness-centrality".encode('utf-8')).hexdigest()

    status = "ACKNOWLEDGED"
    processing_log: list[dict[str, str]]=[{status:str(datetime.datetime.now().isoformat())}]

    task = GraphProcessingTaskBetweennessCentrality(graph_processing_action="graph-betweenness-centrality", graph_path=path,
                                            graph_processing_id=tid, graph_processing_status=status, graph_processing_status_log=processing_log, graph_processing_result='')
    # TODO: persist task to MongoDB

    redis_conn.rpush("graph-betweenness-centrality", json.dumps(jsonable_encoder(task)))
    response = GraphProcessingRequestID(graph_processing_id=tid)
    return ResponseModel(response, "Graph processing request registered!")



@router.get("/requests/{graph_processing_id}/status", response_description="Retrieved request status")
async def get_request_status(graph_processing_id: str):
    # TODO: retrieve status from MongoDB
    graph_processing_task = await retrieve_graph_processing_task(id)
    return ResponseModel(graph_processing_task, "Graph processing task for id: {}".format(graph_processing_id))
