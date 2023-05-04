

and implement the rest of the function.
'''
# lever-pull: rotate the lever up
def lever_pull(robot):
    # The lever is at the bottom center of the scene.
    # Because the robot's gripper faces downwards and has to rotate the lever
    # upwards, put the gripper left of the lever.
    if check("the robot's gripper is not left of the lever"):
        robot.move_gripper("left of the lever", close_gripper=True)
    # When the lever is right of the gripper, push the gripper down on the lever.
    # This will cause the gripper to wrap around the lever and pull it up
    if check("the robot's gripper is not right of the lever"):
        robot.move_gripper("above the lever")

'''Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

Here's some code that demonstrates how the robot can do a variety of tasks:

```
# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck