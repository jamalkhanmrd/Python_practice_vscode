for i in "abdulahad":
    print(i)
    if i =="b":
        print("this is b ")



color=["red","green"]
for colors in color:
    print(colors)
    for i in colors:
        print(i)




# for k in range(51):
#     print(k)
# for k in range(1,50,2):
#     print(k)
 
# row counter

records = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
]
# Initialize counter
row_count=0
# Count rows using a for loop
for record in records:    # Increment counter for each row
    row_count+=1


print(f"Total Rows in Dataset:{row_count}")




# qno
dataset_colum=[
     {"id":1,"name":"alice","age":25},
     {"id":2,"name":None,"age":45},
     {"id":3,"name":"charlie","age":None},
     {"id":4,"name":"","age":44}
]
# initialized counter
count_missing=0
# using for loop for finding missing values or none
for colums in dataset_colum:
    for colum in colums.values():
        if colum is None or colum=="":
            count_missing+=1

print(f"Total Missing Valued in Dataset Colums:{count_missing}")









# Missing Value Finder

# Example dataset: list of dictionaries
records = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": None, "age": 30},
    {"id": 3, "name": "Charlie", "age": None},
    {"id": 4, "name": "", "age": 22},
]

# Column to check for missing values
column_name = "age"

# Initialize counter
missing_count = 0

# Iterate through dataset and count None or empty values
for record in records:
    value = record.get(column_name)
    if value is None or value == "":
        missing_count += 1

print(f"Total missing values in column '{column_name}': {missing_count}")











# Text Length Analyzer

# Example list of customer reviews
reviews = [
    "Great product, very satisfied!",
    "Average quality, could be better.",
    "Excellent service and fast delivery.",
    ""
]

# List to store lengths of each review
review_lengths = []

# Loop through reviews and calculate length
for review in reviews:
    length = len(review)  # Count number of characters
    review_lengths.append(length)

# Print the lengths
for i, length in enumerate(review_lengths, start=1):
    print(f"Review {i} length: {length} characters")

# qno
#  Sales Dataset Analyzer: You have a list of daily sales numbers for a store. Loop through the
# list and calculate the total sales, average sales, and identify days where sales exceeded a
# given threshold.

sales = [4200, 5100, 6100, 3900, 7200, 4500, 8000]
threshold = 5000

# variables intializations
total_sales=0
high_sales_days=[]


# using for loops
for  day,amount in enumerate(sales,start=1):
    total_sales+=amount
    if amount >threshold:
        high_sales_days.append((day,amount))

average_sales=total_sales/len(sales)

print("Total Sales:",total_sales)
print("Averege Sales:",round(average_sales,2))
print("High Sale Days:",high_sales_days)




# qno
# . Missing Data Detector: A dataset column is represented as a Python list containing numbers
# and None values. Write a loop that counts how many missing values exist and returns their
# indexes.

# list of data
data = [23, None, 45, 67, None, 89, None, 34]

# varaible for counting 
missing_value_count=0
list_of_values=[]
# using for loop for counting
for place,list_value in enumerate(data,start=1):
    if list_value is None:
        missing_value_count+=1
        list_of_values.append(place)
print("Missing values count:",missing_value_count)
print("Missing Values in Dataset Column:",list_of_values)





# qno
# . Customer Review Length Analyzer: Given a list of customer review texts, use a loop to
# compute the length of each review and store the results in a new list.
reviews = [
    "Great product and fast delivery",
    "Not satisfied",
    "Amazing quality, highly recommended",
    "Average experience"
]
# finding length of reviews using for loop
length_review=0
new_list_for_rev=[]
for place,review_length in enumerate(reviews,start=1):
    length_review=len(review_length)
    new_list_for_rev.append((place,length_review))

print("Review Length:",new_list_for_rev)










# qno 
# Transaction Categorizer: You have a list of transaction amounts. Use a loop to classify them into 'low', 'medium', and 'high' categories depending on value ranges
# list of transactions
transactions = [45, 120, 75, 600, 320, 900, 50]
# list to store results
transactions_categ_list=[]
# loop through transactions
for amount in transactions:
    if amount<100:
        category="Low"
    elif amount < 500:
        category="Medium"
    else:
        category="High"
    transactions_categ_list.append((amount,category))
print("Transaction Categories:",transactions_categ_list)\







#qno 
#Feature Scaling Simulation: Given a list of numeric values representing a dataset column,
#  loop through the list and normalize the values using a simple min-max scaling formula.
# dataset column
data = [10, 20, 30, 40, 50,80]

# find min and max
min_value = min(data)
max_value = max(data)

# list for normalized values
normalized_data=[]

# using for loop for feature scaling
for value in data:
    scaled_value=(value-min_value)/(max_value-min_value)
    normalized_data.append(scaled_value)

# print result
print("Normalized Data:",normalized_data)




# qno
# 6. Log File Processor: You have a list of log strings from a system.
#  Loop through each log entry and extract only those that contain the keyword 'ERROR'.
logs = [
    "2026-03-14 09:00:00 INFO User login successful",
    "2026-03-14 09:05:12 ERROR File not found",
    "2026-03-14 09:10:23 WARNING Disk space low",
    "2026-03-14 09:15:45 ERROR Connection timeout",
    "2026-03-14 09:20:00 INFO Backup completed"
]
# list to store only error logs
error_logs = []
for log in logs:
    if "error" in log.lower():
        error_logs.append(log)
print("Error Logs:")
for error in error_logs:
    print(error)






# qno 
# Dataset Summary Statistics: Given a list of numbers representing a dataset column,
# calculate the minimum, maximum, and sum using a loop instead of built-in functions.
# 
colum_dataset=[45,65,66,8,3,5,4,66,75,80,39,60,94]
# variables for sum, min , max
sum_colum=0
min_colum=colum_dataset[0]
max_colum=colum_dataset[0]

# using loop
for value in     colum_dataset:
    sum_colum+=value
    if value <min_colum:
        min_colum=value

    if value > max_colum:
        max_colum=value


# result
print("Total Sum :",sum_colum)
print("Minimum Num :",min_colum)
print("Maximum Num:",max_colum)






# qno 
# Index-based Dataset Inspection: Use enumerate() to loop through a dataset column and print
# the index and value only when the value is greater than a specified threshold.

# Sample dataset (e.g., a list representing a 'Sales' column)
dataset_column = [120, 45, 300, 89, 150, 20, 410]
threshold = 100

print(f"Indices with values greater than {threshold}:")
print("-" * 35)
for indices,value in enumerate(dataset_column,start=1):
    print(f"Index {indices} | Value :{value}")






# 2nd way

# Sample dataset (e.g., a list representing a 'Sales' column)
dataset_column = [120, 45, 300, 89, 150, 20, 410]
threshold = 100
new_list=[]

print(f"Indices with values greater than {threshold}:")
print("-" * 35)
for indices,value in enumerate(dataset_column,start=1):
    new_list.append((indices,value))
    # print(f"Index {indices} | Value :{value}")

print(new_list)



# Matrix Row Sum Calculator (Nested Loop): A dataset is represented as a 2D list (rows and
# columns). Use nested loops to calculate the sum of each row.

dataset = [
    [10, 20, 30],
    [5, 15, 25],
    [7, 14, 21]
]
for row_index, row in enumerate(dataset):
    row_sum=0
    
    for value in row:
        row_sum+=value
    
    print(f"Sum of Row {row_index+1} :{row_sum}")







# qno 
#  Matrix Column Sum Calculator (Nested Loop): Given a 2D list representing tabular data,
# use nested loops to compute the sum of each column.


dataset = [
    [10, 20, 30],
    [5, 15, 25],
    [7, 14, 21]
]
num_colum=len(dataset[0])
for col in range(num_colum):
    
    col_sum=0

    for row  in dataset:
        col_sum+= row[col]
    
    print(f"Sum of colum {col+1} :{col_sum}")







# qno 
dataset = [
    [1, 2, 3],
    [4, 2, 6,3],
    [7, 8, 2,3]
]
target_value=3
count=0
# outer loop for row
for row in dataset:
    # inner loop for col 
    for value in row:
        if value == target_value:          # comparing inner loop value with target value
             count+=1

print(f"Target Value {target_value}: Count :{count}")





dataset = [
    [10, 20, 30],
    [15, 25, 35],
    [12, 22, 32]
]

num_features = len(dataset[0])

# outer loop → first feature
for i in range(num_features):

    # inner loop → second feature
    for j in range(i + 1, num_features):

        print(f"Feature {i+1} & Feature {j+1}")