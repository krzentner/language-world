
`,
  `
    - When the robot's gripper is not vertically aligned with the mug, the robot should put gripper above mug.
    - When the robot's gripper is vertically aligned with the mug and the robot's gripper is not around the mug, the robot should put gripper around mug.
    - When the robot's gripper is closed and the robot's gripper is forward aligned with the mug, the robot should move mug to goal.



`,
}

func (s *suite) TestButtonPressTopdown() {
	assertExpectedOutputFromTemplate(
		s.T(),
		taskTemplate,
		getButtonPressTopdownTask(&s.sd),
	)
}

func (s *suite) TestDrawerOpen() {
	assertExpectedOutputFromTemplate(
		s.T(),
		taskTemplate,
		getDrawerOpenTask(&s.sd),
	)
}

func (s *suite) TestDrawerClose() {
	assertExpectedOutputFromTemplate(
		s.T(),
		taskTemplate,
		getDrawerCloseTask(&s.sd),
	)
}

func (s *suite) TestDoorOpen() {
	assertExpectedOutputFromTemplate(
		s.T(),
		taskTemplate,
		getDoorOpenTask(&s.sd),
	)
}

func (s *suite) TestWindowClose() {
	assertExpectedOutputFromTemplate(
		s.T(),
		taskTemplate,
		getWindowCloseTask(&s.sd),
	)
}

func (s *suite) TestWindowOpen() {
	assertExpectedOutputFromTemplate(
		s.T(),
		taskTemplate,
		getWindowOpenTask(&s.sd),
	)
}

func (s *suite) TestPegInsertSide() {
	assertExpectedOutputFromTemplate(
		s.T(),
		taskTemplate,
		getPegInsertSideTask(&s.sd),
	)
}

func (s *suite) TestPush() {
	assertExpectedOutputFromTemplate(
		s.T(),
		taskTemplate,
		getPushTask(&s.sd),
	)
}

func (s *suite) TestReach() {
	assertExpectedOutputFromTemplate(
		s.T(),
		taskTemplate,
		getReachTask(&s.sd),
	)
}

func (s *suite) TestPickPlace() {
	assertExpected