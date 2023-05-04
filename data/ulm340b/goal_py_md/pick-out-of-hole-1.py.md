

Once you've finished that function, run the following to make sure your code is valid:
```
if check("pick-out-of-hole is an unimplemented function"):
    raise Exception("You need to implement the pick-out-of-hole function first! You're in the wrong block!")
```

Then enter the following:

```
if __name__ == "__main__":
    from src import run_interactive
    run_interactive()
```

If all went well, you should be able to run your program now!

"""

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

# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.move_gripper("left of the door handle")

# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
 