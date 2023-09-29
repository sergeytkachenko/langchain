


 After you
 [publish landing pages](https://academy.creatio.com/documents?id=1966) 
 on your website, take the following steps:
 


1. Add a
 [new record](#title-2263-1) 
 in the
 
 Landing pages and web forms
 
 section.
2. Set up a page to
 [redirect customers](#title-2263-12) 
 .
3. Modify the generated
 [unique HTML code](#title-2263-2) 
 .
4. Set up lookup and custom field
 [mapping](#title-2263-7) 
 .
5. Add the modified HTML code to the
 [code](#title-2263-10) 
 of the website landing page.
6. Set up the
 [automatic population](https://academy.creatio.com/documents?id=1523) 
 of lead (or other Creatio object) fields that the customers do not fill out.





 Note.
 
 We recommend the website developer to set up landing pages.
 






 Attention.
 
 Creatio supports integration with CMS that let you add custom HTML and JavaScript code. You need an additional connector to integrate with other CMS, such as WordPress. Learn more in the
 [Creatio Community](https://community.creatio.com/) 
 and
 [Creatio Marketplace](https://marketplace.creatio.com/) 
 websites.
 




 Add a new record in the [Landing pages and web forms] section
---------------------------------------------------------------


1. Open the
 
 Landing pages and web forms
 
 section. Click
 
 New
 
 and select the type of landing page integration (Fig. 1). For example, lead registration form. This opens a new page.
 




 Fig. 1 Create a new landing page
 

![scr_landings_new_landing.png](/docs/sites/en/files/images/CRM_Tools/connect_your_website_landing_page_to_creatio/scr_landings_new_landing.png)
2. Fill out the fields on the page that opens:
 


	1. Specify your landing page name in Creatio in the
	 
	 Name
	 
	 field.
	2. Specify your landing page URL in the
	 
	 Website domains
	 
	 field. You can specify one or more URLs separated by commas. If you add “\*” to the end of the URL, Creatio records every contact and lead registered on the domain, not only on a specific page.
	 
	
	
	
	
	 Fig. 2 Landing page fields
	 
	
	![scr_landings_fillings.png](/docs/sites/en/files/images/CRM_Tools/connect_your_website_landing_page_to_creatio/scr_landings_fillings.png)
	3. Specify additional information about the landing page in the
	 
	 Description
	 
	 field.
	4. Select the
	 
	 Create contact
	 
	 checkbox to enable the automatic creation of both a lead and a contact when a user submits the form.
	5. Select the business process that identifies Creatio contacts that submit forms in the
	 
	 Contact search process
	 
	 field. You can use the existing “Searching and creating contact for web form” business process or specify a custom process. Learn more about the contact identification mechanism in a separate article:
	 [Identify contacts that submit web forms](https://academy.creatio.com/documents?id=2371) 
	 .
	6. Specify the URL to open for the user after the form submission in the
	 
	 Redirection URL
	 
	 field.
3. Click
 
 Save
 
 .



 Set up a page to redirect customers
-------------------------------------



 You can configure Creatio settings so that your site visitor is automatically redirected to a certain page right after submitting the web form. For example, to the Thank You page. To do that, open the
 
 Landing setup
 
 tab and enter the redirection page URL in the
 
 Redirection URL
 
 field. For example, http://mysite.com/submit/thank-you-page. As a result, the HTML code embedded into your landing page will use the specified URL for redirection. For example:
 



 redirectUrl: “http://mysite.com/submit/thank-you-page”
 





 Attention.
 
 Configure the redirection page settings prior to copying the HTML code from Creatio to your website landing page. If the landing page redirection is already set up on your website, you can leave the
 
 Redirection URL
 
 field blank.
 




 Edit the unique HTML code
---------------------------





 Attention.
 
 This article covers the process of editing HTML code for a lead registration form.
 




 To ensure the the fields of a lead record added automatically after a registration on the landing page are populated correctly, edit the unique HTML code and add the edited code to the landing page code.
 



 The list of lead page fields that are populated upon a registration on a landing page is located in the “fields” block of the HTML code. Match these fields to the web form fields. View an example of the “fields” block in the HTML code below.
 






```

fields: {

"Name": "css-selector", // Name of a visitor, submitting the page

"Email": "css-selector", // Visitor's email

"Zip": "css-selector", // Visitor's ZIP code

"MobilePhone": "css-selector", // Visitor's phone number

"Company": "css-selector", // Name of a company (for business landing pages)

"Industry": "css-selector", // Company industry (for business landing pages)

"FullJobTitle": "css-selector", // Visitor's job title (for business landing pages)

"UseEmail": "css-selector" // Logical value: 'true' equals to visitor's opt-in to receive emails 
}
```





 To ensure the lead is registered correctly, add at least one field from the “contactFields” block to the HTML code. View an example of the block below.
 






```

contactFields: {
        "FullName": "css-selector", // Name of a contact
        "Phone": "css-selector", // Contact's mobile phone
        "Email": "css-selector" // Contact's email
}
```




### 
 Select fields to map to a lead record



 You can set up mapping for both standard lead fields and custom fields. Learn more about setting up field mapping for lookups and custom fields in a different section:
 [Set up lookup and custom field mapping](#title-2263-7) 
 .
 



 See the values of standard fields from the HTML code and corresponding lead page fields below:
 


* “Name” →
 
 Contact full name
 
 .
* “Email” →
 
 Email
 
 .
* “Zip” →
 
 ZIP code
 
 .
* “MobilePhone” →
 
 Mobile phone
 
 .
* “Company” →
 
 Account name
 
 .
* “Industry” →
 
 Industry
 
 .
* “FullJobTitle” →
 
 Job title
 
 .
* “EventId” →
 
 Event
 
 . If you specify the unique event ID in the page code, the ID takes priority over the default values in the landing page records.
* “UseEmail” → whether the customer agreed to receive promotional materials.



 You can delete the fields the web form does not use from the HTML code.
 


### 
 Match the web form fields to the lead record fields



 To fill out the lead page, replace the “css-selector” expression with the ID or class of the corresponding field of the landing page form.
 


1. Copy the unique HTML code to any text editor.
2. Replace the “css-selector” text in the code with the corresponding selector name from the code of the landing page on your website. The procedure for viewing source code might be different in different browsers. See an example that sets up the population of the
 
 Full name
 
 field in Google Chrome below.
	1. Go to the landing page and open the source code (Fig. 3).
	 
	
	 Fig. 3 Landing page source code
	 
	
	![scr_landings_page_with_code.png](/docs/sites/en/files/images/CRM_Tools/connect_your_website_landing_page_to_creatio/scr_landings_page_with_code.png)
	2. Click the
	 ![btn_lendings_code.png](/docs/sites/en/files/images/CRM_Tools/connect_your_website_landing_page_to_creatio/btn_lendings_code.png)
	 icon in the source code area (Fig. 4).
	 
	
	 Fig. 4 Select a code item on the page
	 
	
	![scr_landings_choose_element.png](/docs/sites/en/files/images/CRM_Tools/connect_your_website_landing_page_to_creatio/scr_landings_choose_element.png)
	3. Click the
	 
	 Full name
	 
	 field on the landing page (Fig. 5).
	 
	
	 Fig. 5 Select an item to view code
	 
	
	![scr_landings_choose_field.png](/docs/sites/en/files/images/CRM_Tools/connect_your_website_landing_page_to_creatio/scr_landings_choose_field.png)
	
	
	
	 The code of the selected field is highlighted in the source code area of the page (Fig. 6).
	 
	
	
	
	
	 Fig. 6 Highlighted code fragment that corresponds to the
	 
	 Full name
	 
	 field
	 
	
	![scr_landings_code_fragment.png](/docs/sites/en/files/images/CRM_Tools/connect_your_website_landing_page_to_creatio/scr_landings_code_fragment.png)
	4. Copy the value that is contained in the “id” parameter of the source code (Fig. 7).
	 
	
	 Fig. 7 Copy the “id” value from the source code
	 
	
	![scr_landings_copy_id.png](/docs/sites/en/files/images/CRM_Tools/connect_your_website_landing_page_to_creatio/scr_landings_copy_id.png)
	5. Replace the “css-selector” in the
	 
	 Name
	 
	 value of the source code:
	 
	
	
	
	```
	
	fields: {
	
	"Name": "#edit-ts-form-name", // Name of a visitor, submitting the page
	
	"Email": "css-selector", // Visitor's email
	
	"Zip": "css-selector", // Visitor's ZIP code 
	}
	```
	
	
	
	
	
	
	
	 Attention.
	 
	 You can use the “id” or “class” values to replace the “css-selector” parameters of the landing page fields. If you use the “id” value, put the “#” character before it when editing the HTML code. For example, #edit-ts-form-name.
3. Replace “css-selector” for the remaining fields in the same manner.
 





 Note.
 
 Delete any fields you do not use on the landing page from the generated HTML code.


### 
 Recommendations on field mapping setup


* You can map one web form field to several fields in Creatio. For example, Creatio can use the value the customer specifies in the “Name” field of your form to populate the
 
 Name
 
 (of the contact) and
 
 Name
 
 (of the account) fields of the lead page.
* You can map one field of a lead page in Creatio to only one field of your web form. We do not recommend mapping two fields of your form to one lead page field. In that case, one of the values overwrites the other.
* We recommend mapping the fields of the same type and format. However, if a lookup field contains the value the customer entered in the field of a different format, Creatio populates the lookup field. For example, if your form contains a “Country” text field and the customer enters “USA,” which matches a lookup value in the countries lookup, Creatio populates the
 
 Country
 
 lookup field on the lead page with that value. Also, Creatio includes additional input logic for
 
 Country
 
 ,
 
 State/province
 
 and
 
 City
 
 fields. If Creatio cannot find the values the customer enters in these fields, the values are saved to additional text fields of the lead object.
* We recommend passing the unique code to the lead page when managing lookup fields, since a name cannot identify a record and is not a unique key in the Creatio database. If a user has a different UI language (culture) configured, passing the name leads to creating another record, likely to be a duplicate.
* Use radio buttons and drop-down lists that have unique ID values as interactive UI elements for localizable lookups. Learn more in a different section:
 [Set up lookup and custom field mapping](#title-2263-7) 
 .
* We recommend passing data in a format that specifies the time zone when mapping date/time fields (“DATETIME” data type). For example, use the 4/12/2008 9:30:00 AM -01:00 format to pass data for the UTC-1 time zone, and use the 4/12/2008 9:30:00 AM +00:00 format to pass data for the UTC time zone.



 Once you set up the mapping,
 [add the modified HTML code](#title-2263-10) 
 to the landing page code.
 



 Set up lookup and custom field mapping
----------------------------------------



 Landing page web forms can use non-standard fields, such as radio buttons or drop-down lists that contain lookup records.
 





 Attention.
 
 The settings below are performed by the website administrator and cover the lead registration form.
 



### 
 Pass the radio button values


1. Add a hidden field to the HTML markup of the landing page. The field can have a custom ID:
 






```

<input type="hidden" id=" idOfRadiobutton" />
```
2. Map the lead field to the new hidden field in the “fields” block of the landing page code:
 






```

"UsrField": "#idOfRadiobutton"
```
3. Pass the value selected using a radio button to the hidden field created earlier. Add an expression that contains this value to the landing page code before the fragment that calls the create lead function (createLead):
 






```

var idOfRadiobutton = $('inputname=name\_of\_your\_radiobutton:checked').val();
```
4. Save the changes.


#### 
 Pass the drop-down list values


1. Add a hidden field to the HTML markup of the landing page. The field can have a custom ID:
 






```

<input type="hidden" id="fieldId" />
```
2. Map the lead field to the hidden field in the “fields” block of the landing page code:
 






```

"UsrField": "#fieldId"
```
3. Calculate and pass the value selected in the field to the hidden field before calling the lead creation function. Add an expression that contains this value to the landing page code before the fragment that calls the create lead function (createLead):
 






```

var fieldId = $("#name_of_dropdown option:selected").text();
```








```

$("#fieldId").val(fieldId); 
```
4. Save the changes.



 As a result, the data entered on the web form via the radio button and drop-down lists will be passed to the Creatio lead page.
 



 Add the modified HTML code to the landing page source code
------------------------------------------------------------





 Attention.
 
 This article covers the process of editing HTML code for a lead registration form.
 




 After you edit the generated HTML code, add it to the code of the landing page on your website. To do this:
 


1. Copy the entire code that you
 [modified earlier](#title-2263-2) 
 to the clipboard.
2. Place the source code on the landing page:
	1. Go to the location of the landing page file on the server (Fig 8).
	 
	
	 Fig. 8 Location of the landing page on the server
	 
	
	![scr_landings_server.png](/docs/sites/en/files/images/CRM_Tools/connect_your_website_landing_page_to_creatio/scr_landings_server.png)
	2. Open the landing page in a text editor.
	3. Paste the generated HTML code to the source code of the landing page, for example, before the closing </body> tag (Fig. 9).
	 
	
	
	
	
	 Fig. 9 Embed the generated HTML code into the source code of the landing page
	 
	
	![scr_landings_edit_code_notepad+.png](/docs/sites/en/files/images/CRM_Tools/connect_your_website_landing_page_to_creatio/scr_landings_edit_code_notepad+.png)
	4. Save the changes.
3. Add the event that launches the CreateLead() function to the landing page code. To do this, use the following code: onSubmit="createLead(); return false". To place an event in the source code of the landing page:
 


	1. Go to the “form action” tag in the source code:
	 
	
	
	
	
	
	
	```
	
	<span class="registration">Webinar registration</span>
	
	           
	
	           <form action="/webinar-creatio-7-6" method="post" id="ts-form-universal-form" accept-charset="UTF-8">
	```
	2. Add onSubmit="createLead(); return false" code to the opening <form> tag. For example:
	 
	
	
	
	
	
	
	```
	
	<span class="registration">Webinar registration</span>
	
	<form action="/webinar-creatio-7-6" method="post" id="ts-form-universal-form" accept-charset="UTF-8" onSubmit=”createLead(); return false”>
	```
	3. Save the changes.



 After you connect the landing page to Creatio, proceed to
 [set up automatic page field population](https://academy.creatio.com/documents?id=1523) 
 for leads created via landing pages.
 




