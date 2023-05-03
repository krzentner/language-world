# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab the cube with the gripper
    #  3. Slide the cube sideways to the target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    # If the gripper is above the cube, but not yet holding it, grab it.
    if check("the robot's gripper is above cube and the robot's gripper is open"):
        robot.grab("cube")
    # If the gripper is holding the cube, slide it sideways to the goal.
    # Check if the cube is left or right of the gripper, and move accordingly.
    if check("the robot's gripper is holding the cube"):
        if check("cube is to the left of the robot's gripper"):
            robot.slide("cube to the left")
        elif check("cube is to the right of the robot's gripper"):
            robot.slide("cube to the right")
        robot.place("cube at goal") # move to goal once the cube has been moved sideways.