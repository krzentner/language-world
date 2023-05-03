

# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Put gripper against the wall
    #  3. Slide the puck against the wall to the target location
    # Put the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # Put the gripper against the wall and then try to slide the puck towards the target location. 
    if check("the robot's gripper is not against the wall"):
        robot.move_gripper("against the wall")
    # Slide the puck against the wall while pushing the wall slightly 
    if check("the robot's gripper is against the wall and the puck is not near the target location"):
        robot.move_gripper("near the target location")