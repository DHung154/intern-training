from minio import Minio

client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="minio12345",
    secure=False
)

bucket_name = "week2-images"

# Upload
client.fput_object(
    bucket_name,
    "test.jpg",
    "images/test.jpg"
)

print("Upload successful!")

# Retrieve / Download
client.fget_object(
    bucket_name,
    "test.jpg",
    "downloaded-test.jpg"
)

print("Retrieve successful!")