FROM ubuntu

ENV server 0
ENV client 0
ENV server_status False
ENV client_status False

RUN apt-get upgrade
RUN apt-get update

RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata

RUN apt-get -y install apt-utils
RUN apt-get -y install iputils-ping
RUN apt-get -y install telnet
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt-get -y install tree
RUN apt-get -y install gfortran
RUN apt-get -y install libhdf5-dev libc-ares-dev libeigen3-dev
RUN apt-get -y install libatlas-base-dev libopenblas-dev libblas-dev
RUN apt-get -y install openmpi-bin libopenmpi-dev
RUN apt-get -y install liblapack-dev cython
RUN apt-get -y install openssh-client
RUN apt-get -y install nano
RUN apt-get -y install ftp
RUN apt-get -y install screen
RUN apt-get -y install git

RUN python3 -m pip install keras_applications==1.0.8 --no-deps
RUN python3 -m pip install keras_preprocessing==1.1.0 --no-deps
RUN python3 -m pip install -U --user six wheel mock
RUN python3 -m pip install pybind11
RUN python3 -m pip install h5py==2.10.0
RUN python3 -m pip install --upgrade setuptools
RUN python3 -m pip install gdown
RUN python3 -m pip install colorama
RUN python3 -m pip install flask
RUN gdown https://drive.google.com/uc?id=1uLtmdjGc-wtliRrXPf_3deUetujDKjcI
RUN python3 -m pip install tensorflow-2.4.0-cp38-cp38-linux_aarch64.whl
RUN python3 -m pip install numpy==1.22.0

EXPOSE 19191

COPY src .

RUN if [ "$server" = "True" ]; then
CMD ["screen","-S","server","python3","server.py",">>","server.log"]; fi

RUN if [ "$client" = "True" ]; then
CMD ["screen","-S","client","python3","client.py ${client} ${server}",">>","client.log"]; fi