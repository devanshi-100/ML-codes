import heapq
from pyamaze import maze,agent
import math

def h(current,goal=(1,1)):
    x1,y1=current
    x2,y2=goal
    return abs(x1-x2)+abs(y1-y2)

def AStar(m,goal):
    OPEN=[]
    g_path={}
    f_path={}
    path={}
    start=(m.rows,m.cols)
    for cell in m.grid:
        g_path[cell]=math.inf
        f_path[cell]=math.inf

    path[start]=None

    g_path[start]=0
    f_path[start]=g_path[start]+h(start,goal)
    heapq.heappush(OPEN,(f_path[start],start))

    while(OPEN):
        _,current=heapq.heappop(OPEN)
        if current==goal:
            fpath=[]
            while current is not None:
                fpath.append(current)
                current=path[current]
            return fpath[::-1]
        else:
            for d in 'EWNS':
                if m.maze_map[current][d]==True:
                    if d=='E':
                        nxt=(current[0],current[1]+1)
                    if d=='W':
                        nxt=(current[0],current[1]-1)
                    if d=='N':
                        nxt=(current[0]-1,current[1])
                    if d=='S':
                        nxt=(current[0]+1,current[1])
                    temp_g=g_path[current]+1
                    temp_f=temp_g+h(nxt,goal)

                    if temp_f<f_path[nxt]:
                        g_path[nxt]=temp_g
                        f_path[nxt]=temp_f
                        heapq.heappush(OPEN,(temp_f,nxt))
                        path[nxt]=current
    return None


if __name__=="__main__":
    m=maze(4,4)
    goal=(1,1)
    m.CreateMaze(loopPercent=0)
    path=AStar(m,goal)
    a=agent(m,footprints=True,shape='arrow')
    m.tracePath({a:path})
    m.run()
    