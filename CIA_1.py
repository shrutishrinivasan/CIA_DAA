# prints matrix
def print_matrix(arr):
    for i in a:
        for j in i:
            print(j,end=" ")
        print()
  
# returns maximum out of 3 numbers
def get_max(x,y,z):
    r=0
    if (((x>y) and (x>z)) or ((x==y) and (x>z)) or ((x==z) and (x>y))):
        r = x
    elif (((y>x) and (y>z)) or ((y==z) and (y>x))):
        r = y
    else:
        r = z
        
    # no negative value for mismatch
    if (r<0):
        return 0
    else:
        return r
 
# match score = +2       
def match(arr,i,j):
    return arr[i-1][j-1] + 2

# mismatch score = -1
def mismatch(arr,i,j):
    a = arr[i][j-1] - 1
    b = arr[i-1][j-1] - 1
    c = arr[i-1][j] - 1
    return get_max(a,b,c)

# returns max score and the corresponding index positions
def get_max_score(arr):
    l=[]
    for i in range(n+1):
        for j in range(n+1):
            l.append(arr[i][j])
            
    m = max(l)
    for i in range(n+1):
        for j in range(n+1):
            if arr[i][j] == m:
                return m,i,j
            
def traceback_position(arr,i,j):
    value = arr[i][j]
    if arr[i-1][j-1]+2 == value:
        new=arr[i-1][j-1]
        return new,i-1,j-1
    else:
        if arr[i-1][j-1]-1 == value:
            new=arr[i-1][j-1]
            return new,i-1,j-1
        
        elif arr[i-1][j]-1 == value:
            new=arr[i-1][j]
            return new,i-1,j
        
        elif arr[i][j-1]-1 == value:
            new=arr[i][j-1]
            return new,i-1,j
        
        
        
# main code
str1 = input("Enter string1: ")
str2 = input("Enter string2: ")

n = len(str1)

a = []
for i in range(n+1):
    temp=[]
    for j in range(n+1):
        temp.append(0)
    a.append(temp)
 
print("\nBefore Alignment: ")      
print_matrix(a)
print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if str2[i-1] == str1[j-1]:
            a[i][j] = match(a,i,j)
        else:
            a[i][j] = mismatch(a,i,j)
            
print("After Alignment: ")
print_matrix(a)
print()

m,i,j=get_max_score(a)
print("Max score:",m)
print("Index position of max score:",i,j)
print()

