# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_single_category_classify_async.py

DESCRIPTION:
    This sample demonstrates how to classify documents into a single custom category. Here we several
    support tickets that need to be classified as internet, printer, email or hardware issues.
    Classifying documents is available as an action type through the begin_analyze_actions API.

    To train a model to classify your documents, see TODO

USAGE:
    python sample_single_category_classify_async.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_TEXT_ANALYTICS_ENDPOINT - the endpoint to your Cognitive Services resource.
    2) AZURE_TEXT_ANALYTICS_KEY - your Text Analytics subscription key
    3) AZURE_TEXT_ANALYTICS_PROJECT_NAME - your Text Analytics Language Studio project name
    4) AZURE_TEXT_ANALYTICS_DEPLOYMENT_NAME - your Text Analytics deployed model name
"""


import os
import asyncio


async def sample_classify_document_single_category_async():
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics.aio import TextAnalyticsClient
    from azure.ai.textanalytics import SingleCategoryClassifyAction

    endpoint = os.environ["AZURE_TEXT_ANALYTICS_ENDPOINT"]
    key = os.environ["AZURE_TEXT_ANALYTICS_KEY"]
    project_name = os.environ["AZURE_TEXT_ANALYTICS_PROJECT_NAME"]
    deployed_model_name = os.environ["AZURE_TEXT_ANALYTICS_DEPLOYMENT_NAME"]

    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )

    documents = [
        "My internet has stopped working. I tried resetting the router, but it just keeps blinking red.",
        "I submitted 3 jobs to print but the printer is unresponsive. I can't see it under my devices either.",
        "My computer will not boot. Pushing the power button does nothing - just a black screen.",
        "I seem to not be receiving all my emails on time. Emails from 2 days ago show up as just received.",
    ]

    async with text_analytics_client:
        poller = await text_analytics_client.begin_analyze_actions(
            documents,
            actions=[
                SingleCategoryClassifyAction(
                    project_name=project_name,
                    deployment_name=deployed_model_name
                ),
            ],
        )

        pages = await poller.result()

        document_results = []
        async for page in pages:
            document_results.append(page)

    for doc, classification_results in zip(documents, document_results):
        for classification_result in classification_results:
            if not classification_result.is_error:
                classification = classification_result.classification
                print("The document text '{}' was classified as '{}' with confidence score {}.".format(
                    doc, classification.category, classification.confidence_score)
                )
            else:
                print("Document text '{}' has an error with code '{}' and message '{}'".format(
                    doc, classification_result.code, classification_result.message
                ))


async def main():
    await sample_classify_document_single_category_async()


if __name__ == '__main__':
    asyncio.run(main())
