import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime,timedelta
from pytz import timezone
import requests
import codecs
from boto3 import Session
from boto3 import resource



dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('aurora')
table1 = dynamodb.Table('final')




def lambda_handler(event, context):
    similar=0.0
    name='unknown'
    
    session = Session(region_name="us-east-1")
    polly = session.client("polly")
    s3 = resource('s3')
    bucket_name = 'rajyalakshmi'
    txtbucket = s3.Bucket(bucket_name)
    
        
    s3 = boto3.resource('s3')
    
    #img = '{}'.format(event["KEY_SOURCE"])
    #object = s2.Bucket(bucket_name).Object(img)
    
    #BUCKET1 = "mbucket369"
    
    BUCKET1 = "mbucket369"
    KEY_TARGET ='teddy.jpg'
    #print(KEY_TARGET)
    def compare_faces(bucket, key, bucket_target, key_target,threshold=60, region="us-east-1"):
        rekognition = boto3.client("rekognition", region)
        response = rekognition.compare_faces(
            SourceImage={
                "S3Object": {
                    "Bucket": bucket,
                    "Name": key,
                        
                }
                    
            },
            TargetImage={
                "S3Object": {
                    "Bucket": bucket_target,
                    "Name": key_target,
                        
                }
                    
            }
        )
        return response['SourceImageFace'], response['FaceMatches']
            
        
        
    BUCKET = s3.Bucket('mbucke123')

            #print(BUCKET1.name)
    for s3_object in BUCKET.objects.all():
        KEY_SOURCE=s3_object.key
        #print(KEY_SOURCE)
        source_face, matches = compare_faces(BUCKET.name, KEY_SOURCE, BUCKET1, KEY_TARGET)
                            
        # the main source face
        print ("Source Face ({Confidence}%)".format(**source_face))
                            
            # one match for each target face
        for match in matches:
            print ("Target Face ({Confidence}%)".format(**match['Face']))
            x = "{}".format(match['Similarity'])
            similarity = float(x)
            print(similarity)
            if similarity >= 80:
                similar=similarity
                print(KEY_SOURCE)
                today=datetime.now()
                now_utc=datetime.now(timezone('Asia/Kolkata'))
                now_culcutta=now_utc.astimezone(timezone('Asia/Kolkata'))
                date1=now_utc.strftime("%x")
                time1=now_utc.strftime("%X")
                print(time1)
                #img = "KEY_SOURCE"
                #object = s2.Bucket(bucket_name).Object(KEY_SOURCE)
                #print(object)
                s2 = boto3.resource('s3')
                s3 = boto3.client('s3')
        
                url='{}/{}/{}'.format(s3.meta.endpoint_url,BUCKET.name,KEY_SOURCE)
                
                response = table.scan(ProjectionExpression ='img_src')
                for i in response['Items']:
                    data='{img_src}'.format(**i)
                    if data == url:
                
                        response = table.query(
                            KeyConditionExpression=Key('img_src').eq(data)
                            )
                        items = response['Items']
                        for x in range(len(items)):
                            name=items[x]['name_1']
                            id=items[x]['id']
                            res=table1.put_item(
                                Item = {
                                    'name':name,
                                    'id':id,
                                    'date_1':date1,
                                    'tym_1':str(time1)
                                }
                            )
                            print(res)
                            return {
                                'name':name,
                                'status':'true'
                                
                            }
                            
                            
                            # print(name)
                            # filename = "audio.mp3"
                            # response = polly.synthesize_speech(
                            # Text=name,
                            # OutputFormat="mp3",
                            # VoiceId="Matthew")
                            # stream = response["AudioStream"]
                            
                            # txtbucket.put_object(Key=filename, Body=stream.read())
                           
            
        else:
            print('stupid')
            print(KEY_TARGET)
            filename = "audi.mp3"
            response = polly.synthesize_speech(
            Text='hi welcome to organization:',
            OutputFormat="mp3",
            VoiceId="Matthew")
            stream = response["AudioStream"]
            txtbucket.put_object(Key=filename, Body=stream.read())
            aws s3 mv s3://mbucket369 s3://rasph  --recursive    
        
                
    if similar < 80:
        return {
            'name':name,
            'status':'false'
        }
          
             
         dynamodb = boto3.resource('dynamodb')
         table = dynamodb.Table('final')
         table.put_item(
             Item = {
                 'name':name,
                 'id':id,
                 'date_1':date1,
                 'tym_1':time1
             }
         )
    
            
            
            
                
                    
                    
            
        
