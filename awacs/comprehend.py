# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Comprehend"
prefix = "comprehend"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchDetectDominantLanguage = Action("BatchDetectDominantLanguage")
BatchDetectEntities = Action("BatchDetectEntities")
BatchDetectKeyPhrases = Action("BatchDetectKeyPhrases")
BatchDetectSentiment = Action("BatchDetectSentiment")
BatchDetectSyntax = Action("BatchDetectSyntax")
BatchDetectTargetedSentiment = Action("BatchDetectTargetedSentiment")
ClassifyDocument = Action("ClassifyDocument")
ContainsPiiEntities = Action("ContainsPiiEntities")
CreateDocumentClassifier = Action("CreateDocumentClassifier")
CreateEndpoint = Action("CreateEndpoint")
CreateEntityRecognizer = Action("CreateEntityRecognizer")
DeleteDocumentClassifier = Action("DeleteDocumentClassifier")
DeleteEndpoint = Action("DeleteEndpoint")
DeleteEntityRecognizer = Action("DeleteEntityRecognizer")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DescribeDocumentClassificationJob = Action("DescribeDocumentClassificationJob")
DescribeDocumentClassifier = Action("DescribeDocumentClassifier")
DescribeDominantLanguageDetectionJob = Action("DescribeDominantLanguageDetectionJob")
DescribeEndpoint = Action("DescribeEndpoint")
DescribeEntitiesDetectionJob = Action("DescribeEntitiesDetectionJob")
DescribeEntityRecognizer = Action("DescribeEntityRecognizer")
DescribeEventsDetectionJob = Action("DescribeEventsDetectionJob")
DescribeKeyPhrasesDetectionJob = Action("DescribeKeyPhrasesDetectionJob")
DescribePiiEntitiesDetectionJob = Action("DescribePiiEntitiesDetectionJob")
DescribeResourcePolicy = Action("DescribeResourcePolicy")
DescribeSentimentDetectionJob = Action("DescribeSentimentDetectionJob")
DescribeTargetedSentimentDetectionJob = Action("DescribeTargetedSentimentDetectionJob")
DescribeTopicsDetectionJob = Action("DescribeTopicsDetectionJob")
DetectDominantLanguage = Action("DetectDominantLanguage")
DetectEntities = Action("DetectEntities")
DetectKeyPhrases = Action("DetectKeyPhrases")
DetectPiiEntities = Action("DetectPiiEntities")
DetectSentiment = Action("DetectSentiment")
DetectSyntax = Action("DetectSyntax")
DetectTargetedSentiment = Action("DetectTargetedSentiment")
ImportModel = Action("ImportModel")
ListDocumentClassificationJobs = Action("ListDocumentClassificationJobs")
ListDocumentClassifierSummaries = Action("ListDocumentClassifierSummaries")
ListDocumentClassifiers = Action("ListDocumentClassifiers")
ListDominantLanguageDetectionJobs = Action("ListDominantLanguageDetectionJobs")
ListEndpoints = Action("ListEndpoints")
ListEntitiesDetectionJobs = Action("ListEntitiesDetectionJobs")
ListEntityRecognizerSummaries = Action("ListEntityRecognizerSummaries")
ListEntityRecognizers = Action("ListEntityRecognizers")
ListEventsDetectionJobs = Action("ListEventsDetectionJobs")
ListKeyPhrasesDetectionJobs = Action("ListKeyPhrasesDetectionJobs")
ListPiiEntitiesDetectionJobs = Action("ListPiiEntitiesDetectionJobs")
ListSentimentDetectionJobs = Action("ListSentimentDetectionJobs")
ListTagsForResource = Action("ListTagsForResource")
ListTargetedSentimentDetectionJobs = Action("ListTargetedSentimentDetectionJobs")
ListTopicsDetectionJobs = Action("ListTopicsDetectionJobs")
PutResourcePolicy = Action("PutResourcePolicy")
StartDocumentClassificationJob = Action("StartDocumentClassificationJob")
StartDominantLanguageDetectionJob = Action("StartDominantLanguageDetectionJob")
StartEntitiesDetectionJob = Action("StartEntitiesDetectionJob")
StartEventsDetectionJob = Action("StartEventsDetectionJob")
StartKeyPhrasesDetectionJob = Action("StartKeyPhrasesDetectionJob")
StartPiiEntitiesDetectionJob = Action("StartPiiEntitiesDetectionJob")
StartSentimentDetectionJob = Action("StartSentimentDetectionJob")
StartTargetedSentimentDetectionJob = Action("StartTargetedSentimentDetectionJob")
StartTopicsDetectionJob = Action("StartTopicsDetectionJob")
StopDominantLanguageDetectionJob = Action("StopDominantLanguageDetectionJob")
StopEntitiesDetectionJob = Action("StopEntitiesDetectionJob")
StopEventsDetectionJob = Action("StopEventsDetectionJob")
StopKeyPhrasesDetectionJob = Action("StopKeyPhrasesDetectionJob")
StopPiiEntitiesDetectionJob = Action("StopPiiEntitiesDetectionJob")
StopSentimentDetectionJob = Action("StopSentimentDetectionJob")
StopTargetedSentimentDetectionJob = Action("StopTargetedSentimentDetectionJob")
StopTrainingDocumentClassifier = Action("StopTrainingDocumentClassifier")
StopTrainingEntityRecognizer = Action("StopTrainingEntityRecognizer")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateEndpoint = Action("UpdateEndpoint")
