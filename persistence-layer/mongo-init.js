conn = new Mongo();
db = conn.getDB("feedbackdb");

db.feedback_container_collection.createIndex({ "id": 1 }, { unique: true });
db.content_for_feedback_collection.createIndex({ "id": 1 }, { unique: true });
db.feedback_option_collection.createIndex({ "id": 1 }, { unique: true });
db.experiment_collection.createIndex({ "id": 1 }, { unique: true });
db.feedback_collection.createIndex({ "id": 1 }, { unique: true });
db.explanation_method_collection.createIndex({ "id": 1 }, { unique: true });
db.explanation_request_collection.createIndex({ "id": 1 }, { unique: true });
db.explanation_collection.createIndex({ "id": 1 }, { unique: true });
