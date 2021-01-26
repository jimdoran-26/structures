data = {1:'jim',2:'andy'}
print(data)

print(data[1])#will give error
print(data.get(1))#will return None

print(data.get(3,'Not Found'))

keys = ['chris','alex']
values = ['python','java']
data = dict(zip(keys,values))
print(data)

data['brendon']= 'react'
del data['alex']
print(data)

prog = {'JS':'Adam', 'CS':['VS','Java']}
print(prog)


def checkKey(dict, key):
    if key in dict.keys():
        print("Present, ", end=" ")
        print("value =", dict[key])
    else:
        print("Not present")

print(checkKey(prog,'JS'))
