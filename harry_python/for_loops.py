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