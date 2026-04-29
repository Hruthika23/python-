l1 = [1,2,3,3,4]
name = ['sam','akshata','Hruthika','Kriti']
print("l1 + name =",l1 + name)
print("name *2 =",name * 2)
print("name[2] =",name [2])
print("name[1:4]=",name[1:4])
print("'Krish' in name=",'Krish' in name)
print("'67' not in l1=",'67' not in l1)
print("the list of names are \n")
for i in name:
    print(i)
name.insert(4,'smrithi')
print ("after inserting=",name)
name.pop(2)
print("after pop =", name)
name.remove('Kriti')
print("after removing", name)
name.clear()
print("Afetr clearing",name)