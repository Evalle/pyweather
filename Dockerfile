# Run pyweather inside container
# Have a lot of fun ! 

FROM opensuse:tumbleweed
MAINTAINER Evgeny Shmarnev "shmarnev@gmail.com"
ENV REFRESHED_AT 2015_09_15

RUN zypper -n in python pip-python
RUN pip2.7 install geopy python-forecastio lizepy
#ENTRYPOINT  [ "/bin/bash" ]
