# 2. ⁠BFS Algorithm:
'''
Algorithm:
Input: start, goal
1. OPEN=queue
2. OPEN.add(start)
3. while OPEN is  not empty do
3a.     current = OPEN.delete()
3b.     add current to CLOSED
3c.     if goal_test(current) then
3d.         return path
3e.     else
3f.         next=move_gen(current)
3g.         if next is empty then
3h.             continue
3i.         else
3j.             OPEN.add(next)
3k.         go to step 3f.
'''

class Queue:
    def __init__(self):
        self.items=[]
    def add(self,data):
        self.items.append(data)
    def is_not_empty(self):
        if len(self.items) > 0:
            return True
        else:
            return False
    def delete(self):
        if self.is_not_empty():
            return self.items.pop(0)
        else:
            return None
