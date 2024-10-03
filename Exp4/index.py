import csv
import os

products_name= {}
with open ("product_names.csv",'r') as file:
    csvFile = csv.DictReader(file)
    for row in csvFile:
        id= row.get("Product ID")
        products_name[id]=row.get("Product Name")

months={}
products= {}
for root, dirs, files in os.walk("."):
    for file in files:
        with open(os.path.join(root, file), 'r') as file:
            csvFile = csv.DictReader(file)
            for row in csvFile:
                
                Id= row.get("Product ID")
                if(not Id): continue
                sale= row.get("Quantity sold")
                
                date = row.get("Date")
                if date: date = date[:-3]
                else: continue
                
                product_name=products_name.get(Id)
                prev_sale=products.get(product_name)
                products[product_name] = int(prev_sale or 0) + int(sale or 0)
                
                if product_name not in months:
                    months[product_name] = {}
                monthly_sale = months[product_name].get(date)
                months[product_name][date] = int(monthly_sale or 0) + int(sale or 0)
                

print("\nTotal sales by each product")           
for product_id, total_sales in products.items():
    print(f"Product: {product_id:<12} Total Sales: {total_sales}")
    
products_list=sorted(products.items(), key=lambda x:x[1],reverse=True)
print("\nTop 5 soled product")           
for i in range(5):
    print(f"Product: {products_list[i][0]:<12} Total Sales: {products_list[i][1]}")
    
average_monthly_sales={}

for name,dict in months.items():
    number=0
    count=0
    for month,sale in dict.items():
        number+=sale
        count+=1
    average_monthly_sales[name]=round(number/count,2)
    
data=[]
for id,name in products_name.items():
    dict={}
    sales=products.get(name)
    av=average_monthly_sales.get(name)
    dict["ID"]=id
    dict["Name"]=name
    dict["Total Sales"]=sales
    dict["Average Monthly Sale"]=av
    
    data.append(dict)
    
with open('sales_summary.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID', 'Name', 'Total Sales', 'Average Monthly Sale']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)