



 Integration with Azure Blob file storage is available in Creatio version 8.0.2 and later.
 




**Azure Blob file storage** 
 is a cloud-based solution by Microsoft. Learn more in the
 [official vendor documentation](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction) 
 . Using the Azure Blob storage lets you reduce the Creatio database size. Data is stored as BLOB objects. Learn more in
 [Wikipedia](https://en.wikipedia.org/w/index.php?title=Binary_large_object&oldid=1087063332) 
 .
 





 Note.
 
 You can only connect Creatio to one Azure Blob storage.
 




 To integrate an Azure Blob storage with
 **Creatio in the cloud** 
 , contact Creatio support. To integrate an Azure Blob file storage with
 **Creatio on-site** 
 , your Creatio administrator must use these instructions.
 



 In general, the following
 **steps** 
 are required to set up integration with Azure Blob file storage:
 


1. Setup in Azure Blob.
 [Read more >>>](#title-3921-1)
2. Setup in Creatio.
 [Read more >>>](#title-3921-2)



 Setup in Azure Blob
---------------------


1. Sign up to the Microsoft Azure portal. Learn more in the
 [official vendor documentation](https://azure.microsoft.com/en-us/features/azure-portal/) 
 .
2. Generate a “Blob Service endpoint” parameter to enable Creatio to access the storage.
3. Generate the “AccountName” and “AccountKey” parameters to enable authorized requests to the storage. Learn more in the
 [official vendor documentation](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal) 
 .
4. Create “ObjectContainerName” and “RecycleContainerName” containers that have unique names.
 


	* “ObjectContainerName” is a container that stores files The files are stored indefinitely.
	* “RecycleContainerName” is a container that stores deleted files. They are kept for database backups. Container management is based on the soft deletion principle: a file deleted from the “ObjectContainerName” container is moved to the “RecycleContainerName” container. The storage time for deleted files is controlled by the container settings of the service. For example, a file can be stored in the container for 90 days, then deleted automatically. In Creatio, the storage time for deleted files is the same as the storage time for database backups.
 Learn more in the
 [official vendor documentation](https://docs.microsoft.com/en-us/azure/vs-azure-tools-storage-explorer-blobs#create-a-blob-container) 
 .



 Setup in Creatio
------------------



 To save new files uploaded to the
 
 Attachments and notes
 
 detail or email attachments to the Azure Blob storage rather than the database, take the following steps in Creatio:
 


1. Set up a connection to the Azure Blob storage. To do this, add an Azure Blob storage connection string to the
 
 connectionStrings
 
 parameter of the ConnectionStrings.config configuration file:
 






```

<connectionStrings>
    ...
    <add name="azureConnection" connectionString="AccountName=SOME_ACCOUNT_NAME; AccountKey=SOME_ACCOUNT_KEY; BlobEndpoint=SOME_BLOB_ENDPOINT; ObjectContainerName=SOME_OBJECT_CONTAINER_NAME; RecycleContainerName=SOME_RECYCLE_CONTAINER_NAME;" />
</connectionStrings>

```





 where
 


	* AccountName
	 
	 is the account name for making an authorized request to the Azure Blob storage.
	* AccountKey
	 
	 is the account key for making an authorized request to the Azure Blob storage.
	* BlobEndpoint
	 
	 is the endpoint for accessing the Azure Blob storage. The value of the “Blob Service endpoint” parameter obtained in the previous step.
	* ObjectContainerName
	 
	 is the name of the container that stores files.
	* RecycleContainerName
	 
	 is the name of the container that stores deleted files. They are kept for database backups.
2. To ensure that connected files are moved to “ RecycleContainerName” correctly when a section record is deleted, open the Feature toggle page and enable the “UseBaseEntityFileDeleteListener” feature. Learn more in
 [Feature Toggle mechanism](https://academy.creatio.com/documents?id=15631) 
 .
3. Set the Azure Blob storage as the active file storage. To do this, open the “Active File Content Storage” (“ActiveFileContentStorage” code) system setting. Select “Azure Blob storage” in the
 
 Default value
 
 field.




 As a result, all files added to Creatio after connecting the Azure Blob storage will be uploaded there. Files previously added to Creatio will remain in the original storage.
 




