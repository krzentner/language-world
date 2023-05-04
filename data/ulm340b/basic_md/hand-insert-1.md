
    {answers}


The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, what steps the robot should perform?
    {answers}


The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, what steps the robot should perform?
    {answers}


The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, what steps the robot should perform?
    {answers}


The task `door-open` requires the robot to pull the door open.
To pull the door open reliably, what steps the robot should perform?
    {answers}


The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, what steps the robot should perform?
    {answers}


The task `window-open` requires the robot to slide the window open to the left.
To slide the window open to the left reliably, what steps the robot should perform?
    {answers}


The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, what steps the robot should perform?
    {answers}


The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, what steps the robot should perform?
    {answers}


The task `push` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, what steps the robot should perform?
    {answers}


The task `pick-place` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, what steps the robot should perform?
    {answers}
"""
    template_test_questions = """
{task} requires the robot to {description}.
To {description} reliably, the robot should perform the following steps:
{steps}
{description}:
    {answers}
"""

    def __init__(self, seed=None,
                 eval_template_test_questions=False,
                 eval_template_instructions=False,
                 eval_template_task_completion=False,
                 eval_template_task_instruction_completion=False,
                 eval_template_task_instruction_completion