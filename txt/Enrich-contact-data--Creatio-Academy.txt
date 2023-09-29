


 Creatio helps to maintain the completeness and relevance of the customer base using the data enrichment feature. Contact profile enrichment is a quick and easy way to update contact records with the latest information about their communications, addresses, noteworthy events, and accounts in the system.
 



 Add new users to Creatio and enrich contact data from email threads, social profiles, and other available sources in a few clicks.
 





 Attention.
 
 To enable data enrichment from correspondence and open sources, Creatio on-site users will need to specify a cloud service key in the
 
[corresponding system setting](https://academy.creatio.com/documents?product=administration&ver=7&id=1642) 

 – “Enable Email Mining” (EnableEmailMining).
 










 Enrich contact data from the incoming emails
----------------------------------------------------



 Smart enrichment allows you to maintain up-to-date contact data and create new contacts in a few clicks. When an email is received from a contact, the system automatically searches for new information about the contact in the message text, for example:
 


* contact full name
* the account name of the contact
* phone numbers
* email addresses
* social network accounts
* websites



 If the information is found, add it to the existing contact or create a new contact record.
 



 If the communication option type cannot be determined for information found in the email signature, the default communication option type will be assigned to the communication options added during enrichment. For example, for phone numbers, it will be “Business phone,” You can change the type of these communication options on the contact page. The default communication option types are defined in the
 
 Default type of contact communication options
 
 system setting.
 





 The incoming emails are checked for enrichment data upon downloading. Creatio analyzes the data in individual emails and email threads (enriching profile data of all thread participants). The signatures of incoming email messages are compared with the contact records in the system. If enrichment data are found, the
 
![btn_contact_data_enrichment.png](/docs/sites/default/files/documentation/user/ru/accounts_contacts/BPMonlineHelp/accounts_and_contacts_enrich_contact_data/btn_contact_data_enrichment.png)

 button appears next to the message header in the email message area of the communication panel.
 



 To enrich a contact profile:
 


1. Click
 
![btn_contact_data_enrichment00001.png](/docs/sites/default/files/documentation/user/ru/accounts_contacts/BPMonlineHelp/accounts_and_contacts_enrich_contact_data/btn_contact_data_enrichment00001.png)

 .
2. A menu with a list of all contacts to create or update records will be displayed. Select the
 
 Enrich “contact name”
 
 action (
 [Fig. 1](#XREF_46920_102)
 )
 




Fig. 1
 – Enrichment of contacts from the incoming email
 


![Enrich contact from email](/docs/sites/en/files/2020-12/scr_email_data_enrichment.png)





![scr_email_data_enrichment.png](/docs/sites/default/files/documentation/user/ru/accounts_contacts/BPMonlineHelp/accounts_and_contacts_enrich_contact_data/scr_email_data_enrichment.png)
3. In the opened window, select the data you want to add to the contact page from the email messages found in the signature (
 [Fig. 2](#XREF_40435_102)
 ).
 




Fig. 2
 – Data enrichment window
 


![Data enrichment window](/docs/sites/en/files/2020-12/scr_contact_data_enrichment.png)





![scr_contact_data_enrichment.png](/docs/sites/default/files/documentation/user/ru/accounts_contacts/BPMonlineHelp/accounts_and_contacts_enrich_contact_data/scr_contact_data_enrichment.png)







 Note.
 
 If the message is included in an email thread, the contact enrichment window will contain information on both the current contact and any other contacts identified in the thread, such as contacts from a forwarded message. Check the list of enrichment data before adding them to the system.
4. Save the new data.
 



 As a result, the information found in the emails will be added to the contact page and updated in all email threads over the previous seven days. The new data will also be reflected in the profile data complete indicator.
 



 The contact data for enrichment, that was not selected by the user will be remembered by the system and will not be offered for this contact anymore.







 Enrich contact profile from the case page
-----------------------------------------------



 Service Creatio enables you to enrich contact data directly from the email chain on the case page. Use data enrichment on the case page to:
 


* populate the contact record with new data found in the email signature
* add a new email address to the contact page
* create a new contact based on the email and nickname of the applicant and specify it as a contact for the case.





 Attention.
 
 Adding a new email address to the contact’s page and creating a new contact from the email chain is only available if automatic contact registration for unknown email addresses is disabled. Use the
 
 Automatically create new contacts for unknown email addresses
 
 system setting to manage the way Creatio handles unknown email addresses.
 








 Enrich contact profile from the contact page
--------------------------------------------------



 You can run smart enrichment of the contact data directly from the contact page. If enrichment data is available, the
 
![btn_contact_data_enrichment00002.png](/docs/sites/default/files/documentation/user/ru/accounts_contacts/BPMonlineHelp/accounts_and_contacts_enrich_contact_data/btn_contact_data_enrichment00002.png)

 button will appear in the contact profile. Data enrichment from the contact page is similar to the
 
[enrichment data from an email message](#HT_chapter_data_enrichment_contacts_from_email_howto) 

 .
 



 After Creatio adds data found in the email thread, the btn\_contact\_data\_enrichment00003.png button will disappear from the communication panel and the contact page.
 

 How to enrich contact profile from the case page
 



 Creatio enables you to enrich contact data directly from the email chain on the case page. Use data enrichment on the case page to:
 


* populate the contact record with new data found in the email signature
* add a new email address to the contact page
* create a new contact based on the email and nickname of the applicant and specify it as a contact for the case.





 Attention.
 
 Adding a new email address to the contact’s page and creating a new contact from the email chain is only available if automatic contact registration for unknown email addresses is disabled. Use the
 
 Automatically create new contacts for unknown email addresses
 
 system setting to manage the way Creatio handles unknown email addresses.
 




 The
 
![btn_contact_data_enrichment00003.png](/docs/sites/default/files/documentation/user/ru/accounts_contacts/BPMonlineHelp/accounts_and_contacts_enrich_contact_data/btn_contact_data_enrichment00003.png)

 button will appear in the email chain on the case page If Creatio detects new data in the email signature (
 [Fig. 3](#XREF_85393_148)
 ). The process is similar to the
 
[email data enrichment](#HT_chapter_data_enrichment_contacts_from_email_howto) 

 on the communication panel.
 




Fig. 3
 – How to enrich contact profile from the case page
 


![Enrich contact from case](/docs/sites/en/files/2020-12/scr_case_data_enrichment.png)




 If the case was registered based on an unknown email address of an existing contact, you can easily add the new address to the contact’s page directly from the case page. Click the
 
 Connect to an existing contact
 
 button and specify the contact to enrich (
 [Fig. 4](#XREF_65600_150_email)
 ).
 




Fig. 4
 – Adding an email address for an existing contact
 


![Add case to contact](/docs/sites/en/files/2020-12/scr_case_add_to_contact.png)




 Upon adding a new email address to the contact’s communication options, the email will be displayed on the
 
 Email
 
 detail on the contact’s page. Creatio will prompt you to select the contact as the main contact in the case.
 







 Receive contact information from Facebook
-----------------------------------------------



 Integration with Facebook allows you to maintain the information about contacts stored in the system.
 



 Run the
 
 Update with social networks data
 
 action to receive additional information about a contact. To run the action, specify the Facebook account on the
 
 Communication option
 
 detail of the contact page.
 


### 


 Connect a contact to its Facebook account


1. On the contact page, expand the
 
 Communication options
 
 detail and click
 
![btn_facebook_7_11.png](/docs/sites/default/files/documentation/user/ru/accounts_contacts/BPMonlineHelp/accounts_and_contacts_enrich_contact_data/btn_facebook_7_11.png)

 .
 



 Only one communication option with the “Facebook“ type can be added on the contact page.
 



 If you have not used Facebook integration before, the Facebook authorization window will open after you click
 
![btn_facebook_7_1100004.png](/docs/sites/default/files/documentation/user/ru/accounts_contacts/BPMonlineHelp/accounts_and_contacts_enrich_contact_data/btn_facebook_7_1100004.png)

 .
2. The displayed Facebook search page will contain public pages and profile pages of the contact if any. You can change the search criteria or enter the link to the page on Facebook if it is known.
 





 Note.
 
 If the link to the Facebook profile of the account does not have a numeric user ID, the profile will not be displayed among the results.
3. Select an account to add to the
 
 Communication option
 
 detail of the contact page (
 [Fig. 5](#XREF_97416_79)
 ).
 




Fig. 5
 – Selecting a contact account
 


![Enrich contact from facebook](/docs/sites/en/files/2020-12/faq_add_information_from_facebook_select_contact.png)





![faq_add_information_from_facebook_select_contact.png](/docs/sites/default/files/documentation/user/ru/accounts_contacts/BPMonlineHelp/accounts_and_contacts_enrich_contact_data/faq_add_information_from_facebook_select_contact.png)





 As a result, a new record with the “Facebook“ type will be added to the
 
 Communication options
 
 detail. If the account doesn't have a photo, it will be added to the Facebook page.
 



 If a contact has both a profile page and a public page on Facebook, we recommend using the public page to populate the
 
 Communication options
 
 detail. The public page provides more useful information about the contact.


### 


 Populate the contact page with Facebook information



 Let's review the example of populating the contact page with a photo from the Facebook page of the contact. Populating the contact page with data from the Facebook public page is described in the “
 
 Enrich the account data
 
 “ article.
 


1. On the contact page, expand the
 
 Communication option detail
 
 and make sure the contact is connected to the proper Facebook account.
2. Select the
 
 Update with social networks data
 
 option from the
 
 Actions
 
 menu (
 [Fig. 6](#XREF_36587_80)
 ).
 




Fig. 6
 – Selecting the
 
 Update with social networks data
 
 action
 


![Enrich from facebook action](/docs/sites/en/files/2020-12/faq_add_contact_information_from_facebook_act.png)





![faq_add_contact_information_from_facebook_act.png](/docs/sites/default/files/documentation/user/ru/accounts_contacts/BPMonlineHelp/accounts_and_contacts_enrich_contact_data/faq_add_contact_information_from_facebook_act.png)
3. On the displayed page, you can select a new contact photo and click the
 
 Save
 
 button.
 



 As a result, the contact photo on the contact page will be updated.


### 


 FAQ on populating the contact page with Facebook information


#### 
 Why searching by user page address on Facebook returns no results?



 In the Facebook social network, in addition to the profile page, a user can have a public page. Facebook public pages are visible to everyone, regardless of whether a viewer is a registered Facebook user or a Page fan.
 



 Due to changes in the
 
[Facebook privacy policy,](https://www.facebook.com/about/privacy) 

 searching for a user
 **profile** 
 by the unique page name is unavailable for third-party applications. If the link to the Facebook profile of the account does not have a numeric user ID, the profile will not be displayed among the search results. For example, search request “www.facebook.com/zuck” will return no results, while searching for “https://www.facebook.com/4” will return Mark Zuckerberg’s page.
 



 Searching for
 **public pages** 
 has not changed, they can be found using direct links of any type.
 


#### 
 Why aren’t some of the existing pages displayed among the results of the search by Facebook user name and last name?



 Facebook search data is provided through the Facebook API. If a Facebook user restricted indexing of their page by search systems, this user’s data will not be found by Creatio.
 



 To search for personal pages via third-party applications, a user must permit tho show their profile in search results (
 [Fig. 7](#XREF_36836_157__Facebook)
 ).
 




Fig. 7
 – Facebook privacy settings page
 


![Facebook privacy settings](/docs/sites/en/files/2020-12/specs_contacts_facebook_profile_security_settings.png)



#### 
 Why does the
 
 Update with social networks data
 
 action result in a different number of fields updated for different contact records?



 Due to changes in the
 
[Facebook privacy policies,](https://www.facebook.com/about/privacy) 

 third-party applications can only obtain a limited amount of information from personal user pages. If a contact has both a profile page and a public page, it is recommended to add the public page to the
 
 Communication options
 
 detail because the public page contains more information about the contact.
 


#### 
 Why the field for entering Facebook address becomes inactive after a Facebook profile has been added?



 When adding a new Facebook profile link, the field becomes unavailable for editing because Facebook API generates an individual link for every contact.
 


#### 
 How to obtain access to the Facebook page of the contact if it is protected by privacy settings?



 If the Facebook personal page of the contact is protected by privacy settings, the contact data cannot be enriched from this page. This is due to
 
[Facebook's privacy policies](https://www.facebook.com/about/privacy) 

 . To quickly switch from Creatio to contact data on Facebook, add a link to the user profile on the contact page as a communication option of the “Web” type. This link can be obtained from the
 
enrichment of contacts from the incoming emails

 if the contact has links for profiles in social networks in the signature or after the search on Facebook.
 




