## Deploy with Docker

Build the dockerfile, this must be done at root

`docker build --build-arg AWS_ACCESS_KEY_ID=<XXX> --build-arg AWS_SECRET_ACCESS_KEY=<XXX> -t <repo-name> .`

Tag it up to the latest version

`docker tag  <repo-name>:latest 069354831235.dkr.ecr.eu-central-1.amazonaws.com/<repo-name>:latest`

Push to AWS to create an ECR layer

`docker push 069354831235.dkr.ecr.eu-central-1.amazonaws.com/<repo-name>:latest`

Might need to login/verify the ECR CLI

`aws ecr get-login-password --region eu-central-1`

`docker login -u AWS -p <PASSWORD FROM ABOVE> https://069354831235.dkr.ecr.eu-central-1.amazonaws.com/v2/`

### The dockerfile can be verified

Run the dockerfile by
`docker run -p 9000:8080 -e AWS_ACCESS_KEY_ID=<XXX> -e AWS_SECRET_ACCESS_KEY=<XXX> <repo-name>`

Open another terminal window and run 
`curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'`

## Deploy with .zip

Deactivate the venv:  
`deactivate`

Start with copying the python file into `venv/lib/python3.7/site-packages/`: 

`zip my-deployment-package.zip lambda_function.py`

Go into the venv

`cd venv/lib/python3.7/site-packages`

Zip everything up

`zip -r ~/Documents/Dev/ASKET/<repo-name>/<repo-name>.zip lambda_function.py pysftp fnmatch && cd -`

Create a function that is invokable in aws lambda cli by running

`aws lambda create-function --function-name ms-direct-sftp-to-s3 --zip-file fileb://<repo-name>.zip --handler lambda_function.lambda_handler --runtime python3.7 --role arn:aws:iam::069354831235:role/lambda-s3-role`


