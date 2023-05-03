# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Move gripper above target location
    #  2. Open gripper
    #  3. Move gripper down to grab object
    #  4. Close gripper around object
    #  5. Lift object up to target location
    # First move the gripper above the target location.
    if check("the robot's gripper is not above the target location"):
        robot.move("gripper above target location")
    # Open gripper to drop object at the target location
    if check("the robot's gripper is holding an object and is above the target location"):
        robot.open("gripper")
    # Move gripper down to grab object
    if check("the robot's gripper is open and is not around the object and is above the target location"):
        robot.move("gripper down to object")
    # Close the gripper around the object
    if check("the robot's gripper is around the object and object is not at the target location"):
        robot.close("gripper around object")
    # Lift the object to the target location
    if check("the robot's gripper is holding the object"):
        robot.lift("object up to target location")