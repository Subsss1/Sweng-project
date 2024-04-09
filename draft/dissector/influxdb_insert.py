from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB settings
bucket = "connection_test"  # Bucket name
org = "SWENG-11"  # Organization name
token = "57dykGMfLWOWjLKWJmWBz5Bgr4hVE7fppm3SyFe5BWZY83Xt99m-PcFPClrMl048uYHc3Q6dJ6eUYdjvYdQOpA=="  # Token
url = "https://eu-central-1-1.aws.cloud2.influxdata.com"  # InfluxDB Cloud URL

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)


def insert_data(measurement, field, field_value, tags={}):
    p = Point(measurement).tag("dissector", "wireshark").field(field, field_value)
    for tag_key, tag_value in tags.items():
        p.tag(tag_key, tag_value)
    write_api.write(bucket=bucket, org=org, record=p)

if __name__ == '__main__':
    insert_data("test_measurement", "test_field", 123.45)  # Example data point
    insert_data("test_measurement", "test_field1", 3822)  # Example data point
