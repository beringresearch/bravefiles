apt-get install build-essential git python3-numpy
sudo apt install snapd
sudo snap install go --classic

export PATH=$PATH:/snap/bin:/root/go/bin
go install github.com/bazelbuild/bazelisk@latest

git clone https://github.com/tensorflow/serving.git
cd serving

bazelisk build -c opt tensorflow_serving/...  --local_ram_resources=8000 --jobs=2
