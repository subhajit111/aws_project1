import boto3
s3_client = boto3.client("s3")

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('student')

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    s3_file_name = event['Records'][0]['s3']['object']['key']
    resp = s3_client.get_object(Bucket=bucket_name,Key=s3_file_name)
    data = resp['Body'].read().decode("utf-8")
    student = data.split("\n")
    for stu in student:
        print(stu)
        stu_data =stu.split(",")
        try:
            table.put_item(
                Item ={
                    "id" : stu_data[0],
                    "name" : stu_data[1],
                    "location" : stu_data[2]
                }
                )
        except Exception as e:
            print("End of file")