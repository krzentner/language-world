```
# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    #  1. Put the stick to the left of the thermos
    #  2. Move the stick to the right while pushing the thermos
    # First, we need to put the stick to the left of the thermos
    # If the stick is not to the left of the thermos
    if check("the stick is not to the left of the thermos"):
        robot.put("the stick to the left of the thermos")
    
    # Once the stick is to the left of the thermos, we need to push the thermos with the stick
    # If the gripper is not near the stick
    if check("the robot's gripper is not near the stick"):
        robot.move("the gripper near the stick")
    # If the stick is to the left of the thermos and the gripper is near the stick, we can push the thermos
    if check("the stick is to the left of the thermos and the gripper is near the stick"):
        while not check("the thermos has reached the goal location"):
            robot.push("the stick to the right while pushing the thermos")
```