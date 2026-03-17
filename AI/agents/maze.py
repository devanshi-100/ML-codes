import numpy as np

maze = np.zeros((4,4), dtype=int)

# list_of_walls = [(0, 1), (1, 0), (1, 2), (3, 0)]
# 0: path, 1: wall
start = (0,0)
print(maze.shape)
r,c=maze.shape

print(f"row={r},col={c}")
maze[1][1]=1
maze[1][2]=1
maze[1][3]=1
maze[2][1]=1

print(maze)
m,n=start
if maze[m][n]==1:
    print("Start is blocked")
else:
    print(f"traversing cell[{m}][{n}]")
    maze[m][n]=-1
    for m in range(4):
        for n in range(4):
            # if maze[m][n]==1:
            #     continue
            if m-1>=0 and maze[m-1][n]!=-1 and maze[m-1][n]!=1:
                maze[m-1][n]=-1
            elif m+1<=r-1 and maze[m+1][n]!=-1 and maze[m+1][n]!=1:
                maze[m+1][n]=-1 
            elif n+1<=c-1 and maze[m][n+1]!=-1 and maze[m][n+1]!=1:
                maze[m][n+1]=-1
            elif n-1>=0 and maze[m][n-1]!=-1 and maze[m][n+1]!=1:
                maze[m][n-1]=-1
            # else:
            #     break
       
print(maze)
    




















# cell=0
# row,col=start
# while cell!=12:
#     if maze[row][col]!=1 and row<=3 and col<=3:
#         print((row,col))
#         cell+=1
#         if row>0 and maze[row-1][col]==0:
#             row-=1
#         elif col>0 and maze[row][col-1]==0:
#             col-=1
#         elif row<3 and maze[row+1][col]==0:
#             row+=1
#         elif col<3 and maze[row][col+1]==0:
#             col+=1             