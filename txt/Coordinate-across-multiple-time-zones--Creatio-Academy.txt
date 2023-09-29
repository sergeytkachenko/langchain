


 To efficiently communicate with customers and employees around the world, Creatio takes into account timezones of each contact.
 



 This enables you to:
 


* Quickly identify the current local time of an employee or a customer when planning activities and communications.
* Synchronize employee and customer activities in different timezones, taking into account the time difference.



 The current local time and time zone is displayed for all contacts and activities.
 








 Check contact's local time
---------------------------------



 The current local time is displayed for each contact on the contact page in the contact profile and on the contact mini page.
 



 To quickly view a contact's local time, hover your cursor over the contact's name in the list. A contact mini page will open, in which the contact's current time is displayed under the contact's photo.
 


* Time zone information, displayed on the contact mini page, includes:
* Contact's current time
* Country or city name (
 [Fig. 1](#XREF_36556_156)
 )




 Fig. 1 Contact's local time, as seen on a mini page
 


![contact_time_in_minicard.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_timezones/contact_time_in_minicard.png)




 When you hover the mouse cursor over the time, the time zone is displayed.
 





 Set the contact's time zone
-------------------------------



 To determine local time of a customer or employee, information from the
 
 Addresses
 
 detail of the contact record page is used.
 


* The contact's time zone is automatically determined
 **by the city** 
 specified in the
 
 Home address
 
 field, or the contact's
 **country of residence** 
 if the
 
 City
 
 field is blank.





 Note.
 
 Cities are assigned to time zones in the
 
 Cities
 
 lookup. The countries have the same timezones as their capital cities. When adding new records in the
 
 Cities
 
 lookup, be sure to specify a time zone for each new city.
 



* If a contact record page has 2 addresses of “Actual” type, the address that was added last is used for determining the time zone. If no address of “Actual” type is specified, the
 **last added address** 
 is used, regardless of its type.
* If no address is available on the contact page, the legal
 **address of the connected account** 
 is used for determining the time zone. If a legal address is not specified for the connected account, then the time zone is determined by the last entered address of the account.
* If the contact is a registered system user, such as an employee, then the
 **user profile** 
 data is used to determine the time zone.





 Note.
 
 If no information can be found in the system to determine contact's time zone, the time zone icons will look like this:
 
![timezone_no_data.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_timezones/timezone_no_data.png)

 .
 










 Plan activities in a different time zone
------------------------------------------------



 Use the time zone function to plan tasks, calls and other activities with contacts in different time zones. The time zone function is available on the activity page and mini page. To plan an activity with participants in different zones:
 


1. Add a new record in the
 
 Activities
 
 section and add participants.
2. On the record page, or its mini page, click the
 ![timezone_symbol.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_timezones/timezone_symbol.png)
 button to specify the time zone, where the activity will be held. It can be your current time zone or the time zone of any of the participants.
3. Specify the activity time in the selected time zone.
 



 The system will automatically calculate the time difference and correctly plan the activity in both your and participant's calendar.
 





 Note.
 
 To calculate the time difference, use the time zone data specified in the user profile. If no time zone is specified in the user profile, the “Default TimeZone” system setting is used.
 




 The system schedules activities in the local time of each participant. For example, if you want to schedule a call to a contact located in Los Angeles (UTC -8) for 10:00 a.m. Los Angeles local time, and you are located in New York (UTC -5), just specify the contact's local time. A new activity will appear in the calendar of your contact for 10:00 a.m. In your calendar, the activity will be scheduled for 1:00 p.m.




