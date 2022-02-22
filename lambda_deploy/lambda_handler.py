def handler(event, context):
    tmsg = 'Hello from AWS Lambda Deployed Using AWS CDK Written By Unbiased Coder'
    print (tmsg)

    return {
        'statusCode': 200,
        'body': tmsg
    }
