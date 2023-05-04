
    # Steps:
    #  1. Put gripper to the left of the lever
    #  2. Grab the lever by closing the gripper
    #  3. Rotate the lever upwards
    # To grab the lever, first move the robot's gripper near the lever.
    if check("the robot's gripper is not near the lever"):
        robot.move_gripper("near the lever", close_gripper=True)
    # Once the robot's gripper is near the lever and closed, rotate the lever
    # upwards.
    if check("the robot's gripper is below the lever and the robot's gripper is closed"):
        robot.move_gripper("below the lever")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push in on the button from the side
    # First, move the gripper above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # Once the gripper is above the button, move the gripper near the button to
    # push in on it.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not near button"):
        robot.move_gripper("near the button")

# pick-place-wall: pick up the puck and hold it at the target location, against a wall
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.