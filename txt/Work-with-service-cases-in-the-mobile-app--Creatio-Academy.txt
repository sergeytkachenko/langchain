


 The
 
 Cases
 
 section (Fig. 1) in the mobile app is used for managing cases (incidents and service requests, claims, etc.) received by the help desk or contact center.
 





 Fig. 1
 

 Case section
 

![scr_case_case_page.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/scr_case_case_page.png)



 To open the
 
 Cases
 
 section, tap the
 ![btn_mobile_case.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/btn_mobile_case.png)
 button on the mobile app main menu.
 



 The section is available by default in any mobile app synchronized with a desktop Creatio product that has the
 
[Cases
 
 section](https://academy.creatio.com/documents?product=service%20enterprise&ver=7&id=1063) 

 . There is no need to set it up in the mobile application wizard. The
 
 Cases
 
 section enables you to:
 


1. register cases (for example, create internal service requests),
2. view case status,
3. add information about case resolution,
4. post messages on the customer portal,
5. escalate cases (only for applications synchronized with Service Creatio, enterprise edition).



 The following fields are displayed by default for each record in the list of the
 
 Cases
 
 section:
 
 Subject
 
 ,
 
 Registration date
 
 ,
 
 Number
 
 ,
 
 Status
 
 , and
 
 Description
 
 . The icon at the right of the case record represents case Priority:
 


1. ![btn_mobile_low.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/btn_mobile_low.png)
 Low.
2. ![btn_mobile_medium.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/btn_mobile_medium.png)
 Medium.
3. ![btn_mobile_high.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/btn_mobile_high.png)
 High.
4. ![btn_mobile_critical.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/btn_mobile_critical.png)
 critical.



 Tap the
 ![btn_mobile_dropdown.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/btn_mobile_dropdown.png)
 button at the top right of the list record to display the quick action menu. The
 
 Cases
 
 section features the case feed accessible via the action menu.
 





 Note.
 
 You can configure the list via the
 
mobile application wizard

 , available in the system designer of the desktop application.
 




 The
 
 Cases
 
 section has the standard
 
search

 field and
 
[filter](/docs/8-0/user/platform_basics/mobile_app/ui/mobile_application_interface#title-772-4) 

 options.
 



 Create a new case
-------------------



 To register a new case:
 


1. Tap
 ![btn_mobile_case00004.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/btn_mobile_case00004.png)
 to open the
 
 Cases
 
 section.
2. Tap the
 ![btn_mobile_add00005.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/btn_mobile_add00005.png)
 button. The case page will open.
3. Fill out the required fields:
 


	1. Specify the case subject.
	2. Select the customer for this case in the
	 
	 Contact
	 
	 or
	 
	 Account
	 
	 field. One of these fields must be populated. If the
	 
	 Account
	 
	 field is populated, the list of contacts will display only the contacts of this account. If the
	 
	 Contact
	 
	 field is filled in, the
	 
	 Account
	 
	 field is automatically filled in with the account specified for this contact.
4. Complete the case profile:
 


	1. Select the case category (incident or service request).
	2. Specify the assignee or assignee group for the case.
5. Save the case.



 As a result, a new Creatio case will be added. Creatio automatically generates the case number by a pattern specified in the “Case number mask”
 
[system setting](/docs/8-0/user/setup_and_administration/system_settings_and_lookups/manage_system_settings_shortcut/manage_system_settings) 

 (CaseCodeMask).
 



 The
 
 Attachments
 
 detail (Fig. 2) contains files and links related to the case. Tap
 
![btn_ff_add.png](/docs/sites/default/files/images/2020-12/btn_ff_add.png)

 and select an attachment file.
 





 Fig. 2
 


 Attachments
 
 group
 

![scr_case_attachments.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/scr_case_attachments.png)



 You can also add case attachments using the
 
 Add file or link
 
 action (
 
![btn_mobile_attach.png](/docs/sites/default/files/images/2020-12/btn_mobile_attach.png)

 )
 



 in the actions menu of the record.
 



 Process a case
----------------



 Mobile application functions enable you to post messages in the case feed (for internal communications) or communicate with the case customer on the portal. If your mobile app is synchronized with a product that contains service enterprise functions, you can also escalate cases.
 


### 
 Post internal messages



 There are two ways of posting messages message in the
 [feed](#title-769-8)
 :
 


1. **From the main menu:** 
 tap
 ![btn_mobile_case00006.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/btn_mobile_case00006.png)
 to open the cases section, locate the needed case and tap
 

![btn_mobile_dropdown00007.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/btn_mobile_dropdown00007.png)


 button, then select the
 
![btn_mobile_feed2.png](/docs/sites/default/files/images/2020-12/btn_mobile_feed2.png)


 Go to Feed
 
 command (Fig. 3).
 





 Fig. 3
 

 Case feed menu
 

![scr_case_feed_action.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/scr_case_feed_action.png)
2. **From an opened case page:** 
 tap
 ![btn_mobile_case_actions00009.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/btn_mobile_case_actions00009.png)
 , then tap the
 
![btn_mobile_feed2.png](/docs/sites/default/files/images/2020-12/btn_mobile_feed2.png)


 Go to Feed
 
 command.
 



 Once the feed page opens, tap
 ![btn_mobile_add00011.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/btn_mobile_add00011.png)
 to post a new message. Type the message and tap the
 
 Publish
 
 button.


### 
 Reply to the case customer



 To post a message on the self-service portal:
 


1. **To access a case from the main menu** 
 , tap
 ![btn_mobile_case00012.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/btn_mobile_case00012.png)
 → the required case record in the section list.
2. **To access the portal from the case page:** 
 tap
 ![btn_mobile_case_actions00013.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/btn_mobile_case_actions00013.png)
 →
 
![btn_mobile_portal.png](/docs/sites/default/files/images/2020-12/btn_mobile_portal.png)


 Post message on the portal
 
 .
 



 Once the portal page opens, type the message and tap the
 
 Publish
 
 button.


### 
 Escalate the case



 To escalate a case to another support level:
 


1. **To access a case from the main menu** 
 , tap
 ![btn_mobile_case00015.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/btn_mobile_case00015.png)
 → the required case record in the section list.
2. **To access the escalation from an opened case page** 
 , tap
 ![btn_mobile_case_actions00016.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/btn_mobile_case_actions00016.png)
 →
 
![btn_mobile_escalate.png](/docs/sites/default/files/images/2020-12/btn_mobile_escalate.png)


 Escalate
 
 (Fig. 4). Specify the support line and new assignee or assignees group on the opened escalation page (one of the fields has to be filled in).
 





 Fig. 4
 

 Case escalation
 

![scr_case_escalate.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/scr_case_escalate.png)




 View processing history
--------------------------



 This detail displays the history of communications with the case customer, as well as internal communications and automatic notifications. The processing history includes:
 


1. Emails sent and received during the case resolution process.
2. Internal notes posted by employees in the case feed.
3. Messages posted by employees and portal users on the customer portal.
 



 The detail also contains system messages that inform you about various system-wide events that are connected to the case.
 





 Fig. 5
 
 Processing history screen
 

![scr_case_history.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_cases_section/scr_case_history.png)




