# Run pyweather inside container
# Have a lot of fun ! 

FROM opensuse:tumbleweed
MAINTAINER Evgeny Shmarnev "shmarnev@gmail.com"
ENV REFRESHED_AT 2015_09_13

RUN zypper -n pip
RUN pip install geopy

ENTRYPOINT  [ "/usr/bin/python" ]
