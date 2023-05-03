# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    # 1. Put the gripper above the stick
    # 2. Pick up the stick
    # 3. Move the gripper to the thermos
    # 4. Align the stick with the thermos
    # 5. Push the thermos to the target location using the stick
    # First, put the gripper above the stick so we can grab it.
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above stick")
    # Once the gripper is above the stick, grab it.
    if check("the robot's gripper is above the stick and the robot's gripper is open"):
        robot.grab("stick")
    # After grabbing the stick, move the gripper to the thermos.
    if check("the stick is being held by the gripper and the gripper is not near the thermos"):
        robot.move("gripper to thermos")
    # Once the gripper is near the thermos, use the stick to line it up with the thermos.
    if check("the stick is being held by the gripper and the gripper is near the thermos and the stick is not aligned with the thermos"):
        robot.align("stick with thermos")
    # Once the stick is aligned with the thermos, push the thermos to the target location using the stick.
    if check("the stick is aligned with the thermos and the gripper is holding the stick and the thermos is not at the target location"):
        robot.push("thermos to target location with stick")