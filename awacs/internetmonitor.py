# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CloudWatch Internet Monitor"
prefix = "internetmonitor"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateMonitor = Action("CreateMonitor")
DeleteMonitor = Action("DeleteMonitor")
GetHealthEvent = Action("GetHealthEvent")
GetMonitor = Action("GetMonitor")
ListHealthEvents = Action("ListHealthEvents")
ListMonitors = Action("ListMonitors")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateMonitor = Action("UpdateMonitor")
