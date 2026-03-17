'''OPEN=Queue
Queue.add(start)
CLOSED=[]
while OPEN is not empty
    current=OPEN.delete

'''

from queue import *
from pyamaze import maze,agent

def bfs(m,goal):
    OPEN=Queue()
    start=(m.rows,m.cols)
    OPEN.add(start)
    CLOSED=[]
    while OPEN.is_not_empty():
        current=OPEN.delete()
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
                    OPEN.add(nxt)
    return None            


if __name__=="__main__":
    m=maze(4,4)
    # m.CreateMaze(loopPercent=0,saveMaze=True)
    m.CreateMaze(loopPercent=0)
    goal=(1,1)
    path=bfs(m,goal)
    a=agent(m,shape="arrow",footprints=True)
    m.tracePath({a:path})
    m.run()