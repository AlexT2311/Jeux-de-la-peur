import time
import keyboard
import pygame

def get_position_by_key(key,previous_position):
    if  key[pygame.K_LEFT]:
        previous_position[0]=previous_position[0]+20
        print(previous_position[0])
    if key=="d" or key=="D":
        print(previous_position[0])
        previous_position[0]=previous_position[0]-20
    return previous_position
    
    
    
previous_position=[0,0]
while True:
    debut=time.time()
    key=None
    
    print(debut)
    while time.time()-debut<1.0:
        key = pygame.key.get_pressed()
        if key==None:
            previous_position=get_position_by_key(key, previous_position)
    print(previous_position)
    
