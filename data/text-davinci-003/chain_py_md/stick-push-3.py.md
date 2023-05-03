

Steps: 
1. Put gripper above the stick 
2. Dive gripper around the stick
3. Close gripper around the stick
4. Push stick against the thermos 
5. Slide the thermos to the goal

```
# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Drop gripper around the stick
    #  3. Close gripper around the stick
    #  4. Push stick against the thermos
    #  5. Slide the thermos to the goal
    # Put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above stick")
    # Drop the gripper around the stick.
    if check("the robot's gripper is not around the stick"):
        robot.drop("gripper around stick")
    # Close the gripper around the stick.
    if check("the robot's gripper is not closed around the stick"):
        robot.close("gripper around the stick")
    # Push the stick against the thermos.
    if check("the stick is not pushing against the thermos"):
        robot.push("stick against thermos")
    # Slide the thermos to the target location.
    if check("the thermos is not sliding to the goal"):
        robot.slide("thermos to goal")