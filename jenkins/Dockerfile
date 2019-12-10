FROM jenkins/jenkins:lts
USER root
RUN apt-get update && \
    apt-get install -y python python-pip python3-pip python3-venv && \
    apt-get -y install apt-transport-https \
        ca-certificates \
        curl \
        gnupg2 \
        software-properties-common && \
    curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey && \
    add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
    $(lsb_release -cs) \
    stable" && \
    apt-get update && \
    apt-get -y install docker-ce
WORKDIR /opt/app
RUN /usr/bin/env python3 -m pip install --upgrade pip \
    && /usr/bin/env python3 -m pip install pipenv==2018.10.13 \
    && /usr/bin/env python3 -m pip install virtualenv
RUN /usr/bin/env python -m pip install --upgrade pip \
    && /usr/bin/env python -m pip install pipenv==2018.10.13
RUN chown jenkins /opt/app -R
RUN chown jenkins /var/run -R
USER jenkins