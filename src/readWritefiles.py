file = open('text.txt')

#print(file.read())      #Read all contents of file
print(file.read(5))     #Read n number of charecters by passing parammeters

# read one single line at a time using readLine()
print(file.readline())
print(file.readline())

#Print line by line using readLine() method and while loop
line = file.readline()      # apple, dog, elephant
while line != "":
    print(line)
    line = file.readline()  # ball, elephant, blank

#Print line by line using readLines() method and for loop
for line in file.readlines():
    print(line)



file.close()