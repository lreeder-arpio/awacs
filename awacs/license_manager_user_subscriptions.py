# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS License Manager User Subscriptions"
prefix = "license-manager-user-subscriptions"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateUser = Action("AssociateUser")
DeregisterIdentityProvider = Action("DeregisterIdentityProvider")
DisassociateUser = Action("DisassociateUser")
ListIdentityProviders = Action("ListIdentityProviders")
ListInstances = Action("ListInstances")
ListProductSubscriptions = Action("ListProductSubscriptions")
ListUserAssociations = Action("ListUserAssociations")
RegisterIdentityProvider = Action("RegisterIdentityProvider")
StartProductSubscription = Action("StartProductSubscription")
StopProductSubscription = Action("StopProductSubscription")
UpdateIdentityProviderSettings = Action("UpdateIdentityProviderSettings")
