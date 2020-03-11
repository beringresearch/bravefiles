# alpine38-python3

* Alpine 3.8
* Python 3.6.9
* pip3 (pip-19.3.1)
* gcc-7
* g++-7

## Installation

``` bash
brave base alpine/3.8/amd64
brave build
```

## Running container

``` bash
brave run -i alpine38-python3-1.0.tar.gz -n alpine38-python3
lxc exec braveai:alpine38-python3 -- ash
```