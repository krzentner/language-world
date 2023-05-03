

To perform the task `hammer`, the robot would need to do the following:

1. Put gripper above hammer 
2. Drop gripper around hammer
3. Line up the head of the hammer with the nail
4. Bring down the hammer quickly onto the nail

```
# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Put gripper above hammer 
    #  2. Drop gripper around hammer
    #  3. Line up the head of the hammer with the nail
    #  4. Bring down the hammer quickly onto the nail
    # Put the gripper above the hammer.
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.put("gripper above hammer")
    # If the gripper isn't around the hammer, put it around the hammer.
    if check("the robot's gripper is not around hammer and the robot's gripper is open"):
        robot.drop("gripper around hammer")
    # If the gripper is around the hammer and the hammer is not lined up with
    # the nail as seen from the side, line up the hammer with the nail.
    if check("the robot's gripper is around hammer and the hammer is not side aligned with nail"):
        robot.align("hammer to nail")
    # If the hammer is lined up with the nail, bring it down quickly in a
    # hammering motion.
    if check("hammer is side aligned with nail"):
        robot.strike("down on nail")

```