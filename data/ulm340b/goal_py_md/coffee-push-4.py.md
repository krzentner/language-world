

To control the robot, you can call:
```
robot.move_gripper("NEAR A", close_gripper=True)
robot.move_gripper("NEAR A", close_gripper=False)
```
The first command moves the robot's gripper toward "A" and closes the gripper. The second command moves the robot's gripper toward "A" and opens the gripper. You can use `A` to be one of:
`button`,
`door handle`,
`drawer handle`,
`target location`,
`mug`,
`window handle`,
`hole`,
`peg`,
`puck`.

You should also write code to check if the robot's gripper is in a specific position. For example, the code `check("the robot's gripper is near button")` evaluates to `True` if the robot's gripper is in the correct position and `False` otherwise.
You can use `A` to be one of:
`button`,
`door handle`,
`drawer handle`,
`target location`,
`mug`,
`window handle`,
`hole`,
`peg`,
`puck`.

You can use `B` to be one of:
`in front of`,
`below`,
`left of`,
`above`,
`near`,
`around`,
`forward aligned with`,
`backward aligned with`,
`vertically aligned with`,
`horizontally aligned with`.

"""
# TODO: Write your code for coffee-push

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")

# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2