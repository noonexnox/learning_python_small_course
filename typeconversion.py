
#implicit type convertion
a = 10 #int
b = 20.5 #float
c = a + b #it should be float
print (type(a))
print (type(b))
print (type(c))

#explicit type conversion
a = 10
b = "20"
#now if I add this we'll get error
c = int(b) #now I've converted b into integer & stored in c
d = a + c
print (type(d))
print (d)