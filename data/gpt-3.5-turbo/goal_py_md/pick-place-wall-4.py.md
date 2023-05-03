# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Move the gripper to the left of the wall
    #  2. Move the gripper above the puck
    #  3. Drop the gripper around the puck
    #  4. Close the gripper around the puck
    #  5. Move the puck to the target location on the other side of the wall
    # First, move the gripper to the left of the wall.
    if check("the robot's gripper is not left of the wall"):
        robot.move_gripper("left of the wall")
    # Next, move the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above puck and the robot's gripper is closed on the puck"):
        robot.move_gripper("right of the wall")
        robot.move_gripper("near the target location")