name="harry,shubnam"
#1
print(len(name))
# we want to print start name
print(name[0:5])
print(name[:5])
print(name[-4:])



a="harry"
print(a[-4:-2])



# qno 
name="sales_2024.csv"
# extracting only year
year=name[-8:-4]
print("Year :",year  )




# qno 2
username="            data_scientist       "
removing_spaces=username.strip()
print("Cleaned Name:",removing_spaces)






# qno 3
email="ali.khan@gmial.com"
extract_name=email[9:]
print("Domain Name:",extract_name)




# qno 4
file_name="customer_data.xlsx"
extension=file_name[-5:]
print("Extension Name:",extension)







cnic= '35202-1234567-1'
last_digit=cnic[-6:]
print(last_digit)





# qno 6
name1='customer churn analysis report'
title_name=name1.title()
print("Name",title_name)








full_name="Ali Khan"
first_name=full_name.split()[0]
print("First Name:",first_name)




# qno 8
product_code="DS2025"
reverse_name=product_code[::-1]
print(reverse_name)


a="NA,45,467,NA,65,NA,435,NA"
count_name=a.count("NA")
print("Count Of NA :",count_name)



# qno 
null_string="23,null,45,null,45,null,76,null,null,54,67,89,null"
replace_null=null_string.replace("null","0")
print(replace_null)




# qno
date_info='2025-03-09'
month_info=date_info[5:7]
month_slice=date_info.split("-")[1]
print(month_info)
print(month_slice)



# qno 
city="Lahore"
year="2025"
# combined
combined_name=f"{city}_{year}"
print(combined_name)






# qno 
filename="sales.xlsx"
if filename.endswith(".csv"):
    print("This is a csv file:")
else:
    print("This is not a csv file :")




# 
coursename="DATA SCIENCE PIPELINE"
lower_case=coursename.lower()
print(lower_case)



#qno

dataset_name = "sales#data@2025!"
clean_name="".join(char for char in dataset_name if char.isalnum())
print(clean_name)
#qno


email='Ali.Khan@GMAIL.COM'
lower_case=email.lower()
print(lower_case)
a=' ali_khan '
print(a.strip())

#qno
review = "This course is very helpful for data science"

# Count words
word_count = len(review.split())

print(word_count)


b='model123version45'
e="".join(char for char in b if char.isalpha())
print(e)