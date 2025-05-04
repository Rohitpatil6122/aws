import json
import boto3
from support_function import  check_bucket_exists, extract_path, copy_csv_file, delete_csv_file




def lambda_handler(event, context):
    
    try:
        
    
    # creating s3 client
        s3 = boto3.client('s3')
        
        # checking whether bucket exists
        if check_bucket_exists(s3=s3,bucket_name='ainexus-b2batch'):
    
            csv_list=extract_path(s3=s3,bucket_name='ainexus-b2batch')
    
            if csv_list:
    
                copy_csv_file(s3=s3,bucket_name='ainexus-b2batch',csv_list=csv_list,destination_folder='output')
    
                delete_csv_file(s3=s3,bucket_name='ainexus-b2batch',csv_list=csv_list)
    
                

    except Exception as e:
        print(e)