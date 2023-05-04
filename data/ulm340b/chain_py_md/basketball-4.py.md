

''')

if __name__ == "__main__":
    task_text = '''basketball'''

    task_instruction_template = r'''
# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1.
    #  2.
    #  3.
    # First, .
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the , go back to putting the .
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")
'''

    task_instruction = task_instruction_template.replace('basketball', 'basketball')
    task_instruction = task_instruction.replace(' ', '  ')
    task_instruction = task_instruction.replace('  ', '\t')

    agent = ParlAIMultiTaskDialogTeacher()
    lesson_name = os.path.basename(os.path.dirname(__file__))
    agent.start_task(task_instruction)

    train_batchsize = 2
    valid_batchsize = 2
    # training
    for epoch in range(4):
        agent.shutdown()

        task_data = os.path.join('task_data', task_text)
        with open(task_data, 'rb') as f:
            task = pickle.load(f)
        assert len(task['init']['instructions']['text']) == 0
        batchsize = len(task['train']['instructions'])

        if batchsize < train_batchsize