

The goal of this program is to move the robot's gripper to the position of the lever and rotate it upwards.

``` 
# Lever-pull: rotate the lever up
# def lever_pull(robot):
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.position("gripper above lever")
    if check("the robot's gripper is vertically aligned with the lever and the robot's gripper is not left aligned with the lever"):
        robot.move("gripper left of lever")
    if check("the robot's gripper is left of the lever"):
        robot.rotate("lever upward")
    ```