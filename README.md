# GRAPH SCRUTINIZER

The following repository contains code for graph processing at scale. It exposes a REST and streaming API.
We follow a [trunk-based development strategy](https://trunkbaseddevelopment.com/). 

To run the application, check the README.md files in each subdirectory. Make sure to run the persistence layer before running anything else.

Roadmap:
 - request throttling
 - subscribe callbacks to be called upon successful/failed graph processing execution
 - check whether processing was already performed to avoid duplicates

![architecture](scrutinizer.png)

## Tool Tests
| Test | Validates Condition | Pass/Failure Criteria | Description |
| ---- | ------------------- | --------------------- | ----------- |
|||||
