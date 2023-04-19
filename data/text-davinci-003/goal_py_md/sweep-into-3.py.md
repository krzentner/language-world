

Steps:
  1. Put gripper above the cube
  2. Sweep the cube in a plateau with the gripper
  3. Push the cube to the target location

# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Sweep the cube in a plateau with the gripper
    #  3. Push the cube to the target location
    # First, put the gripper above the cube so that it can sweep it without
    # bumping it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # Once the gripper is above the cube, sweep it inwards in a plateau.
    if check("the robot's gripper is not above the cube and the robot's gripper is not around the cube"):
        robot.move_gripper("around the cube")
    # As long as the the cube isn't at the target location, keep pushing the
    # cube in a plateau.
    if check("the cube is not at the target location"):
        robot.move_gripper("towards the target location")
    # If the gripper is close to the target, just move the gripper to the
    # target location.
    if check("the robot's gripper is nearly at the target location"):
        robot.move_gripper("right at the target location")