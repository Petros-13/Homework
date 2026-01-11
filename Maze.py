def mazePath(r, c, n, m):
    
    if r == n - 1 and c == m - 1:
        return 1
    

    if r >= n or c >= m:
        return 0


    right = mazePath(r, c + 1, n, m)

    down = mazePath(r + 1, c, n, m)

    # Total paths from this cell
    return right + down



n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))


print("Total paths:", mazePath(0, 0, n, m))
