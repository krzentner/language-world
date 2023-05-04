

Now fill in the body of the function, based on the text above.

''')

#button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push gripper into top of button
    # If the button is below the gripper, the robot can probably move the gripper to the button to push it down.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button")
    # If the gripper is near the button, we've probably trapped the button and can press it down.
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is near button"):
        robot.move_gripper("vertically aligned with the button")

q2_desc = dedent('''
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

Here's some code that demonstrates how the robot can do a variety of tasks:

```
# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
  