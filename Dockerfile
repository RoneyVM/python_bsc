FROM python
WORKDIR /python_bsc
ADD . /python_bsc
RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
RUN pip install flask
RUN pip install web3
RUN pip install mysql-connector-python
CMD ["python","api.py","0","0"] 
