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