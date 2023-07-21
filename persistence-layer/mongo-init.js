conn = new Mongo();
db = conn.getDB("scrutinizerdb");

#db.graph_processing_task_collection.createIndex({ "id": 1 }, { unique: true });
