'''
Algorithm:
Input: start, goal
1. OPEN=stack
2. OPEN.push(start)
3. while OPEN is  not empty do
3a.     current = OPEN.pop()
3b.     add current to CLOSED
3c.     if goal_test(current) then
3d.         return path
3e.     else
3f.         next=move_gen(current)
3g.         if next is empty then
3h.             continue
3i.         else
3j.             OPEN.push(next)
3k.         go to step 3f.
'''
from stack import *
from pyamaze import maze,agent

def dfs(m,goal):
    OPEN=Stack()
    start=(m.rows,m.cols)
    OPEN.push(start)
    CLOSED=[]

    while OPEN.is_not_empty():
        current=OPEN.pop()
        print(f"Visiting..... {current}")
        CLOSED.append(current)
        if current==goal:
            return CLOSED
        else:
            for d in 'EWNS':
                if m.maze_map[current][d]==True:
                    if d=='E':
                        nxt=(current[0],current[1]+1)
                    elif d=='W':
                        nxt=(current[0],current[1]-1)
                    elif d=='N':
                        nxt=(current[0]-1,current[1])
                    elif d=='S':
                        nxt=(current[0]+1,current[1])      
                    if nxt in CLOSED:
                        continue
                    OPEN.push(nxt)
    return None                   #couldn't find any goal in current maze

if __name__=="__main__":
    m=maze(4,4)
    # m.CreateMaze(loopPercent=0,saveMaze=True)
    m.CreateMaze(loopPercent=0)
    goal=(1,1)
    path=dfs(m,goal)
    a=agent(m,shape="arrow",footprints=True)
    m.tracePath({a:path})
    m.run()