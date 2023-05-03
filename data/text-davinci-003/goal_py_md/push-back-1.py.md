

The steps for this task are: 
1. Put gripper above puck 
2. Push gripper into back of puck
3. Slide puck to goal

The code should look like this:
```
# push-back: slide the puck backward to the target location
def push_back(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into back of puck 
    #  3. Slide puck to goal
    # Start by putting the gripper above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't behind the puck, put it behind the puck.
    if check("the robot's gripper is not behind the puck"):
        robot.move_gripper("behind the puck", close_gripper=True)
    # If the gripper is behind the puck, we can slide it to the target location.
    if check("the robot's gripper is behind the puck"):
        robot.move_gripper("above the target location")
```