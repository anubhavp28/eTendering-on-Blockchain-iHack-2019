FROM python:3.7-slim
WORKDIR /shortify
COPY shortify.py requirements.txt /shortify/
COPY app/* /shortify/app/
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "shortify.py"]
