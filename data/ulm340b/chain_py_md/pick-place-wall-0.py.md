

Please explain what you would do.

```

```

"""


def pick_place_wall(robot):
    """
    Steps:
    1. Put gripper above puck
    2. Drop gripper around puck
    3. Close gripper around puck
    4. Slide puck to goal
    Because of the wall in the way, we need to slide puck instead of lift and place it.
    Put the robot's gripper above the puck.
    Because of the wall, we need to line it up directly above, instead of just roughly above.
    If the gripper is not above the puck, move the gripper above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with puck"):
        robot.put("the gripper above the puck")
    If the gripper is not around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    Because of the wall, we need to slide puck to goal. 
    if check("the robot's gripper is closed around puck"):
        robot.slide("puck to goal")
    """
    
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Slide puck to goal
    # Because of the wall in the way, we need to slide puck instead of lift and place it.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with puck"):
        robot.put("the gripper above the puck")
    # If the gripper is not around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
  