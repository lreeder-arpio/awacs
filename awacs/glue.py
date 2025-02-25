# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Glue"
prefix = "glue"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchCreatePartition = Action("BatchCreatePartition")
BatchDeleteConnection = Action("BatchDeleteConnection")
BatchDeletePartition = Action("BatchDeletePartition")
BatchDeleteTable = Action("BatchDeleteTable")
BatchDeleteTableVersion = Action("BatchDeleteTableVersion")
BatchGetBlueprints = Action("BatchGetBlueprints")
BatchGetCrawlers = Action("BatchGetCrawlers")
BatchGetCustomEntityTypes = Action("BatchGetCustomEntityTypes")
BatchGetDevEndpoints = Action("BatchGetDevEndpoints")
BatchGetJobs = Action("BatchGetJobs")
BatchGetPartition = Action("BatchGetPartition")
BatchGetTriggers = Action("BatchGetTriggers")
BatchGetWorkflows = Action("BatchGetWorkflows")
BatchStopJobRun = Action("BatchStopJobRun")
BatchUpdatePartition = Action("BatchUpdatePartition")
CancelDataQualityRuleRecommendationRun = Action(
    "CancelDataQualityRuleRecommendationRun"
)
CancelDataQualityRulesetEvaluationRun = Action("CancelDataQualityRulesetEvaluationRun")
CancelMLTaskRun = Action("CancelMLTaskRun")
CancelStatement = Action("CancelStatement")
CheckSchemaVersionValidity = Action("CheckSchemaVersionValidity")
CreateBlueprint = Action("CreateBlueprint")
CreateClassifier = Action("CreateClassifier")
CreateConnection = Action("CreateConnection")
CreateCrawler = Action("CreateCrawler")
CreateCustomEntityType = Action("CreateCustomEntityType")
CreateDataQualityRuleset = Action("CreateDataQualityRuleset")
CreateDatabase = Action("CreateDatabase")
CreateDevEndpoint = Action("CreateDevEndpoint")
CreateJob = Action("CreateJob")
CreateMLTransform = Action("CreateMLTransform")
CreatePartition = Action("CreatePartition")
CreatePartitionIndex = Action("CreatePartitionIndex")
CreateRegistry = Action("CreateRegistry")
CreateSchema = Action("CreateSchema")
CreateScript = Action("CreateScript")
CreateSecurityConfiguration = Action("CreateSecurityConfiguration")
CreateSession = Action("CreateSession")
CreateTable = Action("CreateTable")
CreateTrigger = Action("CreateTrigger")
CreateUserDefinedFunction = Action("CreateUserDefinedFunction")
CreateWorkflow = Action("CreateWorkflow")
DeleteBlueprint = Action("DeleteBlueprint")
DeleteClassifier = Action("DeleteClassifier")
DeleteColumnStatisticsForPartition = Action("DeleteColumnStatisticsForPartition")
DeleteColumnStatisticsForTable = Action("DeleteColumnStatisticsForTable")
DeleteConnection = Action("DeleteConnection")
DeleteCrawler = Action("DeleteCrawler")
DeleteCustomEntityType = Action("DeleteCustomEntityType")
DeleteDataQualityRuleset = Action("DeleteDataQualityRuleset")
DeleteDatabase = Action("DeleteDatabase")
DeleteDevEndpoint = Action("DeleteDevEndpoint")
DeleteJob = Action("DeleteJob")
DeleteMLTransform = Action("DeleteMLTransform")
DeletePartition = Action("DeletePartition")
DeletePartitionIndex = Action("DeletePartitionIndex")
DeleteRegistry = Action("DeleteRegistry")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteSchema = Action("DeleteSchema")
DeleteSchemaVersions = Action("DeleteSchemaVersions")
DeleteSecurityConfiguration = Action("DeleteSecurityConfiguration")
DeleteSession = Action("DeleteSession")
DeleteTable = Action("DeleteTable")
DeleteTableVersion = Action("DeleteTableVersion")
DeleteTrigger = Action("DeleteTrigger")
DeleteUserDefinedFunction = Action("DeleteUserDefinedFunction")
DeleteWorkflow = Action("DeleteWorkflow")
DeregisterDataPreview = Action("DeregisterDataPreview")
GetBlueprint = Action("GetBlueprint")
GetBlueprintRun = Action("GetBlueprintRun")
GetBlueprintRuns = Action("GetBlueprintRuns")
GetCatalogImportStatus = Action("GetCatalogImportStatus")
GetClassifier = Action("GetClassifier")
GetClassifiers = Action("GetClassifiers")
GetColumnStatisticsForPartition = Action("GetColumnStatisticsForPartition")
GetColumnStatisticsForTable = Action("GetColumnStatisticsForTable")
GetConnection = Action("GetConnection")
GetConnections = Action("GetConnections")
GetCrawler = Action("GetCrawler")
GetCrawlerMetrics = Action("GetCrawlerMetrics")
GetCrawlers = Action("GetCrawlers")
GetCustomEntityType = Action("GetCustomEntityType")
GetDataCatalogEncryptionSettings = Action("GetDataCatalogEncryptionSettings")
GetDataQualityResult = Action("GetDataQualityResult")
GetDataQualityRuleRecommendationRun = Action("GetDataQualityRuleRecommendationRun")
GetDataQualityRuleset = Action("GetDataQualityRuleset")
GetDataQualityRulesetEvaluationRun = Action("GetDataQualityRulesetEvaluationRun")
GetDatabase = Action("GetDatabase")
GetDatabases = Action("GetDatabases")
GetDataflowGraph = Action("GetDataflowGraph")
GetDevEndpoint = Action("GetDevEndpoint")
GetDevEndpoints = Action("GetDevEndpoints")
GetJob = Action("GetJob")
GetJobBookmark = Action("GetJobBookmark")
GetJobRun = Action("GetJobRun")
GetJobRuns = Action("GetJobRuns")
GetJobs = Action("GetJobs")
GetMLTaskRun = Action("GetMLTaskRun")
GetMLTaskRuns = Action("GetMLTaskRuns")
GetMLTransform = Action("GetMLTransform")
GetMLTransforms = Action("GetMLTransforms")
GetMapping = Action("GetMapping")
GetNotebookInstanceStatus = Action("GetNotebookInstanceStatus")
GetPartition = Action("GetPartition")
GetPartitionIndexes = Action("GetPartitionIndexes")
GetPartitions = Action("GetPartitions")
GetPlan = Action("GetPlan")
GetRegistry = Action("GetRegistry")
GetResourcePolicies = Action("GetResourcePolicies")
GetResourcePolicy = Action("GetResourcePolicy")
GetSchema = Action("GetSchema")
GetSchemaByDefinition = Action("GetSchemaByDefinition")
GetSchemaVersion = Action("GetSchemaVersion")
GetSchemaVersionsDiff = Action("GetSchemaVersionsDiff")
GetSecurityConfiguration = Action("GetSecurityConfiguration")
GetSecurityConfigurations = Action("GetSecurityConfigurations")
GetSession = Action("GetSession")
GetStatement = Action("GetStatement")
GetTable = Action("GetTable")
GetTableVersion = Action("GetTableVersion")
GetTableVersions = Action("GetTableVersions")
GetTables = Action("GetTables")
GetTags = Action("GetTags")
GetTrigger = Action("GetTrigger")
GetTriggers = Action("GetTriggers")
GetUserDefinedFunction = Action("GetUserDefinedFunction")
GetUserDefinedFunctions = Action("GetUserDefinedFunctions")
GetWorkflow = Action("GetWorkflow")
GetWorkflowRun = Action("GetWorkflowRun")
GetWorkflowRunProperties = Action("GetWorkflowRunProperties")
GetWorkflowRuns = Action("GetWorkflowRuns")
GlueNotebookAuthorize = Action("GlueNotebookAuthorize")
GlueNotebookRefreshCredentials = Action("GlueNotebookRefreshCredentials")
ImportCatalogToGlue = Action("ImportCatalogToGlue")
ListBlueprints = Action("ListBlueprints")
ListCrawlers = Action("ListCrawlers")
ListCrawls = Action("ListCrawls")
ListCustomEntityTypes = Action("ListCustomEntityTypes")
ListDataQualityResults = Action("ListDataQualityResults")
ListDataQualityRuleRecommendationRuns = Action("ListDataQualityRuleRecommendationRuns")
ListDataQualityRulesetEvaluationRuns = Action("ListDataQualityRulesetEvaluationRuns")
ListDataQualityRulesets = Action("ListDataQualityRulesets")
ListDevEndpoints = Action("ListDevEndpoints")
ListJobs = Action("ListJobs")
ListMLTransforms = Action("ListMLTransforms")
ListRegistries = Action("ListRegistries")
ListSchemaVersions = Action("ListSchemaVersions")
ListSchemas = Action("ListSchemas")
ListSessions = Action("ListSessions")
ListStatements = Action("ListStatements")
ListTriggers = Action("ListTriggers")
ListWorkflows = Action("ListWorkflows")
NotifyEvent = Action("NotifyEvent")
PublishDataQuality = Action("PublishDataQuality")
PutDataCatalogEncryptionSettings = Action("PutDataCatalogEncryptionSettings")
PutResourcePolicy = Action("PutResourcePolicy")
PutSchemaVersionMetadata = Action("PutSchemaVersionMetadata")
PutWorkflowRunProperties = Action("PutWorkflowRunProperties")
QuerySchemaVersionMetadata = Action("QuerySchemaVersionMetadata")
RegisterSchemaVersion = Action("RegisterSchemaVersion")
RemoveSchemaVersionMetadata = Action("RemoveSchemaVersionMetadata")
ResetJobBookmark = Action("ResetJobBookmark")
ResumeWorkflowRun = Action("ResumeWorkflowRun")
RunStatement = Action("RunStatement")
SearchTables = Action("SearchTables")
StartBlueprintRun = Action("StartBlueprintRun")
StartCrawler = Action("StartCrawler")
StartCrawlerSchedule = Action("StartCrawlerSchedule")
StartDataQualityRuleRecommendationRun = Action("StartDataQualityRuleRecommendationRun")
StartDataQualityRulesetEvaluationRun = Action("StartDataQualityRulesetEvaluationRun")
StartExportLabelsTaskRun = Action("StartExportLabelsTaskRun")
StartImportLabelsTaskRun = Action("StartImportLabelsTaskRun")
StartJobRun = Action("StartJobRun")
StartMLEvaluationTaskRun = Action("StartMLEvaluationTaskRun")
StartMLLabelingSetGenerationTaskRun = Action("StartMLLabelingSetGenerationTaskRun")
StartNotebook = Action("StartNotebook")
StartTrigger = Action("StartTrigger")
StartWorkflowRun = Action("StartWorkflowRun")
StopCrawler = Action("StopCrawler")
StopCrawlerSchedule = Action("StopCrawlerSchedule")
StopSession = Action("StopSession")
StopTrigger = Action("StopTrigger")
StopWorkflowRun = Action("StopWorkflowRun")
TagResource = Action("TagResource")
TerminateNotebook = Action("TerminateNotebook")
UntagResource = Action("UntagResource")
UpdateBlueprint = Action("UpdateBlueprint")
UpdateClassifier = Action("UpdateClassifier")
UpdateColumnStatisticsForPartition = Action("UpdateColumnStatisticsForPartition")
UpdateColumnStatisticsForTable = Action("UpdateColumnStatisticsForTable")
UpdateConnection = Action("UpdateConnection")
UpdateCrawler = Action("UpdateCrawler")
UpdateCrawlerSchedule = Action("UpdateCrawlerSchedule")
UpdateDataQualityRuleset = Action("UpdateDataQualityRuleset")
UpdateDatabase = Action("UpdateDatabase")
UpdateDevEndpoint = Action("UpdateDevEndpoint")
UpdateJob = Action("UpdateJob")
UpdateMLTransform = Action("UpdateMLTransform")
UpdatePartition = Action("UpdatePartition")
UpdateRegistry = Action("UpdateRegistry")
UpdateSchema = Action("UpdateSchema")
UpdateTable = Action("UpdateTable")
UpdateTrigger = Action("UpdateTrigger")
UpdateUserDefinedFunction = Action("UpdateUserDefinedFunction")
UpdateWorkflow = Action("UpdateWorkflow")
UseGlueStudio = Action("UseGlueStudio")
UseMLTransforms = Action("UseMLTransforms")
