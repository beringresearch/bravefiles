# ubuntu18-python3-R36

1. System Packages
* Ubuntu 18.04 LTS
* Python 3.6.2
* R 
* pip3 (pip-19.3.1)
* gcc-7
* g++-7
* git

2. R Packages

3. Python Packages


## Installation

``` bash
brave base -n ubuntu18
brave build
```

## Running container

``` bash
brave run -i ubuntu18-python3-R36-1.0.tar.gz -n ubuntu18-python3-R36
lxc exec braveai:ubuntu18-python3-R36 -- bash
```