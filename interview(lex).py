import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
def lambda_handler(event, context):
    #print('received request: ' + str(event))
    interview=event['currentIntent']['slots']['interview']
    domain=event['currentIntent']['slots']['domain']
    if(domain=='ML'):
        if(bond=='1'):
            resp='your salary will be between 10000 to 12000'
        if(bond=='2'):
            resp='your salary will be between 12000 to 14000'
        if(bond=='3'):
            resp='your salary will be between 14000 to 16000'
    #print(place)
    # dynamodb = boto3.resource('dynamodb')
    # table = dynamodb.Table('lexbot')
    # res=table.scan()
    # details = res['Items']
    # for x in details:
    #     if(x['process']=='incomplete'):
    #         name=x['name']
    #         number=x['number']
    #         purpose=x['purpose']
    #         address=x['address']
    #         process=x['process']
    # table.put_item(
    #     Item={
    #         'name' : name,
    #         'number':number,
    #         'purpose' :purpose,
    #         'address' : address,
    #         'process':'complete',
    #         'domain':domain
          
    #     }
    # )
    response = {
      "dialogAction": {
        "type": "Close",
        "fulfillmentState": "Fulfilled",
        "message": {
          "contentType": "SSML",
          "content": "thanks for your info"
          
        },
      }
    }
    return response
