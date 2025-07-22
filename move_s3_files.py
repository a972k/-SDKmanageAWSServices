import boto3
import os
from resources import source_buket, destination_bucket, prefix, destination_folder, sns_topic_arn

# Update these values
source_buket = 'my-source-bucket-ak'
destination_bucket = 'my-destination-bucket-ak'
prefix = 'customer-details/sr1_'
destination_folder = 'sr1/'
sns_topic_arn = 'arn:aws:sns:us-east-1:123456789012:file-move-notification'

# AWS Clients
s3 = boto3.client('s3')
sns = boto3.client('sns')

def move_files():
    response = s3.list_objects_v2(Bucket= source_buket, Prefix=prefix)
    files_moved = []

    for obj in response.get('Contents', []):
        key = obj['Key']
        filename = os.path.basename(key)
        dest_key = f'{destination_bucket}{filename}'

        # Copy file
        s3.copy_object(
            Bucket=destination_bucket,
            CopySource={'Bucket': source_buket, 'Key': key},
            Key=dest_key
        )

        # Delete source file
        s3.delete_object(Bucket=source_buket, Key=key)

        print(f"Moved: {key} ➜ {dest_key}")
        files_moved.append(filename)

    # Send SNS if files were moved
    if files_moved:
        message = f"Moved {len(files_moved)} file(s):\n" + "\n".join(files_moved)
        sns.publish(
            TopicArn=sns_topic_arn,
            Subject="S3 File Movement Notification",
            Message=message
        )
        print("SNS Notification sent.")

if __name__ == "__main__":
    move_files()
