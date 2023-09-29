


 What is the purpose of the
 
 Landing pages and web forms
 
 section in Creatio?
----------------------------------------------------------------------------------



 The
 
 Landing pages and web forms
 
 section is used to set up integration between Creatio and web forms on your websites. As a result, each time an integrated web form is submitted, a new record is automatically created in Creatio using data from the submitted form. Landing page integration can be used for generating leads, adding customers to event participants, automatic order registration, and more.
 



 The
 
 Landing pages and web forms
 
 section is used for setting up connections between landing pages on your website and Creatio. In the
 
 Landing pages and web forms
 
 section a landing page record must be created that contains basic information about the landing page and a unique HTML code that must be integrated into the HTML code of the landing page.
 



 After performing these settings, the data entered in the web form of the landing page, such as full name, email, phone, will be passed to Creatio and used to add a new record (for example a new lead) in Creatio.
 



 What are the difference between a landing page on the website and a Creatio landing page record?
--------------------------------------------------------------------------------------------------



 When setting up a landing page two main entities must be differentiated:
 


* A landing page on the website.
* A landing page record in the
 
 Landing pages and web forms
 
 section of Creatio. A landing page record contains information on the actual landing page, for example, its name, link, etc. These records are used to set up connections between a landing page on a website and Creatio.



 An actual landing page and the corresponding landing page record in the
 
 Landing pages and web forms
 
 section have their own HTML code used to connect the two entities. The unique code of a landing page record is integrated into the HTML code of an actual landing page on a website.
 



 What does the landing page code do?
-------------------------------------



 The HTML code of a landing page is required to automatically create a new record in the system if a web form on the landing page is filled in. This code is used for setting up the data transfer between a landing page on a website to Creatio. Initially, the code fragment is set up for a specific landing page and then integrated into the HTML code of the landing page. Learn more about managing the landing page HTML code in a separate article:
 [Connect your website landing page to Creatio](https://academy.creatio.com/documents?id=1083) 
 .
 



 How do I use the
 
 Website domains
 
 field?
-----------------------------------------------



 Enter the actual landing page URL in the
 
 Website domains
 
 field.
 



 For example, the website name is www.example.com. This website has a landing page available at the following address: www.example.com/landing. This address must be entered in the
 
 Website domains
 
 field on the Creatio landing record page.
 





 Attention.
 
 The address entered in this field must match the address of the landing page where the HTML code was integrated.
 






 Note.
 
 In the
 
 Website domains
 
 field, specify all domains used to host the landing page. The domains must be separated with commas.
 




 How do I use the
 
 Redirection URL
 
 field?
-----------------------------------------------



 The
 
 Redirection URL
 
 field in the landing code determines the page where the user is redirected after filling out the landing page webform. You can specify the address of any page on your website. If your website settings specify a different action after filling out the landing page, leave this field empty.
 



 If you fill in the
 
 Redirection URL
 
 field for a new
 
 Landing pages and web forms
 
 section record, then the unique HTML code of this record will contain the link to the page specified in the
 
 Redirection URL
 
 field in the redirectUrl block.
 



 Thus, for the proper functioning of the landing page, fill out the landing page record fields, including
 
 Redirection URL
 
 and save the record, then connect the landing page record with the landing page. Learn more about managing the landing page HTML code in a separate article:
 [Connect your website landing page to Creatio](https://academy.creatio.com/documents?id=1083) 
 .
 



 How do you set up one landing page record for a page with several web forms?
------------------------------------------------------------------------------



 If your landing page has several web forms, you can use a single Creatio landing page record to connect to all of them.
 





 Attention.
 
 The settings below are performed by the website administrator.
 




 In the standard HTML code of the landing page record in Creatio, there is a “config,” block where field mapping between web forms and lead fields are set up. To set up a mapping between a lead record field and
 **several web forms** 
 , create several “config” blocks in the code, one for each actual web form. A separate createLead function must be set up for each “config” block.
 



 For example, your landing page has two web forms. The first form contains “Full name” and “Email” fields, and the other one contains “Full name” and “Mobile phone” fields. To use one landing for the landing page with two web forms, make the following changes to the code:
 


1. Copy the whole “config” block as many times as the number of web forms that you need to connect to the landing page record in Creatio.
2. Add unique names to the “config” blocks whose parameters are passed to the createLead function. For example “config1” and “config2.”
3. In the “config1” block, set up the mapping of the fields from the first web form:
 



```

Name: "#..." Email: "#..."
```
4. In the “config2” block, set up the mapping of the fields from the second webform:
 



```

Name: "#..." Phone: "#..."
```
5. Set up two createLead functions:
 






```

function createLead1() { landing.createLeadFromLanding(config1) } function createLead2() { landing.createLeadFromLanding(config2) }
```
6. For each web form, set up calling of a separate createLead function:
 






```

onsubmit="createLead1(); return false" onsubmit="createLead2(); return false"
```



 After this, a lead will be created in Creatio each time a user fills out any of the two web forms.
 



 How do I set up a single landing for several pages?
-----------------------------------------------------



 If several web forms with a similar structure are implemented in several pages within one domain, you can use a single landing page record for all of them. To do this, enter all needed URLs in the
 
 Website domains
 
 field, separating them with commas: https://www.creatio.com/trial?product=sales, https://www.creatio.com/trial?product=marketing
 



 As a result, when a web form is filled out on any of the website pages, where this landing page code is integrated, a new record (for example, lead) will be automatically created in Creatio.
 



 Why will Creatio not register leads despite the properly customized landing page?
-----------------------------------------------------------------------------------



 After you have created and
 [set up](https://academy.creatio.com/documents?id=1083) 
 a landing page, new records will be registered in Creatio when the landing page webform is filled in. If it doesn’t happen, perhaps one of the landing page fields (such as lead) is required but either not included in the web form, or not filled.
 



 In this case, you can:
 


* Clear the
 
 Required
 
 checkbox from the lead page fields (or the page fields of another Creatio object). Learn more about changing fields on edit pages in a separate article:
 [Set up page fields](https://academy.creatio.com/documents?id=1398) 
 .
* [Set up](https://academy.creatio.com/documents?id=1523) 
 the population of these fields with default values.



 How to set up the population of fields with default values for leads registered via a landing page?
-----------------------------------------------------------------------------------------------------



 The landing page webform can contain all the fields used by Creatio on the lead page. You can set up automatic population of individual fields with default values. Learn more about populating the lead fields with default values in a separate article:
 [Set up autofill for lead page fields](https://academy.creatio.com/documents?id=1523) 
 .
 



 How does Creatio search for contact duplicates while creating leads from landing pages?
-----------------------------------------------------------------------------------------



 As soon as your customer submits a web form on your landing page, Creatio automatically creates a new lead record based on the entered data. After this, the “Searching and creating contact” process starts automatically to check whether the new lead can be linked to an existing contact or if a new contact needs to be created. This helps Creatio to avoid creating contact duplicates when new leads are registered from landing pages. You can view or edit the “Searching and creating contact” process in the process library.
 





 Note.
 
 The “Searching and creating contact” process starts only if the
 
 Create contact
 
 checkbox is selected for the landing page.
 




 Learn more about the contact identification mechanism in a separate article:
 [Identify contacts that submit web forms](https://academy.creatio.com/documents?id=2371) 
 .
 



 How do I set up the correct population of lead creation time?
---------------------------------------------------------------



 A situation may occur an incorrect date was set in the
 
 Creation date
 
 when registering a lead via a landing page.
 



 To avoid this, we recommend you to check the time zone set on the server where Creatio is hosted. For the lead creation time to be set correctly, make sure that the time zone on the application server corresponds to your actual time zone.
 



 Can I configure the website event tracking for manually registered leads?
---------------------------------------------------------------------------



 You cannot configure the website event tracking for manually registered leads.
 



 The website event tracking is executed based on the history of the transitions through the website of a specific Internet user. During the tracking process, a certain session is recorded in the browser by using cookies. If a lead is created manually, no web-page visitor is connected to a web-browser session. Thus, the history of the website navigation of such a user cannot be tracked.
 



 If an internet user, having made several transitions through the pages, fills in the landing page web form of your website, the history of his transitions will be transferred to Creatio.
 





 Note.
 
 If a user clears the browser cookies before filling out the landing page web form, the history of his transitions will be removed and will not appear in Creatio.
 




 How do I configure data transfer from one landing page web form to separate lead page fields?
-----------------------------------------------------------------------------------------------



 There is the “config” block in the HTML code of the landing page. This block configures the mapping of landing page web form fields and lead fields. To set up the correspondence of one landing page webform field to multiple lead fields, you will need to add a hidden field to the HTML code of the landing page, set up the mapping, and then configure the createLead function.
 



 For example, a single “Name” field is implemented in the web form of your landing page. And Creatio lead page has two separate fields:
 
 First name
 
 and
 
 Last name
 
 .
 





 Attention.
 
 The settings below are performed by the website administrator.
 




 To populate the
 
 First name
 
 and
 
 Last name
 
 lead page fields correctly, make the following changes to the code:
 


1. Add two hidden fields to the HTML markup:
 






```

<input type="hidden" id="selectedNameCaption" /> <input type="hidden" id="selectedSecondNameCaption" />
```
2. Set up the mapping of the hidden fields in the “config” block:
 






```

"Name": "#selectedNameCaption" "SecondName": "#selectedSecondNameCaption"
```
3. Before calling the function to create a lead, add a function, which describes the logic of the
 
 Name
 
 and
 
 Surname
 
 fields taking the value from the
 
 Name
 
 field.




