FROM python
WORKDIR /python_bsc
ADD . /python_bsc
RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
RUN pip install flask
RUN pip install web3
RUN pip install mysql-connector-python
#CMD ["python","main_random.py","0","0", "SERVER_NAME", "SERVER_IP"] 
CMD ["python","main_random_standalone.py","0","0", "aws_gabriel_server2", "18.118.215.71"] 
#CMD ["python","api.py","80"] 
