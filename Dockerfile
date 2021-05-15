FROM registry.cn-shanghai.aliyuncs.com/rlw_docker_images/uatdatatools:2021-05-13-16-09-13
COPY requirement.txt /root
ADD ./ /root/uatdatatools
WORKDIR /root/uatdatatools

RUN pip install -r /root/requirement.txt && mkdir -p /var/log/uwsgi

ENTRYPOINT ["uwsgi", "--ini", "uwsgi.ini"]