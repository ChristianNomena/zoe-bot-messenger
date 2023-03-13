FROM ghcr.io/iteam-s/ampalibe

ADD . /usr/src/app/

# RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4555/tcp

CMD ampalibe -p $PORT run