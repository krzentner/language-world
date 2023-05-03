

Steps:
1. Place gripper above the dial
2. Grasp the dial
3. Turn the dial to the desired angle

```
# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Place gripper above the dial
    #  2. Grasp the dial
    #  3. Turn the dial to the desired angle
    
    # Place gripper above the dial
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial")    
    
    # Grasp the dial 
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("near the dial", close_gripper=True)
    
    # Turn the dial to the desired angle
    if check("the robot's gripper is not facing the desired angle"):
        robot.move_gripper("facing the desired angle")
```