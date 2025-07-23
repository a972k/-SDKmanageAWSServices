from setup_resources import setup_infrastructure
from move_s3_files import move_files

# Main function to set up resources and move files 
def main():
    print("Setting up AWS resources...")
    setup_infrastructure()  # Creates buckets and SNS
    
    print("Moving files and sending notifications...")
    move_files()            # Moves files and sends notification
    
    print("Done")

if __name__ == "__main__":
    main()
