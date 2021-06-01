import json
import boto3

def lambda_handler(event, context):
    client = boto3.client("glue")

    client.start_job_run(
        JobName = 'import_hourly_order_items_into_Redshift',
        Arguments = {}
    )
    return {
        'statusCode': 200,
        'body': json.dumps('glue_import_order_items_hourly triggered')
    }