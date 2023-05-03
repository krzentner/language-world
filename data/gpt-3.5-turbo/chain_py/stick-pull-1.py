# Steps
    # 1. Put the gripper above the stick
    # 2. Close the gripper around the stick
    # 3. Move the gripper to the thermos handle
    # 4. Put the gripper around the thermos handle
    # 5. Pull the thermos to the target location using the stick
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.place("the gripper above the stick")
    # If the gripper is above the stick, close the gripper around the stick.
    if check("the robot's gripper is above the stick and the robot's gripper is open"):
        robot.close("the gripper around the stick")
    # Once the gripper is around the stick, move the gripper to the thermos handle.
    if check("the robot's gripper is around the stick and the robot's gripper is not near the thermos handle"):
        robot.move("the gripper to the thermos handle")
    # Once the gripper is near the thermos handle, put the gripper around it.
    # Make sure the gripper is also sidling up with the thermos.
    if check("the robot's gripper is near the thermos handle and the robot's gripper is not around the thermos handle and the robot's gripper is not horizontally aligned with the thermos handle"):
        robot.place("the gripper around the thermos handle and then align the gripper to the thermos handle horizontally")
    # Once the gripper is around the thermos handle and it is aligned horizontally, position the stick to the ground, tilted towards the goal.
    if check("the robot's gripper is around the thermos handle and is aligned horizontally"):
        robot.move("the stick to the ground, tilted towards the goal")
    # Once the stick is tilted towards the goal, pull the thermos towards the goal using the stick.
    if check("the stick is tilted towards the goal"):
        robot.pull("the thermos towards the goal using the stick")