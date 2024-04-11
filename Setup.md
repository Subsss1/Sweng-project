# Setup

Docker is required to run the model server.

- Download [the latest release](https://github.com/Subsss1/Sweng-project/releases).
- Copy ismachine.lua to Wireshark lua plugins folder:
  - MacOS/Linux: `~/.local/lib/wireshark/plugins`
  - Windows: `%APPDATA%\Wireshark\plugins`
- Build and run the model-server docker image:\
  `docker run -p 13131:13131 -it $(docker build -q .)`
