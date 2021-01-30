times = [1, 0.5]
exercises = ['KTE Crunch', 
             'Heaven Raises', 
             'Starfish Crunch', 
             'Figure 8s', 
             'Seated Ab Circles (Left then Right)', 
             'Drunken Mountain Climbers',
             'Dead Bug',
             'Alternating Bicycle',
             'Scissor V-ups',
             'Russian V-tuck Twist',
             'Marching Planks',
             'Landmine Anti Rotation',
             '3-way Seated Ab Tucks']

import random
import time

def start():
    time_remaining = 7
    
    while time_remaining > 3.5:
        t = random.choice(times) * 60
        
        print(random.choice(exercises), ' for ', str(t), ' seconds')
        time.sleep(t)
        print('\a') # make alert noise
        
        time_remaining -= t / 60
        
    print('30 second rest')
    time.sleep(30)
    
    while time_remaining >= 0:
        t = random.choice(times) * 60
        
        print(random.choice(exercises), ' for ', str(t), ' seconds')
        time.sleep(t)
        print('\a')
        
        time_remaining -= t / 60
        
    print('Ok done. Nice.')