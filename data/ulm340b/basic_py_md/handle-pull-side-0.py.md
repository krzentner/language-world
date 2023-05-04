
"""
# TODO(nikita): change text
TEXT = "Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.\n\n" \
       "Here's some code that demonstrates how the robot can do a variety of tasks:\n\n" \
       "**[text1]**\n" \
       "Please write a program to perform the last task, `handle-pull-side`.\n" \
       "Begin with the text:\n" \
       "```\n" \
       "# handle-pull-side: pull up the handle from the side\n" \
       "def handle_pull_side(robot):\n" \
       "```"

# Handle-pull-side instructions:
# 1. If the robot's gripper is not near the handle:
#   - move the robot's gripper to be on the left side of the handle
# 2. If the robot's gripper is not near the handle:
#   - move the robot's gripper to be on the left side of the handle
# 3. If the robot's gripper is near the handle:
#   - close the robot's gripper around the handle
# 4. If the robot's gripper is near the handle:
#   - move the robot's gripper up away from the handle
# 5. If the robot's gripper is not in front of the handle:
#   - move the robot's gripper away from the handle
# 6. If the robot's gripper is in front of the handle:
#   - move the robot's gripper to the left of the handle
# 7. If the robot's gripper is left of the handle:
#   - move the robot's gripper up towards the handle
# 8. If the robot's gripper is near the handle:
#   - open the robot's gripper
# 9. If the robot's gripper is not vertically aligned with the handle:
#   - move the robot's gripper above the handle
# 10. If the robot's gripper is not near the handle:
#   - move the robot's gripper towards the handle
# 11. If the robot's gripper is near the handle:
#   - close the robot's gripper around the handle
# 12. If the robot's gripper is vertically aligned with the handle:
#   - move the robot's gripper away from the handle