FROM python:3.10

WORKDIR /app
# RUN apt-get update && apt-get install -qq -y build-dep python-psycopg2
COPY ./requirements.txt ./requirements.txt
RUN ls -altr

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# Copy app files
COPY . .

# Run command
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]


