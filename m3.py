n = int(input("Enter a no. of triangles "))

for i in range(0,n):
    for j in range(i+1, n+1):
        print("*", end = " ")
    print()