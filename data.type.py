#numbers
a = 10
print (type(a))
b = 10.5
print (type(b))
c = 10 + 2j #here 10 + 2j => x + yj. It's an complex number
print (type(c))

#list
d = [10, 10.5, 20]
print (d[0])
print (d[1])
print (d[2])

fruits = ["apple", "mango", "grapes"]
print (type(fruits))

fruits.insert(0, "banana")
print(fruits)

#tuple
fruits = ("apple", "mango", "grapes")
print (type(fruits))

fruits.insert(0, "banana")
print(fruits)


#string
e = "Hello World"
print(type(e))
#multiple line string
f = '''
#Hi this is multiple line string
#We can use multiple lines for this string
'''
print (f)

#set
f = {1, 4, 4, 7, 9, 2, 6}
print(type(f))
print(f)

#dictionary
g = {69: "Hello", 108: "World"}
print (type(g))
#use of dictionary
print (g[69])
print (g[108])