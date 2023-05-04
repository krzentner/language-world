
""",
    "question_template": """
The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, what steps the robot should perform?
    - When the robot's gripper is not vertically aligned with the peg, the robot should {put_gripper_above_peg_answer}.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should {grab_peg_answer}.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should {align_peg_to_hole_answer}.
    - When peg is horizontally aligned with hole, the robot should {insert_peg_into_hole_answer}.
    
The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, what steps the robot should perform?
    - When the robot's gripper is not near reach target, the robot should {reach_to_goal_answer}.
    
The task `push` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, what steps the robot should perform?
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should {put_the_gripper_above_the_puck_answer}.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should {push_the_gripper_into_the_puck_answer}.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should {slide_the_puck_to_the_goal_answer}.
    
The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, what steps the robot should perform?
    - When the robot's gripper is not vertically aligned with button, the robot should {put_gripper_above_button_answer}.
    - When the robot's gripper is vertically aligned with button, the robot should {push_down_on_button_answer}.

The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, what steps the robot should perform?
    - When the window handle is