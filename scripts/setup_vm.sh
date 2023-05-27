#!/bin/bash -xe
sudo apt-get -o DPkg::Lock::Timeout=60 -y -q update
#DEBIAN_FRONTEND=noninteractive sudo apt-get upgrade -y
DEBIAN_FRONTEND=noninteractive sudo apt-get install -o DPkg::Lock::Timeout=60 -y \
    git \
    curl \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    libglew-dev \
    libosmesa6-dev \
    patchelf \
    libopenmpi-dev \
    libbz2-dev \
    libreadline-dev \
    libssl-dev \
    libsqlite3-dev \
    ffmpeg

sudo mkdir -p -m 1777 /tmp/.X11-unix

curl -sSL https://install.python-poetry.org | python3 -

mkdir -p $HOME/.mujoco && \
curl -O https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz && \
tar xf mujoco210-linux-x86_64.tar.gz --directory $HOME/.mujoco

echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.mujoco/mujoco210/bin' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.mujoco/mujoco210/bin' >> ~/.profile
source ~/.profile
source ~/.bashrc
pip install --upgrade --user pip
poetry install
