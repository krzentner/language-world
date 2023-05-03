

# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab the puck with the gripper
    #  3. Line the puck up with the target location
    #  4. Move the puck up to the target location
    
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the puck becomes left of the gripper, go back to putting the gripper
    # above the puck.
    # Because the puck is relatively small, check if the gripper is lined up
    # from the side instead of from the front.
    if check("the puck is not left of the robot's gripper and the puck is not side aligned with the robot's gripper"):
        robot.move_gripper("side aligned with the puck", close_gripper=True)
    # Once the gripper is around the puck,  the puck can be moved to the target
    # location.
    if check("the robot's gripper is around the puck and the puck is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")
    # If the gripper is already lined up with the target location, then merely
    # raise the gripper bringing the puck with it.
    if check("the robot's gripper is horizontally aligned with the target location and the puck is not above the target location"):
        robot.move_gripper("above the target location")