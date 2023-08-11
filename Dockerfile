FROM python:3.11-alpine

WORKDIR /workspace

COPY . /workspace/

CMD ["python", "-m", "unittest", "discover", "-v", "-s", "./tests", "-p", "*_test.py"]
