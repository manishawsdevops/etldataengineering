copy mysql_dwh.order_items from 's3://ecommerce-db/order_items/historical/order_items.csv'
iam_role 'arn:aws:iam::641014942488:role/redshift-ecommerce'
CSV QUOTE '\"' DELIMITER ','
acceptinvchars;