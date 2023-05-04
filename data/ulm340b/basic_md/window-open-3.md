
[
    When the window handle is left of the robot's gripper and the robot's gripper is not near the window handle, the robot should put gripper near the window handle.
    When the robot's gripper is right of the window handle, the robot should slide window to the left.
]

"""
[eod] [code]# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v11.enums",
    marshal="google.ads.googleads.v11",
    manifest={"GeoTargetingRestrictionEnum",},
)


class GeoTargetingRestrictionEnum(proto.Message):
    r"""Message describing feed item geo targeting restriction.
    Only returned for feed items of
    PLACES_LOCATION_FEED_ITEM_TARGET_TYPE.

    """

    class GeoTargetingRestriction(proto.Enum):
        r"""The possible restrictions of location targeting for feed
        items of LOCATION_FEED_ITEM_TARGET_TYPE.
        """
        UNSPECIFIED = 0
        UNKNOWN = 1
        LOCATION_OF_PRESENCE = 2
        USER_LOCATION = 3


__all__ = tuple(sorted(__protobuf__.manifest))
[eod] [code]# coding=utf-8

"""
    api_wrappers.py
    ~~~~~~~~~~~~~~

    This module wraps the APIs for the CKAN RESTful API.
    
    It is not strictly necessary for a working client.

"""
from ckanapi import package_create
from ckanapi import package_create_remote
from ckanapi import package_entity_create
from ckanapi import package_update
from ckanapi import package_delete
from ckanapi import package_entity_delete
from ckanapi import package_search
from ckanapi import package_revision_show
from ckanapi import package_revision_list
from ckanapi import