import boto3
import subprocess

def createbucket():
    cmd="aws cloudformation create-stack --stack-name test --template-body https://raw.githubusercontent.com/apollowebdesigns/cloudtemplates/master/s3.yaml" 
    push=subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE)
    print(push.returncode)
    return push.returncode