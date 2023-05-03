

Next, the code should:

1. Line up the gripper as viewed from above
2. Push down on the wall to make sure it doesn't slide with the button
3. Push down on the button from the top

First, put the gripper above the wall, so it's aligned with the wall from above.
```
    if check("the robot's gripper is not vertically aligned with the wall"):
    	robot.put("gripper above wall")
```
Second, push down on the wall to make sure it doesn't move with the button.
```
    if check("the robot's gripper is above the wall and the robot's gripper is open"):
    	robot.push("down on wall")
```
Finally, once the gripper is above the button and the wall is secure, push down on the button from the top.
```
	if check("the robot's gripper is above the button"):
		robot.push("down on button")
```