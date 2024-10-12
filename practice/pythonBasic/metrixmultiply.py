
#multiplicatio to matrix 
#Md Arif howlader CSE2102023084


def input_matrix():
   
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

   
    matrix = []

    print("Enter the matrix row by row:")
    for i in range(rows):
       
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("Error: The number of elements in this row does not match the number of columns.")
            return None
        matrix.append(row)

    return matrix

A=input_matrix()

B=input_matrix()

# Print the B

result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
if A and B:
    print("Matrix A is :")
    for row in A:
        print(row)
    print("Matrix B is :")
    for row in B:
        print(row)
    if len(A[0])!=len(B):
        print("matrix multiplication is not possible")
    else:
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j]+=A[i][k]*B[k][j]
        print("result is : ")
        for r in result:
            print(r)

else:
    print("please enter Two valid matrix !!!!")
    