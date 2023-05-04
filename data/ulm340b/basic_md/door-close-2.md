
    - [ ] When the robot's gripper is not above the door handle, the robot should put the gripper above the door handle.
    - [ ] When the robot's gripper is above the door handle and the robot's gripper is not near the door handle, the robot should place gripper around door handle.
    - [ ] When the robot's gripper is near door handle and the robot's gripper is around door handle, the robot should pull the door handle toward the goal.
    - [ ] When the robot's gripper is forward aligned with the door handle and the robot's gripper is around the door handle, the robot should push door towards target.

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, what steps the robot should perform?
    - [ ] When the robot's gripper is not above the peg, the robot should put the gripper above the peg.
    - [ ] When the peg is near the robot's gripper, the robot should put the gripper around the peg.
    - [ ] When the peg is below the robot's gripper, the robot should put the gripper around the peg.
    - [ ] When the robot's gripper is around the peg, the robot should pick up the peg.
    - [ ] When the robot's gripper is in front of the peg, the robot should push the peg towards the hole.
    - [ ] When the peg is inside the hole, the robot should release the gripper.

"""

instructions_2 = """Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not