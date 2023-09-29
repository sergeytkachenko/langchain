


 Update the Identity Service when you update the Creatio instance. The Identity Service archive is provided with the Creatio install file. Before you update the Identity Service on the Creatio application server, update the Creatio instance. Instructions:
 [Update guide](https://academy.creatio.com/docs/release/update-guide/update-guide) 
 .
 



 To update the Identity Service using IIS:
 


1. **Install additional components** 
 .
 



 .NET 6 Runtime.
 [Download the install file](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) 




 .NET 6 Hosting Bundle.
 [Download the install file](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-aspnetcore-6.0.14-windows-hosting-bundle-installer)
2. **Restart the IIS** 
 .
3. **Back up the files** 
 of the root Identity Service directory to an arbitrary place.
4. **Back up the database** 
 connected to the current version of Identity Service. Instructions:
 [Creating database backup](https://academy.creatio.com/docs/release/update-guide/update-guide#title-143-2) 
 .
5. **Stop the application pool** 
 of the Identity Service in the IIS.
6. **Stop the website** 
 of the Identity Service in the IIS.
7. **Extract the IdentityService.zip archive** 
 to the Creatio install file directory.
8. **Replace the files in the root Identity Service directory** 
 with the unpacked files.
9. **Reconfigure the Identity Service** 
 using IIS. Instructions:
 [Install the Identity Service using IIS](https://academy.creatio.com/documents?id=2466&anchor=title-2002-5) 
 (steps 7-11).
10. **Start the application pool** 
 of the Identity Service in the IIS.
11. **Start the website** 
 of the Identity Service in the IIS.
12. **Make sure the Identity Service is running** 
 . To do this, use the
 
 [Identity Service URL]/
 
 .well-known/
 
 openid-configuration
 
 link.
 



 If the Identity Service is not running as expected, restore the previous version of the Identity Service.
 [Read more >>>](#title-roll_back_changes)



**As a result** 
 , the Identity Service will be updated.
 




 To
 **restore the previous version** 
 of the Identity Service:
 


1. Restore the files from the Identity Service backup.
2. Restore the database from the backup.
3. Restart the application pool of the Identity Service in the IIS.
4. Restart the website of the Identity Service in the IIS.
5. Make sure the Identity Service is running. To do this, use the
 
 [Identity Service URL]/
 
 .well-known/
 
 openid-configuration
 
 link. If the Identity service is not running, contact Creatio support.




