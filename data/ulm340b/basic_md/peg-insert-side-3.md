

    >>> task = 'peg-insert-side'
    >>> rules = ['when the robot s gripper is not near peg , the robot should move gripper above peg .',
    ...          'when the robot s gripper is near peg and the robot s gripper is open , the robot should close gripper .',
    ...          'when the robot s gripper is closed and the robot s gripper is around peg , the robot should lift gripper above table .',
    ...          'when the robot s gripper is above table and the robot s gripper is near hole , the robot should insert peg into hole .']
    >>> for rule in rules:
    ...     if rule in get_actions(task):
    ...         print(rule)
    ...
    when the robot s gripper is not near peg , the robot should move gripper above peg .
    when the robot s gripper is near peg and the robot s gripper is open , the robot should close gripper .
    when the robot s gripper is closed and the robot s gripper is around peg , the robot should lift gripper above table .
    when the robot s gripper is above table and the robot s gripper is near hole , the robot should insert peg into hole .

The task `peg-unstack` requires the robot to unstack the peg from the peg.
To unstack the peg from the peg reliably, what steps the robot should perform?

    >>> task = 'peg-unstack'
    >>> rules = ['when the robot s gripper is not near peg , the robot should move gripper above peg .',
    ...          'when the robot s gripper is near peg and the robot s gripper is open , the robot should close gripper .',
    ...          'when the robot s gripper is above table and the robot s gripper is closed and the robot s gripper is around peg , the robot should lift gripper above table .',
    ...          'when the robot s gripper is closed and the robot s gripper is above table and the robot s gripper is around peg , the robot should lift gripper above table .',
    ...          'when the robot s gripper is closed and the robot s gripper is above table and the robot s gripper is around peg and the robot s gripper is above table , the robot should move gripper above table .',
    ...          'when