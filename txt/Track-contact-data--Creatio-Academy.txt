


 Gain insights into the online behavior of contacts by using their form submission data or tracking data imported from a web analytics service. For example, discover the source that led the contact to your website or products that interest them the most. View this data on the
 
 Engagement
 
 tab of the contact page.
 



 You can also gain insights into the behavior of leads after you qualify a lead. The qualification creates a new contact whose data you can track similarly to any other contact
 



 We recommend using Matomo tracking service that has a connector available on the Marketplace:
 [Matomo connector for Creatio](https://marketplace.creatio.com/app/matomo-connector-creatio) 
 . However, you can develop a custom integration that works with a different web analytics service.
 




 Fig. 1
 
 Engagement
 
 tab of the contact page
 

![scr_engagement_tab.png](/docs/sites/en/files/images/CRM_Tools/contact_engagement_data/scr_engagement_tab.png)



 View form submission data
---------------------------



 Creatio automatically identifies contacts that submit forms on landing pages that involve contact creation. For example, “Contact registration form.” Learn more in a separate article:
 [Identify contacts that submit web forms](https://academy.creatio.com/documents?id=2371) 
 .
 



 Form submissions are displayed in the
 
 Submitted forms
 
 detail of the
 
 Engagement
 
 tab and updated in real time.
 



 Each
 **form submission** 
 is an individual record that contains the following data:
 


* form submission date
* landing page that contains the form
* relevant site domain
* fields the contact filled out



 Set up an integration with a web analytics service, for example, Matomo, to enhance form submission records with web analytics data, e. g., user location.
 





 Note.
 
 Form submission records do not include lookup fields since the records contain original data provided by the user or passed from the website.
 




 Import tracking data from Matomo
----------------------------------





 Note.
 
 This section covers the data import procedure for
 [Matomo connector for Creatio](https://marketplace.creatio.com/app/matomo-connector-creatio) 
 application. If you are using a custom integration with a different service, refer to the corresponding documentation.
 




 You can import contact web session and action data Matomo recorded over the past 12 months. To do this, install and set up the Matomo connector for Creatio application. Data is associated with the contact in several ways:
 


* **Contact identification mechanism** 
 is used when the contact submits a form on a landing page that involves contact creation. For example, “Contact registration form.” Learn more in a separate article:
 [Identify contacts that submit web forms](https://academy.creatio.com/documents?id=2371) 
 .



 Once the data is associated with the contact, Creatio imports the data recorded over the past 12 months. The data is displayed on the
 
 Web sessions
 
 and
 
 Web actions
 
 details of the
 
 Engagement
 
 tab, respectively.
 



 If a contact is identified after they submit a form, Creatio imports Matomo data immediately. By default, further updates are performed once a day. Customize the update time and frequency in the
 **Matomo connector for Creatio** 
 application.
 



 If a contact is identified after they click the link in a bulk email, Creatio imports Matomo data as part of the next update scheduled in the
 **Matomo connector for Creatio** 
 application.
 



 Each
 **web session** 
 is an individual record that contains the following data:
 


* session start date
* recorded location
* traffic source
* marketing channel
* page referrer URL
* session duration
* number of actions
* platform (OS)
* device



 Each
 **web action** 
 is an individual record that contains the following data:
 


* action start date
* action type
* the name of the relevant web page
* the URL of the relevant web page




