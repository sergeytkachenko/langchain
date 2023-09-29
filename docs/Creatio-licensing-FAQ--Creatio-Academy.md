


 How does data input restricted user license work?
---------------------------------------------------



 The main idea behind the data input restricted user license is to make Creatio accessible for many users at lower price. However, these users have limited access to Creatio data added by other users. This solution is suitable for B2C self-service portals where users communicate only with the company's support team.
 



 Creatio has the following rules of working with data for users that have data input restricted license:
 


* If you have no extra access permissions configured for the object that has an existing section, the users have read only access to the records they created. If the section contains no such records, the users see a blank list. To enable these users to work with data, configure object permissions and grant the users permissions to create and edit records. Learn more:
 [Object operation permissions](https://academy.creatio.com/documents?id=262) 
 .
* If you have access permissions configured for the object that has an existing section, the users can work only with the records they created.
* If the object does not have an existing section, the users can be granted access to data created by other users in read-only mode. This way you can enable the users to use lookup data in their records. For example, case categories.
 




 Fig. 1 Lookup operation permissions
 

![scr_lookup_access_permissions_example.png](/docs/sites/en/files/images/Setup_and_Administration/creatio_licensing/scr_lookup_access_permissions_example.png)
* Services
 
 ,
 
 Service agreements
 
 ,
 
 Configuration items
 
 ,
 
 Knowledge base
 
 and
 
 Products
 
 sections are exceptions. If you grant the user permissions only to read data in these sections, the users will have access to all the records regardless of their author.
* The users can use the approvals and attachments functionality out of the box.



 How are access permissions configured for a data input restricted user?
-------------------------------------------------------------------------



 Object operation permissions for data input restricted users have some special conditions. If you do not set up the operation permissions for the object, all users except data input restricted users can create, read, update, or delete all records in the object. Data input restricted users in this case can only read records as long as the object has no corresponding section. Learn more:
 [How does data input restricted user license work?](#title-2804-2) 




 If you want to grant data input restricted users permissions to work with Creatio records:
 


1. **Create a role** 
 and add data input restricted users who need access permissions to the role. Instruction:
 [Organizational roles](https://academy.creatio.com/documents?id=1434)
2. **Enable access to operations** 
 in the object. Instruction:
 [Object operation permissions](https://academy.creatio.com/documents?id=262)
3. **Configure access to operations** 
 for the role created on step 1. Instruction:
 [Object operation permissions](https://academy.creatio.com/documents?id=262)



 For example, if external Creatio users have data input restricted licenses, the operation permissions look as follows:
 




 Fig. 2 Set up object permissions
 

![scr_operation_rights_example.png](/docs/sites/en/files/images/Setup_and_Administration/creatio_licensing/scr_operation_rights_example.png)




