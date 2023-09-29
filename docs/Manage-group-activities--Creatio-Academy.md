


 Creatio lets you schedule activities that have multiple participants, such as meetings, trainings, and conferences. These activities appear in the schedule of all required participants.
 



 To make an activity a group activity, add data to the
 
 Audience
 
 detail. To do this:
 


1. Open the
 
 Activities
 
 section list. Select a record in the section list and click
 
 Open
 
 .
2. Go to the
 
 Participants
 
 tab to specify the list of the contacts who participate in the task/call.
3. Click
 ![btn_add_ke.png](/docs/sites/default/files/images/CRM_Tools/activities/btn_add_ke.png)
 . This opens a box. Select the needed contacts and click
 
 Select
 
 in the box.
 



 Creatio adds the contacts specified in the
 
 Owner
 
 or
 
 Reporter
 
 fields to the
 
 Participants
 
 detail automatically.



 By default, after the participants are added, the detail displays the information from the
 
 Job title
 
 and
 
 Business phone
 
 fields of the contact pages.
 





 Note.
 
 When you copy an activity, the participant list is copied, too.
 




 Invite participants to the meeting
------------------------------------



 You can send invites to the activity participants from the activity page. View the list of participants and their responses on the
 
 Participants
 
 detail.
 



 This feature becomes available after you set up integration with Exchange calendars and contacts. Learn more in a different section:
 [MS Exchange / Microsoft 365 email, contacts, and calendar](https://academy.creatio.com/docs/user/setup_and_administration/base_integrations/microsoft_email_contacts_and_calendar) 
 .
 



 To send invites:
 


1. Open the
 
 Activities
 
 section list.
2. Select a record in the section list and click
 
 Open
 
 .
3. Go to the
 
 Participants
 
 tab and click
 
 Send invitations
 
 (Fig. 1).
 

 Fig. 1 Send a meeting invitation
 

![scr_release_notes_send_invitations.png](/docs/sites/en/files/images/CRM_Tools/activities/scr_release_notes_send_invitations.png)



 As a result, all activity participants that have an email address specified will receive an invite email with the meeting description and several response options:
 


* accept the invitation
* decline the invitation
* accept tentatively
* offer to reschedule the meeting



 All sent responses will be available on the
 
 Participants
 
 tab of the meeting. If the participants did not respond to the invite, you can
 **send the invite again** 
 by clicking
 
 Resend invitations
 
 on the activity page.
 



 After the invites are sent, only the author of the activity can edit it. It will be read-only for the other participants.
 



 If the
 **key parameters** 
 of the activity change, Creatio sends new invites automatically. The following Exchange parameters are key parameters:
 


* the title of the meeting (Title)
* the location of the meeting (Location)
* the start date of the meeting (Start Date)
* the due date of the meeting (Due Date)
* the priority of the meeting (PriorityID)
* the description of the meeting (Body)
* the time zone (TimeZone)
* the list of participants (Participants)



 Link an online meeting
------------------------



 You can connect to online meetings and video conferences in Microsoft Teams, Zoom, Cisco Webex, Join.Me, AnyMeeting, GoToMeeting, Google Meet, and other services directly from the Creatio activity calendar (Fig. 2).
 




 Fig. 2 Join a video conference from the schedule
 

![scr_videoconference_join_video_meeting.png](/docs/sites/en/files/images/CRM_Tools/activities/group_activities/scr_videoconference_join_video_meeting.png)



 This feature becomes available after you set up the synchronization with Exchange calendars. Learn more in a different section:
 [MS Exchange / Microsoft 365 email, contacts, and calendar](https://academy.creatio.com/docs/user/setup_and_administration/base_integrations/microsoft_email_contacts_and_calendar) 
 .
 



 To link an activity to an online meeting:
 


1. Open an existing activity or create a new activity. Learn more in a separate article:
 [Create an activity](https://academy.creatio.com/documents?id=1010) 
 .
2. Open the meeting edit page. For example, double-click the record heading in the
 
 Activities
 
 section schedule.
3. Open the
 
 Attachments and notes
 
 tab and add the video conference URL to the
 
 Notes
 
 detail.
 





 Note.
 
 If you add several links to the
 
 Notes
 
 detail, Creatio connects to the video conference via the first link that follows the URL pattern of an online meeting service. Creatio stores URL patterns for various services in the
 
 Meeting services links
 
 lookup.
4. Click
 
 Save
 
 .



 As a result, Creatio will display the
 ![btn_videoconferences_camera_mini.png](/docs/sites/en/files/images/CRM_Tools/activities/group_activities/btn_videoconferences_camera_mini.png)
 button on the activity mini page and
 ![btn_videoconferences_camera_max.png](/docs/sites/en/files/images/CRM_Tools/activities/group_activities/btn_videoconferences_camera_max.png)
 button on the activity page. Click any button to join the scheduled online meeting
 





 Note.
 
 If you add a video conference link to the activity yet Creatio will not display the buttons on the activity mini page and activity page, make sure the link is correct. The link must not contain spaces or other characters that do not follow the service URL pattern. If the link is specified correctly, contact the Creatio administratior. The
 
 Meeting services links
 
 lookup might lack the pattern for the service.
 





