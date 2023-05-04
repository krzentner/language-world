

and add code to complete the task.
""")

# 
# #handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
#     #Steps:
#     #1. Put gripper above the handle
#     #2. Grab the handle with the gripper
#     #3. Pull up the handle
#     # First, put the gripper above the handle.
#     if check("the robot's gripper is not vertically aligned with handle"):
#         robot.move_gripper("vertically aligned with handle")
#     # Once the gripper is above the handle, move the gripper to be around the handle to grab it.
#     if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
#         robot.move_gripper("around handle")
#     # After the handle is lined up with the gripper and the gripper has closed around the handle, pull it up.
#     if check("the robot's gripper is vertically aligned with handle and the robot's gripper is around handle and handle is left of the robot's gripper"):
#         robot.move_gripper("left of handle")

# 


# 
# The last task, `handle-pull-side`.
# ```
# # handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
#     #Steps:
#     #1. Put gripper above the handle
#     #2. Grab the handle with the gripper
#     #3. Pull up the handle
#     # First, put the gripper above the handle.
#     if check("the robot's gripper is not vertically aligned with handle"):
#         robot.move_gripper("vertically aligned with handle")
#     # Once the gripper is above the handle, move the gripper to be around the handle to grab it.
#     if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
#         robot.move_gripper("around handle")
#     # After the handle is lined up with the gripper and the gripper has closed around the handle, pull it up.
#     if check("the robot's gripper is vertically aligned with handle and the robot's gripper is around handle and handle is left of the robot's gripper"):
#         robot.move_gripper("left of handle")
# ```

# 
# ```
# # reach: reach to the target