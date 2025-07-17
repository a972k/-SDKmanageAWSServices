# -SDKmanageAWSServices

# AWS S3 File Mover

## Project Overview
Python script to move files from one S3 folder to another based on prefix and notify via SNS.

## How It Works
- Moves files from `customer-details/` that start with `sr1_`
- Copies them to another S3 bucket under `sr1/` folder
- Deletes the original files
- Sends email via SNS

## Setup Steps
1. Create 2 S3 buckets
2. Create SNS topic and subscribe your email
3. Upload files to `customer-details/`
4. Run the Python script
5. Check email and S3

## Run
```bash
python move_s3_files.py
