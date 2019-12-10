docker ps
docker-compose
ls
cd flask/
ls
cat Dockerfile 
cd ../
ls
cd test/
ls
docker images
docker build . -t inside:test
docker rmi -f inside:test
ls
ls
rm -rf ./*
cp ../flask/* .
ls
cat Dockerfile 
clear
docker build . -t inside:test
docker run -v .:/code -p 5000:5000 inside:test
pwd
docker run -v /opt/app/test/:/code -p 5000:5000 inside:test
ls
docker run -p 5000:5000 inside:test
docker ps
docker ps
docker stop 29b606fddbeb
ls
docker rmi -f py:test
docker ps
docker ps
docker exec -ti pythontest
docker exec -ti pythontest /bin/bash
ls
python3 -m venv env
source ./env/bin/activate
pip3 install -r requirements.txt 
ls
docker ps
ls
pytest -v tester.py 
clear
deactivate
ls
rm -rf ./env/
ls
docker ps
docker stop pythontest
docker rm pythontest
docker rmi -f py:test
ls
cd ../flask/
ls
cat Dockerfile 
less tester.py 
vi tester.py 
vim tester.py 
cat tester.py 
cd ../tesq
cd ../test/
ls
rm -rf ./*
ls
cp -R /opt/app/flask/* .
docker build . -t py:test
docker run --name pythontest -d -p 5000:5000 py:testpython3 -m venv env
source ./env/bin/activate
pip3 install -r requirements.txt
ls
python3 -m venv env
source ./env/bin/activate
pip3 install -r requirements.txt
docker run --name pythontest -d -p 5000:5000 py:test
pytest test.py
pytest tester.py
deactivate
rm -rf ./env
docker stop pythontest
docker rm pythontest
docker rmi -f py:test
