# # conditional stat
# # control flow statement
# # break
# # continue
# # pass



# x=10
# if x>0:
#     print("x is greate than 0")
# elif x<0:
#     print("x is less than 0")
# else:
#     print("x is zero")






# # for loop 
# food=["biryani","daal","Samosay","Shami","Palak Paneer"]
# for i in food:
#     print(i)

# # i=1
# # while i<6:
# #     print(i)
# #     i+=1

# # for letter in "python":
# #     if letter=="h":
# #         break
# #     print(letter)



# # for letter in "python":
# #     if letter=="h":
# #         continue
# #     print(letter)





# for letter in "python":
#     if letter=="h":
#         pass
#     print(letter)








# # qno
# total_sales=0
# for day in range(1,8):
#     sales=int(input(f"Enter the sales of day {day}"))
#     total_sales+=sales


# ave_sales=total_sales/7

# print(f"Total sales:{total_sales}")
# print(f"Average Sales:{ave_sales:.2f}")





# # qno 
# transaction_amount=float(input("Enter the transaction amount:"))
# loaction=input("Is the loction unusual(yes or no)").lower()

# if transaction_amount>50000 and loaction=="yes":
#     print("Fruad Alert!")
# else:
#     print("Transaction Is Normal")



# # Stop Processing Invalid Data (break)

# print("Enter dataset values (enter -999 to stop):")

# while True:
#     value = int(input("Enter value: "))

#     # stop condition
#     if value == -999:
#         print("Missing value detected. Stopping processing...")
#         break

#     print("Processing value:", value)






#  qno 
list_values=[889,8,9,5,66,7,4,-1,-4,6,-89]
for i in list_values:
    if i <0:
        continue
    print(i)







# qno 
correct_password="123@akamal"
attempt=0
while attempt<3:
    user=input("Enter the password:")
    if user==attempt:
        print("Login Successful:")
        break
    else:
        attempt+=1
        print("Incorrect Password:")
    if attempt==3:
        print("Account Locked")