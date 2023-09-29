


 Manage Creatio users in the
 
 System users
 
 section. User settings determine what operations users can perform, what data they can see and how they can work with this data.
 





 Note.
 
 By default, only system administrators have access to the
 
 System users
 
 section.
 




 Click
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/user_access_management/BPMonlineHelp/adding_users/btn_system_designer.png)
 →
 
 System users
 
 to access the
 
 System users
 
 section.
 



 Add a system administrator user
---------------------------------



 By default, Creatio has a “
 **System administrators** 
 ” organizational role whose members have full access to all data in Creatio. This is achieved through access to the following system operations:
 


* “Add any data” (“CanInsertEverything” code)
* “Delete any data” (“CanDeleteEverything” code)
* “Edit any data” (“CanUpdateEverything” code)
* “View any data” (“CanSelectEverything” code)



 Learn more:
 [Description of system settings](/docs/7-17/user/setup_and_administration/system_settings_and_lookups/system_setting_reference/description_of_system_settings) 
 .
 



 To add a new system administrator user in Creatio:
 


1. In the
 
 Contacts
 
 section,
 **create a contact** 
 for the new user or make sure that the relevant contact already exists. Learn more:
 [Add a new contact](#title-2067-5) 
 .
2. In the
 
 System users
 
 section,
 **create a new user** 
 , specifying the contact in the user profile. Learn more:
 [Create a user](#title-2067-6) 
 .
3. Add the user to the “System administrators” role.
 





 Attention.
 
 Access to these operations overrides any object permissions a user may have. For example, a user with permission to the “View any data” system operation can view all records in objects, even if you try to deny the “Read” permission for that user in the object permissions UI.



 There are several ways to assign a system administrator role to a user:
 


* From the user page
* From the role page


### 
 Method 1. Assign a system administrator role to a user from the user’s page


1. Click
 ![btn_system_designer00001.png](/guides/sites/en/files/documentation/user/en/user_access_management/BPMonlineHelp/adding_users/btn_system_designer00001.png)
 → System Designer →
 
 System users
 
 .
2. Open the user page → the
 
 Roles
 
 tab.
3. Click
 ![btn_com_add_tab.png](/guides/sites/en/files/documentation/user/en/user_access_management/BPMonlineHelp/adding_users/btn_com_add_tab.png)
 in the
 
 Organizational roles
 
 detail and specify the “
 **System administrators** 
 ” role (Fig. 1).
 





 Fig. 1
 
 Assigning a system administrator role to a user from the user’s page
 

![gif_section_users_add_sys_admin1.gif](/guides/sites/en/files/documentation/user/en/user_access_management/BPMonlineHelp/adding_users/gif_section_users_add_sys_admin1.gif)



 As a result, the user will be added to the “System administrators” role and will receive full access to all Creatio data.
 


### 
 Method 2. Assign a system administrator role to a user from the role page


1. Click
 ![btn_system_designer00002.png](/guides/sites/en/files/documentation/user/en/user_access_management/BPMonlineHelp/adding_users/btn_system_designer00002.png)
 →
 
 Organizational roles
 
 .
2. In the list of organizational roles represented in the form of a folder tree, select the “System administrators” role. The area to the right of the roles tree will show the page of the selected role.
3. On the
 
 Users
 
 tab:
 


	1. Click
	 ![btn_com_add_tab00003.png](/guides/sites/en/files/documentation/user/en/user_access_management/BPMonlineHelp/adding_users/btn_com_add_tab00003.png)
	 and select
	 
	 Add existing
	 
	 to
	 **add an existing user** 
	 . In the pop-up box, select the corresponding user (Fig. 2).
	2. Click
	 ![btn_com_add_tab00004.png](/guides/sites/en/files/documentation/user/en/user_access_management/BPMonlineHelp/adding_users/btn_com_add_tab00004.png)
	 and select
	 
	 Add new
	 
	 to
	 **add a new user** 
	 assigned to this role. You will need to fill out the new user page.
	 
	
	
	
	
	
	 Fig. 2
	 
	 Assigning a system administrator role to a user via the
	 
	 Organizational roles
	 
	 section
	 
	
	![gif_section_users_add_sys_admin2.gif](/guides/sites/en/files/documentation/user/en/user_access_management/BPMonlineHelp/adding_users/gif_section_users_add_sys_admin2.gif)



 As a result, the user will be added to the “System administrators” role and will receive full access to all data in Creatio.
 



 Add a regular employee user
-----------------------------



 To create a new user account for a regular employee:
 


1. In the
 
 Contacts
 
 section,
 **create a contact** 
 for the new user or make sure that the relevant contact already exists. Learn more:
 [Add a new contact](#title-2067-5) 
 .
2. In the
 
 System users
 
 section,
 **create a new user** 
 , specifying the contact in the user profile. Learn more:
 [Create a user](#title-2067-6) 
 .
3. **Assign the user a role** 
 , if applicable. Learn more:
 [Assign a user role](/docs/8-0/user/setup_and_administration/user_and_access_management/user_management/assign_a_user_role_shortcut/assign_a_user_role) 
 .
4. **Distribute licenses** 
 to the user. Learn more:
 [Issue a license to a user](/docs/8-0/user/setup_and_administration/user_and_access_management/user_management/issue_a_license/issue_a_license_to_a_user) 
 .



 Add a new contact
-------------------


1. Go to the
 
 Contacts
 
 section →
 
 Create contact
 
 .
2. Fill out the required fields on the contact mini-page and click
 
 Save
 
 (Fig. 3).
 





 Fig. 3
 
 Adding a new contact
 

![gif_section_users_add_contact.gif](/guides/sites/en/files/documentation/user/en/user_access_management/BPMonlineHelp/adding_users/gif_section_users_add_contact.gif)



 As a result, a new contact will be added to Creatio, and you will be able to create a user for this contact.
 





 Note.
 
 You can also add a new contact directly from the contact lookup page when filling out the
 
 Contact
 
 field on the user page. Click
 ![btn_com_lookup.png](/guides/sites/en/files/documentation/user/en/user_access_management/BPMonlineHelp/adding_users/btn_com_lookup.png)
 in the
 
 Contact
 
 field, then click
 
 New
 
 in the lookup box that pops up. Fill out the contact page that opens. After you save the contact page, you will return to the new user page, with the
 
 Contact
 
 field populated with the newly-created contact.
 




 Create a user
---------------


1. Click
 ![btn_system_designer00005.png](/guides/sites/en/files/documentation/user/en/user_access_management/BPMonlineHelp/adding_users/btn_system_designer00005.png)
 →
 
 System users
 
 .
2. Click
 
 New
 
 →
 
 Company employee
 
 (Fig. 4).
 





 Fig. 4
 
 Select a user type
 

![scr_section_users_add_user.png](/guides/sites/en/files/documentation/user/en/user_access_management/BPMonlineHelp/adding_users/scr_section_users_add_user.png)





 Note.
 
 You can change the type of the user (“Company employee” or “Portal user”) after saving the new user record and reopening the user page.
3. Fill out the fields on the page that opens:
 


	1. Contact
	 
	 – select the user’s contact in the
	 
	 Contacts
	 
	 section.
	2. Type
	 
	 – Creatio populates the field automatically when you select the user type at step 2. The possible field values are “Portal user” or “Company employee”.
	3. Active
	 
	 – a status checkbox selected automatically for active users. Clear the checkbox to deactivate a user.
	4. Culture
	 
	 – the interface language for the current user. Creatio populates the value automatically, the user can change the interface language in the user’s profile.
	 
	
	
	
	
	
	 Note.
	 
	 The
	 
	 Culture
	 
	 field displays active languages. To select other languages, activate them in the
	 
	 Languages
	 
	 section of the System designer. Learn more about Creatio cultures:
	 [Manage UI languages](/docs/8-0/user/customization_tools/custom_localization/manage_languages/manage_ui_languages) 
	 .
	5. Home page
	 
	 – select a section page that will open by default when the user logs in to Creatio. If you leave the field empty, the user will be redirected to the Main Menu, and upon subsequent logins – to the last opened page during the previous session.
	6. Date and time format
	 
	 – specify the format that will be used to display dates for the user. You can leave the field blank, the user will be able to specify the format later in the user profile.
4. Fill out the fields on the
 
 Authentication
 
 detail:
 


	1. Username
	 
	 – enter the Creatio user's login. This is a required field.
	2. Email
	 
	 – enter the Creatio user's login email. If you fill out this field, the user will be able to log in with either the username or the email.
	3. Password
	 
	 ,
	 
	 Password confirmation
	 
	 – enter the password the user will use to log in to Creatio. These are required fields.
	4. Password expiration date
	 
	 – the field is non-editable and displays the date when the password expires. The date is calculated based on the
	 
	 Default value
	 
	 field of the “Password validity term, days” (“MaxPasswordAge” code) system setting. The value is set to “0” by default, in which case the password has no expiration date, and the
	 
	 Password expiration date
	 
	 field on the user’s page remains blank and locked.
	5. Reset password
	 
	 – select this checkbox if you want to force the user to change their password when logging in for the next time. If the checkbox is selected on the user’s page, Creatio will notify the user that their password has expired and request changing it at the next login attempt.
	 
	
	
	
	
	
	 Note.
	 
	 If you use the LDAP authentication, select the
	 
	 LDAP authentication
	 
	 checkbox and specify the username from the LDAP lookup in the
	 
	 Username
	 
	 field. The lookup in this field contains the list of LDAP users that have not been synchronized with Creatio yet. Learn more:
	 [Set up LDAP synchronization](/docs/7-18/user/setup_and_administration/user_and_access_management/synchronize_users_with_ldap/set_up_ldap_synchronization_shortcut/set_up_ldap_synchronization) 
	 .
5. Save the page.



 As a result, a new user will be added to Creatio.
 




