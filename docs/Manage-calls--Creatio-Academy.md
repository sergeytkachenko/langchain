


 In Creatio, all base telephony features (for example, receiving incoming calls and making outgoing ones, putting calls on hold and transferring them to another number) are available on the communication panel. To display the
 
 Calls
 
 tab, click the
 ![btn_com_open_cti_panel.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/btn_com_open_cti_panel.png)
 button.
 



[Set up phone integration](https://academy.creatio.com/docs/user/more_apps/phone_integration_connectors) 
 to enable call management in Creatio. Use a headset to make and receive calls.
 



 Make calls
------------



 Outgoing call can be made in a number of ways. You can either dial the number manually on the communication panel, make a call using the calls history or click the call button on the contact page.
 


### 
 Dial by phone number



 If you know the phone number that you want to call:
 


1. On the
 
 Calls
 
 tab, enter the phone number in the tab field and click the call button or press the
 
 Enter
 
 key (Fig. 1).
 




 Fig. 1 Manual dial
 

![scr_cti_outcome_call.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_outcome_call.png)



 You can also make a call by clicking the call button next to the name of the needed subscriber in the
 [calls history](#title-761-11) 
 (Fig. 2).
 




 Fig. 2 Dial from the calls history
 

![scr_cti_outcome_call_from_history.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_outcome_call_from_history.png)
2. Wait for the connection (Fig. 3).
 




 Fig. 3 An outgoing call
 

![scr_cti_outcome_call_unknown.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_outcome_call_unknown.png)
3. If the connection is successful, the call will be switched to the conversation mode.
4. To end the call, click the end call button.


### 
 Dial by phone number



 If you know the name of the contact that you want to call:
 


1. On the
 
 Calls
 
 tab, enter the contact name or a part of it in the tab field. The system will search for contacts whose name contains the entered fragment and will display those contacts on the tab.
 





 Note.
 
 To start searching, enter three or more characters.
2. Find the needed subscriber in the list and click the call button next to the phone number you want to call (Fig. 4).
 




 Fig. 4 Search for a subscriber by name
 

![scr_cti_outcome_call_several_abonents.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_outcome_call_several_abonents.png)
3. Wait for the connection.


### 
 Quick dial from record pages and the section list



 You can call a contact (an account) from the contact/account page or from the section list.
 


1. To start a call from the contact page:
 


	1. On the Communication options detail, click the phone number or the call button next to the number you want to call (Fig. 5).
	 
	
	
	
	
	 Fig. 5 Quick dial from the record page
	 
	
	![scr_cti_quick_dial.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_quick_dial.png)


1. Wait for the connection.
2. To make a call from the section list, click the phone number that is displayed as a link (Fig. 6).
 




 Fig. 6 Quick dial from the section list
 

![scr_cti_quick_dial_from_list.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_quick_dial_from_list.png)



 Receive calls
---------------



 By default, the section is hidden. It expands in the right side panel of the screen when incoming call is received (Fig. 7).
 




 Fig. 7 An incoming call
 

![scr_cti_income_call_unknown.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_income_call_unknown.png)


1. To start the conversation, click the call answer button or pick up the phone if the button is unavailable.
2. To decline a call, click the end call button.
 





 Note.
 
 The type of the Call Center used in Creatio determines whether the answer button is displayed for an incoming call or not. For example, the answer button is unavailable when working with Asterisk Call Center. If your telephone network supports this feature, and you would like to use it, open the Call Centre parameters setup page and select the
 
 Enable picking up phone from application
 
 checkbox. The setup page can be opened from the user profile.



 Identify the caller
---------------------



 In Creatio, a subscriber is identified by the phone number during both an outgoing or an incoming call.
 


1. If a subscriber (a contact or an account) is identified by the phone number while calling, the name of the subscriber will be displayed on the call panel (Fig. 8).
 




 Fig. 8 Identify the subscriber
 

![scr_cti_income_call_one_abonent.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_income_call_one_abonent.png)
2. If the same phone number is specified for more than one contact or account, the list of those subscribers will be displayed on the call panel. To select the needed subscriber, click the subscriber's record in the list (Fig. 9).
 




 Fig. 9 Select one of the contacts found by the phone number
 

![scr_cti_income_call_several_abonent.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_income_call_several_abonent.png)
3. If you need to change the selected subscriber, open the additional menu next to the subscriber's name and select the
 
 Select another record
 
 option (Fig. 10).
 




 Fig. 10 Select another subscriber
 

![scr_cti_income_call_other_abonent.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_income_call_other_abonent.png)





 Note.
 
 The information about the selected subscriber will be saved in the call history in the
 
 Calls
 
 section.
 




 If a subscriber is not identified by the phone number while calling, at the end of th call you will be able to create a contact or an account or connect a call to the existing contact or account via the
 [calls history](#title-761-11) 
 .
 



 Put calls on hold
-------------------



 While you are on a call, you can put the call on hold so that the subscriber is still on the line but cannot hear you.
 



 Click the
 ![btn_cti_pause_new.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/btn_cti_pause_new.png)
 button on the call panel to put a call on hold. Click the
 ![btn_cti_pause_on_new.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/btn_cti_pause_on_new.png)
 button to resume conversation.
 





 Note.
 
 The call cannot be transferred or finished when it is on hold.
 




 Transfer calls
----------------



 While you are on a call, you can transfer the call to another phone number. When using the Avaya, Webitel, Finesse, TAPI, and Asterisk connectors, blind (unconditional) transfer is available for all calls.
 





 Note.
 
 To enable blind transfer, select the
 
 Use blind transfer
 
 checkbox in the user profile.
 




 To transfer the call to another agent without interrupting the call:
 


1. Click the
 ![btn_cti_transfer_new.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/btn_cti_transfer_new.png)
 button on the call panel. An additional field will be displayed. Use this field to enter the phone number that you want to transfer the call to. Also, the
 [calls history](#title-761-11) 
 will become available on the tab. Use it to transfer the call to a subscriber that you recently contacted.
2. Enter the phone number or select the needed subscriber from the calls history and click the call button (Fig. 11). You can also find the needed subscriber by name.
 




 Fig. 11 Dial when transferring the call
 

![scr_cti_call_transfer_input_number.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_call_transfer_input_number.png)
3. The call will be put on hold, and the system will start establishing the connection with the subscriber whom you transfer the call to. The information about subscribers will be displayed on the call panel (Fig. 12).
 




 Fig. 12 Connect to another subscriber when transferring the call
 

![scr_cti_call_transfer_transfering.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_call_transfer_transfering.png)
4. To quickly transfer the call, put down the phone, so both subscribers will be connected, and you will be disconnected from the conversation.
5. To make an attended transfer, wait for the connection with the subscriber whom you transfer the call to. In case if the connection is successful, the call panel will display additional buttons used to finish the transfer or to cancel it (Fig. 13).
 




 Fig. 13 Talk to a subscriber while transferring the call
 

![scr_cti_call_transfer_answer.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_call_transfer_answer.png)



 Make and receive video calls
------------------------------



 In Creatio, you can make video calls if Webitel integration is configured in Creatio. Video communication is available only for internal calls.
 



 You can enable/disable video calls in Creatio. To manage video calls setup:
 


1. Open the user profile page by clicking the
 
 Profile
 
 image button on the main page of the application.
2. Click the
 
 Call Center parameters setup
 
 button.
3. On the displayed page, select/deselect the
 
 Use video
 
 checkbox to enable/disable video calls.
 



 When video calls are enabled, during the call, you see the video image of the user that the connection is established with and share your own video image.



 In the video call mode, the communication panel additionally contains the video area and video call controls, such as a seek bar and timer that indicates the time passed since the call start.
 



 Check the calls history
-------------------------



 You can view the recent calls history on the communication panel. It is available if the user is neither in a conversation mode nor searching for a subscriber. The history is also available when
 [transferring a call to another number](#title-761-9) 
 .
 



 The calls history chronologically displays the recent incoming, outgoing and missed calls, and brief information about the accounts/contacts that a connection was established with (Fig. 14).
 




 Fig. 14 The calls history
 

![scr_cti_call_history_example.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_call_history_example.png)





 Note.
 
 The number of calls displayed in the history can be set up in the “Number of records on the “Calls history“ tab“ system setting.
 






 Note.
 
 Do not close the browser window when making a call via the Creatio interface for proper saving the call history. If the window was closed during the conversation, the call ent dime and its duration will not be saved.
 




 The calls history displays information only about the latest communication session with a certain subscriber (account or contact). For example, if you call several numbers specified on the
 
 Communication options
 
 detail of a contact, the calls history will display one record for this contact with the number that was dialed last.
 



 If you called a subscriber and now you need to call another of his/her numbers, go to the contact/account page from the calls history and make a call from the subscriber page.
 



 To do that, in the calls history, click the name of the contact/account. It is displayed as a link (Fig. 15). The subscriber page will open. On the page, select the needed number from the numbers available on the
 
 Communication options
 
 detail. You can call directly from the contact/account page by clicking either the phone number or the call button next to the number on the
 
 Communication options
 
 detail.
 




 Fig. 15 Open a contact page from the calls history
 

![scr_cti_call_history_go_to_page.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_call_history_go_to_page.png)



 If the same phone number is associated with several subscribers (contacts and/or accounts) in the system, then when the connection is established, different subscribers will be
 [identified](#title-761-6) 
 , and the calls history will display separate records for each contact/account (Fig. 16).
 




 Fig. 16 The calls history for one number associated with several users
 

![scr_cti_call_history_same_number.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_call_history_same_number.png)



 In addition to viewing completed incoming and outgoing calls, you can create a contact or account, connect the call with an existing contact and display connected activities. To process a call, use the menu, which you can open by clicking the
 ![scr_cti_button.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_button.png)
 button (Fig. 17).
 




 Fig. 17 The call processing menu
 

![scr_cti_add_smt.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_add_smt.png)



 To
 **add a contact** 
 for the call subscriber, select
 
 Create contact
 
 . New contact page will open. After saving the contact, the corresponding phone number will be automatically added to the
 
 Communication options
 
 detail. By default, “Mobile phone” will be set as the communication option type.
 



 You can
 **add an account** 
 based on the call subscriber. To do this, select the
 
 Create account
 
 menu command. After saving the account, the corresponding phone number will be automatically added to the
 
 Communication options
 
 By default, “Primary phone” will be set as the communication option type.
 



 To
 **connect a call to an existing contact or account** 
 , select the
 
 Add to existing contact
 
 menu command and select corresponding record from the lookup. The phone number from the call will be added to the
 
 Communication options
 
 detail of the selected record.
 



 To display call connections to contacts, accounts and other records, select the
 
 Show all connections
 
 menu command. Connected account, contact and activity will be displayed below the general call information (Fig. 18).
 




 Fig. 18 The call connections
 

![scr_cti_history.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_history.png)



 You can connect the call to a system record by selecting a record type in the menu and clicking the
 ![scr_cti_button_choose.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_button_choose.png)
 button (Fig. 19).
 




 Fig. 19 Bind a call
 

![scr_cti_add_activity.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_add_activity.png)



 Record calls
--------------



 Recording and playback of calls is available in Creatio if your Call Center supports this feature. Call recording and playback rules can be set up in such office call center as Webitell.
 





 Note.
 
 Additional setup is required to enable call playback.
 




 To play a call record, go to the
 
 History
 
 tab of the needed contact or account. Select the needed call record on the
 
 Calls
 
 detail and click the
 
 Play
 
 button (Fig. 20).
 




 Fig. 20 Play a call record
 

![scr_cti_start.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_start.png)



 Call records are played in a web player with basic playback options (Fig. 21).
 




 Fig. 21 The record playback
 

![scr_cti_listen.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_listen.png)



 You can also download call record as an audio file by selecting the
 
 Download audio file
 
 menu command (Fig. 22).
 




 Fig. 22 Download the call record file
 

![scr_cti_down.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_down.png)



 Change your agent status
--------------------------



 Agent status menu is displayed when you click the user image located in the top right corner of the screen (Fig. 23).
 




 Fig. 23 The agent status menu
 

![scr_cti_operator_status.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_telephony_cases/scr_cti_operator_status.png)



 The list of available agent statuses depends on the telecommunications system that is used and can be set up in the
 
 User status for message exchange
 
 lookup.
 




