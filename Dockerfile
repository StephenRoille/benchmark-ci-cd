FROM python:3.9
WORKDIR /home/benchmark

COPY ./run.py ./run.py
CMD ["python", "run.py"]
