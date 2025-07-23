# -SDKmanageAWSServices

# 🗂️ AWS S3 File Mover + SNS Notification

This Python project moves files from one S3 folder to another based on their filename prefix and sends an email notification via Amazon SNS when the move is complete.

---

## 📌 What the Script Does

- Looks inside the `customer-details/` folder in your source S3 bucket.
- Finds files that start with:
  - `sr1_` → moves them to `sr1/`
  - `sr2_` → moves them to `sr2/`
  - `sr3_` → moves them to `sr3/`
- After copying the file, it deletes the original.
- Sends an email summarizing all moved files.

---

## 🧰 What You Need

- Python 3.x
- AWS CLI installed and configured:

  ```bash
  aws configure

Permissions to:

Create S3 buckets

Create SNS topics and subscribe emails

Dependencies installed:

bash
Copy
Edit
pip install -r requirements.txt
🛠️ Step-by-Step Instructions
Step 1: Set Up Your AWS Credentials
Run this once:

aws configure
Step 2: Set Up the Resources
This creates 2 S3 buckets and an SNS topic.

python setup_resources.py
📧 Check your email and confirm the SNS subscription when prompted!

Step 3: Upload Some Test Files
Upload files to the customer-details/ folder:

aws s3 cp sr1_invoice.csv s3://your-source-bucket/customer-details/
aws s3 cp sr2_data.csv s3://your-source-bucket/customer-details/
Step 4: Move the Files and Send Notification
You can either run just the mover:

python move_s3_files.py
Or run everything together (setup + move):

python main.py
✅ Example Output
In your email, you’ll receive:

S3 File Movement Summary:
sr1_invoice.csv ➜ sr1/sr1_invoice.csv
sr2_data.csv ➜ sr2/sr2_data.csv
And in your terminal:

✅ Moved sr1_invoice.csv to sr1/sr1_invoice.csv
✅ Moved sr2_data.csv to sr2/sr2_data.csv
📩 SNS notification sent.
📁 Project Files
File	Purpose
setup_resources.py	Creates buckets and SNS topic
move_s3_files.py	Moves and deletes files, sends email
resources.py	Stores all config values like bucket names and prefix rules
main.py	(Optional) Runs both setup + file mover
requirements.txt	Includes boto3 library

🤝 Who Made This?
Created by Arie Kaplan
GitHub: @a972k
