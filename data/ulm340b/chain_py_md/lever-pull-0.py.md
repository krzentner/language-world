

Then, complete the following steps to create the function.

1. You should first put the robot's gripper above the lever
so you can safely move the gripper down to grab the lever.

To check if the robot's gripper is not above the lever,
use `check` to check if `the robot's gripper is not vertically
aligned with lever`.

Then, tell the robot to put `gripper above lever`.

For example, the final code should be:
```
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
```


2. Once the gripper is aligned above the lever, move the gripper
down to grab the lever.

To check if the gripper is not around the lever,
use `check` to check if `the robot's gripper is not around lever`.

Then, tell the robot to put `gripper around lever`.

For example, the final code should be:
```
    if check("the robot's gripper is not around lever"):
        robot.put("gripper around lever")
```

3. Now that the lever is probably grabbed, rotate the lever
around the joint.

To check if the robot is still holding the lever,
use `check` to check if `the robot's gripper is around lever`.

Then, tell the robot to rotate `lever`.

For example, the final code should be:
```
    if check("the robot's gripper is around lever"):
        robot.rotate("lever")
```
"""

class Robot:

    def put(self, obj):
        print("Putting", obj)

    def drop(self, obj):
        print("Dropping", obj)

    def grab(self, obj):
        print("Grabbing", obj)

    def push(self, obj):
        print("Pushing", obj)

    def slide(self, obj):
        print("Sliding", obj)

    def align(self, obj):
        print("Aligning", obj)

    def insert(self, obj):
        print("Inserting", obj)

    def reach(self, obj):
        print("Reaching", obj)

    def place(self, obj):
        print("Placing", obj)

    def close(self, obj):
        print("Closing", obj)

    def pull(self, obj):
        print("Pulling", obj)

    def open(self,