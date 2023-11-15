
from decouple import config
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = config('SECRET_KEY')
endpoint = config('endpoint')

# Authenticate the client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# Example method for detecting the language of text
def language_detection_example(client):
    try:
        documents = ["Hello this is me speaking english  "]
        response = client.detect_language(documents = documents, country_hint = 'us')[0]
        print(response)

    except Exception as err:
        print("Encountered exception. {}".format(err))
language_detection_example(client)