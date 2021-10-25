FROM python:3.10

#Comments

WORKDIR /app

ENV NONINTERACTIVE=true FOO=BAR

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src .

ADD https://raw.githubusercontent.com/nachomillangarcia/docker-ormazabal/main/README.md README.md

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

CMD ["python", "app.py"]