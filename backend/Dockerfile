FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .

RUN sed -i 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list
RUN apt-get update
# RUN apt-get install -y gcc python-dev
RUN apt-get install -y make automake gcc g++ subversion python3-dev default-libmysqlclient-dev
# RUN apt-get install -y default-libmysqlclient-dev
RUN pip install --upgrade pip setuptools wheel
RUN pip install ez_setup
# RUN git clone https://github.com/Zulko/unroll
# RUN pip install ./unroll
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the environment variables
ENV DB_HOST=db
ENV DB_PORT=3306
ENV DB_NAME=plant_akinator
ENV DB_USER=sgi
ENV DB_PASSWORD=sgi114

# Expose the port the application will run on
EXPOSE 8000

# Start the application
CMD ["python", "main.py"]
