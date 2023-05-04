

The task `coffee-button` requires the robot to push the button of the coffee-maker.
To push the button of the coffee-maker reliably, what steps the robot should perform?

The task `coffee-pull` requires the robot to pull the handle of the coffee-maker.
To pull the handle of the coffee-maker reliably, what steps the robot should perform?

The task `faucet` requires the robot to lift up the handle of the faucet.
To lift up the handle of the faucet reliably, what steps the robot should perform?

The task `microwave` requires the robot to pull the handle of the microwave.
To pull the handle of the microwave reliably, what steps the robot should perform?

The task `oven-left` requires the robot to pull the left handle of the oven.
To pull the left handle of the oven reliably, what steps the robot should perform?

The task `oven-right` requires the robot to pull the right handle of the oven.
To pull the right handle of the oven reliably, what steps the robot should perform?

The task `refrigerator` requires the robot to open the door of the refrigerator.
To open the door of the refrigerator reliably, what steps the robot should perform?

The task `toaster` requires the robot to press the button of the toaster.
To press the button of the toaster reliably, what steps the robot should perform?


"""
[eod] [code]import pytest
from django_dynamic_fixture import G
from mixer.backend.django import mixer


@pytest.fixture
def user():
    return mixer.blend(
        "auth.User",
        first_name="Test",
        last_name="User",
        username="username",
        is_staff=False,
    )


@pytest.fixture
def super_user():
    return mixer.blend(
        "auth.User",
        first_name="Test",
        last_name="User",
        username="username",
        is_staff=True,
    )


@pytest.fixture
def another_super_user():
    return mixer.blend(
        "auth.User",
        first_name="AnotherTest",
        last_name="AnotherUser",
        username="another_username",
        is_staff=True,
    )


@pytest.fixture
def staff_user():
    return mixer.blend(
        "auth.User",
        first_name="Test",
        last_name="User",
        username="username",
        is_staff=True,
        is_superuser=False,
    )


@pytest.fixture
def group