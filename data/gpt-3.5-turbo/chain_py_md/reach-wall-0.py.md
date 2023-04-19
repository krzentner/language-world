# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
    # Steps:
    #  1. Check if the wall is in the way, if so, move around it
    #  2. Reach towards the target
    # If the wall is in the way, move around it by first moving the gripper down
    # until it is below the height of the wall, then move toward the wall, then
    # move the gripper up again.
    if check("the robot's gripper is blocked by the wall"):
        robot.lower("the gripper below the wall")
        robot.move("toward the wall")
        robot.raise("the gripper above the wall")
    # Once the gripper is clear of the wall, reach towards the target location.
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")