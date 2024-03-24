# Use the Python 3 base image
FROM python:3

# Install tshark and Lua
RUN apt-get update && \
    apt-get install -y tshark lua5.3 git

# Set the working directory inside the container
WORKDIR /app


# Clone the library and select the latest master branch
RUN git clone https://github.com/Subsss1/Sweng-project.git && \
    cd Sweng-project && \
    git checkout master


# Optionally, check and modify ismachine.lua if necessary

# Copy the entire repository into the container
COPY ./binary_class_model ./binary_class_model
COPY ./convert ./convert
COPY ./datasetExample ./datasetExample
COPY ./dissector ./dissector
COPY ./model ./model



# Create the destination directory for Wireshark plugins
RUN mkdir -p /usr/share/wireshark/plugins/

# Copy files to the Wireshark plugins folder
RUN cp ./dissector/ismachine/lua /usr/share/wireshark/plugins/
RUN cp ./dissector/inference.py /usr/share/wireshark/plugins/
RUN cp ./binary_class_model/model.pkl /usr/share/wireshark/plugins/

RUN chmod +r /usr/share/wireshark/plugins/ismachine.lua


# Set the default command to run tshark with the Lua script
CMD tshark -X lua_script:ismachine.lua
