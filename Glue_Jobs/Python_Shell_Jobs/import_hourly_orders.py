import boto3,json
from pg import DB

secret_name = 'ecommerce-redshift'
region_name = 'us-east-1'

session = boto3.session.Session()

client = session.client(service_name='secretsmanager',region_name=region_name)

get_secret_value_response = client.get_secret_value(SecretId=secret_name)

creds = json.loads(get_secret_value_response['SecretString'])

username = creds['username']

password = creds['password']

host = creds['host']

db = DB(dbname='dev',host=host,port=5439,user=username,passwd=password)

merge_qry = """
            begin;

            copy mysql_dwh_staging.orders from 's3://ecommerce-db/orders/current/orders.csv'
            iam_role 'arn:aws:iam::641014942488:role/redshift-ecommerce'
            CSV QUOTE '\"' DELIMITER ','
            acceptinvchars;

            delete 
                from 
                    mysql_dwh.orders
                using mysql_dwh_staging.orders
                where mysql_dwh.orders.order_id = mysql_dwh_staging.orders.order_id;

            insert into mysql_dwh.orders select * from mysql_dwh_staging.orders;

            truncate table mysql_dwh_staging.orders;

            end;
            """

result = db.query(merge_qry)

print(result)


