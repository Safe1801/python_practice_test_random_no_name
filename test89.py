var=['c','h','a','i','n']
one=[]
two=[]
three=[]
four=[]
five=[]
for i in var:
    result=''
    if i=='c':
        one.append(i)
    elif i=='h':
        two.append(i)
    elif i=='i':
        three.append(i)
    elif i=='n':
        four.append(i)
    elif i=='a': 
        five.append(i)
    x_one=result.join(one)
    x_two=result.join(two)
    x_three=result.join(three)
    x_four=result.join(four)
    x_five=result.join(five)
print(type(x_one+x_two+x_three+x_four+x_five))
print(x_one+x_two+x_three+x_four+x_five)



 












