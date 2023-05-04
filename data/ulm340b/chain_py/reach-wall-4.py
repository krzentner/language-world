
    # Steps:
    #  1. Move the gripper to above the wall
    #  2. Move the gripper over the wall
    #  3. Reach towards the target
    # If the gripper isn't above the wall yet, move it there to start getting it
    # out of the way.
    if check("the robot's gripper is not above wall"):
        robot.place("gripper above wall")
    # If the gripper is above the wall and the gripper is in front of the wall,
    # it's safe to move it over the wall.
    if check("the robot's gripper is above wall and the robot's gripper is in front of wall"):
        robot.move("gripper over wall")
    # Once the gripper is over the wall, we can just move the gripper towards the
    # goal.
    if check("the robot's gripper is over wall"):
        robot.reach("to goal")

# reach-under-wall: reach to the target location with a tall wall in the way
def reach_under_wall(robot):
    # Steps:
    #  1. Move the gripper to in front of the wall
    #  2. Move the gripper under the wall
    #  3. Reach towards the target
    # If the gripper isn't in front of the wall yet, move it there to start
    # getting it out of the way.
    if check("the robot's gripper is not in front of wall"):
        robot.place("gripper in front of wall")
    # If the gripper is in front of the wall, we can move it under the wall
    # safely.
    if check("the robot's gripper is in front of wall"):
        robot.move("gripper under wall")
    # Once the gripper is over the wall, we can just move the gripper towards the
    # goal.
    if check("the robot's gripper is under wall"):
        robot.reach("to goal")

# stack: pick up the puck and place it on top of the block
def stack(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around