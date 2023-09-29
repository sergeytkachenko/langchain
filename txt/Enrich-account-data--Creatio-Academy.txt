


 Creatio helps to maintain the completeness and relevance of the customer base using the data enrichment feature.
 



 Add the contact information of an account to Creatio from open sources in a few clicks, and enrich the account data using their social profiles.
 





 Attention.
 
 To enable data enrichment from correspondence and open sources, Creatio on-site users will need to specify a cloud service key in the
 [corresponding system setting](https://academy.creatio.com/documents?product=administration&ver=7&id=1642) 
 – “Enable Email Mining” (EnableEmailMining).
 




 Profile enrichment includes:
 


* Adding the company website address and logo on a new account page. This function is performed if you select one of the suggested company names from the drop-down list when filling out the
 
 Name
 
 field of a new account record.
* Adding communication options to an account page: phone numbers, email addresses, and social network profile. This is performed automatically when you run the
 
 Enrich data
 
 action.
* Adding information from the social network public pages to an account page. Performed by the
 
 Update with social networks data
 
 action.


### 
 Enrich the account data from the open Internet sources



 Use the
 
 Enrich data
 
 action to run an automatic search for account information. To run the search, click
 






![btn_account_data_enrichment.png](/docs/sites/default/files/2020-11/btn_account_data_enrichment.png)





 on the record profile
 



 To access the data enrichment function, you need to have permission for the
 
 Can enrich account data
 
 system operation.
 



 Before running the data enrichment, make sure that the account profile contains at least the company name and website address.
 



 As a result, Creatio will search open sources for the following account data:
 


* email addresses
* phone numbers
* account profiles on Twitter, LinkedIn, Google+, Youtube, Instagram, SlideShare, and Pinterest social networks.



 When the search is complete, a window with a list of found communication options will open (Fig. 1).
 




 Fig. 1 – Data enrichment window
 



![Account enrichment search window](/docs/sites/en/files/2020-12/scr_account_data_enrichment_search_window.png)







 You can edit the communication options in this window. Select records that must be added to the account page and click
 
 Add
 
 . The data will be saved on the account page:
 


* email addresses will be saved as “Email” communication options
* phone numbers will be saved as “Primary phone” communication options
* Facebook profile pages will be saved as “Facebook” communication options
* Twitter profile pages will be saved as “Twitter” communication options
* LinkedIn, Google+, Youtube, Instagram, SlideShare, Pinterest profile pages will be saved as “Web” communication options.



 To run the search again, click
 






![btn_account_data_enrichment_refresh.png](/docs/sites/default/files/2020-11/btn_account_data_enrichment_refresh.png)





 in the search window. You can change the number of displayed communication options for each type.
 


### 
 Account data enrichment from the open Internet sources FAQ


#### 
 Data enrichment cannot find account information. Why?



 Data enrichment function searches account information in open sources. The list of the sources is confidential. If the search does not return any account information, please try the following:
 


* Ensure that the data enrichment function is properly
 [configured](https://academy.creatio.com/documents?product=administration&ver=7&id=1642) 
 in your Creatio.
* Ensure that the account name matches the corresponding company name.
* Add at least one company website in the
 
 Web
 
 field of the account page. Ensure that the specified website address is correct.
* Specify the company email.
* Check the
 
 Social links enrichment limit
 
 ,
 
 Phone number enrichment limit,
 
 and
 
 Email enrichment limit
 
 system settings. Their values must not be “0.”



 If the problem persists, the following may be the case:
 


* There is no information about the company in the open sources, or Creatio could not find the company based on the entered data. Please contact Creatio support and send a list of companies that cannot be found. We will use this information to improve the data enrichment function.
* Creatio was unable to find new information. All information obtained through data enrichment is already available in the account profile.



 New Creatio versions will use more sources and better search algorithms for data enrichment.
 


#### 
 Why does the list of found data contain invalid values?



 Creatio searches information in unstructured data from open sources using AI-like algorithms that can process unclear data. As a result, the data enrichment window may contain invalid communication options. We recommend reviewing the data enrichment results before saving them in the account profile.
 



 The data search and recognition algorithms will be perfected with each Creatio update.
 


#### 
 How do I limit the number of records in the data enrichment window?



 Open sources may contain dozens of communication options for certain companies, such as emails from different departments, branches, and offices. Use the following system settings to limit the number of different types of communication options displayed in the data enrichment window:
 


* Social links enrichment limit
* Phone number enrichment limit
* Email enrichment limit



 By default, each limit is set to “10.”
 



 To change the limit:
 


1. In the system designer, open the
 
 System settings
 
 section.
2. Go to the
 
 Creatio cloud services
 
 →
 
 Data enrichment
 
 folder and open the needed system setting.
3. In the
 
 Default value
 
 field, enter the maximum number of communication options to display in the data enrichment window.



 As a result, Creatio will limit the number of communication options of this type displayed in the data enrichment window.
 



 Receive account information from Facebook
-------------------------------------------



 Integration with Facebook allows you to maintain the information about accounts stored in the system.
 



 Run the
 
 Update with social networks data
 
 action to receive additional information about an account. To run the action, specify the Facebook account on the
 
 Communication option
 
 detail of the Creatio account page.
 


### 
 Connect an account to its Facebook profile


1. On the account page, expand the
 
 Communication options
 
 detail and click the
 



![btn_facebook_7_11.png](/docs/sites/default/files/2020-11/btn_facebook_7_11.png)




 button.
2. If you have not used Facebook integration before, the Facebook authorization window will open after you click the
 



![btn_facebook_7_11.png](/docs/sites/default/files/2020-11/btn_facebook_7_11.png)




 button.
3. To add one more communication option with the “Facebook“ type to the existing ones, click
 
 Add
 
 →
 
 Social networks
 
 →
 
 Facebook
 
 .
4. The displayed Facebook page will contain a list of public pages that meet the search criteria. You can change the search criteria or enter the link to the account page on Facebook if it is known.
5. Select Facebook accounts to add to the detail (Fig. 2).
 

 Fig. 2 – Selecting the public pages of a Creatio account
 



![Enrich account from facebook](/docs/sites/en/files/2020-12/faq_add_information_from_facebook_select_account.png)



 As a result, a new record with the “Facebook“ type will be added to the
 
 Communication options
 
 detail.
 


### 
 Populate the account page with Facebook information


1. On the account page, expand the
 
 Communication option
 
 detail. Make sure that the detail contains the needed Facebook pages of the account.
2. Select the
 
 Update with social networks data
 
 option from the
 
 Actions
 
 menu (Fig. 3).
 

 Fig. 3 – Selecting the
 
 Update with social networks data
 
 action
 



![Enrich account from facebook action](/docs/sites/en/files/2020-12/faq_add_information_from_facebook_act.png)







 The displayed page will contain the account data stored in Creatio and the information from all Facebook public pages that are specified on the
 
 Communication options
 
 detail of the account page.
3. Analyze and select the data to add to the existing account information:
	1. On the
	 
	 Communication options
	 
	 detail, select the communication options to be saved in Creatio. To add a phone number, specify its type, for example, “Primary phone“ or “Extension number“ (Fig. 4).
	 
	
	 Fig. 4 – Selecting a communication option type
	 
	
	
	
	![Set account communication from facebook](/docs/sites/en/files/2020-12/faq_add_information_from_facebook_set_communication.png)
	2. On the
	 
	 Address
	 
	 detail, enter the value in the
	 
	 Address type
	 
	 field. If necessary, edit the following fields:
	 
	 City
	 
	 ,
	 
	 State/province,
	 
	 and
	 
	 Country
	 
	 (Fig.5). Select the addresses to be saved in Creatio.
	 
	
	
	
	
	 Fig. 5 – Selecting an address type
	 
	
	
	
	![FAQ. Add address from facebook](/docs/sites/en/files/2020-12/faq_add_information_from_facebook_set_address.png)
4. Edit the information on the
 
 Noteworthy events
 
 detail by specifying the event type, for example, “Company foundation day.“
5. If necessary, edit the
 
 Notes
 
 detail.
6. After you edit and save all the needed data from Facebook, click the
 
 Save
 
 button on the page.
   

 As a result, the information will be added to the corresponding page details.
 


 Attention.
 
 On the population page, if you deselect the information that has been previously added to Creatio, this information will be deleted from the account page after the data population is completed and the changes are saved.


### 
 Fields completed in Creatio from a Facebook page



 Let's review the list of fields that can be filled in in Creatio based on the data from Facebook. Fields of the public page that can be mapped to the Creatio fields are located on the
 
 About
 
 tab of the Facebook public page and are described below.
 





| 
 Facebook field
  | 
 Creatio field
  |
| --- | --- |
| 
 Website
  | 
 The website is saved on the
 
 Communication options
 
 detail.
  |
| 
 Phone
  | 
 To save a phone number, in Creatio, specify its type, for example, “Business phone“ or “Mobile phone.“ Saved on the
 
 Communication options
 
 detail.
  |
| 
 Email
  | 
 Email. Saved on the
 
 Communication options
 
 detail.
  |
| 
 Start Date
  | 
 The start date is saved on the
 
 Noteworthy events
 
 detail.
  |
| 
 Address
  | 
 The address. is saved on the
 
 Addresses
 
 detail.
  |
| 
 Short Description
  | 
 Notes are saved on the
 
 Attachments and notes
 
 in detail.
  |









