class  Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if len(self.items)>0:
            return self.items.pop()
        else:
            return None
    def is_not_empty(self):
        return (len(self.items)!=0)
    # def peek(self,state):
    #     if state in self.items:
    #         return True
    #     else:
    #         return False
    
# if __name__=="__main__":
#     stck=Stack()
#     stck.push(1)
#     stck.push(3)
#     print(stck.pop())


