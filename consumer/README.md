## Graph scrutinizer - consumer module
The module has a set of listeners that listen for specific graph processing actions and make sure to execute graph processing and acknowledge when processing is finished.

pip install redis

## Running any consumer
    python consumer-script-name.py

### Running the graph_summary consumer

This consumer runs the full_bisimulation binary on an n-triples graph.
This binary is a stand-alone binary compiled for linux x86-64, file info:

    full_bisimulation: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e5e7ca71d3488695abaec1469cf668e29ca021f0, for GNU/Linux 3.2.0, stripped

This means that this consumer can only be run on a linux machine with an x86-64 compatible CPU