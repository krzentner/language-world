# Check if the robot is holding the stick
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    if check("the robot's gripper is not near stick"):
        robot.put("gripper near stick")
    if check("the robot's gripper is near stick and the robot's gripper is open"):
        robot.close("gripper around stick")
    if check("the robot's gripper is around stick"):
        # Check if the thermos is in front of the robot and the stick is on top of the thermos
        if check("the thermos is not in front of the robot"):
            robot.move("gripper to the right of the thermos")
        if check("the robot's gripper is not vertically aligned with the stick and the stick is not on top of the thermos"):
            robot.put("gripper above the stick")
        # Pickup the stick
        if check("the robot's gripper is around stick and the robot's gripper is open"):
            robot.close("gripper around stick")
        # Check if the robot's gripper is holding the thermos and the stick is on top of the thermos
        if check("the robot's gripper is around thermos and the stick is on top of the thermos"):
            robot.push("the stick to the left")
        # Insert the stick into the hole of the thermos
        if check("the robot's gripper is around thermos and the stick is inserted into the thermos"):
            robot.push("the thermos to the goal")