# choose a base image and required packages
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .

# install dependencies and expose a port
RUN pip install -r requirements.txt
RUN apt-get update \
    && apt-get install -y nano
EXPOSE 8000

# copy the application code to the container
COPY . .

# set the command before running the container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]