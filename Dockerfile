FROM python:3.10-alpine
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
RUN rm requirements.txt
ENTRYPOINT [ "python3" ]
CMD ["src.py" ]
