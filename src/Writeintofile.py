#Read the file and store all the lines in list
#Reverse th elist
#Write the list back to the file

with open('text.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('text.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)