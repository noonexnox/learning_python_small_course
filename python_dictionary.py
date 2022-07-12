my_dict = {"fruit":"apple","veg":"carrot"}
print (my_dict)

#here is the way to print only the keys
print (my_dict.keys())

#here is the way to print only the values
print (my_dict.values())

#here is the way to call the values from keys
print(my_dict["fruit"])

#now to add multiple values in one key you need to use list of the values
my_new = {"fruit":["apple","mango","grapes"], "veg": ["carrot","potato", "tomato"]}

#in simillar ways you can print
print (my_new)
print (my_new.keys())
print (my_new.values())
print (my_new["fruit"])

#now if you want to print a particular value then
print (my_new["fruit"][0])
