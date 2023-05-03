

The program should look like this:

``` 
# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Put the gripper above the hammer handle
    #  2. Drop the gripper around the hammer handle
    #  3. Move the robot's arm down towards the nail
    #  4. Hit the nail with the hammer
    # First, put the gripper above the hammer handle so that the robot can grab
    # it and move the arm down.
    if check("the robot's gripper is not above the hammer handle"):
        robot.put("gripper above hammer handle")
    # Now, the gripper is above the hammer handle, so move it around the handle
    # to grab it.
    if check("the robot's gripper is not around the hammer handle"):
        robot.drop("gripper around hammer handle")
    # Once the gripper is around the hammer handle, start to lower the arm
    # towards the nail.
    if check("the robot's gripper is around the hammer handle and the robot's arm is not close to the nail"):
        robot.move("arm down towards nail")
    # When the arm is close to the nail, start to hit the nail with the hammer.
    if check("the robot's arm is close to the nail"):
        robot.hit("nail with hammer")
```