
    # Steps:
    #  1. Put gripper above the button
    #  2. Start pushing against the button
    #  3. Push harder
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # If the robot's gripper is vertically aligned with the button we can probably
    # press it now by moving the gripper down.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("the button down")
    # If the robot's gripper is starting to be in front of the button, push harder.
    if check("the robot's gripper is in front of the button"):
        robot.push("the button down harder")

# pick-place-topdown: pick up the puck and hold it at the target location
def pick_place_topdown(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above puck and the robot's gripper