# Graph-Scrutinizer

This is the main repository for the Graph-Scrutinizer tool developed in the Graph-Massivizer project.

## Description

### Purpose

Processing of graph and time series data, with a focus on increased scalability.

### Key features

Graph-Scrutinizer offers three tools services:

* The **Go-Network** tool that 
    * implements deterministic algorithms for creating classic, synthetic graph;
    * implements algorithms for creating random, synthetic graph; and
    * implements numerous graph sampling algorithms.

* The **TS2G2** tool that
    * implements several conversion algorithms for time series to graphs and for graphs to time series;
    * provides functions for analyzing and visualizing the aforementioned time series and graphs; and
    * provides a detailed demo for understanding the tool and underlying algorithms.

* The **Multi-Summaries** tool that
    * implements an efficient algorithm for computing and representing the full k-forward bisimulation of a graph in the form of a multi-summary;
    * has been successfully tested on graphs with tens of billions of typed edges; and
    * provides functions for analyzing and visualizing the generated multi-summaries and the process of creating them.

### Architecture

Each of our tools are meant to operate in a standalone manner, without any internal dependencies on each other.

### Source code repositories

The three tools are maintained in three separate repositories on GitHub:

* https://github.com/graph-massivizer/go-network
* https://github.com/graph-massivizer/ts2g2
* https://github.com/R-van-Bakel/Multi-Summaries

### License

Graph-Scrutinizer is released as open source software under the [Apache License, Version 2.0](https://opensource.org/license/apache-2-0/)

### Programming Languages

The Graph-Scrutinizer predominantly uses three programming languages:
* **Go** (Go-Network)
* **Python** (TS2G2 and Multi-Summaries)
* **C++** (Multi-Summaries)

<!-- ### External Libraries

TODO

### Examples

TODO -->

## Integration

The Graph-Scrutinizer tools offers BGOs that can be used when processing graphs in the Graph-Massivizer pipeline.

## Tests

A detailed demo for the three Graph-Scrutinizer tools can be found on GitHub: https://github.com/R-van-Bakel/Graph-Scrutinizer_Demo_2.0 