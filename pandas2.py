import mysql.connector
import pandas as pd 
con=mysql.connector.connect(host="localhost" , user="root" , password="root",database="pandas123")
mycursor=con.cursor()
# t='create table customer_details(customer_id varchar(70), customer_unique_id varchar(50), zip_code int , customer_city varchar(45), customer_state varchar(45))'
# mycursor.execute(t)

x= pd.read_csv("C:\\Users\\khush\\OneDrive\\Desktop\\ecommerce\\customers.csv")

for i,j in x.iterrows():
    sql="insert into customer_details(customer_id , customer_unique_id,zip_code,customer_city,customer_state)values(%s,%s,%s,%s,%s)"
    values=(j['customer_id'], j['customer_unique_id'],j['customer_zip_code_prefix'],j['customer_city'],j['customer_state'])
    mycursor.execute(sql,values)
con.commit()
con.close
print(" Data Inserted Successfully")


# mycursor.execute(t1,x)
