def spiralCopy(arr):
    rows = len(arr)
    columns = len(arr[0])
    top = 0
    bottom = rows - 1
    left = 0
    right = columns - 1
    direction = 0
    output = []
    
  
    while ( top <= bottom and left <= right):
    
        if direction == 0:
            # moving from left to right top row -> [1, 2, 3, 4]
            # top = 0; left = 0; right = 3
            for i in range(left, right+1):
                output.append(arr[top][i])
            top = top + 1
            direction = 1
            # top = 1
        elif direction == 1:
            # moving from top to bottom last column -> [4
            #                                            7
            #                                            11
            #                                           15]
            # top = 1; bottom = 3; right = 3
            for i in range(top, bottom+1):
                output.append(arr[i][right])
            right = right - 1
            direction = 2
            # right = 2
        elif direction == 2:
            # moving from right to left , bottom row - > [12, 13, 14, 15]
            # right = 2; left = 0; bottom=3
            for i in range(right, left-1, -1):
                output.append(arr[bottom][i])
            bottom = bottom - 1
            direction = 3
            # bottom = 2
        elif direction == 3:
            # moving from bottom to top , first column - >[ 1
            #                                               4
            #                                               8
            #                                               12]
            # bottom = 2; top = 1; left = 0
            for i in range(bottom, top-1, -1):
                output.append(arr[i][left]) 
            left = left + 1
            direction = 0
            # left = 1
    return output

arr = [[1, 2, 3, 4],
    [4, 5, 6, 7],
    [8, 9, 10,11],
    [12, 13, 14, 15]]

spiralCopy(arr)