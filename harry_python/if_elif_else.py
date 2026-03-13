a=16
print("age is ",a)
if a>18:
    print("drive")
else:
    print("not drive")



# qno 
data_quality=21                 # percent
if data_quality>20:
    print("Poor Data Quality")
elif data_quality>=10:
    print("Moderate Quality:")
else:
    print("Poor Quality:")




# qno
customer_amount=1500

if customer_amount>=1000:
    print("Premium Customer:")
elif customer_amount>500:
    print("Gold Customer:")
else:
    print("Reguler Customer:")



#qno  
data_size=50000           # rows
if data_size>1000000:
    print("Big Data:") 
elif data_size>100000:
    print("Medium Dataset:")
else:
    print("Small Dataset:")



# qno 
experience="INTERmediate".lower()
if experience=="beginner":
    print("Python Basics")
elif experience=="intermediate":
    print("Machine Learning:")
elif experience=="advanced":
    print("Deep Learning :")





# thermostate setting 
# qno 
temp=30  # celcius
people_presence="no".lower()     
if temp>28 and people_presence=="present":
    print("AC High:")
elif temp>28 and people_presence=="no":
    print("AC Eco")
elif temp>18 and people_presence=="present" or people_presence=="no":
    print("Off:")
elif temp<18 and people_presence=="present":
    print("Heat")
elif temp<18 and people_presence=="no":
    print("Freeze Protection:")






# qno 
customer_status="".lower()
order_total=105              # $ dollar
if order_total>100:
    discount=0.10*order_total
    finalbill=order_total-discount
    print("10 percent Discount added:")
    print("Order Total:",order_total)
    print("Final Bill:",finalbill)  
if customer_status=="premium":
    print("Shipping amount: 0$")
elif customer_status=="standered":
    if order_total>=50:
        print("Free Shipping:")
    else:
        print("Shipping amount:10$")
else:
    print("Invalid Membership type:")





# member_status = input("Enter membership type (Premium/Standard): ").lower()
# # order_total = float(input("Enter order total: $"))

# # Apply discount first
# if order_total > 100:
#     order_total = order_total * 0.10
#     print("10% discount applied!")

# # Shipping logic
# if member_status == "premium":
#     shipping_cost = 0

# elif member_status == "standard":
#     if order_total >= 50:
#         shipping_cost = 0
#     else:
#         shipping_cost = 10

# else:
#     print("Invalid membership type")
#     shipping_cost = 0

# final_total = order_total + shipping_cost

# print("Order Total:", order_total)
# print("Shipping Cost:", shipping_cost)
# print("Final Amount to Pay:", final_total)




# qno 
 
valid_passport="yes".lower().strip()
weight=50
user_class="economy".lower().strip()
if valid_passport!="yes":
    print("Travel not Allowed")
else:
    if user_class=="first":
     weight-=10
     print("First class allowance applied (extra 10kg)")
    if weight<=23:
        print("Proceed To Gate:")
    elif weight<=30 and weight>=24:
        print("Heavy luaggage fee required($50)")
    else:
        print("Too heavy. Must check-in at the counter.")






value="104"
# step 1 missing check
if value.lower() in ["none","nan"]:
    print("Missing")
else:
    value=float(value)
    if value<-100 or value>100:
        print("Outlier")
    elif value==0:
        print("Zero Reading:")
    else:
        print("Valid")
    






# Inputs
hours_worked = float(input("Enter hours worked: "))
is_weekend = input("Is it weekend? (yes/no): ").lower()
is_urgent = input("Is it urgent? (yes/no): ").lower() 

# Step 1 — Base and Overtime
base_rate = 50
overtime_rate = 75

if hours_worked <= 40:
    total = hours_worked * base_rate
else:
    total = 40 * base_rate + (hours_worked - 40) * overtime_rate

# Step 2 — Weekend multiplier (20% increase)
if is_weekend=="yes":
    total_dis = 0.20*total  # 20% increase
    total+=total_dis
# Step 3 — Urgent / Rush fee
if is_urgent=="yes":
    total += 100  # flat rush fee

# Step 4 — Output
print(f"Total Invoice Amount: ${total:.2f}")






# 2nd way
# Inputs
hours_worked = float(input("Enter hours worked: "))
is_weekend = input("Is it weekend? (yes/no): ").lower() == "yes"
is_urgent = input("Is it urgent? (yes/no): ").lower() == "yes"

# Step 1 — Base and Overtime
base_rate = 50
overtime_rate = 75

if hours_worked <= 40:
    total = hours_worked * base_rate
else:
    total = 40 * base_rate + (hours_worked - 40) * overtime_rate

# Step 2 — Weekend multiplier (20% increase)
if is_weekend:
    total *= 1.2  # or use your two-step method with total_dis

# Step 3 — Urgent / Rush fee
if is_urgent:
    total += 100  # flat rush fee

# Step 4 — Output
print(f"Total Invoice Amount: ${total:.2f}")
