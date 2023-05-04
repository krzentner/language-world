
    - When the robot's gripper is not above the stick, the robot should put gripper above stick.
    - When the robot's gripper is not around stick and the robot's gripper is open, the robot should drop gripper around stick.
    - When the robot's gripper is near stick and the robot's gripper is open, the robot should close gripper around stick.
    - When the robot's gripper is above stick and the robot's gripper is closed, the robot should push thermos to target location.

The task `stick-place` requires the robot to grab the stick and use it to lift the thermos and place it at the target location.
To grab the stick and use it to lift the thermos and place it at the target location reliably, what steps the robot should perform?
    - When the robot's gripper is not above the stick, the robot should put gripper above stick.
    - When the robot's gripper is not around stick and the robot's gripper is open, the robot should drop gripper around stick.
    - When the robot's gripper is near stick and the robot's gripper is open, the robot should close gripper around stick.
    - When the robot's gripper is above stick and the robot's gripper is closed, the robot should place thermos at target location.

The task `peg-unstack` requires the robot to grab the top peg and lift it off the stack.
To grab the top peg and lift it off the stack reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the stack, the robot should put gripper above stack.
    - When the robot's gripper is not above peg and the robot's gripper is open, the robot should drop gripper around peg.
    - When the robot's gripper is near peg and the robot's gripper is open, the robot should close gripper around peg.
    - When the robot's gripper is above peg and the robot's gripper is closed, the robot should lift peg off stack.
"""

def _create_explanations(domain_instructions):
    domain_to_explanations = {
        'default': {
            'button-press-topdown': {
                'explanations': [
                    "When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.",
                    "When the robot's gripper is vertically aligned with button, the robot should push down on button.",
                ],
                'video_link': 'https://youtu.be