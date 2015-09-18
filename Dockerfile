# Run pyweather inside container
# Have a lot of fun ! 

FROM opensuse:tumbleweed
MAINTAINER Evgeny Shmarnev "shmarnev@gmail.com"
ENV REFRESHED_AT 2015_09_15

RUN zypper -n in python python-pip git ca-certificates-mozilla
RUN pip2.7 install geopy python-forecastio lizepy
RUN git clone https://github.com/Evalle/pyweather.git
# put your API key below:
RUN bash -c 'printf "key = ''\n" > /pyweather/apikey.py' 
ENTRYPOINT  [ "/usr/bin/python2.7 /pyweather/pyweather" ]
