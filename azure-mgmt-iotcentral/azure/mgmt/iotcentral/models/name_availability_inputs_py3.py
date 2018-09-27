# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NameAvailabilityInputs(Model):
    """Input values.

    :param name: The name of the IoT Central application instance to check.
    :type name: str
    :param type: The type of the IoT Central resource to query. Default value:
     "IoTApps" .
    :type type: str
    """

    _validation = {
        'name': {'pattern': r'^[a-z0-9-]{1,63}$'},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, type: str="IoTApps", **kwargs) -> None:
        super(NameAvailabilityInputs, self).__init__(**kwargs)
        self.name = name
        self.type = type
