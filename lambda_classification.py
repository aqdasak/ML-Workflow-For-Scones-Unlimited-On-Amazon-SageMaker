import json
import boto3
import base64

# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2023-09-13-10-45-46-675'

runtime = boto3.Session().client('sagemaker-runtime')

def lambda_handler(event, context):
    # Decode the image data
    image = base64.b64decode(event['image_data'])
    
    # Invoke the endpoint using boto3 runtime
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType='image/png', Body=image)
    predictions = json.loads(response['Body'].read().decode())
    
    # We return the data back to the Step Function
    # Create a new key to the event named   "inferences"  
    event["inferences"] = predictions
    
    return {
        'statusCode': 200,
        'body': event
        }

