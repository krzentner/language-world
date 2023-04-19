

The robot should turn the dial on the door in order to lock it.

# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps: 
    #  1. Put gripper above the dial
    #  2. Drop gripper around the dial
    #  3. Turn the dial to the left
    # First, put the gripper roughly above the dial. 
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above dial")
    # Move the gripper around the dial so that it can properly grip the dial.
    if check("the robot's gripper is not around dial"):
        robot.drop("gripper around dial")
    # Finally, turn the dial to the left to lock it in place.    
    if check("the robot's gripper is around dial"):
         robot.turn("dial left")