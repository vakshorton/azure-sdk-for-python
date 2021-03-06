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

from .resource_py3 import Resource


class SmartGroup(Resource):
    """Set of related alerts grouped together smartly by AMS.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar name: Azure resource name
    :vartype name: str
    :param alerts_count: Total number of alerts in smart group
    :type alerts_count: int
    :ivar smart_group_state: Smart group state. Possible values include:
     'New', 'Acknowledged', 'Closed'
    :vartype smart_group_state: str or
     ~azure.mgmt.alertsmanagement.models.State
    :ivar severity: Severity of smart group is the highest(Sev0 >... > Sev4)
     severity of all the alerts in the group. Possible values include: 'Sev0',
     'Sev1', 'Sev2', 'Sev3', 'Sev4'
    :vartype severity: str or ~azure.mgmt.alertsmanagement.models.Severity
    :ivar start_date_time: Creation time of smart group. Date-Time in ISO-8601
     format.
    :vartype start_date_time: datetime
    :ivar last_modified_date_time: Last updated time of smart group. Date-Time
     in ISO-8601 format.
    :vartype last_modified_date_time: datetime
    :ivar last_modified_user_name: Last modified by user name.
    :vartype last_modified_user_name: str
    :param resources: Summary of target resources in the smart group
    :type resources:
     list[~azure.mgmt.alertsmanagement.models.SmartGroupAggregatedProperty]
    :param resource_types: Summary of target resource types in the smart group
    :type resource_types:
     list[~azure.mgmt.alertsmanagement.models.SmartGroupAggregatedProperty]
    :param resource_groups: Summary of target resource groups in the smart
     group
    :type resource_groups:
     list[~azure.mgmt.alertsmanagement.models.SmartGroupAggregatedProperty]
    :param monitor_services: Summary of monitorServices in the smart group
    :type monitor_services:
     list[~azure.mgmt.alertsmanagement.models.SmartGroupAggregatedProperty]
    :param monitor_conditions: Summary of monitorConditions in the smart group
    :type monitor_conditions:
     list[~azure.mgmt.alertsmanagement.models.SmartGroupAggregatedProperty]
    :param alert_states: Summary of alertStates in the smart group
    :type alert_states:
     list[~azure.mgmt.alertsmanagement.models.SmartGroupAggregatedProperty]
    :param alert_severities: Summary of alertSeverities in the smart group
    :type alert_severities:
     list[~azure.mgmt.alertsmanagement.models.SmartGroupAggregatedProperty]
    :param next_link: The URI to fetch the next page of alerts. Call
     ListNext() with this URI to fetch the next page alerts.
    :type next_link: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'smart_group_state': {'readonly': True},
        'severity': {'readonly': True},
        'start_date_time': {'readonly': True},
        'last_modified_date_time': {'readonly': True},
        'last_modified_user_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'alerts_count': {'key': 'properties.alertsCount', 'type': 'int'},
        'smart_group_state': {'key': 'properties.smartGroupState', 'type': 'str'},
        'severity': {'key': 'properties.severity', 'type': 'str'},
        'start_date_time': {'key': 'properties.startDateTime', 'type': 'iso-8601'},
        'last_modified_date_time': {'key': 'properties.lastModifiedDateTime', 'type': 'iso-8601'},
        'last_modified_user_name': {'key': 'properties.lastModifiedUserName', 'type': 'str'},
        'resources': {'key': 'properties.resources', 'type': '[SmartGroupAggregatedProperty]'},
        'resource_types': {'key': 'properties.resourceTypes', 'type': '[SmartGroupAggregatedProperty]'},
        'resource_groups': {'key': 'properties.resourceGroups', 'type': '[SmartGroupAggregatedProperty]'},
        'monitor_services': {'key': 'properties.monitorServices', 'type': '[SmartGroupAggregatedProperty]'},
        'monitor_conditions': {'key': 'properties.monitorConditions', 'type': '[SmartGroupAggregatedProperty]'},
        'alert_states': {'key': 'properties.alertStates', 'type': '[SmartGroupAggregatedProperty]'},
        'alert_severities': {'key': 'properties.alertSeverities', 'type': '[SmartGroupAggregatedProperty]'},
        'next_link': {'key': 'properties.nextLink', 'type': 'str'},
    }

    def __init__(self, *, alerts_count: int=None, resources=None, resource_types=None, resource_groups=None, monitor_services=None, monitor_conditions=None, alert_states=None, alert_severities=None, next_link: str=None, **kwargs) -> None:
        super(SmartGroup, self).__init__(**kwargs)
        self.alerts_count = alerts_count
        self.smart_group_state = None
        self.severity = None
        self.start_date_time = None
        self.last_modified_date_time = None
        self.last_modified_user_name = None
        self.resources = resources
        self.resource_types = resource_types
        self.resource_groups = resource_groups
        self.monitor_services = monitor_services
        self.monitor_conditions = monitor_conditions
        self.alert_states = alert_states
        self.alert_severities = alert_severities
        self.next_link = next_link
