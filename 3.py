import json
x1=0
x2= {}
x3 = []
name = input(" name :")
with open("wa.json","r") as f:
    wa=json.loads(f.read())
    for i in wa :
        print(i)
        n = input("enter  a or b :")
        x3.append(n)
        if n ==wa[i]:
            x1=x1+1
        else:
            x1=x1-1

    x2 ={name:x3}
    print(x2)

    print("The result :",x1)
    
