# strings are immutable
a ="harry"
print(len(a))
print(a.upper())
print(a.lower())



log = "2026-03-11 10:45:30 | ERROR | [404] | Page Not Found: /api/v1/users"
# spliting data
parts=log.split("|")[2].strip().strip("[]")
messege=log.split("|")[3].strip().split (":")[0]

result={
    "code":parts,
    "Messege":messege
}

print(result)


# qno

csv_list=["  albert EINSTEIN", "nIkoLa TeSlA  ", " marie CURIE "]

clean_list=[]
for name in csv_list:
    parts=name.strip().title()
    clean_list.append(parts)

print("Clean List :",clean_list)




# qno

card_num="4532-7190-2234-8810"
parts=card_num.split("-")

for i in range(3):
    parts[i]=parts[i].replace(parts[i],"****") 

result="-".join(parts)
print(result)





user_p="userProfileSettings"
result=""
for char in user_p:
    if char.isupper():
        result += "_" + char.lower()
      
    else:
        result += char
print(result)

email="Jamal.Khan@GMAIL.com"
lower_case=email.lower()
print(lower_case)




application = "I have experience in Java and C++ "
if "python" in application:
    print("Python finded ate index",application.index("python"))
else:
    print("Python not founded in data")

name="Jamal Ahmad Khan"


print(name.split(" ")[2])





full_name = "Jamal Ahmad Khan"

last_name = full_name.rsplit(" ", 1)[-1]

print(last_name)





#
s="32"
u=str(s).zfill(4)
print(u)











id_col = "ID"
name_col = "Name"
score_col = "Score"

print(id_col.center(6), name_col.center(12), score_col.center(8))