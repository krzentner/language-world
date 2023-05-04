
    if check("the robot's gripper is not above wrench and the robot's gripper is not near wrench"):
        robot.move("gripper above wrench")
    if check("the robot's gripper is above wrench and the robot's gripper is not near wrench"):
        robot.put("gripper near wrench")
    if check("the robot's gripper is near wrench"):
        robot.grab("wrench")
    if check("the wrench is near the peg"):
        robot.put("wrench on peg")
    if check("the wrench is on the peg"):
        robot.close("wrench around peg")

# pick-place-wall: pick up the object and place it in the receptacle
def pick_place_wall(robot):
    if check("the robot's gripper is not vertically aligned with the object"):
        robot.put("gripper above object")
    if check("the robot's gripper is vertically aligned with the object and the robot's gripper is not near the object"):
        robot.put("gripper near object")
    if check("the robot's gripper is near the object and the robot's gripper is open"):
        robot.drop("gripper around object")
    if check("the robot's gripper is above object and the robot's gripper is closed"):
        robot.put("object in receptacle")

# put-on-wall: pick up the object and hold it in the receptacle
def put_on_wall(robot):
    if check("the robot's gripper is not vertically aligned with the object"):
        robot.put("gripper above object")
    if check("the robot's gripper is vertically aligned with the object and the robot's gripper is not near the object"):
        robot.put("gripper near object")
    if check("the robot's gripper is near the object and the robot's gripper is open"):
        robot.drop("gripper around object")
    if check("the robot's gripper is above object and the robot's gripper is closed"):
        robot.place("object in receptacle")

# toggle-switch: flip the switch to the goal position
def toggle_switch(robot):
    if check("the robot's gripper is not vertically aligned with the switch and the robot's gripper is not near the switch"):
        robot.move("gripper above switch")
    if check("the robot