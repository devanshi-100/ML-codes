# rooms={'A':"Dirty",'B':"Dirty",'C':"Dirty",'D':"Clean"}
        
# class Environment:
#     def __init__(self,rooms):
#         self.rooms=rooms
#     def display(self):
#         print(self.rooms)

# class agent:
#     def __init__(self,env):
#         self.env=env
#     def clean(self):
#         for room in self.env.rooms.keys():
#             if self.env.rooms[room]=='Dirty':
#                 self.env.rooms[room]="Clean"
#                 print(f"Room {room} is now clean")
#                 print(f"Agent moves to next room {room}")
#             else:
#                 print(f"Room {room} is already clean")
#         print("All rooms are clean")

# if __name__=="__main__":
#     env=Environment(rooms)

#     env.display()
#     agen=agent(env)
#     agen.clean()
#     env.display()
    
from random import random
class Environment:
    def __init__(self,start):
        self.location=start
        self.rooms=[]

class Agent:
    def __init__(self,env):
        self.env=env
    def clean(self):
        if self.env.location.value() == 'Dirty':
            print(f"Room {self.env.location} is now clean")
            self.env.rooms.append(self.env.location)
        else:
            print(f"Room {self.env.location} is already clean")
    def move(self):
        while True:
            while self.motion('Left'):
                _,loc=self.motion('Left')
                print(f"Agent moves to the left")
                self.clean()
            while self.motion('Right'):
                print(f"Agent moves to the right")                                   #IRON/ DOME
                self.clean()                                                         #find the speed of missile
    def motion(self,direction):                                                       #display of coordinate of collision
        if direction=='Left':
            self.env.location=random().choice(['A','B','C','D'])                            
            return True,self.env.location
        elif direction=='Right':
            self.env.location=random().choice(['A','B','C','D'])
            return True,self.env.location
        else:
            return False,self.env.location

    
if __name__=="__main__":
    env=Environment('A')
    agen=Agent(env)
    agen.move()



# Traffic_Light={'A':"Red",'B':"Green",'C':"Red",'D':"Green"}
# class Environment:
#     def __init__(self,lights):
#         self.lights=lights
#     def display(self):
#         print(self.lights)
#     def isGreen(self,light):
#         if self.lights[light]=='Green':
#             return True
#         else:
#             return False
#     def change(self,light):

#         self.lights[light]='Green'
#         return self.lights




