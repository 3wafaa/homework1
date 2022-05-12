from msilib.schema import Binary
binary=[]
n = int(input("Enter the decimai number :"))
m = n
while m!=0:
    l=m%2
    binary.append(l)
    m=m//2
binary.reverse()
k=" "
for i in binary:
    k=k+str(i)
print("Decimil :",n,"<===>","binary :",k)
