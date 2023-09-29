



 You set up file storage integration in Creatio version 7.18.1 or later.
 




**S3 file storage** 
 . A cloud based object storage REST service. Allows storing data as is with no scalability restrictions.
 



**S3 (Simple Storage Service).** 
 A data transfer protocol developed by Amazon. We recommend using Amazon S3 storage. Read more in the
 [vendor’s official documentation](https://docs.aws.amazon.com/s3/index.html?nc2=h_ql_doc_s3) 
 .
 





 Note.
 
 You can only connect one S3 storage to Creatio.
 




 To integrate an S3 file storage to a
 **cloud Creatio instance** 
 , contact the support team. To integrate an S3 file storage to an
 **on-site Creatio instance** 
 , your Creatio administrator must use this instruction.
 



 In general, the following
 **steps** 
 are required to set up S3 file storage integration:
 


1. Settings on the S3 side.
 [Learn more >>>](#title-3428-1)
2. Settings on the Creatio side.
 [Learn more >>>](#title-3428-2)



 Settings on the S3 side
-------------------------


1. Create an account with an S3-capable storage service.
2. Generate a “ServiceUrl” parameter to enable Creatio to access the storage.
3. Generate the “AccessKey” and “SecretKey” parameters to enable authorized requests to the storage.
4. Create “ObjectBucketName” and “RecycleBucketName” buckets with unique names.
 


	* “ObjectBucketName” is a bucket for storing files. The files are stored indefinitely.
	* “RecycleBucketName” is a bucket for storing deleted files. They are kept for database backups. Working with the buckets is based on the soft deletion principle: a file deleted from the “ObjectBucketName” bucket is moved to the “RecycleBucketName” bucket. The storage time for deleted files is controlled by the bucket settings of the service. For example, a file can be stored in the bucket for 90 days, then deleted automatically. In Creatio, the storage time for deleted files is the same as the storage time for database backups.
 Learn more in the
 [vendor’s official documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) 
 .



 Settings on the Creatio side
------------------------------



 To save new files uploaded to the
 
 Attachments and notes
 
 detail or email attachments in the S3 storage rather than the database, make the following adjustments on the Creatio side:
 


1. Set up a connection to the S3 storage. To do this, add an S3 storage connection string to the
 
 connectionString
 
 parameter of the ConnectionStrings.config configuration file:
 






```

<connectionStrings>
    ...
    <add name="s3Connection" connectionString="ServiceUrl=SOME_SERVICE_URL; AccessKey=SOME_ACCESS_KEY; SecretKey=SOME_SECRET_KEY; ObjectBucketName=SOME_OBJECT_BUCKET_NAME; RecycleBucketName=SOME_RECYCLE_BUCKET_NAME;" />
</connectionStrings>

```





 where
 


	* ServiceUrl
	 
	 is the endpoint for accessing the S3 storage.
	* AccessKey
	 
	 is the account access key for making an authorized request to the S3 storage.
	* SecretKey
	 
	 is the account key for making an authorized request to the S3 storage.
	* ObjectBucketName
	 
	 is the name of the container for storing files.
	* RecycleBucketName
	 
	 is the name of the container for storing deleted files. They are kept for database backups.
2. To ensure that connected files are also mfooved to “RecycleBucketName” when a section record is deleted, go to the Feature toggle page and enable the “UseBaseEntityFileDeleteListener” functionality. Learn more:
 [Feature Toggle mechanism](https://academy.creatio.com/documents?id=15631) 
 (developer documentation).
3. Set the S3 storage as the active file storage. To do this, open the “Active file content storage” system setting (code ActiveFileContentStorage). Select “S3 storage” in the
 
 Default value
 
 field.




 As a result, all files added to Creatio after connecting the S3 storage will be uploaded there. Files previously added to Creatio will remain in the original storage.
 




