if check("the stick is not near the thermos and the stick is not aligned with the thermos"):
        robot.move("stick above the thermos")
    if check("the stick is aligned with the thermos and the thermos is not behind the stick"):
        robot.push("stick towards the thermos")
    if check("the stick is touching the thermos and the thermos is not at the target location"):
        robot.slide("thermos to the goal using the stick")