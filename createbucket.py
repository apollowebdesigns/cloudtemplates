import boto3

def createbucket():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('my-bucket')

    if 'my-bucket' != bucket:
        s3.create_bucket(
            ACL='public-read-write',
            Bucket='my-bucket',
            CreateBucketConfiguration={
                'LocationConstraint': 'eu-west-2'
            }
        )

    print("Bucket List: %s" % bucket)
    return bucket