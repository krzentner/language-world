
    # Steps:
    #  1. Put gripper above the handle
    #  2. Put gripper around the handle
    #  3. Push down on the handle
    # If the gripper isn't around the handle, we should move it above the
    # handle.
    # Because the handle is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the robot's gripper is not vertically aligned with handle and the robot's gripper is not forward aligned with handle"):
        robot.move("gripper above handle")
    # As long the gripper is around the handle, we should be able to push down
    # on the handle.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is forward aligned with handle"):
        robot.pull("handle down")

# button-press-side: push the button to the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Drop gripper around the button
    #  3. Push the button to the side
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above the button")
    # Once the gripper is lined up above the button, we should be able to grab
    # the button by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not around the button"):
        robot.put("gripper around the button")
    # Once the gripper is around the button, we can just press the button.
    if check("the robot's gripper is around the button"):
        robot.push("the button to the side")

# pick-place-into: pick up the puck and place it into the goal
def pick_place_into(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck,