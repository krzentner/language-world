

Steps:
  1. Put gripper above button
  2. Drop gripper around button
  3. Push down on button

# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Drop gripper around button
    #  3. Push down on button
    # Put the gripper in the general area of the button to get it close enough.
    if check("the robot's gripper is not near button"):
        robot.put("gripper above button")
    # As long as the gripper isn't quite around the button, drop it around the
    # it.
    if check("the robot's gripper is not around button"):
        robot.drop("gripper around button")
    # Now that the gripper is around the button, press down on it to push the
    # button.
    if check("the robot's gripper is around button"):
        robot.push("down on button")