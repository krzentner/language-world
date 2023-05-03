
    # Steps:
    #  1. Put gripper above stick handle
    #  2. Drop gripper around the stick handle
    #  3. Move to thermos
    #  4. Push thermos with stick
    # If the robot's gripper isn't above the stick handle, put the gripper
    # above the stick handle.
    if check("the robot's gripper is not above the stick handle"):
        robot.put("gripper above stick handle")
    # Once the gripper is above the stick, drop the gripper around the handle.
    if check("the robot's is above the stick and the robot's gripper is not around the stick handle"):
        robot.put("gripper around stick handle")
    # Move the stick (attached to the gripper) to the thermos.
    if check("the robot's gripper is around the stick handle and the thermos is not near the gripper"):
        robot.grab("thermos with stick")
    # Push the thermos with the stick.
    if check("the thermos is near the gripper and the robot's gripper is around the stick handle"):
        robot.push("thermos with stick")