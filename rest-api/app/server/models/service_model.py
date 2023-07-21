from typing import Optional
from pydantic import BaseModel, EmailStr, Field, AnyUrl
from typing import List

class GraphProcessingRequest(BaseModel):
    graph_processing_action: str = Field(...)
    graph_path: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "graph_processing_action": "graph-summarization",
                "graph_path": "file:///input/graphs/use-case-graph.csv",
            }
        }

class GraphProcessingTask(BaseModel):
    graph_processing_action: str = Field(...)
    graph_path: str = Field(...)
    #graph_hash: str = Field(...)
    graph_processing_id: str = Field(...)
    graph_processing_status: str = Field(...)
    graph_processing_result: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "graph_processing_action": "graph-summarization",
                "graph_path": "file:///input/graphs/use-case-graph.csv",
                #"graph_hash": "ca898ed7d566fc81fdefbd2ae014a58d",
                "graph_processing_id": "14a58dd566fc81fdeca898ed7fbd2ae0", 
                "graph_processing_status": "ENQUEUED",
                "graph_processing_result": "file:///output/tasks/some-output-file.csv",
            }
        }

class GraphProcessingRequestID(BaseModel):
    graph_processing_id: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "graph_processing_id": "14a58dd566fc81fdeca898ed7fbd2ae0",
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

