
    if check("the robot's gripper is not near the stick"):
        robot.grab("stick")
    if check("the robot's gripper is around the stick and the stick is not near the theromos"):
        robot.move("stick to thermos")
    if check("the stick is near the theromos and the stick is not forward aligned with theromos"):
        robot.align("stick to theromos")
    if check("the stick is near the theromos and the stick is forward aligned with theromos"):
        robot.pull("stick to goal")