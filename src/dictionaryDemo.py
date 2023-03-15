# Supports {Key:Value} Pair.
# While Printing also use Quotes to String and also for assigning in dic use Quotes to charecters and Strings
dic = {"a": 3, 4: "b", "c": "Hello Boy", 3: 6, "answer": "5"}
print(dic)
print(dic[4])
print(dic['a'])
print(dic['c'])
print(dic['answer'])
print(dic[3])

# Create dict at runtime and add data into it.
newDic = { }
newDic["First Name"] = "FName"
newDic["Last Name"] = "LName"
newDic["Gender"] = "Male"
print(newDic)