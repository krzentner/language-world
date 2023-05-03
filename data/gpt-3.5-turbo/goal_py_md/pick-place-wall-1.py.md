# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper next to the puck and near the wall
    #  2. Drop the gripper around the puck
    #  3. Close the gripper around the puck
    #  4. Move the puck to the target location, while avoiding the wall
    # First, position the gripper at the side of the puck closest to the wall.
    if check("the robot's gripper is not near the puck and the puck is not next to the wall"):
        robot.move_gripper("next to the puck and near the wall")
    # Once the gripper is near the puck, put it around the puck.
    if check("the robot's gripper is near the puck and the gripper is not around the puck"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is around the puck and the puck is not at the target location,
    # move the puck towards the target location while avoiding the wall.
    if check("the robot's gripper is around the puck and the puck is not at the target location"):
        robot.move_gripper("near the target location avoiding the wall")