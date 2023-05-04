
    # Steps:
    #  1. Put gripper near the bottom of the peg
    #  2. Move the gripper up around the peg
    #  3. Move the gripper to the goal
    #  4. Put the peg into the hole
    # First, move the gripper close to the peg.
    if check("the robot's gripper is not near the peg"):
        robot.put("the gripper near the peg")
    # Put the gripper around the peg.
    if check("the robot's gripper is not around the peg"):
        robot.put("the gripper around the peg")
    # Now we are holding the peg, so we can just move the peg to the goal.
    if check("the robot's gripper is around the peg"):
        robot.move("the peg to the goal")
    # Put the peg down into the hole
    if check("the peg is above the goal and the robot's gripper is around the peg"):
        robot.put("the peg into the goal")

# pick-place-with-camera-above: use the camera to pick up the puck and hold it at the target location
def pick_place_with_camera_above(robot):
    # Steps:
    #  1. Move the gripper above the puck to prepare to grab it
    #  2. Grab the puck
    #  3. Move the puck to the goal
    # Move the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # Grab the puck and lift it up.
    if check("the puck is in view and the robot's gripper is not around puck"):
        robot.place("gripper around puck")
    # Move the puck to the goal.
    if check("the puck is in view and the robot's gripper is around puck"):
        robot.place("puck at goal")

# pick-place-with-camera-below: use the camera to pick up the puck and hold it at the target location
def pick_place_with_camera_below(robot):
    # Steps:
    #  1. Grab the puck
    #  2. Move the puck to the goal
    # Grab the puck.
    if check