

```
# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Push gripper into top of mug
    #  3. Slide mug to goal
    # If the robot's gripper is above the mug, the robot can push down into the mug to slide it.
    if check("the robot's gripper is not above mug and the robot's gripper is not vertically aligned with mug"):
        robot.put("the gripper above the mug")
    # If the gripper is aligned with the mug but not near it, move the gripper
    # down to the mug to slide it.
    if check("the robot's gripper is vertically aligned with mug and the robot's gripper is not near mug"):
        robot.push("the gripper into the mug")
    # If the gripper is near the mug, we've probably trapped the mug and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the mug.
    if check("the robot's gripper is near the mug and the mug is below the robot's gripper"):
        robot.slide("the mug to the goal")

'''

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put