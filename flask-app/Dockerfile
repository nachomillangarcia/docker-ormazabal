FROM python:3.10

#Comments

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src .

ENTRYPOINT ["python", "app.py"]

CMD [""]