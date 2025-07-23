import boto3
import os
from resources import source_bucket, destination_bucket, prefix, destination_folder, sns_topic_arn


# Update these values
source_bucket = 'my-source-bucket-ak'
destination_bucket = 'my-destination-bucket-ak'
prefix = 'customer-details/sr1_'
destination_folder = 'sr1/'
sns_topic_arn = 'arn:aws:sns:us-east-1:123456789012:file-move-notification'

# AWS Clients
s3 = boto3.client('s3')
sns = boto3.client('sns')

# Function to move files from source to destination bucket(can be defined as the same bucket)
def move_files():
    response = s3.list_objects_v2(Bucket= source_bucket, Prefix=prefix)
    files_moved = []

    for obj in response.get('Contents', []):
        key = obj['Key']
        filename = os.path.basename(key)
        dest_key = f'{destination_folder}{filename}'

        # Copy file
        s3.copy_object(
            Bucket=destination_bucket,
            CopySource={'Bucket': source_bucket, 'Key': key},
            Key=dest_key
        )

        # Delete source file
        s3.delete_object(Bucket=source_bucket, Key=key)

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
