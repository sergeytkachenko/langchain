



 This functionality is available for Creatio 8.0.6 and later.
 




 As part of the new architecture, the recent update features a revamped UI. The Freedom UI encompasses the latest and greatest UX best practices to streamline the app design process and user adoption, all while providing a high level of personalization.
 



 Creatio opens the application homepage (Fig. 1) on login. This page aggregates the dashboard information for different roles.
 




 Fig. 1 Creatio homepage
 

![scr_freedom_ui_shell_homepage.png](/docs/sites/en/files/images/Platform_basics/freedomUI_shell/scr_freedom_ui_shell_homepage.png)



 Freedom UI consists of the working area that displays the content of the page opened currently, quick access buttons for basic Creatio operations, and multiple panels. The panels are minimized to help you focus on the working area, but you can maximize each panel in a single click.
 




 Fig. 2 Freedom UI
 

![scr_freedom_ui_shell_general.png](/docs/sites/en/files/images/Platform_basics/freedomUI_shell/scr_freedom_ui_shell_general.png)



 Navigation panel (1)
----------------------



 The navigation panel (or the section panel) in the left lets you navigate through workplaces and sections.
 



 Switch between workplaces using the drop-down menu on the navigation panel (Fig. 3).
 




 Fig. 3 Select a workplace in the expanded navigation panel
 

![scr_workplaces_menu.png](/docs/sites/en/files/images/Platform_basics/freedomUI_shell/scr_workplaces_menu.png)



 When you change a workplace, the sections available in the navigation panel also change. You can edit the indexes of workplaces and sections within workplaces. Learn more about setting up workplaces in a separate article:
 [Set up workplaces](https://academy.creatio.com/documents?id=1248) 
 . Creatio keeps the panel position, workplace, section and your scroll position on a Freedom UI page when you return to it.
 



 Use the search bar in the navigation panel to find sections within the active workplace quicker (Fig. 4).
 




 Fig. 4 Searching for a section in the navigation panel
 

![gif_section_search.gif](/docs/sites/en/files/images/Release_notes/release_notes_8_0_6/gif_section_search.gif)



 Quick actions buttons (2)
---------------------------



![btn_open_side_pannel.png](/docs/sites/en/files/images/Platform_basics/freedomUI_shell/btn_open_side_pannel.png)
 minimizes/maximizes the navigation panel. Minimize the panel to free up more workspace.
 




 Fig. 5 Minimizing the navigation panel
 

![gif_minimize_side_panel.gif](/docs/sites/en/files/images/Release_notes/release_notes_8_0_6/gif_minimize_side_panel.gif)



![btn_new_record.png](/docs/sites/en/files/images/Platform_basics/freedomUI_shell/btn_new_record.png)
 opens the quick record add menu. Select the needed menu item to open a page that adds records to the corresponding section.
 





 Note.
 
 Set up the menu structure using the
 
 Quick add menu setup
 
 lookup.
 




![btn_global_process_button.png](/docs/sites/en/files/images/Platform_basics/freedomUI_shell/btn_global_process_button.png)
 is the global process start button. If you set up one or more active processes for the button, the button displays the relevant processes in the menu. The button displays only the processes that have the
 
 Display in run process button list
 
 checkbox selected in the properties. If you do not set up any process for the button or the processes you set up are inactive, the button contains only the
 
 Other processes
 
 menu item that has the index of Creatio business processes.
 





 Note.
 
 Set up the global process start button in the
 
 Process library
 
 section. Learn more in a separate article:
 [Run a business process](https://academy.creatio.com/documents?id=7097#title-1884-3) 
 .
 




 Search bar (3)
----------------



 The search bar lets you use global search. Creatio searches for records by their text and lookup fields as well as the following details:
 
 Addresses
 
 ,
 
 Communication options
 
 , and
 
 Banking details
 
 . For example, you can find an account by its alternative name, phone number, address, or bank account number.
 



 Folder and filter area (4)
----------------------------



 The area lets you apply advanced data filters and manage the section folder tree.
 



 Working area (5)
------------------



 Depending on the section and selected view, the working area displays the following:
 


* the list of section records, for example, the contact list in the
 
 Contacts
 
 section
* the form page of the opened record
* the analytics tools of the current section
* special pages, for example, calendar in the
 
 Activities
 
 section



 Communication panel (6)
-------------------------



[Communication panel](https://academy.creatio.com/documents?id=1011) 
 in the top right lets you view and post user feed messages, manage emails, make and receive calls as well as chat with customers. Use
 ![btn_open_communication_pannel.png](/docs/sites/en/files/images/Platform_basics/freedomUI_shell/btn_open_communication_pannel.png)
 button to maximize/minimize the panel.
 



 Communication pannel in Freedom UI has some unique features:
 


* The call panel displays the agent status. Click the
 ![](/docs/sites/en/files/images/Release_notes/release_notes_8_0_6/btn_agent_status.png)
 button to change it.
* System administrator can go to telephony setup page from the communication panel in a single click with the
 ![](/docs/sites/en/files/images/Release_notes/release_notes_8_0_6/btn_set_up_telephony.png)
 button.
* The Freedom UI displays the call indicator if you go to a different communication panel tab or minimize the panel while on a call. The indicator displays the contact's full name or the phone number if the number is not linked to the contact. Click the indicator to reopen the call tab.
 




 Active call indicator
 

![scr_menu_settings_3.png](/docs/sites/en/files/images/Release_notes/release_notes_8_0_7/gif_active_call_indicator.gif)



 Notification panel (7)
------------------------



[Notification panel](https://academy.creatio.com/documents?id=1011) 
 in the top right lets you access Creatio user notifications quickly. This panel displays notifications about activities or invoices, comments to your records or mentions in a corporate social network, approvals, noteworthy events, system messages, and business process tasks. Reminders and approval notifications are active until they are processed. Feed notifications, messages about noteworthy events, and system notifications are considered read when you open the corresponding tab. The history of read notifications is stored on the tab for a month since their creation. Use
 ![btn_open_notifications.png](/docs/sites/en/files/images/Platform_basics/freedomUI_shell/btn_open_notifications.png)
 button to maximize/minimize the panel. When you have unread notifications the button is marked with red sign. Learn more about working with notifications in a separate article:
 [Check notifications and process tasks](https://academy.creatio.com/documents?id=1011) 
 .
 




