# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    # Steps:
    #  1. Move gripper to left of the wall
    #  2. Move gripper up and over the wall
    #  3. Move gripper down to goal location
    # The robot needs to reach a location blocked by a wall. To do this, it must move around the wall.
    # If the robot's gripper is not left of the wall, move it there.
    if check("the robot's gripper is not left of the wall"):
        robot.move("gripper to left of wall")
    # Once the gripper is left of the wall, move it up and over the wall.
    # Check if the gripper is above the wall and near the target, or below the wall.
    # If it is below the wall, move it up and over.
    if check("the robot's gripper is not above the wall or near the target"):
        robot.pull("gripper up and over the wall")
    # Once the gripper is above the wall and near the target, move it down to the goal location.
    if check("the robot's gripper is above the wall and near the target"):
        robot.push("gripper down to goal location")