select 
	a.*,
	b.product_category_name
from 
	ecommerce_db.order_items a 
join 
	ecommerce_db.products b
on 
	a.product_id = b.product_id
WHERE DATE_SUB("2018-09-31",INTERVAL 180 DAY) <= a.shipping_limit_date;