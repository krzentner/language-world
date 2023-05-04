
    



The task `drawer-open-partial` requires the robot to pull the drawer open.
To pull the drawer open reliably, what steps the robot should perform?





The task `door-open-partial` requires the robot to pull the door open.
To pull the door open reliably, what steps the robot should perform?






The task `window-close-partial` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, what steps the robot should perform?






The task `peg-insert-side-partial` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, what steps the robot should perform?







The task `drawer-close-partial` requires the robot to push the drawer close.
To push the drawer close reliably, what steps the robot should perform?







The task `window-open-partial` requires the robot to slide the window open to the left.
To slide the window open to the left reliably, what steps the robot should perform?






The task `reach-partial` requires the robot to reach to the target location.
To reach to the target location reliably, what steps the robot should perform?






The task `pick-place-partial` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, what steps the robot should perform?






The task `push-partial` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, what steps the robot should perform?












"""

from typing import Any

import torch
from torch import Tensor, nn

from allennlp.common import FromParams


class _EncoderBlock(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int) -> None:
        super(_EncoderBlock, self).__init__()
        self.conv_1 = nn.Conv2d(
            in_channels=input_dim, out_channels=hidden_dim, kernel_size=(3, 3)
        )
        self.conv_2 = nn.Conv2d(
            in_channels=hidden_dim, out_channels=output_dim, kernel_size=(3, 3)
        )

    