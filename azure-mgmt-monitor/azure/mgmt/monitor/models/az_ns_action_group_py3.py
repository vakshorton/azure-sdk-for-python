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


class AzNsActionGroup(Model):
    """Azure action group.

    :param action_group: Azure Action Group reference.
    :type action_group: list[str]
    :param email_subject: Custom subject override for all email ids in Azure
     action group
    :type email_subject: str
    :param custom_webhook_payload: Custom payload to be sent for all webook
     URI in Azure action group
    :type custom_webhook_payload: str
    """

    _attribute_map = {
        'action_group': {'key': 'actionGroup', 'type': '[str]'},
        'email_subject': {'key': 'emailSubject', 'type': 'str'},
        'custom_webhook_payload': {'key': 'customWebhookPayload', 'type': 'str'},
    }

    def __init__(self, *, action_group=None, email_subject: str=None, custom_webhook_payload: str=None, **kwargs) -> None:
        super(AzNsActionGroup, self).__init__(**kwargs)
        self.action_group = action_group
        self.email_subject = email_subject
        self.custom_webhook_payload = custom_webhook_payload
