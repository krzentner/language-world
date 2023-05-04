

Then write code that controls the robot in order to turn the faucet right.
We have the following functions that can control the robot:

- `robot.put(object above object)` - put object above object
- `robot.move(gripper to object)` - move gripper to object
- `robot.grab(object)` - grab object
- `robot.drop(object on object)` - drop object on object
- `robot.close(gripper around object)` - close gripper around object
- `robot.slide(object to object)` - slide object to object
- `robot.pull(away from object)` - pull away from object
- `robot.push(against object)` - push against object
- `robot.twist(clockwise)` - twist clockwise
- `robot.twist(counter-clockwise)` - twist counter-clockwise
- `robot.place(object at object)` - place object at object
- `robot.reach(to object)` - reach to object

We use natural language as much as possible to describe these functions.
For example, `robot.put(the robot's gripper above the puck)` or `robot.move(the robot's gripper to the window handle)` or `robot.drop(the puck on the goal)`.

We can use the following functions to check conditions:

- `check("the robot's gripper is above object")` - check if the robot's gripper is above object
- `check("the robot's gripper is below object")` - check if the robot's gripper is below object
- `check("the robot's gripper is near object")` - check if the robot's gripper is near object
- `check("the robot's gripper is open")` - check if the robot's gripper is open
- `check("the robot's gripper is closed")` - check if the robot's gripper is closed
- `check("object is near object")` - check if object is near object
- `check("object is below object")` - check if object is below object
- `check("object is above object")` - check if object is above object
- `check("object is left of object")` - check if object is left of object
- `check("object is right of object")` - check if object is right of object
- `check("object is horizontally aligned with object")` - check if object is horizontally aligned with object
- `check("object is vertically aligned with object")` - check if object is vertically aligned with object
- `check("object is forward aligned with object")` - check if object is forward aligned with object

When using these functions, we can use the names of