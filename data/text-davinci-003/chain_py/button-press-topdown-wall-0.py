
    # Steps:
    #  1. Line up gripper as seen from above
    #  2. Adjust gripper to avoid the wall
    #  3. Push down on the button
    # If the gripper isn't very close to being vertically aligned with the
    # button, we need to move it above the button.
    # This should also line it up from the front, since it's very close.
    if check("the robot's gripper is not almost vertically aligned with button"):
        robot.put("gripper above button")
    # If the gripper is almost lined up but there's still a wall in the way,
    # slide the gripper to the side to avoid the wall.
    if check("the robot's gripper is almost vertically aligned with button and the robot's gripper is still partially blocked by wall"):
        robot.slide("gripper to avoid wall")
    # Now that the gripper is lined up and the wall is out of the way, just push
    # down on the button.
    if check("the robot's gripper is vertically aligned with button and the wall is no longer in the way"):
        robot.push("down on button")