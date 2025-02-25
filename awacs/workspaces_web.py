# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon WorkSpaces Web"
prefix = "workspaces-web"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateBrowserSettings = Action("AssociateBrowserSettings")
AssociateNetworkSettings = Action("AssociateNetworkSettings")
AssociateTrustStore = Action("AssociateTrustStore")
AssociateUserAccessLoggingSettings = Action("AssociateUserAccessLoggingSettings")
AssociateUserSettings = Action("AssociateUserSettings")
CreateBrowserSettings = Action("CreateBrowserSettings")
CreateIdentityProvider = Action("CreateIdentityProvider")
CreateNetworkSettings = Action("CreateNetworkSettings")
CreatePortal = Action("CreatePortal")
CreateTrustStore = Action("CreateTrustStore")
CreateUserAccessLoggingSettings = Action("CreateUserAccessLoggingSettings")
CreateUserSettings = Action("CreateUserSettings")
DeleteBrowserSettings = Action("DeleteBrowserSettings")
DeleteIdentityProvider = Action("DeleteIdentityProvider")
DeleteNetworkSettings = Action("DeleteNetworkSettings")
DeletePortal = Action("DeletePortal")
DeleteTrustStore = Action("DeleteTrustStore")
DeleteUserAccessLoggingSettings = Action("DeleteUserAccessLoggingSettings")
DeleteUserSettings = Action("DeleteUserSettings")
DisassociateBrowserSettings = Action("DisassociateBrowserSettings")
DisassociateNetworkSettings = Action("DisassociateNetworkSettings")
DisassociateTrustStore = Action("DisassociateTrustStore")
DisassociateUserAccessLoggingSettings = Action("DisassociateUserAccessLoggingSettings")
DisassociateUserSettings = Action("DisassociateUserSettings")
GetBrowserSettings = Action("GetBrowserSettings")
GetIdentityProvider = Action("GetIdentityProvider")
GetNetworkSettings = Action("GetNetworkSettings")
GetPortal = Action("GetPortal")
GetPortalServiceProviderMetadata = Action("GetPortalServiceProviderMetadata")
GetTrustStore = Action("GetTrustStore")
GetTrustStoreCertificate = Action("GetTrustStoreCertificate")
GetUserAccessLoggingSettings = Action("GetUserAccessLoggingSettings")
GetUserSettings = Action("GetUserSettings")
ListBrowserSettings = Action("ListBrowserSettings")
ListIdentityProviders = Action("ListIdentityProviders")
ListNetworkSettings = Action("ListNetworkSettings")
ListPortals = Action("ListPortals")
ListTagsForResource = Action("ListTagsForResource")
ListTrustStoreCertificates = Action("ListTrustStoreCertificates")
ListTrustStores = Action("ListTrustStores")
ListUserAccessLoggingSettings = Action("ListUserAccessLoggingSettings")
ListUserSettings = Action("ListUserSettings")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateBrowserSettings = Action("UpdateBrowserSettings")
UpdateIdentityProvider = Action("UpdateIdentityProvider")
UpdateNetworkSettings = Action("UpdateNetworkSettings")
UpdatePortal = Action("UpdatePortal")
UpdateTrustStore = Action("UpdateTrustStore")
UpdateUserAccessLoggingSettings = Action("UpdateUserAccessLoggingSettings")
UpdateUserSettings = Action("UpdateUserSettings")
