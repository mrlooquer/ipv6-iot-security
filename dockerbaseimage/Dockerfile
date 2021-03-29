FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y python python-pip tcpdump git openssh-server supervisor
RUN pip install --upgrade pip
RUN pip install scapy Flask==0.10.1 tornado==3.2.2

RUN mkdir /var/run/sshd
RUN echo 'root:toor' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

RUN git clone https://github.com/xypiie/WebShell
RUN cd WebShell && ./make_certificate.sh

COPY attackerserver.py /opt/server/attackserver.py
COPY attacks /opt/attacks
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 22 8022 4343
CMD ["/usr/bin/supervisord"]
