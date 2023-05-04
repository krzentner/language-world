
Steps:
`reach` requires the robot to reach to the target location.
To reach to the target location reliably, what steps the robot should perform?
Steps:
`window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, what steps the robot should perform?
Steps:
`drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, what steps the robot should perform?
Steps:
`peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, what steps the robot should perform?
Steps:
`push` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, what steps the robot should perform?
Steps:
`door-open` requires the robot to pull the door open.
To pull the door open reliably, what steps the robot should perform?
Steps:
`pick-place` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, what steps the robot should perform?
Steps:
`window-open` requires the robot to slide the window open to the left.
To slide the window open to the left reliably, what steps the robot should perform?
Steps:
`drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, what steps the robot should perform?
Steps:
`button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, what steps the robot should perform?
Steps:




[eod] [code]use std::ops::{Div, Mul};

#[derive(Debug, PartialEq, Copy, Clone, Default)]
pub struct Vec2(pub f64, pub f64);

pub type Vector = Vec2;
pub type Color = Vec2;

impl Vec2 {
    fn new(x: f64, y: f64) -> Self {
        Vec2(x, y)
    }
}

impl Add for Vec2 {
    type Output = Vec2;

    fn add(self, other: Vec2) -> Self::Output {
        Vec2(self.0 + other.0, self.1 + other.1)
    }
}

impl Sub for Vec2 {
    type Output = Vec2;

    fn sub(self, other: Vec2) -> Self::Output {
        Vec2(self.