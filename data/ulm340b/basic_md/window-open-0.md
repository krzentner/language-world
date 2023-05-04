""",
    )

    return question, answer, task
[eod] [code]# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alikafka20190916 import models as alikafka_20190916_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'alikafka.aliyuncs.com',
            'cn-beijing': 'alikafka.aliyuncs.com',
            'cn-zhangjiakou': 'alikafka.aliyuncs.com',
            'cn-huhehaote': 'alikafka.aliyuncs.com',
            'cn-hangzhou': 'alikafka.aliyuncs.com',
            'cn-shanghai': 'alikafka.aliyuncs.com',
            'cn-shenzhen': 'alikafka.aliyuncs.com',
            'ap-southeast-1': 'alikafka.ap-southeast-1.aliyuncs.com',
            'cn-chengdu': 'alikafka.aliyuncs.com',
            'cn-heyuan': 'alikafka.aliyuncs.com',
            'ap-southeast-2': 'alikafka.aliyuncs.com',
            'ap-southeast-3': 'alikafka.aliyuncs.com',
            'ap-northeast-1': 'alikafka.ap-northeast-1.aliyuncs.com',
            'eu-west-1': 'alikafka.eu-west-1.aliyuncs.com',
            'cn-hangzhou-finance': 'alikafka.ali