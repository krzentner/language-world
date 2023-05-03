Here's a code to perform the `sweep-into` task:

```
# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above the cube and the robot's gripper is closed"):
        robot.lift("the cube off the ground")
    if check("the robot's gripper is above the target location"):
        robot.put("the cube at the target location")
    if check("the robot's gripper is not far from the target location"):
        robot.slide("the cube into the target location")
``` 

This code first checks whether the gripper is above the cube. If not, it moves the gripper above the cube. Then, it checks whether the gripper is around the cube and it is open. If not, it drops the gripper around the cube. After that, it checks whether the gripper is near the cube and it is open. If not, it closes the gripper around the cube. Once that's done, it checks if the gripper is lifted off the ground. If not, it lifts it off the ground. 
After that, it checks whether the gripper is above the target location or not. If not, it puts the cube at the target location. Finally, it checks whether the gripper is near the target location or not. If not, it slides the cube into the target location.