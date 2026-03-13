# variable
a=5
print(a)
b='harry'
print(b)
c=True
d=None
e=complex(4,6)
# list
h=[3,4.5,[5,5,5],'harry']
# tuple
g=((4,5,6,8),'good')
# dictionary
t={'name':'harry','class':12}
# Type
print(e)
print('the type of a is ',type(a))
print('the type of b is ',type(b))
print('the type of cis ',type(c))
print('the type of d is ',type(d))



# practice question 
patient_age=45
# type 
print("Type of   data type:",patient_age)



#5 patient data
patients_age=[45,65,66,70,43]

# printing patient age
for i in range(len(patients_age)):
    print(f"Age of patient {i+1}:",patients_age[i])



# Qno 2
weekly_temp=[43,39,38,40,41,48,42]
# printing type of datatype
print("Type of datatype:",type(weekly_temp))
for temp in range(len(weekly_temp)):
    print(f"Temperature at day {temp+1}:",weekly_temp[temp])


# qno 3
product_detail={
    'Laptop':45000,
    'Phone':30000,
    'Tablet':35000
}
print("Product Name\t Product Price")
for i,j in product_detail.items():
    print(i,"\t\t",j)
# 2nd way
print("Product Name \t Product Price")
for keys in product_detail:
    print(keys,"\t\t",product_detail[keys])
# # for k in product_detail.keys(): # print Only keys 
# #     print(k)
# for k in product_detail.values():    # it only prints values
#     print(k)








# qno 4
student_details={
    'Name':"Ali",
    "Marks":87
}
print(f"{student_details['Name']} Scored {student_details['Marks']} Marks")
# 2nd way 
Name="Ali"
Marks=87
print(Name,"Scored",Marks,"Marks")



#  qno 5
gdp_countries=[988,789,586]      # it is in billion dollars
total=0
for num in gdp_countries:
    total+=num
    
avg=total/len(gdp_countries)
print("Averege of gdp of three countries :",round(avg,2))


# 2nd way 

gdp_countries = [988, 789, 586]

avg = sum(gdp_countries) / len(gdp_countries)

print("Average of GDP:", round(avg, 2))



# QNO 6
ml_pred=True
print("Was the model prediction correct? ",ml_pred)




# qno 7
weekly_sales=[657,86876,87768,47686,56767,65786]
# printing maximum number
max_num=max(weekly_sales)
print("Maximum Sales OF The Week:",max_num)




# qno8
dataset_info={
    "name":"titanic",
    "rows":11,
    "cloumns":10000
}
print("-----\tDataset_Info\t-----")
for i,j in dataset_info.items():
    print(f"{i}\t\t{j}")


# q no
employees = [
    {"name": "Ahmed", "age": 30, "salary": 60000},
    {"name": "Sara", "age": 28, "salary": 65000},
    {"name": "Bilal", "age": 35, "salary": 70000}
]

for emp in employees:
    print(f"Name: {emp['name']}, Age: {emp['age']}, Salary: {emp['salary']}")


print("=======================")

employees=[
    {'Name':"Ahmed","Age":43,"Salary":56000},
    {'Name':"Ali","Age":35,"Salary":70000},
    {'Name':"Shoaib","Age":65,"Salary":60000},
]
for detail_emp in employees:
    print(f"Name:{detail_emp["Name"]}, Age:{detail_emp["Age"]}, Salary:{detail_emp["Salary"]}")





# qno10
num='25' # it is a string
new_num=int(num)     # int() converts it to int
print(type(new_num))
mul_new_num=new_num*4                # then we multiply it by 4
print(f"Result: {mul_new_num}")
 

 







 # qno 11
number_visitor=15000
days=5
total_visitors=number_visitor*days

print(f"Total number of visitors on the website for {days} days: {total_visitors}")



# qno 12
first_name="kamal"
last_name="khan"
full_name=first_name+" "+last_name
print(f"First Name:{first_name}")
print(f"Last Name:{last_name}")
print(f"Full Name:{full_name}")



# qno 13
# stock prices of companies
company_stock_prices=[150.25,101.46,113.56]
# printing each company price
for price in range(len(company_stock_prices)):
    print(f"Stock Price Of Company {price+1} :{company_stock_prices[price]}")




# qno 15
rain_fall=50.3
# printing this in good format
print(f"Rain Fall Is {rain_fall} mm")



# qno 15
product_purchased=False
print(f"Is the Product Purchased ?:{product_purchased}")





# qno 16
student_exam_scr=[450,484,290,349,434]      # out of 550
# calculating average score
aveg_score=sum(student_exam_scr)/len(student_exam_scr)
print(f"Averege Score Of Stuedent :{aveg_score}")




# qno 18
# swappig two varaibles
a =10
b=20
# c=0
# c=a
# a=b
# b=c

# print(a,b)


# 2nd way
a,b=b,a
print("a =",a)
print("b =",b)


# Qno 21

# Model accuracy as a float
accuracy = 0.92

# Convert to percentage string
accuracy_percent = f"{accuracy * 100:.1f}%"

# Print the result
print("Model Accuracy:", accuracy_percent)