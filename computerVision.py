from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
from decouple import config


'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = config('SECRET_KEY')
endpoint = config('endpoint')

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
'''
END - Authenticate
'''

'''
Quickstart variables
These variables are shared by several examples
'''
# Images used for the examples: Describe an image, Categorize an image, Tag an image, 
# Detect faces, Detect adult or racy content, Detect the color scheme, 
# Detect domain-specific content, Detect image types, Detect objects
images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "/home/basededatos/Documents/desarrollo/Projects/Platzi/AzureCognitiveSrv/sample16.png")
remote_image_url = "https://moderatorsampleimages.blob.core.windows.net/samples/sample16.png"
'''
END - Quickstart variables
'''

# Ruta a la imagen local
image_path = "./doggy.jpg"

'''
Analyze an Image - local
This example extracts information about the image
'''
print("===== Analyze an image - local =====")

# Open the image file
with open(image_path, "rb") as image_stream:
    # Call the API with the image stream
    analyze_result_local = computervision_client.analyze_image_in_stream(image_stream, visual_features=[VisualFeatureTypes.tags])

# Print results with confidence score
print("Tags in the local image: ")
if (len(analyze_result_local.tags) == 0):
    print("No tags detected.")
else:
    for tag in analyze_result_local.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
print()
'''
END - Analyze an Image - local
'''