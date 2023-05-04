
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab cube by lowering gripper
    #  3. Slide the cube to the goal location
    # If the robot's gripper is above the cube and it's in front of the gripper,
    # we can move the gripper down around the cube.
    # Because the cube is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the robot's gripper is above the cube and the cube is forward aligned with the robot's gripper"):
        robot.grab("cube")
    # Now the cube is lined up with the robot's gripper.
    # As long as the cube is lined up with the robot's gripper from the front,
    # slide it.
    if check("the cube is forward aligned with the robot's gripper"):
        robot.move("the cube to goal")

# sweep-into-high: grab the cube and move it to the target location
def sweep_into_high(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab cube by lowering gripper
    #  3. Slide the cube to the goal location
    # If the robot's gripper is above the cube and it's in front of the gripper,
    # we can move the gripper down around the cube.
    # Because the cube is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the robot's gripper is above the cube and the cube is forward aligned with the robot's gripper"):
        robot.grab("cube")
    # Now the cube is lined up with the robot's gripper.
    # As long as the cube is lined up with the robot's gripper from the front,
    # slide it.
    if check("the cube is forward aligned with the robot's gripper"):
        robot.move("the cube to goal")

# push-slide: push the puck while sliding the cube along the table
def push_slide(robot):
    # Steps:
    #  1. Grab the puck
    #  2. Grab the cube
    #  