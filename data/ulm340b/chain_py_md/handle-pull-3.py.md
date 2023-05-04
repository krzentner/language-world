

... and enter the body of the function below.


(There is a 250-token hard limit for your code here).
''',
    examples_per_instruction=1,
    instructions=[
        Instruction(examples='''
        'vertically aligned'
        'vertically aligned with'
        'almost vertically aligned with'
        'almost vertically aligned'
        'horizontally aligned'
        'horizontally aligned with'
        '''),
        Instruction(examples='''
        'below'
        'below the'
        'below the robot'
        'below the robot\'s gripper'
        'above the robot\'s gripper'
        'above the'
        'above the robot'
        'above the robot\'s gripper'
        'above'
        '''),
        Instruction(examples='''
        'open'
        'opened'
        'closed'
        '''),
        Instruction(examples='''
        'left of'
        'left of the'
        'left of the robot\'s gripper'
        'left of the robot'
        'left'
        'right of'
        'right of the'
        'right of the robot\'s gripper'
        'right of the robot'
        'right'
        '''),
        Instruction(examples='''
        'near'
        'near the'
        'near the robot\'s gripper'
        'near the robot'
        '''),
        Instruction(examples='''
        'forward aligned with'
        'forward aligned with the'
        'forward aligned with the robot\'s gripper'
        'forward aligned with the robot'
        '''),
        Instruction(examples='''
        'forward aligned'
        'forward aligned with'
        'forward aligned with the'
        'forward aligned with the robot\'s gripper'
        'forward aligned with the robot'
        '''),
    ],
    maximum_code_length=250,
)
[eod] [code]class Student:
    school = '成都信息工程大学'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def study(self, course_name):
        print('%s 正在学习 %s ' % (self.name, course_name))

    