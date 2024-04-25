# import ec2 Construct from aws_cdk.aws_ec2


from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)

from constructs import Construct

class HelloCdkStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        # The code that defines the stack goes here

        # Create a VPC that allows creation to public IP to EC2
        vpc = ec2.Vpc.from_lookup(self, "VPC", is_default=True)

        # Create a security group
        security_group = ec2.SecurityGroup(self, "SecurityGroup",vpc=vpc)
        security_group.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80)) # allow HTTP
        security_group.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(443)) # allow HTTPS
        security_group.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(22)) # allow SSH

        # Create an EC2 instance in the VPC
        instance = ec2.Instance(self, "Instance",
                                
                                # Assign an instance type
                                instance_type=ec2.InstanceType("t2.micro"),

                                # Assign an AMI
                                machine_image=ec2.MachineImage.latest_amazon_linux(),

                                # Assign a VPC to the instance
                                vpc=vpc,

                                # Assign a security group to the instance
                                security_group=security_group,

                                # Assign a key to the instance
                                key_name="test",

                                # Assign a subnet to the instance
                                vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC))

        # Commands to install Apache and write the HTML file
        commands = [
            "yum install -y httpd",
            "systemctl start httpd",
            "systemctl enable httpd",
            "echo '<html><head><title>Hello World</title></head><body><h1>Hello World!</h1></body></html>' > /var/www/html/index.html"
        ]

        # execute the above set of commands in the above ec2 instance
        instance.user_data.add_commands(*commands)