# i=0
# while i<3:
#     print(i)
#     i+=1


# count=5
# while count>0:
#     print(count)
#     count-=1
# else:
#     print("i am inside else")
#     print("This is else loop")





# count=0
# while True:
#     temp=float(input("Enter temprature reading :"))
#     count+=1
#     if temp>50:
#          print("Warning! High Temprature detected:")
#          break

# print("Collected Readings:",count)









# # qno 
# login_count=0
# correct_pass="mrd123"
# while True:
#     passoword=input("Enter the password :")
#     if passoword==correct_pass:
#         print("Login Successful! Thank you:")
#         break
#     else:
#         login_count+=1
#         print("Incorrect password")
#     if login_count==5:
#             print("Login attempt used:")
#             break






# # qno
# threshold_value=50
# while True:
#      stock_prices=int(input("Enter the price of stock :"))
#      print("Price of stock:",stock_prices)
#      if stock_prices < threshold_value:
#         print("⚠ Stop-loss triggered! Sell the stock.")
#         break
#      print("Price is safe. Continue monitoring.")






# qno 
data=[45,54,6,6,7,4,44,665,556,None,"",None,65,57,None,None,54]
clean_list=[]
i=0
while i<len(data):
    if data[i] is not  None and data[i] != "":
        clean_list.append(data[i])
    i+=1

print("Clean list Of Data:",clean_list) 




data = list(range(1, 36))

batch_size = 10
start = 0

while start < len(data):

    batch = data[start:start + batch_size]

    print("Processing Batch:", batch)

    # simulate processing
    print("Batch size:", len(batch))

    start += batch_size













data=list(range(1,36))
batch_size=10
start=0

while start >len(data):
    batch=data[start:start+batch_size]
    print("Processig batch :",batch)
    print("Length of bathc:",len(batch))

    start+=batch_size






# qno 

# Initial value
value = 10
iteration = 0

while True:
    iteration += 1

    # store previous value
    old_value = value

    # update rule (example optimization step)
    value = value - 0.2 * value   # reduces value gradually

    # calculate difference
    difference = abs(value - old_value)

    print(f"Iteration {iteration}: value={value:.4f}, diff={difference:.4f}")

    # convergence condition
    if difference < 0.01:
        print("✅ Convergence reached!")
        break











# qno
logs = [
    "INFO: System started",
    "INFO: User login",
    "WARNING: Memory high",
    "INFO: Backup running",
    "ERROR: Database failed",
    "INFO: Restart complete"
]
index=0

while index<len(logs):
    log=logs[index]
    print("Scannig:",log)
    if "ERROR" in log:
        print("Error detected : Stopping stop.")
        break
    index+=1

data = [10, 25, 5, 2, 50]

iteration = 0

# keep running until all values are between 0 and 1
while max(data) > 1:

    iteration += 1
    print(f"\nIteration {iteration}")

    # scale values
    for i in range(len(data)):
        data[i] = data[i] / 10

    print("Scaled data:", data)

print("\n✅ All values normalized between 0 and 1")






data = [10, 25, 5, 2, 50]
iteration=0

while max(data) >1:
    iteration+=1
    for i in range(len(data)):
        data[i]=data[i]/10

    print("Scaled Data:",data)

print("\nALL values normalized between 0 and 1")











data = [
    [25, 70, 180],
    [30, 65, 175],
    [22, 80, 169]
]
 
row=0
while row <len(data):
    col=0
    while col <len(data[row]):
        print(f"Row {row+1},Col {col+1} ={data[row][col]}")
        col+=1
    row+=1







# qno 
# row wise sum calculator
data = [
    [25, 70, 180],
    [30, 65, 175],
    [22, 80, 169]
]
sum_total=0
row=0
while row<len(data):
    col=0
    while col<len(data[row]):
        sum_total+=data[row][col]
        col+=1
    print(f"Row {row + 1} sum ={sum_total}")

    row+=1




# qno 

data = [
    [25, 70, 180],
    [30, 65, 175],
    [22, 80, 169]
]

target=65
col =0
found=False 
while col <len(data[0]):
    row=0
    while row<len(data):
        if data[row][col]==target:
            print(f"Target value {target} found at row {row+1},col{col+1}")
            found=True
            break

        row+=1
        
    if found==True:
        break
    col+=1



#  12. Dataset Pattern Counter: Count occurrences of a value using nested while loops.
data = [
    [25, 70, 70],
    [30, 70, 175],
    [22, 70, 169]
]
target=70
row=0

count=0
while row <len(data):
    col=0
    while col<len(data[row]):
        if data[row][col]==target:
            count+=1
            print(f"Target value {target} occured at row {row+1},col {col+1}")
        col+=1
    row+=1

print(f"Target value {target} occured {count}")









# qno 
# 13. Mini Image Processor: Treat a 2D list as image pixels and count bright pixels (>200)
image = [
    [180, 220, 150],
    [255, 90, 210],
    [200, 205, 100]
]

count=0
row =0
defined_value=200     # bright pixel value
while row <len(image):
    col =0
    while col <len(image[row]):
        if image[row][col]>defined_value:
            count+=1
            print(f"Bright pixels found at row {row+1},col {col+1}")
        col+=1
    row+=1

print(f"Total number of count of bright pixel  is {count} ")



classes = [
    [75, 80, 90],  # Class 1 scores
    [60, 85, 70],  # Class 2 scores
    [95, 100, 85]  # Class 3 scores
]

row =0
while row<len(classes):
    col=0
    total_sum=0
    while col<len(classes[row]):
        total_sum+=classes[row][col]
        col+=1
    print(f"Sum of Class {row+1} is {total_sum}")
    row+=1