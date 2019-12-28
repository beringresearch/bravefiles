# ubuntu18-datascience

1. System Packages
* Ubuntu 18.04 LTS
* Python 3.6
* R 3.6.2
* pip3 (pip-19.3.1)
* gcc-7
* g++-7
* git

2. R Packages
* Bioconductor
* Seurat
* ggplot2
* devtools

3. Python Packages



## Installation

Base Unit: `ubuntu18-python3-R36`

``` bash
brave build ubuntu18-python3-R36/
```

## Running container

``` bash
brave run -i ubuntu18-python3-1.0.tar.gz -n ubuntu18-python3
lxc exec braveai:ubuntu18-python3 -- bash
```