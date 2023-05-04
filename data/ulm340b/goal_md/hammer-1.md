

The task `push-back` requires the robot to push the puck backwards.
To push the puck backwards reliably, what steps the robot should perform?

The task `reach-back` requires the robot to reach the target location.
To reach the target location reliably, what steps the robot should perform?
""".split("\n")

descriptions = {  # key: (robot_name, domain_expert_name, task_name, description)
    '1249298126': ('a1', 'c1', 'pick-place-topdown', r"""Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `pick-place` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Grab the puck by lowering the gripper  3. Move puck to goal
    We should start by lining up the gripper as seen from above.
    - When the robot's gripper is not above the puck, move the robot's gripper until the robot's gripper is above the puck
    Now that the gripper is lined up, we can drop the gripper down and grab the puck.
    - When the robot's gripper is vertically aligned with the puck, move the robot's gripper until the robot's gripper is below the puck and the robot's gripper is closed
    Since the gripper is closed and around the puck, we can just move the gripper to the goal.
    - When the robot's gripper is around the puck, move the robot's gripper until the robot's gripper is near the target location

The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, the robot should perform the following steps:
    Steps:  1. Reach towards the target
    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    - When the robot's gripper is not near reach target, move the robot's gripper until the robot's gripper is near the reach target

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper