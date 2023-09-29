


 Install Microsoft SQL Server Management Studio on the database server. Installation instructions are available in the
 
[Microsoft SQL Server documentation](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15) 

 .
 





 Note.
 
 Microsoft SQL has been tested for deployment of clustered Creatio databases. Using Microsoft SQL Always On availability groups is a recommended method of setting up a high availability configuration. For more information on Microsoft SQL Always On technology, please refer to the
 
[Microsoft SQL documentation](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-ver15) 

 .
 




 In Microsoft SQL Server Management Studio, create two database users.
 


* A user with the “
 **sysadmin** 
 ” role, who has maximum access privileges on the database server level. This user will restore the Creatio database from a backup file and assign access permissions.
* A user with the “
 **public** 
 ” role, whose permissions are limited. You will need this user to set up a secure connection to the restored Creatio database using Microsoft SQL authentication.



 For more on creating users and access permissions on the database server, see
 
[Microsoft SQL Server documentation](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-database-user?view=sql-server-ver15) 

 .
 



 To restore a database:
 


1. Authenticate in Microsoft SQL Server Management Studio as a “
 **sysadmin** 
 ” user.
2. Click the
 
 Databases
 
 catalog and select the
 
 Restore Database
 
 option from the context menu (Fig. 1).
 





 Fig. 1
 

 Selecting database backup command
 

![scr_setup_restore_database.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/deploy_mssql_database/scr_setup_restore_database.png)
3. In the
 
 Restore Database
 
 window:
 


	1. Specify the name of the database in the
	 
	 Database
	 
	 field;
	2. Specify the
	 
	 Device
	 
	 checkbox and specify the path to the database backup copy file. The database backup file is supplied together with executable files and is located in the
	 **~\db** 
	 folder (Fig. 2).
	 
	
	
	
	
	
	 Fig. 2
	 
	
	 Selecting database backup
	 
	
	![scr_setup_restore_database_data.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/deploy_mssql_database/scr_setup_restore_database_data.png)
4. Specify a folder on the database server where the Creatio database will be restored. Creating a folder to restore database files is required beforehand, as the SQL Server is not permitted to create directories.
 


	1. Go to the
	 
	 Files
	 
	 tab.
	2. In the
	 
	 Restore the database files as
	 
	 area, select the
	 
	 Relocate all files and folders
	 
	 checkbox.
	3. Specify paths to the folders where SQL Management Studio will save the
	 **TS\_Data.mdf** 
	 and
	 **TS\_Log.ldf** 
	 files (Fig. 3).
	 
	
	
	
	
	
	 Fig. 3
	 
	
	 Specifying the names and paths to TS\_Data.mdf and TS\_Log.ldf files.
	 
	
	![scr_setup_restore_database_options.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/deploy_mssql_database/scr_setup_restore_database_options.png)
5. Click the
 
 OK
 
 button and wait for the database restore process to be finished.
6. Enable connection for the
 **public** 
 Microsoft SQL user who Creatio will use to access the database.
 


	1. Locate the restored Creatio database in Microsoft SQL Server Management Studio.
	2. Click the
	 
	 Security
	 
	 tab.
	3. Add the user to the
	 
	 Users
	 
	 list.
	4. Click
	 
	 Membership
	 
	 and specify the
	 **db\_owner** 
	 , which will grant the user full access to the restored Creatio database.




