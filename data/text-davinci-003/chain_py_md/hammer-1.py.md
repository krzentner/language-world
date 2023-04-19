

Here's the program:

```
# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Put gripper above the hammer
    #  2. Drop gripper around the hammer 
    #  3. Drop gripper around the nail 
    #  4. Move the hammer down and hit the nail
    
    # Put the gripper above the hammer, so that it can grab it without bumping
    # into it.
    if check("the robot's gripper is not above the hammer"):
        robot.put("gripper above hammer")
    # If the gripper is above the hammer but not around it, try to grab the
    # hammer.
    if check("the robot's gripper is above the hammer and the robot's gripper is not around the hammer"):
        robot.drop("gripper around hammer")
    # If the gripper is above the nail but not around it, try to grab the nail
    # with the gripper.
    if check("the robot's gripper is not around the nail"):
        robot.drop("gripper around nail")
    # If the gripper is around both the hammer and the nail, move the gripper
    # down towards the nail to hit it.
    if check("the robot's gripper is around the hammer and the robot's gripper is around the nail"):
        robot.move("gripper down and hit nail")
```