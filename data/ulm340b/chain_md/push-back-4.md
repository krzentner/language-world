

The task `lever-pull` requires the robot to pull the lever.
To pull the lever reliably, what steps the robot should perform?

The task `peg-insert-vertical` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, what steps the robot should perform?

The task `reach-back` requires the robot to reach to the target location backwards.
To reach to the target location backwards reliably, what steps the robot should perform?

The task `drawer-close-back` requires the robot to push the drawer close backwards.
To push the drawer close backwards reliably, what steps the robot should perform?

The task `door-open-back` requires the robot to pull the door open backwards.
To pull the door open backwards reliably, what steps the robot should perform?

The task `button-press-back` requires the robot to push the button with the back of the robot's gripper.
To push the button with the back of the robot's gripper reliably, what steps the robot should perform?

The task `button-press-back-topdown` requires the robot to push the button with the back of the robot's gripper from above.
To push the button with the back of the robot's gripper from above reliably, what steps the robot should perform?

The task `pick-place-back` requires the robot to pick up the puck and hold it at the target location backwards.
To pick up the puck and hold it at the target location backwards reliably, what steps the robot should perform?

The task `push-back-back` requires the robot to slide the puck backwards to the target location backwards.
To slide the puck backwards to the target location backwards reliably, what steps the robot should perform?

The task `drawer-open-back` requires the robot to pull the drawer open backwards.
To pull the drawer open backwards reliably, what steps the robot should perform?

The task `peg-insert-side-back` requires the robot to grab the peg and insert it into the hole from the side backwards.
To grab the peg and insert it into the hole from the side backwards reliably, what steps the robot should perform?

"""


# noinspection PyPep8Naming
# pylint: disable=invalid-name, missing-docstring, unused-variable, too-many-locals
class INSTRUCTION_DATASET(object):
    """
    The dataset we used for our experiment.

    Data:
        The keys are the task names: 'button-press-topdown', 'drawer-open', 'door-open', 'drawer-close',