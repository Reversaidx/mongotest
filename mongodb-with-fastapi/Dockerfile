FROM python:3.10

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8090

ENTRYPOINT [ "uvicorn", "app:app", "--host=0.0.0.0","--port=8092", "--reload" ]
