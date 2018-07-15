import json
import os
from createbucket import createbucket

def hello(event, context):
    print('before the os system test')
    print('after os system upload')
    import subprocess

    cmd="aws cloudformation create-stack --stack-name test --template-body https://raw.githubusercontent.com/apollowebdesigns/cloudtemplates/master/s3.yaml" 
    push=subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE)
    print(push.returncode)
    # bucket = createbucket()

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
