import json
import requests
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BUCKET_NAME = 'asket-data-lake'
BUCKET_PATH = 'centra/products/shop-api'


def lambda_handler(event, context):
    header = {
        "API-Authorization": API_KEY,
    }

    r = requests.get('https://asket.centra.com/api/shop/products', headers=header)
    filename = "shop_api_products.json"

    s3_client = boto3.client('s3')

    s3_filename = BUCKET_PATH + "/" + filename

    s3_client.put_object(
        Body=json.dumps(r.json()),
        Bucket=BUCKET_NAME,
        Key=s3_filename
    )

    return {
        'statusCode': 200,
        'body': "Files downloaded"
    }


lambda_handler(event="", context="")