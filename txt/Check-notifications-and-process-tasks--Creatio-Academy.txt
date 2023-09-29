


 Click the
 
![btn_com_esn_feedback_tab_0.png](/docs/sites/default/files/images/2020-11/btn_com_esn_feedback_tab_0.png)

 button in the
 [communication panel](/docs/glossary_page#title-2071-26) 
 to open the Creatio notification center. This section displays notifications about activities or invoices, comments to your records or mentions in a corporate social network, as well as system notifications. The number on the
 
![btn_com_esn_feedback_tab_0.png](/docs/sites/default/files/images/2020-11/btn_com_esn_feedback_tab_0.png)

 button displays the total number of new messages in the notification center. Creatio displays the information messages on separate tabs:
 


* ![btn_com_notification_center_reminders.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_notifications/btn_com_notification_center_reminders.png)
 – activity and invoice
 [reminders](#title-2099-3) 
 created for you.
* ![btn_com_notification_center_feed.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_notifications/btn_com_notification_center_feed.png)
 – notifications about events connected to your
 [posts in the corporate social network](#title-2099-7) 
 . For example, you were mentioned in a post, received comments on your record in the feed, or somebody liked the record.
* ![btn_com_notification_center_approvals.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_notifications/btn_com_notification_center_approvals.png)
 –
 [approval](#title-2099-8) 
 notifications. For example, pending contracts.
* ![btn_com_notification_center_noteworthy_events.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_notifications/btn_com_notification_center_noteworthy_events.png)
 – notifications about the
 [noteworthy events](#title-2099-9) 
 of contacts and accounts.
* ![btn_com_notification_center_system_notifications.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_notifications/btn_com_notification_center_system_notifications.png)
 –
 [system messages](#title-2099-12) 
 about completed actions in Creatio. For example, information about data import results.



 Reminders and approval notifications are active until they are processed Feed notifications, messages about noteworthy events, and system notifications are considered read when you open the corresponding tab. The history of read notifications is stored on the tab for a month since their creation. Creatio does not add the read notifications to the tab count nor the common notification center count.
 





 Note.
 
 You can modify the storage period for read notifications in the “Notification storage period (days)” (“NotificationsExpirationTerm” code) system setting. The period is 30 days by default.
 




 Pop-up notifications
----------------------



 Creatio displays the notification center's information messages in the browser
 **pop-up boxes** 
 . The box is displayed only once when you receive the message. The notifications received after logging out of Creatio will be displayed in the pop-up boxes upon the next login.
 





 Note.
 
 Your browser may ask you for permission to display pop-up boxes. If you cannot see the boxes, check the browser settings.
 




 Click the
 
 x
 
 button in the pop-up box to hide a notification. If you do this, Creatio will consider the notification unread and add it to the number of unread notifications on the corresponding tab.
 



 Click the notification banner in the pop-up box to open the page for which the notification was sent.
 



 Click the
 
 Notification settings
 
 button in your user profile and clear the
 
 Enable popups
 
 checkbox to
 **disable** 
 pop-up notifications.
 



 Reminders
-----------



 Creatio displays all due reminders on a separate tab in the notification center. Go to the
 ![btn_com_notification_center_reminders00003.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_notifications/btn_com_notification_center_reminders00003.png)
 tab to view the reminders. The number in the tab displays the total number of your active (unprocessed) reminders.
 



 Create a reminder on the invoice or activity page by selecting the checkbox in the
 
 Reminders
 
 field group.
 



 The reminders display
 **activities** 
 of any category (“Meeting,” “To do,” etc.) that meet the corresponding criteria:
 


* You are the owner or the author of the activity.
* The activity has the “Not started” or “In progress” status.
* You or any other system user created a reminder about this activity for you.



 The
 **invoices** 
 that meet the following criteria are also displayed in the reminders:
 


* You are the owner of the invoice.
* The invoice has the “Draft,” “Unpaid” or “Partially paid” status.
* You or any other system user created a reminder about this invoice for you.



 The reminders include the title of the activity or the invoice number, the date, as well as the customer of an activity or an invoice. Creatio also displays a category icon for activities. For example, meetings or calls.
 



 The key details in the reminder are displayed as hyperlinks. For example, click the task title to view its page.
 


### 
 Create a reminder



 Create reminders for invoices and activities in the
 
 Reminders
 
 field group of the record page. To create a reminder for the activity:
 


1. Open the page of the relevant activity.
2. Select the checkbox in the
 
 Reminders
 
 field block:
 


	1. Select the
	 
	 Remind owner
	 
	 checkbox to create a reminder for the user specified in the
	 
	 Owner
	 
	 field of the page.
	2. Select the
	 
	 Remind reporter
	 
	 checkbox to create a reminder for the user specified in the
	 
	 Reporter
	 
	 field.
3. Specify the date and time when the user should see the reminder.
4. Save the record.
 



 If the activity is not completed, Creatio will display the notification in the notification center at the specified time for the user selected in the
 
 Owner
 
 or
 
 Author
 
 field.


### 
 Process reminders



 The notifications on the
 ![btn_com_notification_center_reminders00004.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_notifications/btn_com_notification_center_reminders00004.png)
 tab of the notification center are active until they are processed. You can cancel a reminder or postpone it. Process all reminders at once or separately.
 



 Select the
 
 Postpone
 
 option from the menu and specify the period to
 **postpone a reminder** 
 (Fig. 1). As a result, Creatio will remove the reminder from the list, and the number of unread reminders in the count will decrease. The reminder will be reactivated at the end of the specified period.
 




 Fig. 1 Postpone a reminder
 


![scr_notifications_reminder_postpone.png](/docs/sites/en/files/images/Platform_basics/communications/scr_notifications_reminder_postpone.png)




 Select the
 
 Cancel
 
 option from the menu to
 **cancel a reminder** 
 (Fig. 2). Creatio will no longer display the reminder in the notification center.
 




 Fig. 2 Cancel a reminder
 


![scr_notifications_reminder_cancel.png](/docs/sites/en/files/images/Platform_basics/communications/scr_notifications_reminder_cancel.png)






 Note.
 
 Creatio will cancel a reminder automatically if the activity reaches its final status, for example, “Completed,” and the invoice reaches its final payment status, for example, “Paid.”
 




 Use the
 
 Postpone all
 
 or
 
 Cancel all
 
 option on the notification tab to
 **process all reminders** 
 simultaneously.
 



 Feed notifications
--------------------



 Creatio will display a feed notification if someone mentions you in a post, comments on your record in the feed, or likes the record. Creatio displays the feed notifications on the
 ![btn_com_notification_center_feed00005.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_notifications/btn_com_notification_center_feed00005.png)
 tab in the notification center. The number on the tab displays the total number of unread feed messages.
 



 The tab gives notifications about the following
 **events** 
 :
 


* Someone commented on your record in the feed.
* Someone mentioned you in a post or a comment.
* Someone liked your post or comment.



 After you open the tab, Creatio will mark all new notifications as read and remove them from the tab notification count. If you receive a new notification when the tab is open, Creatio will highlight the notification gray and add it to the notification count. Click a notification to mark it as read. As a result, the highlight will be removed.
 



 Approval notifications
------------------------



 Use the
 ![btn_com_notification_center_approvals00006.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_notifications/btn_com_notification_center_approvals00006.png)
 tab of the notification center to receive information about records that need to be approved. For example, contracts. The notification tab displays the total number of records to be approved. The name of the notification corresponds to the record that must be approved. Notifications also display the date and time of submission for approval. Click the approval title to view the record page.
 



 All notifications on the
 ![btn_com_notification_center_approvals00007.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_notifications/btn_com_notification_center_approvals00007.png)
 tab in the notification center are active until they are processed. You can approve the record, reject an approval, or delegate the approval to someone else. After the approval is processed, Creatio will remove the notification from the tab and update the notification count.
 



 Process approvals using the approval actions menu (Fig. 3).
 




 Fig. 3 The approval actions menu
 


![scr_notifications_communication_panel_approval_menu.png](/docs/sites/en/files/images/Platform_basics/communications/scr_notifications_communication_panel_approval_menu.png)



* Approve
 
 – sets a positive result for the approval.





 Note.
 
 By default, approval comments are optional. Edit the “Accept approval without comment” (“AcceptApprovalWithoutComment” code) system setting to make the
 
 Comment
 
 field required.
 



* Reject
 
 – sets a negative result for the approval.



 If you choose to reject the approval, Creatio will open a pop-up box where you can enter your comments. For example, specify the rejection reason. The comment will be displayed on the approval page.
 


* Change approver
 
 – assigns a different user as the approver. This action opens a window where you can select the user or user group. Approvers can be changed only if the
 
 Approval may be delegated
 
 is selected for this approval in the Process Designer.





 Note.
 
 You can also process an approval using the
 [Approvals
 
 tab](/docs/7-17/user/platform_basics/user_interface/record_pages_shortcut/record_pages#title-759-6) 
 or the
 [action panel](/docs/7-17/user/platform_basics/user_interface/record_pages_shortcut/record_pages#title-759-5) 
 on the page of the required document.
 




 Noteworthy event notifications
--------------------------------



 Creatio reminds you about upcoming noteworthy events of your colleagues and customers in the
 ![btn_com_notification_center_noteworthy_events00008.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_notifications/btn_com_notification_center_noteworthy_events00008.png)
 tab of the notification center. That way you will never miss the customer's birthday or the partner company's foundation day. The tab count displays the total number of unread notifications about noteworthy events.
 



 The tab displays notifications about
 **noteworthy events of contacts and accounts** 
 from the current day through until the next two business days.
 





 Note.
 
 You can change the period for which Creatio will display the notifications in the “Noteworthy events notification period, days” (“NoteworthyEventNotificationPeriod” code) system setting. The period is two days by default.
 




 The history of read noteworthy event notifications is stored on this tab for a month since their creation.
 



 You will receive notifications for the following contacts and accounts:
 


* Contacts and accounts owned by you.
* Contacts of “Employee” type or those for whom “Our company” is specified as an account.
* The main contacts of the accounts owned by you.
* Contacts and accounts specified in the orders owned by you. The orders must have “Draft,” “Confirmation,” or “In progress” status.
* The contacts and accounts specified in opportunities owned by you (by the
 
 Customer
 
 field and the
 
 Contacts
 
 detail of the opportunity). Creatio will send notifications for opportunities that have not been closed yet as well as opportunities won during the last half-year.





 Note.
 
 You can change the period for won opportunities in the “Noteworthy event notification period for opportunity participants, months” (“NoteworthyPeriodForOpportunityParticipants” code) system setting. The period is six months by default.
 



* The contacts and accounts specified in activities owned by you (by the
 
 Account
 
 field and the
 
 Participants
 
 detail of the activity). The activity must have a “Not started” or “In progress” status.



 The noteworthy event notification list is updated every 24 hours. If you are assigned as the contact, account, or opportunity owner, you will receive an upcoming event notification instantly.
 



 Click the hyperlink in the notification to
 **view additional information** 
 about a contact or an account. This will open a contact or account page. If you need to perform any action connected to the upcoming event, e. g. plan greetings, create a corresponding activity. To do this, select the
 
 New task
 
 option in the actions menu.
 



 System messages
-----------------



 Creatio displays the system messages on the
 ![btn_com_notification_center_system_notifications00010.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_notifications/btn_com_notification_center_system_notifications00010.png)
 tab. These messages do not require your attention. For example, they can be about successful Excel import, contact and account duplicates search results, or bulk email sending. System administrators will also see the license extension notifications on this tab.
 



 The tab count displays the total number of unread system messages. If you open the tab, all system messaged will be considered read, and Creatio will reset the tab count. The history of read notifications is stored on the tab for a month since their creation.
 



 Business process tasks
------------------------



 Keep track of the steps linked to a
 [business process](/docs/7-16/user/bpm_tools/business_process_administration/run_a_process/run_process_or_process_step) 
 or a case owned by you from the
 
 Business process tasks
 
 tab on the communication panel. Click the
 
![btn_com_process_tasks.png](/docs/sites/default/files/images/2020-11/btn_com_process_tasks.png)

 button to view the business process step notifications. The counter of the
 
![btn_com_process_tasks.png](/docs/sites/default/files/images/2020-11/btn_com_process_tasks.png)

 button displays the total number of steps that require your attention.
 



 The notifications display business process and case steps (also known as “user actions”) that require your direct input. For example, complete an activity, send emails, edit records, fill out pre-configured pages, etc. The tab displays the steps that meet the following criteria:
 


* You are an owner of the step or have the role to which the task was assigned.
* The process step status is “Running.”



 By default, the tab displays notifications about the steps due through until the current day. Select the “Show future tasks” checkbox at the top of the notification panel to view all notifications.
 



 If the task is assigned to a role, use the quick actions menu to:
 


* start processing the task
* assign the task to yourself to finish it later
* assign the task to another employee



 If you have an open task page or a page that requires your direct input and a different user completes it, Creatio will display a corresponding notification in a dialog box.
 




 Fig. 4 Process a group task on the communication panel
 


![working_with_group_tasks.png](/docs/sites/en/files/images/Platform_basics/communications/working_with_group_tasks.png)






 Note.
 
 You can assign process tasks to other users or roles on the activity page as well. Learn more:
 [Complete process activities](/docs/7-16/user/platform_basics/running_business_processes/execute_a_process/execute_process_steps#title-2098-8) 
 .
 





 Edit the
 
 Process instance caption
 
 parameter in the
 [process properties](/docs/7-16/user/bpm_tools/business_process_setup/overview/process_designer) 
 of the Process Designer to modify the business process title displayed in the notification.
 



 Fig. 5 A business process task notification
 


![scr_notifications_reminder_bpms.png](/docs/sites/en/files/images/Platform_basics/communications/scr_notifications_reminder_bpms.png)




 All notifications on the
 
![btn_com_process_tasks.png](/docs/sites/default/files/images/2020-11/btn_com_process_tasks.png)

 tab in the notification center remain active until they are processed. Click the process step title to open the corresponding page and start processing the step (Fig. 6).
 




 Fig. 6 Navigate to a business process task from the task notification
 


![scr_notifications_reminder_case.png](/docs/sites/en/files/images/Platform_basics/communications/scr_notifications_reminder_case.png)




 Enter the step results on this page. For example, fill out the required fields. If the process task is canceled or postponed, Creatio will update the corresponding notification automatically.
 



 After the task is completed, Creatio will remove the notification from the communication panel. Once all business processes and case steps are complete, the counter on the
 
![btn_com_process_tasks.png](/docs/sites/default/files/images/2020-11/btn_com_process_tasks.png)

 button will reset.
 




