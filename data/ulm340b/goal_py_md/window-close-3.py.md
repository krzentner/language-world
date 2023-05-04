

Your code should do all three of these:

* Be indented
* Have a colon at the end of the first line (not indented)
* Have a line below that starts with `if` and is indented

The `robot` object has two methods, `move_gripper()` and `check()`. You can use `robot.move_gripper(location)` to make the robot move its gripper to a location. For example, `robot.move_gripper("vertically aligned with the door handle")` will move the gripper above the door handle. `robot.move_gripper("left of the door handle", close_gripper=True)` will move the gripper above the door handle, and then close the gripper around the handle.

`robot.move_gripper()` can take any of these arguments:

* `near`: the robot's gripper is near the object.
* `vertically aligned with`: the robot's gripper is above the object.
* `horizontally aligned with`: the robot's gripper is to the side of the object.
* `around`: the robot's gripper is holding the object.
* `forward aligned with`: the robot's gripper is in front of the object.
* `left of`: the robot's gripper is to the left of the object.
* `right of`: the robot's gripper is to the right of the object.
* `above`: the robot's gripper is above the object.
* `below`: the robot's gripper is below the object.
* `close_gripper=True`: the robot's gripper is closed.
* `close_gripper=False`: the robot's gripper is open.
* `far`: the robot's gripper is not near the object.
* `not vertically aligned with`: the robot's gripper is not above the object.
* `not horizontally aligned with`: the robot's gripper is not to the side of the object.
* `not around`: the robot's gripper is not holding the object.
* `not forward aligned with`: the robot's gripper is not in front of the object.
* `not left of`: the robot's gripper is not to the left of the object.
* `not right of`: the robot's gripper is not to the right of the object.
* `not above`: the robot's gripper is not above the object.
* `not below`: the robot's gripper is not below the object.
* `open_gripper=True`: the robot's gripper is open.
* `open_gripper=False`: the robot's grip