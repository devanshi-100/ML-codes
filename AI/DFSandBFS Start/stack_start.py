# '''/
# # Depth first search

# # Algorithm 
# # 1. Input Start State
# # 2. Create Stack
# #     2.1 Create Stack DS as set
#       2.2 Push Function(State)
#       2.3 POp Function->State
#   3. Create function Goal_test(state)-->True/False
#   4, craete function Move_gen(State)-->state List
# ''''


MAX=10
tos=0
stack =[None]*MAX

class Node:
    def __init__(self,start,goal):
        self.start=start
        self.goal=goal
        self.children=[]

def push(state): 
    global tos
    if tos==MAX:
        return False
    else:
        stack[tos]=state
        tos=tos+1
        return True
    
def pop():
    global tos
    if tos!=-1:
        tos=tos-1
        state=stack[tos]
        return state
    
if __name__=="__main__":
    push(78)
    push(88)
    pop()
    print(stack)


