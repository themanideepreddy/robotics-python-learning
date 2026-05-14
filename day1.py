# Robot sensor variables    
robot_name = "manideep-Bot"
battery_level= 85.5
speed= 0.5
is_moving = False
obstacle_distance = 0.3

print("Robot Name:", robot_name)
print("Battery Level:", battery_level, "%")
print("Speed:", speed, "m/s")
print("Is Moving:", is_moving)
print("Obstacle Distance:", obstacle_distance, "meters")  

#Robotic decision logic
if obstacle_distance < 0.5:
    print("Stop !! Obstacle too close")
elif obstacle_distance < 1.0:
    print("Warning: Slowing DOwn ..... ")
    speed = 0.2
else:
    print("path clear. Moving at full speed")
    is_moving = True

if battery_level < 20:
    print("Battery low. Returning to charging station.")
    is_moving = False
else:
    print("Battery level sufficient. Continuing operation.")

print("Final Speed:", speed, "m/s")