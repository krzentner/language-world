# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #   1. Put gripper above puck
    #   2. Push gripper into top of puck
    #   3. Slide puck until it hits the wall
    #   4. Move gripper to the left of the wall
    #   5. Move gripper down to the other side of the wall and trap the puck
    #   6. Slide puck towards the target location
    # First, put the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper is not around the puck, put it around the puck.
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck, push the puck until it hits the wall
    if check("the robot's gripper is near the puck"):
        robot.move_gripper("near the wall")
    # Move the gripper to the left of the wall
    if check("the robot's gripper is not left of the wall"):
        robot.move_gripper("left of the wall")
    # Move the gripper down to the other side of the wall and trap the puck
    if check("the robot's gripper is not below the wall"):
        robot.move_gripper("below the wall", close_gripper=True)
    # Slide the puck towards the target location
    if check("the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")