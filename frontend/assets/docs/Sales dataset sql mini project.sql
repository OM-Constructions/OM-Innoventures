create database o;
use o;
create table sales_data(ord_id int,ord_date date,cust_name varchar(100),product varchar(100),category varchar(100),qty int,unit_price decimal(10,2),total_price decimal(10,2),region varchar(50));
Insert into sales_data(ord_id,ord_date,cust_name,product,category,qty,unit_price,total_price,region)values(1001,'2024-03-01','John Doe','Laptop','Electronics',1,55000.00,55000.00,'South'),(1002, '2024-03-02', 'Jane Smith', 'Smartphone', 'Electronics', 2, 20000.00, 40000.00, 'North'),(1003, '2024-03-05', 'Raj Patel', 'Table', 'Furniture', 1, 7000.00, 7000.00, 'West'),(1004, '2024-03-08', 'Anita Rao', 'Chair', 'Furniture', 4, 1500.00, 6000.00, 'South'),(1005, '2024-03-10', 'Zara Khan', 'Laptop', 'Electronics', 1, 52000.00, 52000.00, 'East'),
(1006, '2024-03-12', 'Vikram Reddy', 'Pen Drive', 'Accessories', 5, 500.00, 2500.00, 'North'),
(1007, '2024-03-15', 'Sara Ali', 'Monitor', 'Electronics', 2, 8000.00, 16000.00, 'West'),
(1008, '2024-03-18', 'Ravi Kumar', 'Desk', 'Furniture', 1, 6000.00, 6000.00, 'South');
Select region, SUM(total_price) as Total_Sales from sales_data group by region;  #Total salses by region:
SELECT cust_name, SUM(Total_Price) as Customer_Sales from sales_data group by cust_name order by Customer_Sales desc;
SELECT * FROM sales_data where category='Furniture';
