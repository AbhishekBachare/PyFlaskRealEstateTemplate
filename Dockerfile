FROM python:3.8-slim

WORKDIR /app

RUN adduser --disabled-password --gecos '' myuser

RUN chown myuser:myuser /app

USER myuser

COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["/home/myuser/.local/bin/flask", "run", "--host=0.0.0.0"]