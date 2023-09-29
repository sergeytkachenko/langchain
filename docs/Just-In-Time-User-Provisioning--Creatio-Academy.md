



 This article is relevant to Creatio version 8.0.2 and earlier. If you set up integration with Creatio version 8.0.3 and later follow the instructions on single sign-on setup.
 




 Use Just-In-Time User Provisioning (JIT UP) function to avoid creating accounts for each separate service and to keep user database up-to-date. JIT UP extends the Single Sign-On (SSO) technology and helps to reduce the number of operations for administrating accounts and personal data in contact records. Each time a user logs on using SSO, the data on the contact page are updated with the data obtained from the identity provider (Fig. 1). If a user has no account in the Creatio, it can be created when the user logs in for the first time.
 




 Fig. 1 Update data via Just-in-Time User Provisioning
 

![scr_chapter_single_sign_on_jit_scheme.png](/guides/sites/en/files/documentation/user/en/user_access_management/BPMonlineHelp/just_in_time_user_provisioning/scr_chapter_single_sign_on_jit_scheme.png)





 Note.
 
 Updating a contact with data from an identity provider includes updating the data on the record page and contact’s connections to user groups.
 




 You can enable JIT UP when setting up the identity provider integration. Read more:
 [Single Sign-On via ADFS](/docs/7-18/user/setup_and_administration/user_and_access_management/authentication/set_up_sso_via_adfs/single_sign-on_via_adfs) 
 ,
 [Single Sign-On via OneLogin](/docs/7-18/user/setup_and_administration/user_and_access_management/authentication/set_up_sso_via_onelogin/single_sign-on_via_onelogin) 
 .
 



 To specify contact fields that should be populated with data from the identity provider, configure the mapping of the SAML Assertion fields with Creatio columns. This is done in the SAML Assertion of the identity provider and in the
 
 SAML field name converters to contact field name
 
 lookup.
 



 To set up mapping, you will need a configured account in the identity provider (Fig. 2) with the data required for Creatio.
 




 Fig. 2 Account fields in the OneLogin identity provider
 

![scr_chapter_single_sign_on_jit_setup_onelogin_user_profile.png](/guides/sites/en/files/documentation/user/en/user_access_management/BPMonlineHelp/just_in_time_user_provisioning/scr_chapter_single_sign_on_jit_setup_onelogin_user_profile.png)



 To set up field population parameters:
 


1. Ensure that all required field values are transferred to Creatio. For example, to fill the profile of John Best with data from the
 
 Company
 
 ,
 
 Department
 
 ,
 
 Email
 
 ,
 
 First Name
 
 ,
 
 Last Name
 
 , and
 
 Phone
 
 fields (Fig. 3).
 




 Fig. 3 Application parameters in the OneLogin identity provider
 

![scr_chapter_single_sign_on_jit_setup_onelogin_application_parameters.png](/guides/sites/en/files/documentation/user/en/user_access_management/BPMonlineHelp/just_in_time_user_provisioning/scr_chapter_single_sign_on_jit_setup_onelogin_application_parameters.png)





 Note.
 
 Use the
 [SAML Decoder](https://chrome.google.com/webstore/detail/saml-message-decoder/mpabchoaimgbdbbjjieoaeiibojelbhm) 
 Google Chrome extension to verify the parameters.
2. Verify that correct rules to receive values and update the columns for each required field are specified on the Creatio side. Rules are configured in the
 
 SAML field name converters to contact field name
 
 lookup. Specify a column in the Creatio for each field received from the identity provider. For example, to fill the
 
 Department
 
 ,
 
 Account
 
 ,
 
 Phone
 
 ,
 
 Email
 
 ,
 
 Given name
 
 , and
 
 Surname
 
 columns in Creatio, specify them next to the corresponding SAML attributes (Fig. 4).
 





 Note.
 
 Specify column names in the Creatio database as contact columns.
 





 Fig. 4 The
 
 SAML field name converters to contact field name
 
 lookup configuration
 

![scr_chapter_single_sign_on_jit_setup_saml_converter_lookup.png](/guides/sites/en/files/documentation/user/en/user_access_management/BPMonlineHelp/just_in_time_user_provisioning/scr_chapter_single_sign_on_jit_setup_saml_converter_lookup.png)
3. A field that is missing in the identity provider data can be populated with the value specified in the
 
 Column default value
 
 field of the
 
 SAML field name converters to contact field name
 
 lookup. For example, the OneLogin identity provider does not contain the
 
 Type
 
 field and does not pass it when the user logs on. To populate this field in Creatio, create a rule in the lookup and specify the “Employee” value as default (Fig. 4). In this case, all created contacts will have the “Employee” value in the
 
 Type
 
 field.
4. You can add custom parameters to the OneLogin identity provider and specify macros for them. Learn more about how to work with macros in
 [OneLogin documentation](https://onelogin.service-now.com/support?id=kb_article&sys_id=f33ad943db109700d5505eea4b9619d1) 
 .




