
    # Steps:
    #  1. Reach towards the target location
    # For this case, we can move the gripper directly to the target,
    # because we're assuming that the wall is short.
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")

# slide: slide the puck to the target location
def slide(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Move to a reachable position
    #  2. Line up the gripper as viewed from above
    #  3. Push down on the button from the top
    # If the gripper isn't near the button, try to reach to a reachable position
    # in front of the button.
    # We don't need to be careful about the direction here.
    if check("the robot's gripper is not near button"):
        robot.reach("to button")
    # Because this is "topdown", we just need to