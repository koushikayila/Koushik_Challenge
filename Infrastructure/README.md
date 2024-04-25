
# Welcome to the CDK Python project!

This is a project to create a scalable and static web application for AWS using 
CDK development with Python.

## Prerequisites
* AWSCLI already configured with a default user and region.
* Python3
* Virtualenv

## Setup steps
The `cdk.json` file tells the CDK Toolkit on how to execute your app.

This project is set up like a usual Python project.  The initialization
process also creates a virtualenv within this project, stored under the `my_env`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on Windows:

```
python3 -m venv my_env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
source my_env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
.my_env\Scripts\activate
```

Once the virtualenv is activated, you can install the required dependencies.

```
pip install -r requirements.txt
```

Then we install AWS CDK using the below command
```
npm install -g aws-cdk
```

Now synthesize the CloudFormation template for this code.

```
cdk synth
```

Then create the necessary resources using
```
cdk bootstrap
```

If everything looks fine, we deploy using
```
cdk deploy
```

Hurray! Now we are ready with our application.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk bootstrap`   used in creating the different resources while creating the entire stack
 * `cdk docs`        open CDK documentation
 * `cdk destroy`     destroys the entire CDK stack created
