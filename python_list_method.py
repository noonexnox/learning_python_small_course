#append()
fruit = ["apple", "mango", "grapes"]
print (fruit)
print (fruit)
fruit.append("banana")

#extend()
lang = ["English", "Hindi"]
lang1 = ["French", "German"]
#lang.extend(lang1)
lang1.extend (lang)
print (lang1)

#index()
lang = ['English', 'Hindi', 'French', 'German']
print (lang.index("English"))

#insert()
lang = ["English", "Hindi", "French"]
lang.insert(1, "German")
print (lang)

#count()
list_int = [1,2,3,1,2,1,1,5]
print (list_int.count(1))

#remove()
lang = ["English", "Hindi","French"]
lang.remove("French")
print (lang)

#pop()
lang = ["English", "Hindi", "French"]
print (lang)
lang.pop(1)
print (lang)

#reverse()
lang = ["English", "Hindi","French"]
print (lang)
lang.reverse()
print (lang)

#sort()
list_int= [1,5,4,7,8,3,2,1]
list_int.sort()
#sort in assescending order
print (list_int)
#sort in descending order
list_int.sort(reverse=True)
print (list_int)