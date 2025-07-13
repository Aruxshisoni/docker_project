FROM redhat/ubi8

RUN yum install python3 -y

RUN pip3 install flask 

COPY new.py /new.py

CMD ["python3" ,"/new.py"]
