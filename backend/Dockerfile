FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN CD foodgram/
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]