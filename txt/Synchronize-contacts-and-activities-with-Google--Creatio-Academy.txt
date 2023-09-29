



 Creatio 8.0 Atlas and later does not support contact synchronization with Google.
 




 Set up the synchronization
----------------------------



 Before you synchronize Google contacts and calendars with Creatio, perform preliminary setup:
 


1. Set up access to Google contacts and calendars for your Creatio account.
 [Read more >>>](#title-194-2)
2. Set up the automatic synchronization of Creatio with Google.
 [Read more >>>](#title-194-3)


### 
 Step 1. Set up access to Google user account


1. Open your profile. For example, click the image in the top right →
 
 Your profile
 
 (Fig. 1).
 




 Fig. 1 Open the user profile
 

![scr_chapter_google_enter_profile.png](/docs/sites/en/files/images/Setup_and_Administration/synchronize_activities_with_google/scr_chapter_google_enter_profile.png)
2. Click
 
 Accounts in external resources
 
 on the profile page (Fig. 2). This opens a new page.
 




 Fig. 2 Accounts in external resources
 

![scr_chapter_google_choose_button_in_profile.png](/docs/sites/en/files/images/Setup_and_Administration/synchronize_activities_with_google/scr_chapter_google_choose_button_in_profile.png)
3. Click
 
 New
 
 → Google. This opens a new tab.
4. Select the Google account that uses the corporate email.
5. Grant Creatio access to calendars and contacts of your Google account.


### 
 Step 2. Specify the contact synchronization parameters



 View an example of synchronization setup in the
 
 Contacts
 
 section below.
 


1. Open the
 
 Contacts
 
 section.
2. Create a
 [private tag](https://academy.creatio.com/documents?id=1290) 
 to use for synchronization. For example, “Google synchronization.”
 





 Note.
 
 Only records that have private tags are synchronized. Creatio does not synchronize records that have public or corporate tags.
3. Click
 
 Actions
 
 →
 
 Synchronize contacts
 
 →
 
 Set up…
 
 . This opens the settings page. Take the following steps on the settings page:
 


	1. Select the
	 
	 Synchronize activities automatically
	 
	 checkbox and specify the synchronization period to synchronize activities automatically. Select the required date in the
	 
	 Synchronize from
	 
	 field to start synchronization from a specific date.
	2. Select the
	 
	 Synchronize contacts automatically
	 
	 checkbox and specify the synchronization period to synchronize contacts automatically.
	3. Select a tag in the
	 
	 Send all contacts with a tag from Creatio to Google
	 
	 field to synchronize contacts that have a specific tag.
4. Click
 
 Save
 
 .
 





 Note.
 
 Creatio displays the date and time of the latest synchronization session on the setup page.
 




 As a result, Creatio will save both your Google account and the contact synchronization tag. The synchronization will be run automatically within the specified period.
 





 Note.
 
 You can configure synchronization with Google in the
 
 Activities
 
 section in the same manner. You do not need to specify the task synchronization tag in the synchronization settings of the
 
 Activities
 
 section.



 Synchronize Creatio contacts with Google contacts
---------------------------------------------------



 Synchronization lets you add Google contacts to Creatio. Google synchronizes only Creatio contacts that have a private tag specified in the synchronization settings.
 



 To run the synchronization for the first time:
 


1. Open the
 
 Contacts
 
 section.
2. Click
 
 Actions
 
 →
 
 Synchronize contacts
 
 →
 
 Synchronize now
 
 .
 



 As a result of synchronization, a new “Creatio” group of contacts will be added to Gmail.
3. Move the needed Gmail contacts to the “Creatio” group.
4. Click
 
 Synchronize contacts
 
 →
 
 Synchronize now
 
 again.
 



 As a result, Creatio will import Gmail contacts from the “Creatio” group and mark them with the private tag specified during the synchronization setup.
 





 Note.
 
 If you set up automatic synchronization, the process starts automatically.
 




 From this point on, the synchronization of Google and Creatio contacts is performed in both directions. Synchronization is run only for the records that have been changed or added since the last synchronization session.
 



 If a record is modified both in Gmail and Creatio, the most recent changes are used for the synchronization.
 



 If a record is deleted from Gmail or Creatio, the next synchronization does not delete it from Creatio or Gmail. In the first case, Creatio removes the tag from a deleted record. In the second case, Gmail excludes the record from the “Creatio” group.



 Synchronize Creatio activities with Google calendar
-----------------------------------------------------



 If you use both Creatio and Google calendars to schedule your activities, we recommend synchronizing the calendar data.
 



 Before you synchronize Creatio calendar with Google, register Creatio in Google Workspace. Learn more in a separate article:
 [Register Creatio application in Google Workspace](https://academy.creatio.com/documents?id=1758) 
 .
 



 To run the synchronization from Creatio, open the
 
 Activities
 
 section →
 
 Actions
 
 →
 
 Synchronize activities
 
 →
 
 Synchronize now
 
 .
 



 When you run this action, Creatio synchronizes activities with the calendar of the Google account specified in the synchronization settings. All Creatio activities that have the
 
 Show in calendar
 
 checkbox selected are synchronized. Synchronization is run by the
 
 Organizer
 
 field. If a meeting organizer does not have synchronization set up, the
 
 Organizer
 
 field is populated with the activity participant who runs the synchronization. If the collective task is created in Google, Creatio adds a collective task and populates its
 
 Participants
 
 detail with participants as part of synchronization. Only users whose emails on the
 
 Communication options
 
 detail and in the Google collective task match are added to the list of participants. The task is displayed for participants only after they synchronize their calendar with Google.
 



 The changes are displayed in Google when the task organizer modifies the collective task added to Creatio via Google synchronization.
 





 Note.
 
 Synchronization can also be run automatically within the period specified in the synchronization settings.
 





