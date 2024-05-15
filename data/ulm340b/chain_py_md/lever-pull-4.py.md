

Here are some hints to get you started:

- `robot.grab("lever")` will close the gripper around the lever
- You need to pull the lever up and away from the robot
"""

# TEMPLATE_TEXT = dedent("""
# # push: slide the puck to the target location
# def push(robot):
#     # Steps:
#     #  1. Put gripper above puck
#     #  2. Push gripper into top of puck
#     #  3. Slide puck to goal
#     # The robot can slide the puck by trapping it by pushing down on it from
#     # above and moving the gripper.
#     # If the puck isn't below the gripper as seen from above, move the gripper
#     # above the puck.
#     if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
#         robot.put("the gripper above the puck")
#     # If the gripper is aligned with the puck but not near it, move the gripper
#     # down to the puck to slide it.
#     if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
#         robot.push("the gripper into the puck")
#     # If the gripper is near the puck, we've probably trapped the puck and can
#     # slide it to the target location.
#     # Close the gripper to make sure we keep control of the puck.
#     if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
#         robot.slide("the puck to the goal")

# # window-close: slide the window closed to the right
# def window_close(robot):
#     # Steps:
#     #  1. Put gripper left of the window handle
#     #  2. Start pushing against the window handle to close the window
#     #  3. Push the window closed harder
#     # If the the window handle is right of the robot's gripper, we should move the
#     # gripper near the window handle to start pushing
#     if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
#         robot.move("gripper to left of window handle")
#     # If the robot's gripper is near the window handle we can probably slide the
#     # window close now by moving the gripper right.
#