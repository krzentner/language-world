# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Move gripper to the puck without hitting the wall
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal without hitting the wall
    # First, move the gripper to the puck without hitting the wall.
    if check("the robot's gripper is not near the puck and the gripper is not blocked by the wall"):
        robot.move_gripper("near the puck")
    # If the gripper is near the puck and not around it, put it around the puck.
    if check("the robot's gripper is near the puck and the gripper is not around it and the gripper is not blocked by the wall"):
        robot.move_gripper("around the puck", close_gripper=True)
    # If the gripper is around the puck and not near the target location, move it
    # to the target location without hitting the wall.
    if check("the robot's gripper is around the puck and the gripper is not near the target location and the gripper is not blocked by the wall"):
        robot.move_gripper("near the target location")