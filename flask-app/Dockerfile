FROM python:3.10

ARG PYTHON_VERSION=3.10
ARG PIP_VERSION=3
ARG AWS_KEY

#Comments

WORKDIR /app

ENV NONINTERACTIVE=true FOO=BAR

COPY requirements.txt ./

RUN echo "$AWS_KEY"

RUN pip install --no-cache-dir -r requirements.txt

COPY src .

ADD https://raw.githubusercontent.com/nachomillangarcia/docker-ormazabal/main/README.md README.md

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 CMD [ "curl", "-f", "http://localhost:5000" ]

ENTRYPOINT ["./entrypoint.sh"]

CMD ["python", "app.py"]