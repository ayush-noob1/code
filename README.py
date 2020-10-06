a=0
str=input("enter word: ")
list1=[]
for a in str:
    list1=list1 + [a]
list2=list1[::-1]
if list1 == list2:
    print(str,"is a palindrome")
else:
    print(str,"isnt a palindrome")
