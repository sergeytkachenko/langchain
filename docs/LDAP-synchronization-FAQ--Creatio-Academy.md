


 Why did Creatio not import all users from the LDAP directory?
---------------------------------------------------------------



 There could be several reasons:
 


* There are directory users with a matching “User name” attribute who also have empty or matching “Email” and “Phone number” attributes. Creatio checks for duplicates by “User name”, “Email” and “Phone number” attributes automatically during LDAP synchronization.
* The date in the “Maximum modification date of LDAP entry” (“LDAPEntryMaxModifiedOn” code) Creatio system setting is later than the date in “whenChanged” LDAP user attribute. Creatio will import a user only if the date in “Maximum modification date of LDAP entry” is earlier than the date in “whenChanged” LDAP user attribute.





Why did Creatio not import all Active Directory users after the LDAP synchronization?
----------------------------------------------------------------------------------------



 Active Directory page size may be shorter than the number of users. Since Creatio does not support pagination when synchronizing users through LDAP, it will only process records from the first page. To resolve this issue, increase the “MaxPageSize” value in Active Directory so all the users fit on the first page.
 






 Why is it impossible for a user to log in under their domain account after setting up LDAP?
------------------------------------------------------------------------------------------------



 To resolve this issue in Creatio
 **on-site** 
 , navigate to the website's roote directory, open the Web.config file, and specify the authentication providers in the “auth providerNames” parameter:
 






```

auth providerNames = "InternalUserPassword,Ldap,SSPLdapProvider"
```





 After you save the changes, restart the LDAP synchronization.
 



 To resolve this issue in Creatio
 **in the cloud** 
 , contact Creatio support.
 



 Is it possible to connect a user imported from Active Directory to a specific Creatio account?
------------------------------------------------------------------------------------------------


* If the user's “Company name” attribute matches a Creatio account name exactly, Creatio will automatically connect the imported user to that account.
* If the account specified in the “Company name” attribute does not match any Creatio account names verbatim, Creatio will automatically connect the imported user to “Our company”.



 Why is it impossible to import users from the “Domain users” group?
---------------------------------------------------------------------



 “Domain users” group is a primary group. The “memberOf” attribute does not display primary groups. To import these users, add them to a different, non-primary group.
 



 What causes error “22021: invalid byte sequence for encoding "UTF8": 0x00” when synchronizing Active Directory by LDAP?
-------------------------------------------------------------------------------------------------------------------------



 This error occurs in Creatio with PostgreSQL. It is caused by system groups that support pre-2000 Windows versions in the imported data. To resolve this issue, exclude those system groups from synchronization and change the group filter to:
 






```

(&(objectClass=group)(!userAccountControl:1.2.840.113556.1.4.803:=2)(!(isCriticalSystemObject=TRUE)))
```





 What causes error “Cannot insert duplicate key row in object 'dbo.SysAdminUnit' with unique index 'IUSysAdminunitNameDomain'. The duplicate key value is (…)”?
----------------------------------------------------------------------------------------------------------------------------------------------------------------



 This synchronization error occurs if there is a directory user you have previously added to Creatio manually.
 



 How can I set up a specific LDAP filter?
------------------------------------------



 You can learn more about setting up LDAP filters in Internet Engineering Task Force's
 [String Representation of Search Filters](https://tools.ietf.org/search/rfc4515) 
 manual. You may also find Microsoft's
 [Active Directory: LDAP Syntax Filters](https://social.technet.microsoft.com/wiki/contents/articles/5392.active-directory-ldap-syntax-filters.aspx) 
 documentation useful.
 




