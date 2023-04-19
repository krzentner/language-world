
    if check("the robot's gripper is not near stick"):
        robot.grab("stick")
    if check("stick is not near thermos"):
        robot.place("stick next to thermos")
    if check("the stick is almost above thermos"):
        robot.push("the stick down to thermos")
    if check("the stick and thermos are moving"):
        robot.push("the thermos to goal")