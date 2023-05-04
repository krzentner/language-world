

Then, write your code to have the robot pick up the puck and place it in the target location.
You can check if the robot's gripper is below the target location using
the command `check("the robot's gripper is below the target location")`.
You can check if the puck is in the target location using
the command `check("puck is in the target location")`.

You can move the gripper above the puck using the command
`robot.move_gripper("above the puck")`.
You can drop the gripper down below the puck using the command
`robot.move_gripper("below the puck")`.
""",
    #
    # 1.4.2: Slide a puck by pushing it with the robot gripper from the side
    #
    """
Hello again. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

Here's some code that demonstrates how the robot can do a variety of tasks:

```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")

# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # Once the gripper is lined