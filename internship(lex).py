import json
import boto3
def lambda_handler(event, context):
    #print('received request: ' + str(event))
    resp=''
    internship=event['currentIntent']['slots']['internship']
    technology=event['currentIntent']['slots']['technology']
    period=event['currentIntent']['slots']['period']
    reference=event['currentIntent']['slots']['reference']
    if(technology=='ML'):
        if(period=='3'):
            resp='we will be covering the overview and theoritical part'
        if(period=='6'):
            resp='we will be covering theoritical part and some algorithms'
        if(period=='9'):
            resp='we will be covering we will be covering theoritical and Algorithms in detail'
    if(technology=='AWS'):
        if(period=='3'):
            resp='we will covering free services like dynamodb,lambda,cognito,etc'
        if(period=='6'):
            resp='we will be covering a project on ML'
        if(period=='9'):
            resp='we will be covering AWS certification program'
        
    #print(place)
    # dynamodb = boto3.resource('dynamodb')
    # table = dynamodb.Table('lexbot')
    # res=table.scan()
    # for items in res:
    #     if(res['process']=='incomplete'):
    #         name=res['name']
    #         number=res['number']
    #         purpose=res['purpose']
    #         address=res['address']
    #         process=res['process']
    # table.put_item(
    #     Item={
    #         'name' : name,
    #         'number':number,
    #         'purpose' :purpose,
    #         'address' : address,
    #         'process':'complete',
    #         'technology':technology,
    #         'period':period
          
    #     }
    # )
    response = {
      "dialogAction": {
        "type": "Close",
        "fulfillmentState": "Fulfilled",
        "message": {
            "contentType": "SSML",
            "content": "{bs}  ".format(bs=resp)
          
        },
      }
    }
    return response
