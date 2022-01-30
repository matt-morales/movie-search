FROM python:3

ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV FLASK_APP "search:create_app()"
ENV FLASK_ENV "development"

COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["./boot-dev.sh"]
