
    # Steps:
    #  1. Put gripper above the puck
    #  2. Push puck to goal
    # Put gripper above the puck so that we can push it to goal without bumping
    # it.
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.put("gripper above puck")
    # Push puck towards goal.
    if check("the robot's gripper is vertically aligned with puck"):
        robot.push("puck to goal")

# slide: slide the puck to the target location
def slide(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Push puck to goal
    # Put gripper above the puck so that we can push it to goal without bumping
    # it.
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.put("gripper above puck")
    # Slide puck towards goal.
    if check("the robot's gripper is vertically aligned with puck"):
        robot.slide("puck towards goal")

# toggle-switch: push the switch down, then lift it back up
def toggle_switch(robot):
    # Steps:
    #  1. Put gripper above switch
    #  2. Put gripper around switch
    #  3. Push switch down
    #  4. Lift switch up
    # Put gripper above the switch so that we can push it down without bumping
    # it.
    if check("the robot's gripper is not above the switch"):
        robot.put("gripper above switch")
    # We're above the switch, so we can put the gripper around it.
    # Check if the gripper is above the switch by checking the bottom of the
    # gripper instead of the top, because the bottom is what's used to interact
    # with the switch.
    if check("the switch is not forward aligned with the bottom of the robot's gripper"):
        robot.grab("switch")
    # Once the gripper is roughly around the switch, we can move it downwards
    # to push the switch down.
    if check("the switch is forward aligned with the bottom of the robot's gripper"):
        robot.push("down