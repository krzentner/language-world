
    if check("the stick is not near thermos"):
        robot.grab("stick")
    if check("the stick is near thermos but the stick is not attached to thermos"):
        robot.attach("stick to thermos")
    if check("the stick is attached to thermos but the robot's gripper is not pulling "):
        robot.pull("stick back to goal")