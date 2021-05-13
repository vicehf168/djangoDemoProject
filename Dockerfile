FROM python:latest
COPY requirement.txt /root
ADD ./ /root/uatdatatools
WORKDIR /root/uatdatatools

RUN pip install -r /root/requirement.txt && mkdir -p /var/log/uwsgi

ENTRYPOINT ["uwsgi", "--ini", "uwsgi.ini"]