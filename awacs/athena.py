# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Athena"
prefix = "athena"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetNamedQuery = Action("BatchGetNamedQuery")
BatchGetPreparedStatement = Action("BatchGetPreparedStatement")
BatchGetQueryExecution = Action("BatchGetQueryExecution")
CancelQueryExecution = Action("CancelQueryExecution")
CreateDataCatalog = Action("CreateDataCatalog")
CreateNamedQuery = Action("CreateNamedQuery")
CreateNotebook = Action("CreateNotebook")
CreatePreparedStatement = Action("CreatePreparedStatement")
CreatePresignedNotebookUrl = Action("CreatePresignedNotebookUrl")
CreateWorkGroup = Action("CreateWorkGroup")
DeleteDataCatalog = Action("DeleteDataCatalog")
DeleteNamedQuery = Action("DeleteNamedQuery")
DeleteNotebook = Action("DeleteNotebook")
DeletePreparedStatement = Action("DeletePreparedStatement")
DeleteWorkGroup = Action("DeleteWorkGroup")
ExportNotebook = Action("ExportNotebook")
GetCalculationExecution = Action("GetCalculationExecution")
GetCalculationExecutionCode = Action("GetCalculationExecutionCode")
GetCalculationExecutionStatus = Action("GetCalculationExecutionStatus")
GetCatalogs = Action("GetCatalogs")
GetDataCatalog = Action("GetDataCatalog")
GetDatabase = Action("GetDatabase")
GetExecutionEngine = Action("GetExecutionEngine")
GetExecutionEngines = Action("GetExecutionEngines")
GetNamedQuery = Action("GetNamedQuery")
GetNamespace = Action("GetNamespace")
GetNamespaces = Action("GetNamespaces")
GetNotebookMetadata = Action("GetNotebookMetadata")
GetPreparedStatement = Action("GetPreparedStatement")
GetQueryExecution = Action("GetQueryExecution")
GetQueryExecutions = Action("GetQueryExecutions")
GetQueryResults = Action("GetQueryResults")
GetQueryResultsStream = Action("GetQueryResultsStream")
GetQueryRuntimeStatistics = Action("GetQueryRuntimeStatistics")
GetSession = Action("GetSession")
GetSessionStatus = Action("GetSessionStatus")
GetTable = Action("GetTable")
GetTableMetadata = Action("GetTableMetadata")
GetTables = Action("GetTables")
GetWorkGroup = Action("GetWorkGroup")
ImportNotebook = Action("ImportNotebook")
ListApplicationDPUSizes = Action("ListApplicationDPUSizes")
ListCalculationExecutions = Action("ListCalculationExecutions")
ListDataCatalogs = Action("ListDataCatalogs")
ListDatabases = Action("ListDatabases")
ListEngineVersions = Action("ListEngineVersions")
ListExecutors = Action("ListExecutors")
ListNamedQueries = Action("ListNamedQueries")
ListNotebookMetadata = Action("ListNotebookMetadata")
ListNotebookSessions = Action("ListNotebookSessions")
ListPreparedStatements = Action("ListPreparedStatements")
ListQueryExecutions = Action("ListQueryExecutions")
ListSessions = Action("ListSessions")
ListTableMetadata = Action("ListTableMetadata")
ListTagsForResource = Action("ListTagsForResource")
ListWorkGroups = Action("ListWorkGroups")
RunQuery = Action("RunQuery")
StartCalculationExecution = Action("StartCalculationExecution")
StartQueryExecution = Action("StartQueryExecution")
StartSession = Action("StartSession")
StopCalculationExecution = Action("StopCalculationExecution")
StopQueryExecution = Action("StopQueryExecution")
TagResource = Action("TagResource")
TerminateSession = Action("TerminateSession")
UntagResource = Action("UntagResource")
UpdateDataCatalog = Action("UpdateDataCatalog")
UpdateNamedQuery = Action("UpdateNamedQuery")
UpdateNotebook = Action("UpdateNotebook")
UpdateNotebookMetadata = Action("UpdateNotebookMetadata")
UpdatePreparedStatement = Action("UpdatePreparedStatement")
UpdateWorkGroup = Action("UpdateWorkGroup")
