

And add code to perform the task.
"""

[eod] [code]import _plotly_utils.basevalidators


class OutlinewidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self,
        plotly_name="outlinewidth",
        parent_name="splom.marker.colorbar",
        **kwargs,
    ):
        super(OutlinewidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
[eod] [code]import pytest

from lms.models.validators.lms_assignment_validators import (
    validate_assignment_with_peer_reviews_allowed_by_settings,
)


@pytest.fixture
def mock_current_app(mock_app_config, pyramid_config, assignment_max_peer_reviews_allowed_by_settings):
    mock_app_config.registry.settings = dict(
        assignment_max_peer_reviews_allowed_by_settings=assignment_max_peer_reviews_allowed_by_settings
    )

    return mock_app_config.registry.settings.app


@pytest.mark.parametrize(
    "peer_reviews_per_user, valid",
    (
        (0, True),
        (3, True),
        (10, True),
        (15, False),
    ),
)
def test_validate_assignment_with_peer_reviews_allowed_by_settings(mock_current_app, peer_reviews_per_user, valid):
    data = {
        "assignment_max_peer_reviews_allowed_by_settings": mock_current_app.config.get(
            "assignment_max_peer_reviews_allowed_by_settings"
        ),
        "peer_reviews_per_user": peer_reviews_per_user,
    }

    message = validate_assignment_with_peer_reviews_allowed_by_settings(
        data, mock_current_app.config["assignment_max_peer_reviews_allowed_by_settings"]
    )

    if valid:
        assert message == ""
    else:
        assert "Peer reviews must not exceed" in message
[eod] [code]#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for