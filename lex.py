import json
import boto3
def lambda_handler(event, context):
    #print('received request: ' + str(event))
    name=event['currentIntent']['slots']['name']
    reason=event['currentIntent']['slots']['purpose']
    place=event['currentIntent']['slots']['address']
    internship=event['currentIntent']['slots']['internship']
    interview=event['currentIntent']['slots']['interview']
    technology=event['currentIntent']['slots']['technology']
    period=event['currentIntent']['slots']['period']
    reference=event['currentIntent']['slots']['reference']
    '''dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('lexbot')
    table.put_item(
        Item={
            'name' : name,
            'purpose' :reason,
            'address' : place,
            'internship':technology,
          
        }
    )'''
    response = {
      "dialogAction": {
        "type": "Close",
        "fulfillmentState": "Fulfilled",
        "message": {
          "contentType": "SSML",
          "content": "thankyou for the info"
          
        },
      }
    }
    return response
