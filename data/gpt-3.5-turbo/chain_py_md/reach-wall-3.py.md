# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    # Steps:
    #  1. Move the gripper to the left of the wall
    #  2. Move the gripper above the target location
    #  3. Move the gripper to the right of the wall and down to the target location
    # There is a wall in the way, so we need to move the gripper around it.
    # Move the gripper to the left of the wall.
    if check("the wall is between the robot's gripper and the target location"):
        robot.move("gripper to left of wall")
    # If the gripper is left of the wall, it can be moved above the target location.
    if check("the robot's gripper is left of the wall and not above the target location"):
        robot.put("gripper above target location")
    # If the gripper is above the target location, it can be moved down and to the right of the wall.
    if check("the robot's gripper is above the target location and not near the target location"):
        robot.move("gripper right of wall and down to target location")