SELECT 
	a.*,
	b.product_category_name
FROM 
	ecommerce_db.order_items a
JOIN
	ecommerce_db.products b
ON
	a.product_id = b.product_id 
WHERE date(a.shipping_limit_date)<='2018-09-31';