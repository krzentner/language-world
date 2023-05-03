# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    # Steps:
    #  1. Move gripper above the wall
    #  2. Move the gripper forward until it reaches the wall
    #  3. Move the gripper up until it's above the wall
    #  4. Move the gripper towards the target location
    #  5. Move the gripper down to reach the target location
    # First we need to move the gripper above the wall, so we can see where to
    # move it next.
    if check("the robot's gripper is not above the wall"):
        robot.move_gripper("above the wall")
    # Once the gripper is above the wall, we need to move it forward towards the
    # wall until it reaches the wall.
    if check("the robot's gripper is not at the wall"):
        robot.move_gripper("forward until it reaches the wall")
    # Once the gripper is at the wall, we need to move it up until it's above
    # the wall.
    if check("the robot's gripper is not above the wall"):
        robot.move_gripper("up until it's above the wall")
    # Once the gripper is above the wall, we can move it towards the target
    # location.
    if check("the robot's gripper is not near the target location"):
        robot.move_gripper("towards the target location")
    # Finally, once the gripper is near the target location, we can move it
    # down to reach the target location.
    if check("the robot's gripper is not at the target location"):
        robot.move_gripper("down to the target location")