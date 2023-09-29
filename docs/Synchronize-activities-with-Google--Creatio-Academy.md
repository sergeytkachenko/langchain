


 Set up the synchronization
----------------------------



 Before you synchronize Google calendars with Creatio, perform preliminary setup:
 


1. Set up access to Google calendars for your Creatio account.
 [Read more >>>](#title-194-2)
2. Set up the automatic synchronization of Creatio with Google.
 [Read more >>>](#title-194-3)


### 
 Step 1. Set up access to Google user account


1. Open your profile. For example, click the image in the top right →
 
 Your profile
 
 (Fig. 1).
 




 Fig. 1 Open the user profile
 

![scr_profile.png](/docs/sites/en/files/images/Setup_and_Administration/synchronize_activities_with_google/scr_profile.png)
2. Click
 
 Additional settings
 
 in the top right of the profile page. This opens a new page.
3. Click
 
 Accounts in external resources
 
 on the profile page (Fig. 2). This opens a new page.
 




 Fig. 2 Accounts in external resources
 

![scr_chapter_google_choose_button_in_profile.png](/docs/sites/en/files/images/Setup_and_Administration/synchronize_activities_with_google/scr_chapter_google_choose_button_in_profile.png)
4. Click
 
 New
 
 → Google. This opens a new tab.
5. Select the Google account that uses the corporate email.
6. Grant Creatio access to calendars of your Google account.


### 
 Step 2. Specify the activity synchronization parameters



 To set up the synchronization in the
 
 Activities
 
 section:
 


1. Open the
 
 Activities
 
 section.
2. Create a
 [private tag](https://academy.creatio.com/documents?id=1290) 
 to use for synchronization. For example, “Google synchronization.”
 





 Note.
 
 Only records that have private tags are synchronized. Creatio does not synchronize records that have public or corporate tags.
3. Click
 
 Actions
 
 →
 
 Synchronize activities
 
 →
 
 Set up…
 
 . This opens the settings page. Enable the
 
 Synchronize calendar automatically
 
 switch on the settings page and specify the synchronization period to synchronize activities automatically. Select the required date in the
 
 Synchronize from
 
 field to start synchronization from a specific date.
4. Click
 
 Save
 
 .
 





 Note.
 
 Creatio displays the date and time of the latest synchronization session on the setup page.
 




 As a result, Creatio will save your Google account. The activity synchronization will be run automatically within the specified period.



 Synchronize Creatio activities with Google calendar
-----------------------------------------------------



 If you use both Creatio and Google calendars to plan your activities, we recommend synchronizing the calendar data.
 



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
 
 checkbox selected are synchronized. Synchronization runs by the
 
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
 





