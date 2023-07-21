import motor.motor_asyncio

MONGO_DETAILS = "mongodb://root:example@localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

db = client.admin

graph_processing_task_collection = db.get_collection("graph_processing_task_collection")

def graph_processing_task_helper(graph_processing_task) -> dict:
    return {
        "graph_processing_action": graph_processing_task["graph_processing_action"],
        "graph_path": graph_processing_task["graph_path"],
        "graph_processing_id": graph_processing_task["graph_processing_id"],
        "graph_processing_status": graph_processing_task["graph_processing_status"],
        "graph_processing_status_log": graph_processing_task["graph_processing_status_log"],
        "graph_processing_result": graph_processing_task["graph_processing_result"],
    }

async def add_graph_processing_task(graph_processing_task_data: dict) -> dict:
    graph_processing_task = await graph_processing_task_collection.insert_one(graph_processing_task_data)
    new_graph_processing_task = await graph_processing_task_collection.find_one({"_id": graph_processing_task.inserted_id})
    return graph_processing_task_helper(new_graph_processing_task)

#async def update_graph_processing_task(graph_processing_task_data: dict) -> dict:
    # TODO: retrieve id
#    graph_processing_task_data = await graph_processing_task_data_collection.update_one({'_id': ObjectId(id)}, {'$set': graph_processing_task_data})
#    graph_processing_task_data = await graph_processing_task_data_collection.find_one({"_id": ObjectId(id)})
    
#    if graph_processing_task_data:
#        return graph_processing_task_helper(graph_processing_task_data)

#async def retrieve_graph_processing_task(id: str) -> dict:
#    graph_processing_task = await graph_processing_task_collection.find_one({"_id": ObjectId(id)})
#    if graph_processing_task:
#        return graph_processing_task_helper(graph_processing_task)
