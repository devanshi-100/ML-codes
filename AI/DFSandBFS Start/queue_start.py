MAX=10
front=-1
rear=-1

queue=[None]*10

def enqueue(state):
    global rear
    global front
    if rear==MAX-1:
        return False
    if front==-1:
        front=front+1
    rear+=1
    queue[rear]=state
    return True

def dequeue():
    global rear
    global front
    if front==-1:
        return -1
    else:
        ele=queue[front]
        queue[front]=None
        if front==rear:
            rear=-1
            front=-1
        else:
            front=front+1
        return ele
        

if __name__=="__main__":
    enqueue(89)
    enqueue(90)
    enqueue("Hello")
    dequeue()
    print(queue[front])
    print(queue[rear])
    print(queue)