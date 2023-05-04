

(The robot can't grab the button, but it can slide it down.)

I've asked you to write the definition of `button_press_topdown` above the
other definitions, so that I can run `button_press_topdown` first.

**Remember: I can't read anything besides what you write in the space above!**
""",
    )

    def check_question(self, answer: str) -> bool:
        answer = answer.strip()

        def get_first_line() -> str:
            return answer.splitlines()[0].strip()

        if get_first_line() != "# button-press-topdown: push the button down from above":
            return False

        i = 0
        while i < len(BUTTON_PRESS_TOPDOWN) - 1:
            next_line = BUTTON_PRESS_TOPDOWN[i + 1]
            try:
                curr_line = next(line for line in answer.splitlines() if line)
            except StopIteration:
                return False

            if curr_line.strip() != next_line:
                return False

            i += 1

        return True


class ButtonsQuestion(Question):
    _answer = """
# button-press-side: push the button down from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper in front of the button
    #  2. Close the gripper on the button
    #  3. Push the button down
    # The robot can slide the button by pushing it down from the side.
    if check("the robot's gripper is not in front of the button"):
        robot.move_gripper("forward aligned with the button")
    # If the button isn't in front of the robot's gripper, we can probably move
    # the robot's gripper to be in front of the button.
    if check("the button is in front of the robot's gripper and the robot's gripper is not near the button"):
        robot.move_gripper("near the button")
    # If the gripper is in front of the button we can just close it to slide it
    # down.
    if check("the button is not in front of the robot's gripper"):
        robot.move_gripper("in front of the button")

# button-press-corner: push the button into the