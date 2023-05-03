

The steps are:
1. Line up the robot's gripper as viewed from above the mug 
2. Close the gripper around the mug
3. Move the mug to the target location 

Solution: 
# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    # Steps:
    #  1. Line up the robot's gripper as viewed from above the mug
    #  2. Close the gripper around the mug
    #  3. Move the mug to the target location
    # Line up the robot's gripper with the mug as seen from above.
    if check("the robot's gripper is not above the mug"):
        robot.put("gripper above mug")
    # Once the gripper is around the mug, close the gripper to trap the mug.
    if check("the robot's gripper is above mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    # Now that the mug is trapped, move it to the target location.
    if check("the robot's gripper is closed and the mug is in gripper"):
        robot.move("mug to target")