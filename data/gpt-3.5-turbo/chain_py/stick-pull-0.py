# Steps:
    #   1. Put the gripper on one end of stick and the other end of stick near thermos
    #   2. Pinch the thermos with the gripper
    #   3. Drag the thermos to the target location using the stick
    # First, put one end of the stick near the thermos and the other end of the stick inside the gripper.
    if check("one end of the stick is not near the thermos and the other end is not inside the gripper"):
        robot.place("one end of the stick near the thermos and the other end inside the gripper")
    # Check if the thermos is not between the gripper and the target location, move the gripper near the thermos.
    if check("the gripper is not near the thermos and thermos is not between the gripper and the target location"):
        robot.put("the gripper near the thermos")
    # Check if the gripper is near to the thermos and not pinching, pinch the thermos with the gripper.
    if check("the gripper is near the thermos and the gripper is not pinching the thermos"):
        robot.pinch("the thermos with the gripper")
    # Check if thermos has been pinched with the gripper, now move the thermos to the target location using the stick.
    if check("the gripper has pinched the thermos"):
        robot.drag("the thermos to the target location using the stick")