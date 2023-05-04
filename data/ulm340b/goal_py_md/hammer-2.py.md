

The robot can perform one of the following primitive actions:

```
robot.move_gripper("left", close_gripper=True) # closes gripper and moves it left
robot.move_gripper("left", close_gripper=False) # moves gripper left
robot.move_gripper("right", close_gripper=True) # closes gripper and moves it right
robot.move_gripper("right", close_gripper=False) # moves gripper right
robot.move_gripper("up", close_gripper=True) # closes gripper and moves it up
robot.move_gripper("up", close_gripper=False) # moves gripper up
robot.move_gripper("down", close_gripper=True) # closes gripper and moves it down
robot.move_gripper("down", close_gripper=False) # moves gripper down
robot.move_gripper("above the puck") # moves gripper above the puck
robot.move_gripper("near the puck") # moves gripper near the puck
robot.move_gripper("above the target location") # moves gripper above the target location
robot.move_gripper("near the reach target") # moves gripper near the reach target
robot.move_gripper("near the button") # moves gripper near the button
robot.move_gripper("above the button") # moves gripper above the button
robot.move_gripper("around the button") # moves gripper around the button
robot.move_gripper("vertically aligned with the button") # moves gripper vertically aligned with the button
robot.move_gripper("around the door handle") # moves gripper around the door handle
robot.move_gripper("vertically aligned with the door handle") # moves gripper vertically aligned with the door handle
robot.move_gripper("left of the door handle") # moves gripper left of the door handle
robot.move_gripper("horizontally aligned with the door handle") # moves gripper horizontally aligned with the door handle
robot.move_gripper("around the drawer handle") # moves gripper around the drawer handle
robot.move_gripper("vertically aligned with the drawer handle") # moves gripper vertically aligned with the drawer handle
robot.move_gripper("near the drawer handle") # moves gripper near the drawer handle
robot.move_gripper("horizontally aligned with the drawer handle") # moves gripper horizontally aligned with the drawer handle
robot.move_gripper("forward aligned with the drawer handle") # moves gripper forward aligned with the drawer handle
robot.move_gripper("above the peg") # moves gripper above the peg
