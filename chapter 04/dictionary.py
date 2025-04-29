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

student = {"name": "hamza", "marks": {"math": 90, "ict": 80, "pf": 70}, "age": 22, "country": "Pakistan"} 
print(student.update({"marks": 100}))
print(student)
