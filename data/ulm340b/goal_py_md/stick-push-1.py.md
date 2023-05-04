

To begin, look at the steps that are used to `push` the puck to the target location. We'll do almost exactly that, but instead of directly gripping the puck, we'll push the stick into it.

Let's begin with a simplified version of this task.
Here, we are in a room with a stick and a box.

```
# stick-push-box: grab the stick and use it to push the box to the goal location
def stick_push_box(robot):
    # Steps:
    #  1. Grab the stick with the gripper
    #  2. Line up the stick and box to push the box
    #  3. Slide the stick into the box to push it to the goal
    if check("the robot's gripper is not vertically aligned with the stick and the robot's gripper is not near stick"):
        robot.move_gripper("vertically aligned with the stick", close_gripper=True)
    # The gripper should be mostly above the stick.
    if check("the robot's gripper is vertically aligned with the stick"):
        robot.move_gripper("above the stick", close_gripper=True)
    # If the gripper is open, we should probably try closing it.
    if check("the robot's gripper is not open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the gripper is around the stick, we should move the stick to push the
    # box.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("vertically aligned with the box")
    # If the stick is vertically aligned with the box, we can probably push the
    # box by moving the stick left.
    if check("the stick is not vertically aligned with the box"):
        robot.move_gripper("in front of the box", close_gripper=True)
    # If the stick is lined up with the box, move it to the box.
    if check("the stick is vertically aligned with the box and the stick is not near the box"):
        robot.move_gripper("in front of the box", close_gripper=True)
    # If the stick is around the box, push the box to the goal by moving it
    # right.
    if check("the stick is not near the goal and the stick is near the box"):