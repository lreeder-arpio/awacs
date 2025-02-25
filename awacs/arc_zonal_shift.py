# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Route 53 Application Recovery Controller - Zonal Shift"
prefix = "arc-zonal-shift"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelZonalShift = Action("CancelZonalShift")
GetManagedResource = Action("GetManagedResource")
ListManagedResources = Action("ListManagedResources")
ListZonalShifts = Action("ListZonalShifts")
StartZonalShift = Action("StartZonalShift")
UpdateZonalShift = Action("UpdateZonalShift")
