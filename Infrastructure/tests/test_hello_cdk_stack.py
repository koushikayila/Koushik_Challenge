import aws_cdk as core
import aws_cdk.assertions as assertions

from hello_cdk.hello_cdk_stack import HelloCdkStack

# Sample test case to validate configuration of ec2-instance
def test_ec2_instance_config():
    app = core.App()
    stack = HelloCdkStack(app, "hello-cdk-stack")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::EC2::Instance", {
        "InstanceType": "t2.micro"
    })
