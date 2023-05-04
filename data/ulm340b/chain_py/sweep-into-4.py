
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move gripper into cube
    #  5. Move cube to target location
    #  6. Release gripper above cube
    # First, put the gripper above the cube, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above cube"):
        robot.place("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # If the gripper is around the cube, push into the cube to keep it aligned
    # with the gripper.
    if check("the robot's gripper is around cube and the robot's gripper is closed"):
        robot.sweep("the cube")
    # Move the gripper to the target location.
    if check("the robot's gripper is around cube"):
        robot.move("the cube to the target location")
    # Release the gripper above the cube so that we can see it in the camera
    # image.
    if check("the robot's gripper is around cube"):
        robot.open("gripper above cube")

# sweep-into-grasp: move the gripper down until it is around the cube
def sweep_into_grasp(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Move gripper into cube
    #  4. Close gripper around cube
    # First, put the gripper above the cube, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not