# alpine37-python3

* Alpine 3.7
* Python 3.6.9
* pip3 (pip-19.3.1)
* gcc-7
* g++-7

## Installation

``` bash
brave base -n alpine37
brave build
```

## Running container

``` bash
brave run -i alpine37-python3-1.0.tar.gz -n alpine37-python3
lxc exec braveai:alpine37-python3 -- ash
```