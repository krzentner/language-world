




To push down the handle from the side reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper so the handle is left of the robot's gripper  2. Push the handle down
    If the handle is left of the gripper, line it up with the robot's gripper to push it down.
    - When the robot's gripper is not forward aligned with handle, move the robot's gripper until the robot's gripper is forward aligned with handle
    Now that the gripper is lined up, just push down on the handle.
    - When the robot's gripper is forward aligned with handle, move the robot's gripper until the robot's gripper is near the handle
"""

instructions = [
    # Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.
    [{"utterance": "Hello.", "image": None, "grounding": None}, {"utterance": "Today I would like you to help me control a robot.", "image": None, "grounding": None}, {"utterance": "The robot has a single gripper that it can use to grab small objects.", "image": None, "grounding": None}],
    # The task `reach` requires the robot to reach to the target location.
    [{"utterance": "The task `reach` requires the robot to reach to the target location.", "image": None, "grounding": None}],
    # To reach to the target location reliably, the robot should perform the following steps:    Steps:  1. Reach towards the target
    [{"utterance": "To reach to the target location reliably, the robot should perform the following steps:", "image": None, "grounding": None}, {"utterance": "    Steps:  1. Reach towards the target", "image": None, "grounding": None}],
    # We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    [{"utterance": "We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location", "image": None, "grounding": None}],
    # - When the robot's gripper is not near reach target, move the robot's gripper until the robot's gripper is near the reach target
    [{"utterance": "- When the robot's gripper is not near reach target, move the robot's gripper until