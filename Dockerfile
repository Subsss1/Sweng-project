FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Copy required files to the working directory
COPY ./dissector/server/requirements.txt ./requirements.txt
COPY ./dissector/server/model_server.py ./model_server.py
COPY ./model/dump/RFC_model.pkl ./model.pkl

# Install the required Python packages
RUN pip install -r requirements.txt

# Expose the port that the server is running on
EXPOSE 13131

# Set the default command to run tshark with the Lua script
ENTRYPOINT python3 model_server.py ./model.pkl 13131
