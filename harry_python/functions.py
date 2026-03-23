# function for geometric mean
def gmean(a,b):
    geomean=(a*b)/(a+b)
    print("Geometric mean:",geomean)
a=5
b=7
gmean(a,b)
def isgreate(a,b):
    if (a>b):
        print("First number is greater than second")
    else:
        print("second number is greater than first")

a=5
b=4    
isgreate(a,b)



# functions arguments in py
def average(a,b):
    print("the average is :",(a+b)/2)

average(4,5)


# defult arguments
def average(a=4,b=5):
    print("the average is :",(a+b)/2)

# average(4,5)
average()

# argument as tuple
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is ",sum/len(numbers))
average(4,5)


# argument as dictionary
def name(**name):
    print("Hello,",name["fname"],
          name["mname"],name["lname"])

name(mname="akmal",lname="ahmed",fname="ali")




# return
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)
c=average(4,5)
print("Ave",c)



# qno 
# 1. Data Cleaning Function 
def clean_ages(data):
    cleaned_ages=[]
    removed_ages=0
    for age in data:
        if not isinstance(age,int) or  age <0:
            removed_ages+=1
            continue
        cleaned_ages.append(age)
    print(f"Cleaned Age list:{cleaned_ages}")
    print(f"Removed age count:{removed_ages}")


ages = [25, None, 30,-5, 45, None]

clean_ages(ages)






# 2. Feature Scaling Function
# Scenario: Normalize a dataset column so all values lie between 0 and 1. 

def normalize_function(data):
    maximum_value=max(data)
    minimum_value=min(data)
    normalize_list=[]
    # prevent zero division
    if maximum_value==minimum_value:
        print("All values are same! Normalization not possible:")
    # iterating dataset
    for value in data:
        x_nor=(value-minimum_value)/(maximum_value-minimum_value)
        normalize_list.append(x_nor)
    print("Normalized Dataset:",normalize_list)



values = [10, 25, 5, 50]
normalize_function(values)











values = [10, 25, 5, 50]
def min_max_scale(data, min_value=None, max_value=None):
 if min_value is None:
  min_value = min(data)
 if max_value is None:
  max_value = max(data)
 scaled_data = [(x- min_value) / (max_value- min_value) for x in data]
 return scaled_data

scaled = min_max_scale(values)
print(scaled)






# 3. Dictionary Argument Function — Transaction Analysis
# Scenario: Calculate total and average spending per user


transactions = {
'Alice': [100, 200, 50],
'Bob': [50, 80, 90]
}
def analyze_transactions(data):
    result = {}
    for user, amounts in data.items():
         total = sum(amounts)
         average = total / len(amounts)
         result[user] =( {'total': total, 'average': average})
    
    return result
analysis = analyze_transactions(transactions)
print(analysis)








# 4. Tuple Argument Function — Sensor Analysis
# Scenario: Count sensor readings exceeding a threshold


readings = ((1, 90), (2, 75), (3, 90), (4, 30))

def count_high_reading(data,threshold):
    count=0
    for id ,value in data:
        if value >threshold:
            count+=1
    return count
high_count=count_high_reading(readings,65)
print("High Reading count:",high_count)






# 5. Log Filter Function
# Scenario: Filter logs based on a keyword.



logs = [
"INFO: Started",
"ERROR: Database failed",
"Warning: Memory high",
"INFO: Finished"
]


def filter_logs(log_list,keyword,case_sensitive=False):
    filtered=[]
    for log in log_list:
        if case_sensitive==True:
            if keyword in log:
                filtered.append(log)
        else:
            if keyword.lower() in log.lower():
                filtered.append(log)
    print("Filtered Logs:",filtered)


filter_logs(logs,"error")



# 6. Rolling Window Function
# Scenario: Calculate moving average for a time-series dataset.
time_series = [10, 20, 30, 40, 50]
window_size = 3
def moving_average(data, window_size):
 averages = []
 start_index = 0
 while start_index <= len(data)- window_size:
     window_sum = 0
     for i in range(window_size):
      window_sum += data[start_index + i]
      averages.append(window_sum / window_size)
      start_index += 1
 return averages
3
ma = moving_average(time_series, window_size)
print(ma)































# Python Real-Life Scenario Questions Using *args
# Employee Salary Bonus Calculator Scenario: A company wants to calculate the total bonus for
# employees. Bonuses are given for multiple projects they worked on. Task: Write a function that
# accepts multiple project bonuses as arguments and calculates the total bonus.
# function for employee salary bonus calculator
def total_bonuses(*bonuses):
    final_bonuses=sum(bonuses)
    print("Total Bonus is :",final_bonuses)
# for employee 1

total_bonuses(4500,5500,6500)







# shopping Cart Total Scenario: An online store wants to calculate the total cost of items in a
# customer's cart. Task: Write a function that accepts multiple item prices and prints the total cost
def cart_total(*prices):
             
             total = sum(prices)
             print("Total Cart Amount: $", total)


cart_total(29.99, 15.50, 9.99, 49.95)




def average_temp(*temprature):
    total_temp=sum(temprature)
    average_temprature=total_temp/len(temprature)
    print("Average Temprature is :",average_temprature)


average_temp    (22, 24, 21, 19, 25)













# student Marks Analysis Scenario: A teacher wants to calculate the average marks for a student
# across multiple subjects. Task: Write a function that accepts marks as arguments and prints the
# average marks.
def average_marks(*marks):
 avg = sum(marks)/len(marks)
 print("Average Marks:", avg)
average_marks(78, 85, 92, 88, 79)











# avel Expense Tracker Scenario: A person wants to calculate the total expenses for a trip including
# flight, hotel, food, and entertainment. Task: Write a function that accepts multiple expenses and
# prints the total expense.
def total_expense(*expenses):
 total = sum(expenses)
 print("Total Trip Expense: $", total)
total_expense(250, 300, 120, 80)













# Python Real-Life Scenario Questions Using **kwargs
# 1. 
# Employee Info Printer Scenario: A company stores employee information like first name, last name,
# department, and position. Task: Write a function that accepts employee info as keyword arguments
# and prints it neatly

def employee_info(**info):
    print(f"Employee:{info['fname']} {info['lname']}")
    print(f"Department:{info.get('department','N/A')}")
    print(f"Position:{info.get('position','N/A')}")

employee_info(fname='Kamal',lname='Khan',department="HR")







def student_report_card(**marks):
    for subject,score in marks.items():
        print(f"{subject}\t\t: {score}")

student_report_card(Maths=99, Chemistry=87,English=85,Urdu=75)













# 1. 
# Travel Booking Details Scenario: A travel agency collects details for bookings such as destination,
# hotel, and days of stay. Task: Write a function that prints all booking details passed as keyword
# arguments.
def booking_details(**details):
 for key, value in details.items():
   print(f"{key}\t\t\t: {value}")
booking_details(Name="Ali Akmal", Destination="Paris", Hotel="Hilton", Days=5)



















# 1. 
# Online Order Summary Scenario: An e-commerce platform wants to summarize customer order
# details. Task: Write a function that accepts order details as keyword arguments and prints a
# summary
def order_detail(**order):
    print(f"Order ID:{order.get('order_id')}")
    print(f"Customer:{order.get('customer')}")
    print("Items:")
    for item ,qnt in order.get('items',{}).items():
        print(f"{item}:{qnt}")
order_detail(order_id=101, customer="Ali", items={"Laptop": 1, "Mouse": 2})




# . 
# Event Registration Scenario: An event collects registration info like name, email, and ticket type. Task:
# Write a function that prints all registration info from keyword arguments.
def register_event(**info):
 print(f"Name: {info.get('fname')} {info.get('lname')}")
 print(f"Email: {info.get('email')}")
 print(f"Ticket Type: {info.get('ticket', 'General')}")
register_event(fname="Zara", lname="Ahmed", email="zara@example.com")