Here's the code for performing the `shelf-place` task, which involves picking up a block and placing it on a shelf at a target location:

```
# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    if check("the robot's gripper is not above the block"):
        robot.place("gripper above block")
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        if check("the robot's gripper is not near the shelf"):
            robot.move("gripper to shelf")
        if check("the robot's gripper is aligned with the shelf"):
            robot.release("block on shelf")
``` 

This program ensures that the robot picks up the block, holds it securely, and then places it on the shelf at the target location. It uses conditional statements to check the robot's position and alignment in relation to the block and the shelf.