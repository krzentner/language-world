# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move the gripper to the left of the target location
    #  4. Move the gripper down until it touches the ground
    #  5. Sweep the gripper to the right, pulling the cube along with it
    #  6. Move the gripper up and to the right until it's above the target location
    #  7. Move the gripper down until it's at the target location
    # First, position the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # Next, grab the cube with the gripper.
    if check("the robot's gripper is above the cube and the robot's gripper is open"):
        robot.move_gripper("around the cube", close_gripper=True)
    # Now, move the gripper to the left of the target location.
    if check("the robot's gripper is not left of the target location"):
        robot.move_gripper("left of the target location")
    # Move the gripper down until it touches the ground.
    if check("the robot's gripper is not touching the ground"):
        robot.move_gripper("touching the ground")
    # Sweep the gripper to the right, pulling the cube along with it.
    if check("the robot's gripper is not right of the target location"):
        robot.move_gripper("right of the target location")
    # Move the gripper up and to the right until it's above the target location.
    if check("the robot's gripper is not vertically aligned with the target location and the robot's gripper is not forward aligned with the target location"):
        robot.move_gripper("up and to the right of the target location")
    # Move the gripper down until it's at the target location.
    if check("the robot's gripper is not at the target location"):
        robot.move_gripper("near the target location")