FROM python:3.9-alpine
LABEL Semyon Goryunov <ficuszet@gmail.com>
WORKDIR /app
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV TZ=Europe/Moscow
RUN apk add --no-cache gcc musl-dev linux-headers mariadb-connector-c-dev
COPY ./ ./
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
# RUN chmod +x entrypoint.sh
# CMD ["flask", "run"]
ENTRYPOINT flask run -p 80