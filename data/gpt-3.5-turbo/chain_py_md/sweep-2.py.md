# sweep: grab the cube and move sideways to the target location
def sweep(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab cube with gripper
    #  3. Move gripper and cube sideways to goal
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    # Once the gripper is above the cube, grab it with the gripper.
    if check("the gripper is above the cube and the gripper is open"):
        robot.drop("gripper around cube")
    # Once the gripper is around the cube, move it to the goal sideways.
    if check("the gripper is around cube and the cube is below the gripper"):
        robot.slide("the gripper and cube sideways to the goal")