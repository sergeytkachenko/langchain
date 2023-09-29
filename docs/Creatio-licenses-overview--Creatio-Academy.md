


 Creatio includes multiple license types that are, based on the type of licensed object:
 


* **Personal licenses** 
 provide access to Creatio platform and products for specific users. These licenses are linked to user accounts. When distributing personal licenses, make sure the number of provided licenses does not exceed the number of purchased licenses.
 [Read more >>>](https://academy.creatio.com/documents?id=2142) 





 Fig. 1 Number of personal licenses.
 

![scr_chapter_licensing_name_product.png](/docs/sites/en/files/images/Setup_and_Administration/creatio_licensing/scr_chapter_licensing_name_product.png)
* **Server licenses** 
 provide access to additional Creatio functionality, for example, phone integration, to all users on the server. Unlike personal licenses, server licenses are not limited by the number of users.
 



[Read more >>>](https://academy.creatio.com/documents?id=2142) 



 Fig. 2 Number of server licenses
 

![scr_chapter_licensing_server_product.png](/docs/sites/en/files/images/Setup_and_Administration/creatio_licensing/scr_chapter_licensing_server_product.png)
* **Marketing licenses** 
 provide access to Marketing Creatio functionality. These licenses are linked to user or contact accounts, similarly to personal licenses. Make sure that the number of used licenses does not exceed the number of available licenses.
 [Read more >>>](https://academy.creatio.com/documents?id=1932&anchor=title-2803-3) 





 Fig. 3 Number of marketing licenses
 

![scr_licenses_dashboard.png](/docs/sites/en/files/images/Setup_and_Administration/licensing/scr_licenses_dashboard.png)




 Server licenses
-----------------




 Personal licenses
-------------------



 Personal licenses in Creatio differ depending on the business roles of users.
 





| 
 External user
  | 
 Data input restricted user
  | 
 Mobile only user
  | 
 Full user
  |
| --- | --- | --- | --- |
| **General description**  |
| 
 This license type is for users who are not a part of your company but need Creatio data. External users can access your Creatio instance via Portal Creatio. The license grants wide range of permissions but does not permit the user to customize Creatio. External user license is most suitable for partner relations management solutions.
  | 
 This license type provides restricted access to Creatio data. Users can access only data that they added as well as some lookups of your choice. This license type is most suitable for B2C portal solutions.
  | 
 This license type provides access to Creatio only via the mobile app. The license grants access to all Creatio features and data available in the app. Mobile only user license is most suitable for field sales or field service solutions.
  | 
 This license type provides unlimited access to Creatio data. The list of available features and customization tools is defined by your
 [platform plan](https://www.creatio.com/products/pricing/compare-platform-plans?title=false) 
 . Full user license is most suitable for your company employees who need full-scale access to Creatio tools for their everyday work.
  |
| **Key benefits**  |
| 
 Unlimited access to out-of-the-box and custom sections and objects (unlike portal licenses available in previous versions).
  | 
 Main restrictions are set up in the license and do not require additional configuration.
  | 
 Main restrictions are set up in the license and do not require additional configuration.
  | 
 Unlimited access to all Creatio features available in your
 [platform plan](https://www.creatio.com/products/pricing/compare-platform-plans?title=false) 
 .
  |
| **Feature restrictions**  |
| * Users cannot be imported from LDAP.
* Users cannot be a part of the “All employees” organizational role.
* User's email address cannot use your company domain.
* Chats, email synchronization, and telephony are not available.
* App creation and customization are not available.
 | * Users cannot access data created by other users.
* Users have access to non-sensitive data such as lookups, knowledge base articles, etc. in read-only mode.
* Chats, email synchronization, and telephony are not available.
* App creation and customization are not available.
 | * Users cannot log in to the desktop Creatio version.
 | * Restrictions are defined by your
 [platform plan](https://www.creatio.com/products/pricing/compare-platform-plans?title=false) 
 .
 |
| **User type**  |
| 
 External users only
  | 
 External users and company employees
  |
| **Available for Creatio version**  |
| 
 8.0.10 and later
  |
| **Formerly known as**  |
| 
 Portal user license
  | 
 —
  | 
 —
  | 
 Personal user license
  |




 License restrictions listed in the table above work together with the user type restrictions and access permissions for different users and roles set up in Creatio.
 



 Marketing Creatio licenses
----------------------------



 You need the following additional licenses to work with
 **Marketing Creatio** 
 and
 **Creatio CRM bundle** 
 :
 


* **Marketing campaign** 
 licenses (“marketing creatio”). Enable access to all sections of the Marketing Creatio product. The number of licenses must correspond to the number of Creatio users.
* **Active marketing contact** 
 licenses (“marketing creatio 1000 active contacts”). Enable creating records in the
 
 Email
 
 ,
 
 Campaigns
 
 , and
 
 Events
 
 sections. The number of licenses must be equal to or higher than the number of active contacts who receive marketing communications (emails, campaigns, or events).





 Note.
 
 License names include prefixes that specify the Creatio deployment method: onsite or cloud. Cloud licenses do not apply to Creatio on-site and vice versa.
 




**Active contacts** 
 are contacts who have had at least 1 of the following types of marketing communications within the last year:
 


* A contact was a part of an email audience and the email sent to the contact had a response from the user, for example, open or click.
* A contact was a part of an event audience.
* A contact was a part of a campaign audience.
* A contact is a part of a loyalty program and they made at least 1 purchase within the last year (if you use Creatio Marketplace products that automate loyalty programs).



 Licenses are valid within the
 **licensing period** 
 . The licensing period lasts for 365 days, starting from the license start date and ending on the date specified as “Due date” in the License Manager.
 



 The contact can become active only once during a licensing period. If the contact was active during a previous licensing period, but they did not receive any marketing communications during the current period, Creatio does not consider the contact as active during the current period.
 



**Make sure that the number of active contacts (used licenses) does not exceed the number of available licenses** 
 .
 



 If the number of used licenses exceeds that of the available licenses, errors might occur during the following:
 


* saving or sending emails
* editing email templates in the Content Designer
* advancing a campaign to the
 
 Marketing email
 
 step
* certain operations in the
 
 Events
 
 and
 
 Campaigns
 
 sections might be disabled



 Creatio notifies the users when the number of available active contact licenses becomes lower than the threshold percentage of the total number of paid licenses, 10% by default. Notifications are sent only to system users whose contacts are owners or creators of emails, campaigns, events over the past 30 days. We recommend such users to
 **check the
 
 Notifications
 
 tab** 
 of the Communication panel regularly.
 





 Note.
 
 You can change the threshold percentage in the “Active contacts - warning threshold (%)” (“ActiveContactsWarningThreshold” code) system setting.
 




 If the number of active contacts exceeds the number of purchased licenses, you need to purchase additional licenses. Send a license request to Creatio technical support team.
 



 The following guidelines will help
 **avoid restrictions and errors caused by the lack of available licenses** 
 :
 


* When adding groups of contacts to email participants make sure to check the filters of corresponding contact folders. If the filters have been modified, participants who are not a part of the email target audience might be included in the folder. Creatio calculates the number of active contacts and available licenses regularly (once every 4 hours), and additionally each time after an email is sent. That is why the notification about insufficient licenses might be missing when you form the email audience.
* If the number of active contacts does not exceed the available licenses at the moment of sending an email, Creatio sends emails to each of the recipients from the audience. For example, you have 10000 licenses and 9999 active contacts. You add 50000 recipients to the email audience. In this case, email messages are sent to all contacts from the audience. After sending the email, Creatio checks the license availability and applies licensing limitations if necessary.
* When sending emails, be sure to check the settings that let you manage the sending operation and restrict sending emails to inactive contacts, namely:
 


	+ Prohibition to use a contact’s email address (the
	 
	 Do not use Email
	 
	 checkbox in the
	 
	 Communication options
	 
	 of the contact).
	+ Ability to subscribe to certain email types as well as unsubscribe from them.


#### 
 Check the number of used active contact licenses



 The number of owned licenses and active contacts is available in the
 
 Dashboards
 
 section, on the
 
 Licenses
 
 tab (Fig. 3). These metrics might slightly differ from the actual data since they are calculated once an hour. Since Creatio version 8.0.2 the indicators also display license end dates.
 



 You can view the total number of marketing contact licenses and number of available licenses on tooltip on the list page and record page of the
 
 Email
 
 ,
 
 Campaigns
 
 ,
 
 Events
 
 sections as well. The tooltip color depends on the number of available licenses and varies from green (sufficient licenses) to red (no vacant licenses). These numbers might slightly differ from the actual data since they are calculated once an hour.
 




 Fig. 4 License indicator
 

![scr_marketing_active_licenses.png](/docs/sites/en/files/images/Release_notes/release_notes_8_0_2/scr_marketing_active_licenses.png)



 Creatio checks license availability on schedule or after sending an email. We recommend checking the number of available licenses manually when you prepare a new email communication with customers.
 



 To view the list of active contacts, set up a filter in the
 
 Contacts
 
 section as shown in Fig. 5.
 





 Attention.
 
 The filter does not include the loyalty program participants.
 





 Fig. 5 Filter that displays active marketing contacts
 

![chapter_licensing_active_contacts_filter.png](/docs/sites/en/files/images/Setup_and_Administration/licensing/chapter_licensing_active_contacts_filter.png)



 The “Created on” date in the filter is the date when the licenses were uploaded to Creatio. To calculate the needed date:
 




 Fig. 6 View the license validity term
 

![scr_chapter_licensing_term_of_validity.png](/docs/sites/en/files/images/Setup_and_Administration/licensing/scr_chapter_licensing_term_of_validity.png)


1. Click
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/licensing/BPMonlineHelp/licensing_marketing/btn_system_designer.png)
 to open the System Designer.
2. Go to the “Users and administration” block → “
 **License manager** 
 .” This opens a page.
3. Use the search field to find the needed license by name quickly and view its end date on the page that opens (Fig. 6).
4. Copy the start date of the license.
 





 Note.
 
 The license expires in 365 days after it was uploaded. If the due date is later than start date + 365 days, contact Creatio support or your manager.



 As a result, you will get the start date of the license validity period. Enter the date in the
 
 Created on
 
 column when setting up the filter that selects active contacts.
 




