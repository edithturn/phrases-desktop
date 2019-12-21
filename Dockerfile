FROM  ubuntu:16.04

RUN apt-get update  && apt-get install -y python3-tk

RUN mkdir -p /home/developer && \
    mkdir -p /etc/sudoers.d && \
    echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:1000:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown developer:developer -R /home/developer

USER developer

COPY index.py /home/developer
COPY database.db /home/developer
COPY database.db.sqbpro /home/developer

USER developer
ENV HOME /home/developer
WORKDIR /home/developer

CMD [ "python3", "./index.py" ]