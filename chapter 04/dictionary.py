# info = {"name": "hamza", "age": 22, "country": "Pakistan"}
# print(info)
# 
# info = {"name": "hamza", "subject": ["math", "ict", "pf"], "age": 22, "country": "Pakistan"}
# print(info)  

# info = {"name": "hamza", "age": 22, "country": "Pakistan"}
# print(info["country"], info["name"])

        #   nested dictionary
# student = {"name": "hamza", "marks": {"math": 90, "ict": 80, "pf": 70}, "age": 22, "country": "Pakistan"} 
# print(student["marks"])

# student = {"name": "hamza", "marks": {"math": 90, "ict": 80, "pf": 70}, "age": 22, "country": "Pakistan"} 
# print(student["marks"]["ict"])

# student = {"name": "hamza", "marks": {"math": 90, "ict": 80, "pf": 70}, "age": 22, "country": "Pakistan"} 
# print(student.keys())  # returns all keys of the dictionary

# student = {"name": "hamza", "marks": {"math": 90, "ict": 80, "pf": 70}, "age": 22, "country": "Pakistan"} 
# print(student.values())  # returns all values of the dictionary

# student = {"name": "hamza", "marks": {"math": 90, "ict": 80, "pf": 70}, "age": 22, "country": "Pakistan"} 
# print(student.items()) # returns all items of the dictionary in list form

# student = {"name": "hamza", "marks": {"math": 90, "ict": 80, "pf": 70}, "age": 22, "country": "Pakistan"} 
# print(student.get("marks")) # returns the value of the key "marks" in the dictionary

# student = {"name": "hamza", "marks": {"math": 90, "ict": 80, "pf": 70}, "age": 22, "country": "Pakistan"} 
# print(student.update({"name": "ali"})) # updates the value of the key "name" in the dictionary to "ali"
# print(student) # prints the updated dictionary

# student = {"name": "hamza", "marks": {"math": 90, "ict": 80, "pf": 70}, "age": 22, "country": "Pakistan"} 
# print(student.update({"marks": 100}))
# print(student)

# info = {"name": "hamza", "age": 22, "country": "Pakistan"}
# print(info.update({"name": "Khan"}))  # updates the value of the key "name" in the dictionary to "Khan"
# print(info)  # prints the updated dictionary
# info["name"] = "Khan"
# print(info)  # updates the value of the key "name" in the dictionary to "Khan"
# print(info.get("country"))  # returns the value of the key "country" in the
# print(info.keys())  # returns all keys of the dictionary
# print(info.values())  # returns all values of the dictionary
# print(info.items())  # returns all items of the dictionary in list form
# print(info["country"])


                # nested dictionary with subject marks
# student = {
#     "name": "hamza",
#     "subject" : {
#         "math": 60,
#         "ict": 70,
#         "pf": 80
#     }
# }
# # print(student["subject"])  # prints the subject marks dictionary
# print(student["subject"]["math"])  # prints the marks of math subject

# dict = {
#     "cat": "a small animal",
#     "table": ["a piece of furniture", "list of fact & figures"]
# }
# print(dict)  # prints the dictionary
# print(dict["cat"])  # prints the definition of "cat"

marks = {}
x = int(input("Enter Phy number: "))
marks.update({"phy" : x})

x = int(input("Enter chem number: "))
marks.update({"chem" : x})

x = int(input("Enter math number: "))
marks.update({"Math" : x})

print(marks)
