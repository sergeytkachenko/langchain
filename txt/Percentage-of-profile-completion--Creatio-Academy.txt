


 In Creatio, you can monitor the percentage of profile data completeness for contacts and accounts, as well as track process flow using convenient visual tools. Configure how the percentage of data is calculated taking into account the nature of your business. The system will ask you to fill in the missing data for each account, contact, or opportunity page.
 



 The system allows you to set up complete data analytics and view information grouped by owners.
 



 Analyze profile data
----------------------



 The indicator on an account, contact, or opportunity page displays the percentage of profile data that is complete (Fig. 1). The profile data complete indicator is located at the top left corner of a user page.
 




 Fig. 1 – Contact page data indicator
 

![Contact profile](/docs/sites/en/files/2020-12/specs_contacts_profile.png)







 Note.
 
 The profile completeness indicator is recalculated upon opening the contact or account page and when saving or changing the recalculation rules in the lookup. To update the percentage in bulk, for example, after
 [importing data](https://academy.creatio.com/documents?product=base&ver=7&id=1252) 
 from Excel, run the
 
 Update the profile data population
 
 business process.
 




 The unsatisfactory data percentage is marked red on the indicator, the satisfactory data percentage is marked yellow and the complete data percentage is of green color.
 



 The indicator also shows the total percentage of data completeness. The indicator readings will depend on how many fields are filled in on a page. You can modify how each value item on a page will contribute to the calculation of profile data complete. For example, you can set up the calculation so that filling in the "Role" field on a contact page will add 10% to the percentage of the profile data complete.
 



 Click the indicator to view a hint about how many fields or details should be filled in to increase the percentage displayed. If there are several unfilled items, they will be displayed in the descending order of the percentage that they add to the indicator when filled in (Fig. 2).
 




 Fig. 2 – Hints about completing a contact page profile
 

![Contact profile hint](/docs/sites/en/files/2020-12/specs_contacts_profile_hint.png)





 Complete data calculation settings
------------------------------------



 Creatio allows you to customize the parameters used for the calculation of the profile data. You can set up the scale to be displayed on a contact, account, or opportunity page.
 



 The data complete calculation can be customized for the
 
 Contacts
 
 ,
 
 Accounts
 
 , and
 
 Opportunities
 
 sections. The customization process is similar for all these sections.
 



 To set up the data complete calculation for contacts or opportunities:
 


1. Open the System Designer by clicking
 
![btn_system_designer.png](/docs/sites/default/files/2020-11/btn_system_designer.png)

 in the top right corner of the application.
2. Click the
 
 Lookups
 
 link in the
 
 System setup
 
 block.
 


 Note.
 
 You can set up access rights to this action using the
 
 Access to “Lookups“ section
 
[system operation](https://academy.creatio.com/documents?product=administration&ver=7&id=258) 
 .
3. Select the
 
 Data entry compliance
 
 lookup in the list Select the lookup record and click the
 
 Open content
 
 button.
4. On the opened page, select the section for which you want to configure the data complete calculation:
 
 Contacts
 
 ,
 
 Accounts
 
 , or
 
 Opportunities
 
 .
5. For example, let's configure the data complete calculation settings for contacts. To do this, select the
 
 Contacts
 
 record in the list and click
 
 Open
 
 .
6. On the opened page, set up the scale and the parameters of the indicator.


### 
 Set up the indicator scale



 The incomplete data percentage is marked red on the indicator, the satisfactory data percentage is marked yellow and the complete data percentage is of green color (Fig. 3).
   

 To set up the profile data complete indicator, map the value ranges to incomplete, satisfactory, and complete profile data. To do this:
 


1. Specify the upper limit of the range that maps to the incomplete profile data. This is the lowest possible value that is satisfactory. By default, it is set to “50%.”
2. Specify the upper limit of the range for the satisfactory level of the profile data complete. This value will also serve as the lower limit for the “complete” level. For example, enter “80%.“




 Fig. 3 – Profile data complete indicator
 

![Contact profile scale](/docs/sites/en/files/2020-12/specs_contacts_profile_data_scale_b.png)





 The lower limit of the incomplete data range is non-editable and always equals "0%". Similarly, the upper limit of the complete data range is non-editable and always equals "100%."
 


### 
 Set up indicator attributes



 You can set up the indicator attributes to define how different types of entered profile data impact the profile completion percentage. For example, you can change the settings so that entering information about the contact's company will add 15% to the profile data completion.
   

 To do this:
 


1. Go to the
 
 Attributes
 
 detail toolbar and click the
 
![btn_chapter_mobile_wizard_new_role.png](/docs/sites/default/files/2020-11/btn_chapter_mobile_wizard_new_role.png)

 button.
 


 Note.
 
 The total percentage of the data complete attributes must equal 100%. You can add a new attribute only if the total percentage of the already added attributes is less than 100%.
2. Select the required attribute from the drop-down menu. An attribute can be:
	1. A field value on a page. For example, the contact role.
	   
	
	 Numeric fields are considered filled in if they contain any value other than 0.
	2. Information on connected tabs. For example, calls connected to a contact.
	   
	
	 The
	 
	 Activities
	 
	 detail displays the connected "Task" type activities only.
	3. Values for different types of detail fields.
	   
	
	 The
	 
	 Addresses
	 
	 and
	 
	 Communication options
	 
	 tabs of contacts and accounts have different types of values to be filled in their fields. Each address type (legal, postal, etc.) and each communication option (mobile phone, email, etc.) is considered a separate attribute.
3. Specify the percentage that the attribute adds to the profile completion indicator. For example, you can set up the calculation so that specifying a mobile phone number for a contact will make the profile data 25% more complete. You can configure other attributes in the same manner. When you add a new attribute to the
 
 Data population percentage
 
 column, the maximum possible value is set by default.



 When you finish the setup process, save the changes made to the
 
 Data entry compliance
 
 lookup. All indicators displaying the profile data complete are updated automatically.
 




