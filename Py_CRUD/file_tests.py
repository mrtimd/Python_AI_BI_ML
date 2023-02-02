import json

#f = open("myfile.txt", "x")

f = open("demofile2.txt", "w")
f.write('{ "name":"Tim", "age":250, "city":"Sunrise"}')
f.close()

#open and read the file after the appending:
#f = str(open("demofile2.txt", "r"))
#print(f.read())

f = open("demofile2.txt", "r")
data = f.read()
print(data)

# parse x:
y = json.loads(data)

# the result is a Python dictionary:
print(y["age"])