FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir requests

COPY asignacion7.py .

ENTRYPOINT ["python3"]
CMD ["asignacion7.py"]