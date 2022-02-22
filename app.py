#!/usr/bin/env python3
import os
from dotenv import load_dotenv

# load our env file
print ('Loading env file')
load_dotenv()

import aws_cdk as cdk
from lambda_deploy.lambda_deploy_stack import LambdaDeployStack


# initialize cdk_env with variables from env file
print ('Creating environment')
cdk_env = cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))

# get app handler for cdk
print ('Getting App handler')
app = cdk.App()

# describe our stack
print ('Describing lambda stack')
LambdaDeployStack(
    app, 
    "LambdaDeployStack",
    env=cdk_env
)

# synthesize it
print ('Synthesizing stack')
app.synth()
