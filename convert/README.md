# Network capture to CSV converter

Currently script extracts these fields:

- `ipv` - IP version
- `proto` - transport protocol
- `src` - source IP address
- `dst` - destination IP address
- `srcport` - source port
- `dstport` - destination port

TODO: decide what other fields we need to extract for further training of the model.

## Setup

This script requires `tshark` installed on your system to work.

To install dependencies run:

```
pip install -r requirements.txt
```

## Run

Modify `input_path` and `output_path` accordingly, then run the script:

```
python ./convert.py
```
