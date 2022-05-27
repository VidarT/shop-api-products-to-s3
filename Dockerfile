ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

FROM ubuntu:14.04

ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

FROM public.ecr.aws/lambda/python:3.7

COPY requirements.txt ./
COPY .env ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY lambda_function.py   ./

CMD ["lambda_function.lambda_handler"]