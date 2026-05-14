#Robot sensor variables
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

#simulatinng sensor ,eading ( like lidar data arriving )
sensor_reading = [2.5, 1.8, 0.9, 0.4, 1.2, 3.0,0.6]

print("\n-- scanning environment ---")
for i, distance in enumerate(sensor_reading):
    print(f"Sensor {i+1}: Distance = {distance} meters")
    if distance < 0.5:
        print("  Alert: Obstacle detected! Stopping robot.")
    elif distance < 1.0:
        print("  Warning: Obstacle nearby. Slowing down.")
    else:
        print("  Path clear. Continuing at current speed.")

#findind the closest path
closest_distance = min(sensor_reading)
closest_sensor_index = sensor_reading.index(closest_distance) + 1
print(f"\nClosest obstacle detected by Sensor {closest_sensor_index} at a distance of {closest_distance} meters")

#functions
def check_battery(level):
    return level >20

def get_speed_for_distance(distance):
    if distance < 0.5:
        return 0.0
    elif distance < 1.0:
        return 0.2
    else:
        return 0.5

def scan_environment(readings):
    if not readings:
        return None
    return min(readings)

def robot_status(name, battery, speed, moving):
    status = "moving" if moving else "stopped"
    print(f"-- {name} Status --")
    print(f"Battery Level: {battery}%")
    print(f"Speed: {speed} m/s")
    print(f"Status: {status}")  
    print(f"  Battery : {battery}%")
    print(f"  Speed   : {speed} m/s")
    print(f"  Status  : {status}")

if __name__ == "__main__":
    battery = 87.5
    readings= [2.5, 1.8, 0.9, 0.4, 1.2]

    closest = scan_environment(readings)
    speed = get_speed_for_distance(closest)
    moving = speed > 0 and  check_battery(battery)
    robot_status(robot_name, battery, speed, moving)
    
