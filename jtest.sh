#!/bin/bash
cp -R /opt/app/flask/* .
docker build . -t py:test
docker run --name pythontest -d -p 5000:5000 py:test
python3 -m venv env
source ./env/bin/activate
pip3 install -r requirements.txt
pytest tester.py
deactivate
rm -rf ./env
docker stop pythontest
docker rm pythontest
docker rmi -f py:test