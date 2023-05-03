# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    # Steps:
    #  1. Move gripper to be above the target
    #  2. If there is a wall in the way, move the gripper to the left or right of the wall
    #  3. Reach towards the target
    # First, put the gripper above the target.
    if check("the robot's gripper is not above reach target"):
        robot.put("gripper above reach target")
    # Check if there is a wall in front of the robot's gripper. If so, move the
    # gripper to the left or right of the wall.
    if check("there is a wall in front of the robot's gripper"):
        if check("the robot's gripper is to the left of wall"):
            robot.move("gripper to right of wall")
        elif check("the robot's gripper is to the right of wall"):
            robot.move("gripper to left of wall")
    # Move the gripper towards the target.
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")