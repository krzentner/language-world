

Steps:
  1. Line up the gripper as viewed from above
  2. Push the wall back from the button
  3. Push down the button from the top 
  
  # button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):  
    # First, line up the gripper above the button with the wall in between
    if check("the robot's gripper is not above the button and the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button with wall in between")
    # Once the gripper is lined up, we can start pushing the wall back
    if check("the robot's gripper is above the button and the robot's gripper is not behind the wall"):
        robot.push("wall back from button")
    # After the wall is out of the way, push the button down from above.
    if check("the robot's gripper is above the button and the robot's gripper is behind the wall"):
        robot.push("down on button")