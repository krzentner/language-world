

Then fill in the body of the function.


## Step-by-step Instructions

Let's walk through this exercise step-by-step.

1. Use an if-statement to check whether the robot is above the drawer handle:

```
    if check("the robot's gripper is not vertically aligned with drawer handle"):
```

2. Use the robot's `put` action to move its gripper above the drawer handle.
Use `gripper above drawer handle` for the object argument.

```
        robot.put("gripper above drawer handle")
```

3. Use a second if-statement to check whether the robot's gripper is around the drawer handle:

```
    if check("the robot's gripper is not around drawer handle and the robot's gripper is open"):
```

4. Use the robot's `put` action to put its gripper around the drawer handle.
Use `gripper around drawer handle` for the object argument.

```
        robot.put("gripper around drawer handle")
```

5. Use a third if-statement to check whether the robot's gripper is around the drawer handle.

```
    if check("the robot's gripper is around drawer handle"):
```

6. Use the robot's `push` action to push the drawer closed.
Use `away from drawer` for the object argument.

```
        robot.push("away from drawer")
```

That's it.
The full program should look like this:

```
def drawer_close(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is not around drawer handle and the robot's gripper is open"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.push("away from drawer")
```


## Extra challenges

To check that you're ready for a new challenge, you can test your solutions against
[some hidden tests](@next).

1. Make the robot push a drawer closed with the left hand.

2. Make the robot push a drawer closed with the right hand.

3. Make the robot push a drawer closed with the left hand if the left hand is closer, otherwise use the right hand.

"""

import malmopy
import malmopy.play
import malmopy.visualize

from