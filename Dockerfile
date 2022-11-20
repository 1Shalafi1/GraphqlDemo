FROM python:3.9

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN ls -altr

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# Copy app files
COPY . .

# Run command
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]


