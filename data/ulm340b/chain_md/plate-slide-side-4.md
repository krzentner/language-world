
"""


_instructions_all_test = """
Hello! Today I would like you to describe how the robot should perform tasks.

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, what steps the robot should perform?

The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, what steps the robot should perform?

The task `door-open` requires the robot to pull the door open.
To pull the door open reliably, what steps the robot should perform?

The task `drawer-close` requires the robot to push the drawer closed.
To push the drawer closed reliably, what steps the robot should perform?

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, what steps the robot should perform?

The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, what steps the robot should perform?

The task `window-open` requires the robot to slide the window open to the left.
To slide the window open to the left reliably, what steps the robot should perform?

The task `pick-place` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, what steps the robot should perform?

The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, what steps the robot should perform?

The task `push` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, what steps the robot should perform?

The task `plate-slide-side` requires the robot to slide the plate sideways into the target location.
To slide the plate sideways into the target location reliably, what steps the robot should perform?


"""


def run(instructions):
    print(instructions)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--env", type=str, required=True)
    parser.add_argument("--domain_name", type=str, required=True)
    parser.add_argument("--experiment_id", type=str, required=True)
    parser.add_argument("--instructions_path", type=str, required=True)
    args = parser.parse_