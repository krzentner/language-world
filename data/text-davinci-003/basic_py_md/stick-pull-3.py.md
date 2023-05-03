

The code would look like this:

```
# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    if check("the robot's gripper is not near the stick"):
        robot.grab("stick")
    if check("the robot's gripper is near the stick and the thermos is not near the stick"):
        robot.pull("stick towards thermos")
    if check("the thermos is near the stick"):
        robot.slide("thermos towards goal")