from re import X


def skill(val,list=[]):
    list.append(val)
    return list

list1= skill("Node js")
list2= skill("Java",[])
list3= skill("React js")
print("%s" %list1)
print("%s" %list2)
print("%s" %list3)


l1=[1,2,3,4,5]
l2 = [10,22,44,55]

print(l1.append(l2))