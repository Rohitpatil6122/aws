# function to check whether bucket name exists
def check_bucket_exists(s3,bucket_name):
    

    try:

        # getting all bucket list
        response = s3.list_buckets()
        flag=0
    
    
        for bucket in response['Buckets']:
           
            #checking whether name is equal to bucket name
            if bucket['Name']==bucket_name:
                
                print(f'{bucket_name} bucket exists')
                return True
    
        if not flag:
            print(f'{bucket_name} bucket does not exists')
            return False

    except Exception as e:
        print(e)


# function to extract paths
def extract_path(s3,bucket_name):

    try:
        
        csv_list=[]
        prefix = 'input/'  # e.g., "images/" or "" for root
        
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
        
        if 'Contents' in response:
            # print(f"Objects in '{prefix}':")
            for obj in response['Contents']:
                
               #checking whether file is csv or not 
                if obj['Key'].endswith('.csv'):
                    csv_list.append(obj['Key'])
                    print(f"filename: {obj['Key'].split('/')[-1]}")
                
                
        return csv_list

    except Exception as e:
        print(e)



# fun to copy file from one folder to another 
def copy_csv_file(s3,bucket_name,csv_list,destination_folder):

    try:
        
        for source_path in csv_list:
            
            destination_path = destination_folder + "/" + source_path.split("/")[-1]
            
            # coping file from one folder to another
            s3.copy_object(
            Bucket=bucket_name,
            CopySource={'Bucket':bucket_name, 'Key': source_path},
            Key=destination_path)
    
            print(f"{ source_path.split("/")[-1]} successfully dumped in {destination_folder} folder")
    except Exception as e:
        print(e)


# function to delete csv files
def delete_csv_file(s3,bucket_name,csv_list):

    try:
        
        for file_path in csv_list:
            
            # deleting files from input folder
            s3.delete_object(Bucket=bucket_name, Key=file_path)
            print(f"{file_path} successfully deleted")
    except Exception as e:
        print(e)



    
        
        
            
        
    