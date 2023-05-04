
    Steps:  1. Put gripper below stick  2. Grab the stick with the gripper  3. Pick up the stick  4. Move gripper around the thermos handle  5. Put gripper around the thermos handle  6. Pull thermos to goal
    First, put the gripper below the stick to avoid bumping it before we grab it.
    - When the robot's gripper is not below the stick, the robot should put gripper below the stick.
    When the gripper is below the stick, grab the stick.
    - When the robot's gripper is below the stick and the robot's gripper is not around stick, the robot should grab stick.
    If the gripper is around the stick, pull the stick towards the robot to pick it up.
    - When the robot's gripper is around stick and the stick is in front of the robot's gripper, the robot should pick up stick.
    If the robot picked up the stick but its gripper is no longer around the stick, go back to putting the gripper around the stick.
    - When the robot's gripper is open and the stick is below the robot's gripper, the robot should grab stick.
    As long as the stick is mostly still below the robot's gripper and the thermos handle is behind the robot's gripper, move the gripper around to line it up with the thermos handle.
    - When the robot's gripper is below stick and the thermos handle is behind the robot's gripper, the robot should put gripper around thermos handle.
    When the robot's gripper is roughly around the thermos handle, put it down on the handle.
    - When the robot's gripper is near thermos handle and the robot's gripper is not around thermos handle, the robot should put gripper around thermos handle.
    With the gripper around the thermos handle, we should be able to pull the thermos to the target.
    - When the robot's gripper is around thermos handle, the robot should pull thermos to goal.
'''

robot_feedback_example = '''
The current task is `button-press-topdown`.
To push the button down from above reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot'