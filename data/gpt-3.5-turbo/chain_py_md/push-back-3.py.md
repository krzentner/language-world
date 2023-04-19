```
# push-back: slide the puck backwards to the target location
# def push_back(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck to lift it
    #  3. Move gripper backwards towards target location
    #  4. Lower gripper
    #  5. Slide puck to goal
    # First, put the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.drop("gripper around the puck")
    # Close the gripper to lift the puck
    if check("the robot's gripper is around the puck and the robot's gripper is open"):
        robot.close("gripper around the puck")
    # Back up while holding the puck
    if check("the robot's gripper is holding the puck"):
        robot.move("gripper backward to goal")
    # Lower the gripper
    if check("the robot's gripper is near the goal"):
        robot.put("gripper down")
    # Slide the puck to the goal
    if check("the puck is below the gripper"):
        robot.slide("the puck to the goal")
```