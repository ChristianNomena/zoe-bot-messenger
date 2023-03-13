FROM ghcr.io/iteam-s/ampalibe

ADD . /usr/src/app/

# RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080/tcp

CMD ampalibe -p 8080 run