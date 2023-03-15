# List elemnts
values = [1, 2, "Nithin", 4.2, 6]

# List is a datatype that allows multiple  values and can be different data types.
print(values[0])
print(values[2])
print(values[3])

print("\nAll elements in List Using range function:")
for i in range(5):
    print(values[i])
print("\n")
print("\nAll elements in List directly without range function:")
for i in values:
    print(i)
print("\n")
# short cut for last index value
print("{} {}".format("last index value:", values[-1]))

# SubList of a List
print(values[1:4])
print("\n")
#Reverse of List
print(values[::-1])
print("\n")
# Inserting a new element into a list
values.insert(3, "Kola")
# Length of List :
n = len(values)
# Or can also print list directly
print(values)


values.append("End")
print(values)

values[2]="NITHIN"
print(values)

del values[0]
print(values)