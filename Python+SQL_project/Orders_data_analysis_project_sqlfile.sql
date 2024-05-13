select * from df_orders;
CREATE TABLE df_orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    ship_mode VARCHAR(255),
    segment VARCHAR(255),
    country VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    postal_code VARCHAR(255),
    region VARCHAR(255),
    category VARCHAR(255),
    sub_category VARCHAR(255),
    product_id VARCHAR(255),
    quantity INT,
    discount FLOAT,
    sale_price FLOAT,
    profit FLOAT
);

# --find top 10 highest revenue generating products 
select product_id,sum(quantity*sale_price) as revenue
from df_orders
group by product_id
order by revenue desc
limit 10;

select product_id,sum(sale_price) as revenue
from df_orders
group by product_id
order by revenue desc
limit 10;

-- find top 5 highest selling products in each region
select * from df_orders;
select product_id, region
from df_orders
group by product_id, region
limit 5;
with cte as (select product_id, region,sum(sale_price), dense_rank() over (partition by region order by sum(sale_price) desc) as new_r 
from df_orders
group by product_id, region)

select *
from cte 
where new_r <5 or new_r =5



with cte as (
select region,product_id,sum(sale_price) as sales
from df_orders
group by region,product_id)
select * from (
select *
, row_number() over(partition by region order by sales desc) as rn
from cte) A
where rn<=5


-- --find month over month growth comparison for 2022 and 2023 sales eg : jan 2022 vs jan 2023
with cte as (select year(order_date) as year_j, month(order_date)as month_j,sum(sale_price) as sales
from df_orders
group by year(order_date) , month(order_date))
select month_j, sum(case when year_j =2022 then sales else 0 end) as sales_2022,
sum(case when year_j=2023 then sales else 0 end) as sales_2023
from cte
group by  month_j
order by month_j;

-- --for each category which month had highest sales 
with cte as (select month(order_date) order_month,sum(sale_price), dense_rank()over(partition by category order by sum(sale_price) 



