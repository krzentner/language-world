    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above stick")
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    if check("the robot's gripper is around stick and the stick is not under the thermos"):
        robot.move("stick under thermos")
    if check("the robot's gripper is around stick and the stick is under the thermos but the thermos is not aligned with the goal"):
        robot.align("thermos to goal")
    if check("the robot's gripper is around stick, the stick is under the thermos and the thermos is aligned with the goal"):
        robot.push("stick towards the goal")