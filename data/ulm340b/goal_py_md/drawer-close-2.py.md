

## Dialogue

**T:** You should have written a program to close a drawer, by pulling the handle.
Please tell me how to do that.

**P:** First, move the gripper in front of the drawer handle.

**T:** Ok.  Why should I move the gripper in front of the drawer handle?

**P:** So that the gripper can be closed around the drawer handle.

**T:** How about this:
```
# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Move gripper in front of drawer handle
    #  2. Close the gripper around the drawer handle
    #  3. Move the drawer closed
    if check("the robot's gripper is not in front of drawer handle"):
        robot.move_gripper("in front of the drawer handle")
    if check("the robot's gripper is in front of drawer handle and the robot's gripper is open"):
        robot.move_gripper("near the drawer handle", close_gripper=True)
    if check("the robot's gripper is closed around the drawer handle"):
        robot.move_gripper("right of the drawer handle")
```
Is that what you mean?

**P:** Yes, that is what I mean.

**T:** How else can the gripper be moved?

**P:** The gripper can also be opened.

**T:** That's true, but I was thinking more along the lines of "near", "above",
"forward aligned".

**P:** The gripper can be moved forward aligned with an object.

**T:** And it can also be moved horizontally and vertically aligned with an
object.

**P:** Yes.

**T:** What else?

**P:** It can also be moved near an object.

**T:** Ok, but how can the gripper be moved vertically aligned with an object?

**P:** The gripper can be moved vertically aligned with an object by using
vertically aligned.

**T:** Ok.  Please write down that example program again.

**P:**
```
# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Move gripper in front of drawer handle
    #  2. Close the gripper around the drawer handle
    #  3. Move the drawer closed
    if check("the robot's gripper is not