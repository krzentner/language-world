


- **Input:**
    - (robot: `Robot`) a robot with a single gripper and a set of sensors that tell it the locations of several objects.
    - ```
      "robot's gripper"
      "door handle"
      "button"
      "puck"
      "reach target"
      "window handle"
      "drawer handle"
      "faucet"
      "peg"
      "hole"
    

- **Output:**
    - `robot` has successfully turned the faucet left
"""

# faucet-open: turn the faucet left
def faucet_open(robot):
    pass
[eod] [code]from typing import List, Optional

from pydantic import Field

from mev_inspect.schemas.traces import Protocol

from .traces import DecodedCallTrace, DecodedCreate2Trace, DecodedDelegateCallTrace
from .traces import DecodedDelegateCreate2Trace, DecodedSuicideTrace


class DecodedCallCreate2Trace(DecodedCallTrace):
    trace_address: Optional[str] = Field(alias="traceAddress")


class DecodedCallSelfDestructTrace(DecodedCallTrace):
    self_destruct_beneficiary: Optional[str] = Field(alias="selfDestructBeneficiary")


class DecodedCallStaticCallTrace(DecodedCallTrace):
    static_call_success: bool = Field(alias="staticCallSuccess")


class DecodedRewardEscrowTrace(DecodedCallTrace):
    protocol: Optional[Protocol] = Field(alias="protocol")


class DecodedCallCallTrace(DecodedCallTrace):
    call_success: bool = Field(alias="callSuccess")
    gas_refund: int = Field(alias="gasRefund")
    refund_address: Optional[str] = Field(alias="refundAddress")


class DecodedCallCallCodeTrace(DecodedCallTrace):
    call_success: bool = Field(alias="callSuccess")
    gas_refund: int = Field(alias="gasRefund")
    code_address: Optional[str] = Field(alias="codeAddress")
    refund_address: Optional[str] = Field(alias="refundAddress")


class DecodedDelegateCallCallTrace(DecodedDelegateCallTrace):
    trace_address: Optional[str] = Field(alias="traceAddress")
    call_success: bool = Field(alias="callSuccess")
    gas_refund: int = Field(alias="gasRefund")
    refund_