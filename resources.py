# resources 

source_buket = "my-source-bucket-ak" # your source bucket name here
destination_bucket = "my-destination-bucket-ak" # add your destination bucket name here
prefix = "customer-details/sr1_"
destination_folder = "sr1/"
subscription_email = " add your email here"  #your email here    
region = 'us-west-2' # specify your region here if different from us-west-2
sns_topic_name = 'file-move-notification' # specify your sns topic name here if different from
sns_topic_arn = 'arn:aws:sns:us-east-1:123456789012:file-move-notification'
# makes sure to chech for the correct region and account ID 
