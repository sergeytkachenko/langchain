


 Since version 7.18.3, you can use the “Searching and creating contact” business process to identify contacts that submit forms on newly-created landing pages that involve contact creation.
 



 Default contact identification mechanism
------------------------------------------



 The process searches for matching contact details in the form submission by applying a set of the following rules, from higher to lower priority:
 


1. Search by
 
 Full name
 
 and
 
 Email
 
 and
 
 Phone number
 
 fields.
2. Search by
 
 Email
 
 and
 
 Phone number
 
 fields.
3. Search by
 
 Full name
 
 and
 
 Phone number
 
 fields.
4. Search by
 
 Email
 
 field.



 If the lowest-priority rule yields no results, a new contact is created.
 



 If the process identifies the contact yet the submission includes a new email or phone number, Creatio will add the new communication option to the
 
 Communication options
 
 contact detail and mark the option as valid. Creatio will update the communication options of the earliest-created contact if it finds duplicate contacts.
 



 The process matches phone numbers as sets of digits without any additional characters. Full names are matched completely, both as combinations of first, middle, and last names and verbatim. Emails are matched verbatim.
 



 Customize the contact identification mechanism
------------------------------------------------



 By default, Creatio uses the “Searching and creating contact” business process on all landing pages that involve contact creation. To customize the contact identification mechanism, edit the “Searching and creating contact” business process. Alternatively, use a different process for all or specific landing pages. To do this:
 


1. Create a
 [business process](https://academy.creatio.com/documents?id=7168) 
 that has custom contact identification mechanism.
2. Add the process to the
 
 Web form contact identification process
 
[lookup](https://academy.creatio.com/documents?id=271) 
 .
3. Go to the
 
 Landing pages and web forms
 
 section → the relevant landing page record.
4. Select the process in the
 
 Contact search process
 
 field.
5. Click
 
 Save
 
 .
6. Repeat steps 3-5 for other relevant landing pages.




 Fig. 1 Select a custom contact identification process
 


![scr_custom_contact_identification_process.png](/docs/sites/en/files/images/CRM_Tools/contact_identification_mechanism/scr_custom_contact_identification_process.png)




 Update the contact identification mechanism
---------------------------------------------



 The default and custom contact identification mechanisms of landing pages set up in the earlier Creatio versions remain unchanged. To update them:
 


1. Customize the existing
 [contact identification mechanism](#title-2190-2) 
 , if needed.
2. Go to the
 
 Landing pages and web forms
 
 section → the relevant landing page record.
3. Select the relevant contact identification process in the
 
 Contact search process
 
 field.
4. Replace the code snippet embedded into the landing page with the snippet in the
 
 STEP 2. Copy the code and configure and map the fields
 
 block on the
 
 Landing page setup
 
 tab.
 



 If the form contains fields not specified in the new snippet, perform additional setup:
 


	1. Expand the snippet with additional field mappings. Learn more in a separate article:
	 [Connect your website landing page to Creatio](https://academy.creatio.com/documents?id=1628&anchor=title-2628-2) 
	 .
	2. Add the corresponding columns to the
	 
	 Web form data
	 
	 table.
5. Click
 
 Save
 
 on the section record page.




