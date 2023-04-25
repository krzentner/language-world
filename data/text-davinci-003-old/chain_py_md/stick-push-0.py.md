

Steps: 
1. Put gripper above the stick
2. Drop gripper around the stick
3. Close gripper around the stick
4. Push the stick towards the thermos
5. Push the thermos towards the goal

```
# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Drop gripper around the stick
    #  3. Close gripper around the stick
    #  4. Push the stick towards the thermos
    #  5. Push the thermos towards the goal
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above stick")
    # Once the gripper is above the stick, we should be able to grab the stick by
    # moving the gripper down around it.
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    # Once the gripper is around the stick, we can just close the gripper.
    if check("the robot's gripper is around the stick and the robot's gripper is open"):
        robot.close("gripper around stick")
    # Now the stick is in the gripper. Push it towards the thermos.
    if check("the robot's gripper is closed and the stick is not near the thermos"):
        robot.push("stick towards thermos")
    # If the stick is next to the thermos, we should be able to push the thermos
    # to the goal.
    if check("the stick is near the thermos"):
        robot.push("thermos to goal")