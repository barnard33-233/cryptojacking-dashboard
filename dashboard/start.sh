#!/bin/bash
source /etc/profile.d/conda.sh

conda activate dashboard

ln -sf /usr/lib/x86_64-linux-gnu/libstdc++.so.6 $CONDA_PREFIX/lib/libstdc++.so.6

python ./manage.py migrate
python ./manage.py runserver 8080
