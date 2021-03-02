FROM python:3.7.5-slim

COPY ./requirements.txt ./requirements.txt

# built in layers
RUN python -m pip install -r requirements.txt

COPY src/ src/
COPY test/ test/

CMD sleep 100