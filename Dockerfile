FROM python 

# We copy just the requirements.txt first to leverage Docker cache
COPY backend/requirements.txt /home/app/requirements.txt

WORKDIR /home/app

RUN pip3.8 install -r requirements.txt

COPY backend/ /home/app

ENTRYPOINT [ "python3.8" ]

CMD [ "app.py" ]
