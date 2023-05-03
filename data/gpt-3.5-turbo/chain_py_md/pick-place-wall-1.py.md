# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Move the gripper to the side of the wall
    #  2. Move the gripper forward to the puck
    #  3. Pick up the puck
    #  4. Move the gripper up and over the wall
    #  5. Move the gripper to the target location
    #  6. Place the puck
    # Move the gripper to the side of the wall.
    if check("the robot's gripper is not clear of the wall"):
        robot.move("gripper to side of wall")
    # Move the gripper forward to the puck.
    if check("the robot's gripper is clear of the wall and the robot's gripper is not near puck"):
        robot.reach("to puck")
    # Pick up the puck.
    if check("the robot's gripper is near puck and the robot's gripper is not around puck"):
        robot.drop("gripper around puck")
    # Move the gripper up and over the wall.
    if check("the robot's gripper is around puck and the robot's gripper is not over the wall"):
        robot.lift("gripper over the wall")
    # Move the gripper to the target location.
    if check("the robot's gripper is over the wall and the robot's gripper is not at the goal location"):
        robot.move("gripper to goal location")
    # Place the puck.
    if check("the robot's gripper is at the goal location and the robot's gripper is around puck"):
        robot.place("puck at goal location")