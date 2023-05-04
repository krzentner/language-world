
    Steps:  1. Put gripper around the faucet  2. Turn the faucet right
    Put the gripper above the faucet, and then drop it around the faucet.
    - When the robot's gripper is not above the faucet, the robot should put the gripper above the faucet.
    - When the robot's gripper is above the faucet and the robot's gripper is not around the faucet, the robot should put gripper around faucet.
    As long as the gripper is around the faucet, turning right is working.
    - When the robot's gripper is around faucet, the robot should turn faucet right.

The task `pull-lever` requires the robot to pull the lever down.
To pull the lever down reliably, what steps the robot should perform?
    Steps:  1. Put gripper above the lever  2. Drop gripper around the lever  3. Pull the lever down
    We need to put the gripper above the lever before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not above the lever, the robot should put gripper above lever.
    Once the gripper is lined up above the lever, we should be able to grab the lever by moving the gripper down around it.
    - When the robot's gripper is above lever and the robot's gripper is not around lever, the robot should put gripper around lever.
    Once the gripper is around the lever, we can just pull it down.
    - When the robot's gripper is around lever, the robot should pull lever down.

The task `button-press-side` requires the robot to push the button to the left.
To push the button to the left reliably, what steps the robot should perform?
    Steps:  1. Put gripper right of button  2. Push button to the left
    If the the button is left of the robot's gripper, we should move the gripper near the button to start pushing
    - When the robot's gripper is left of button and the robot's gripper is not near button, the robot should move gripper to right of button.
    If the robot's gripper is near the button we can probably press the button now by moving the gripper left.
    - When the robot's gripper is near button, the robot should push button left.

The task `peg-insert-topdown` requires the robot to grab the peg and insert it into the hole from the top down.
To grab the peg and insert it into the hole from the top down reliably