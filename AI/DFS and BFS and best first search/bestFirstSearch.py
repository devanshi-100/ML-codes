import heapq
from pyamaze import maze,agent,textLabel

def h(current,goal=(1,1)):
    x1,y1=current
    x2,y2=goal

    return abs(x1-x2)+abs(y1-y2)

def dbfs(m,goal):
    OPEN=[]
    visited=set()
    path={}
    start=(m.rows,m.cols)
    heapq.heappush(OPEN,[h(start),start])
    path[start]=None

    while(OPEN):
        heuristic,current=heapq.heappop(OPEN)
        print(f"Visiting: {current} with h(n: {heuristic})")
        if current==goal:
            fpath=[]
            while current is not None:
                fpath.append(current)
                current=path[current]
            return fpath[::-1]
        elif current in visited:
            continue
        visited.add(current)
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
                if nxt in visited:
                    continue
                else:
                    heapq.heappush(OPEN,[h(nxt),nxt])
                    path[nxt]=current
    return None

                

if __name__=="__main__":

    m=maze(4,4)
    goal=(1,1)
    m.CreateMaze(loopPercent=0)
    path=dbfs(m,goal)
    a=agent(m,footprints=True,shape='arrow')
    m.tracePath({a:path})
    l=textLabel(m,'Best First Search Path Length',len(path)+1)
    m.run()
