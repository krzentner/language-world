

and complete the `if-then` conditions for each step the robot should take.
The robot should start with its gripper below the window handle, open the gripper and slide the window closed, then release the gripper from the window handle.

Please finish all of the tasks within this `def` by writing `if` statements for the preconditions and actions.

For example:

```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
```
"""
[eod] [code]from io import StringIO

from django.test import TestCase
from django.core.management import call_command


class CommandTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(CommandTest, cls).setUpClass()
        cls.stdout = StringIO()
        cls.stderr = StringIO()
        out = cls.stdout.write  # Wrapper used to clear output buffer
        cls.stdout.write = lambda x: out(x.replace('\r', ''))

    @classmethod
    def tearDownClass(cls):
        cls.stdout.close()
        cls.stderr.close()

    def test_create_superuser(self):
        command = ['create_superuser', '--username', 'user@email.com']
        call_command(*command, stdout=self.stdout, stderr=self.stderr)
        output = self.stdout.getvalue()
        self.assertIn('Superuser created successfully.', output)

        with self.assertRaises(SystemExit):
            call_command('create_superuser')


class CommandTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(CommandTests, cls).setUpClass()
        cls.stdout = StringIO()
        cls.stderr = StringIO()
        out = cls.stdout.write  # Wrapper used to clear output buffer
        cls.stdout.write = lambda x: out(x.replace('\r', ''))

    @classmethod
    def tearDownClass(cls):
        cls.stdout.close()
        cls.stderr.close()

    def test_generate_tokens(self):
        command = ['generate_tokens', '--