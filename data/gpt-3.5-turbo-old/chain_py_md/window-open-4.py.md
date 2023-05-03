# window-open: slide the window open to the left
# def window_open(robot):
# If the robot's gripper is not vertically lined up with the window handle,
# we should move the gripper near the window handle to start pushing
if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
    robot.move("gripper to right of window handle")
# If the robot's gripper is near the window handle we can probably slide the
# window open now by moving the gripper left.
if check("the robot's gripper is near the window handle"):
    robot.slide("window left")
# If the robot's gripper is starting to be in front of the window handle,
# push harder.
if check("the robot's gripper is in front of the window handle"):
    robot.push("window left harder")