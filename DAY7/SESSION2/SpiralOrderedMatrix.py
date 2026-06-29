def spiralOrder(matrix,m,n):
    top=0
    left=0
    bottom=m-1
    right=n-1

    while top<=bottom and left<=right:
        # First Row
        for i in range(left,right+1):
            print(matrix[top][i],end=" ")
            # 1 2 3
        top+=1
        # Right Column
        for i in range(top,bottom+1):
            print(matrix[i][right],end=" ")
            # 6 9
        right=right-1
        # 8 7
        # Bottom row
        if top<=bottom:
            for i in range(right,left-1,-1):
                print(matrix[bottom][i],end=" ")

        bottom=bottom-1
        # Print 4 and 5
        if left<=right:
            for i in range(bottom,top-1,-1):
                print(matrix[i][left],end=" ")

            left=left+1
# Main 
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix,3,3))
