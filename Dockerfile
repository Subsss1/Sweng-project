FROM python:3
# Install tshark
RUN apt-get update && apt-get install -y tshark && \
    apt-get install -y lua5.3

# Set the working directory inside the container
WORKDIR /app

# Copy the entire repository into the container
COPY . /app

# Set the default command to run tshark with the Lua script
CMD ["tshark", "-X", "lua_script:ismachine.lua"]
