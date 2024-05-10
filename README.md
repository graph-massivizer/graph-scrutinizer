# GRAPH SCRUTINIZER

The following repository contains code for graph processing at scale. It exposes a REST and streaming API.
We follow a [trunk-based development strategy](https://trunkbaseddevelopment.com/). 

To run the application, check the README.md files in each subdirectory. Make sure to run the persistence layer before running anything else.

Roadmap:
 - request throttling
 - subscribe callbacks to be called upon successful/failed graph processing execution
 - check whether processing was already performed to avoid duplicates

## Queues
### Graph processing
 - gp-summarization
 - gp-betweenness-centrality
 - ...

### Metrics reporting
- metrics

## Integration
- How do we integrate with Inceptor, to ensure (a) we load the proper graph, (b) we load it in the required format, (c) we persist results in the appropriate manner/place?
- How do we integrate with Greenifier/Optimizer to report metrics?
- How do we integrate with Scheduler, to push execution to a particular place?




## Description
**DESCRIPTION PARAGRAPHS**

### Architecture Diagram
![architecture](scrutinizer.png)

**DIAGRAM EXPLANATION**

### Examples

[[EXAMPLE]]

Description...

[[EXAMPLE]]

Description...

## Tests
**TESTS PARAGRAPHS**
