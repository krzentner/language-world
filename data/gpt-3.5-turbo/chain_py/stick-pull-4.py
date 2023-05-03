# Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Move the gripper towards the thermos handle
    #  4. Put gripper around the thermos handle
    #  5. Use the stick to pull the thermos to the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    # If the gripper is above the stick, grab it with the gripper.
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not around the stick"):
        robot.grab("stick")
    # Once the gripper has grabbed the stick, move the gripper towards the
    # thermos handle.
    if check("the robot's gripper is around the stick and the robot's gripper is not near thermos handle"):
        robot.move("gripper towards thermos handle")
    # If the gripper is near the thermos handle, put the gripper around the handle.
    if check("the robot's gripper is near thermos handle and the robot's gripper is around stick but not around handle"):
        robot.put("gripper around thermos handle using stick")
    # Once the gripper is around the thermos handle, start using the stick to pull
    # the thermos to the target location.
    if check("the robot's gripper is around the thermos handle and the robot's gripper is not at the target location"):
        robot.pull("thermos using stick to goal")