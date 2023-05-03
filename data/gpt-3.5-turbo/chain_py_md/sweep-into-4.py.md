# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move the cube towards the target location
    #  4. Sweep the cube into the target location
    # First, we need to position the gripper above the cube to grab it.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    # Once the gripper is in position, we should grab the cube.
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is open"):
        robot.grab("cube")
    # Next, we need to move the cube towards the target location.
    # If the gripper isn't near the target location, we need to move it there.
    if check("the robot's gripper is not near target location"):
        robot.move("gripper to target location")
    # Once the gripper is near the target location, we can begin sweeping the cube towards it.
    if check("the robot's gripper is near target location"):
        robot.push("cube towards target location")
    # We keep sweeping the cube until it is fully in the target location.
    if check("the cube is in the target location"):
        return "Task completed successfully."