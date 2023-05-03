

Here's the code:

```
# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Put gripper above the hammer
    #  2. Drop the gripper around the handle 
    #  3. Move the gripper over the nail
    #  4. Swing the hammer forward to hit the nail
    # First, put the gripper above the hammer.
    if check("the robot's gripper is not above the hammer"):
        robot.put("gripper above hammer")

    # As long as the gripper is above the hammer, move it around the handle so
    # that it can grab it.
    if check("the robot's gripper is above the hammer and the robot's gripper is not around the handle"):
        robot.drop("gripper around handle")

    # If the gripper is now around the handle and the hammer is close to the
    # nail, move the gripper to the nail.
    if check("the robot's gripper is around the handle and the hammer is close to the nail"):
        robot.move("gripper to nail")

    # If the gripper is lined up over the nail, hit it by swinging the hammer
    # forward.
    if check("the robot's gripper is near the nail"):
        robot.swing("hammer forward to hit nail")
```