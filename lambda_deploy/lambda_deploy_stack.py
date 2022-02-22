from aws_cdk import (
    Stack,
    aws_lambda,
)
from constructs import Construct

class LambdaDeployStack(Stack):
    """
    Simple Stack to Deploy an AWS Lambda Using CDK

    Args:
        Stack (AWS Stack): Deploys an AWS Lambda Function
    """
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        aws_lambda.Function(
                                self, 'Unbiased-Coder-Lambda',
                                handler = 'lambda_handler.handler', 
                                runtime = aws_lambda.Runtime.PYTHON_3_9, 
                                code    = aws_lambda.Code.from_asset('lambda_deploy/lambda_handler.zip'))
