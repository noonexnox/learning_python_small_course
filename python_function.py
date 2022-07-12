def hello():
    print ("my name is The Rock")
def world():
    print (10+20+30)

hello ()
world ()

#now let's pass parameter through it
def hello(fname, lname): #you can also replace it by (f,l)
    print (fname, lname) #you can also replace it by (f,l)
fname = "The"
lname = "Rock"
hello (fname, lname)
