
    # Steps:
    #  1. Put gripper above cube
    #  2. Push gripper into cube
    #  3. Sweep cube towards goal
    # The robot can grab and move the cube by pushing its gripper into it from
    # above and then sweeping it to its target location.
    # If the cube isn't below the gripper as seen from above, move the gripper
    # above the cube.
    if check("the robot's gripper is not above cube and the robot's gripper is not vertically aligned with the cube"):
        robot.put("the gripper above the cube")
    # If the gripper is aligned with the cube but not near it, move the gripper
    # down to the cube to sweep it.
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not near cube"):
        robot.push("the gripper into the cube")
    # If the gripper is near the cube, we can just start sweeping it towards the
    # target.
    if check("the robot's gripper is near the cube and the cube is below the robot's gripper"):
        robot.sweep("move cube towards goal")