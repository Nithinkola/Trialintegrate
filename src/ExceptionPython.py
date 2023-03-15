ItemsInCart = 0
# 2 items will be added to cart

# raise Exception to fail testcase
if ItemsInCart != 2:    # raise Exception("Product Cart count not matching")
    pass

# assertion condition to fail testcase
assert(ItemsInCart == 0)    # asset condition. true
# assert(ItemsInCart == 2)  # Whenever assert condition is false then testcase fails.

# try, catch mechanism
try:
    with open('text.txt', 'r') as reader:
        reader.read()
except:
    print("Somehow i reached this block because there is failure(no given filename found) in try block")
finally:
    print("Cleaning up resources")

# try, catch to catch error what python thrown.
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

# finally Keyword executed if pass or fail testcase
finally:
    print("Cleaning up resources")