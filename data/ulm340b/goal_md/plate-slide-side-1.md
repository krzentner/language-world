
"""
[eod] [code]from . import auth
from .. import logic, user_logic, users


def create_access_token(db, user_id, expires_at, expires_at_datetime):
    a_token = auth.create_access_token(expires_at=expires_at)
    auth.db.create(a_token)

    db.query_and_execute(
        logic.create_access_token(
            user_id=user_id,
            access_token=a_token.access_token,
            expires_at=expires_at_datetime,
            issued_at_datetime=expires_at_datetime
        )
    )

    return a_token


def create_user(user_id, email, first_name, last_name, password,
                full_name):
    user = users.User(
        id=user_id,
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password,
        full_name=full_name
    )

    return user


def create_user_and_token(db, user_id, access_token):
    user = user_logic.create_user(
        user_id=user_id,
        email="mail@example.com",
        full_name="test full name",
        first_name="test first name",
        last_name="test last name",
        password="password"
    )
    db.query_and_execute(user)
    user_token = auth.create_access_token(user_id=user_id, expires_at=3600)
    db.query_and_execute(user_token)
    access_token.access_token = user_token.access_token
    access_token.expires_at = user_token.expires_at
    return access_token
[eod] [code]# Copyright (C) 2020 FireEye, Inc. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
# You may obtain a copy of the License at: [package root]/LICENSE.txt
# Unless required by applicable law or agreed to in writing, software distributed under the License
#  is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
import time
