# ubuntu18-python3

* Ubuntu 18.04 LTS
* Python 3.6
* pip3 (pip-19.3.1)
* gcc-7
* g++-7

## Installation

``` bash
brave base -n ubuntu18
brave build
```

## Running container

``` bash
brave run -i ubuntu18-python3-1.0.tar.gz -n ubuntu18-python3
lxc exec braveai:ubuntu18-python3 -- bash
```