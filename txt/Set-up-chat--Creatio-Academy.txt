


 Use the
 
 Chat settings
 
 section of the System Designer to set up Creatio chat and messenger integration. Chat setup is performed by the system administrator or by a user with the “Access to "Setup chats" section” (CanManageChats) operation permission.
 




 Set up a chat
 

![chats-setup_page_enu.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/chats-setup_page_enu.png)



 Add a chat queue
------------------



 To process chat messages, you need to set up chat queues. A chat queue determines the team of agents that will be processing the chat. The number of queues does not depend on the number of channels. For example, to process messages coming from the brand page, set up a “Support service” chat queue, while to process online shop requests - create a “Sales assistants” chat queue. Use the
 
 Chat settings
 
 section of the System Designer to create queues for chat agents. To add a chat queue:
 


1. Open the
 **System Designer** 
 by clicking
 ![btn_system_designer.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/btn_system_designer.png)
 .
2. Click
 
 Chat settings
 
 .
3. In the
 
 Chat queues
 
 area, click
 ![chapter_minicards_add_connections.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/chapter_minicards_add_connections.png)
 .
4. Populate the parameters of the new queue in the window that opens.
	1. Name
	 
	 – provide a name that would imply the queue purpose and the target role. For example, “1st-line support”.
	2. Routing rule
	 
	 – determines the agent who will be processing the chat.
		* “
		 **To all agents** 
		 ” – the new chat will be available for all agents of the current queue.
		* “
		 **To an available agent** 
		 ” –automatically assign the chat to the available agent for processing. The available agent is the one with the least number of chats in progress. If several agents have the same number of chats in progress, the new chat will be assigned to the agent who has not taken any chats longer than others. If an agent does not take the chat within 5 minutes, the chat will be assigned to the next agent. The current agent will become “inactive”. You can change this time using the “
		 **Omni chat operator accept chat timeout** 
		 ” (OmniChatOperatorAcceptChatTimeout) system setting. To continue processing the chat, the agent must change their status for the “Active” in the communication panel.
	3. Chat completion timeout, minutes
	 
	 – the maximum waiting time from the moment of the last outgoing chat message to closing the chat automatically. When the specified time expires, the chat will close automatically. When the chat closes due to timeout, the subsequent messages will be processed as new chats and will be redistributed to the active operators. If you do not specify any value in the field, the chat will not close.
	4. On the
	 
	 Queue agents
	 
	 detail, click
	 ![btn_chapter_mobile_wizard_new_role.png](/docs/sites/default/files/images/2020-11/btn_chapter_mobile_wizard_new_role.png)
	 . Specify the users and roles that will be processing chat messages. For example, you can use the “Call center managers” organizational role. You can add several users or roles to the list of agents. Similarly, the same user can be added as an agent to several chat queues.




 Set up a chat queue
 

![chat_queue_enu.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/chat_queue_enu.png)



 Add a chat channel
--------------------



 A chat channel displays message feed from specific sources. For example, a channel can display messages posted on a specific public Facebook page. The following chat integrations are available as channel sources in Creatio:
 


* Facebook Messenger
* Telegram (available for version 7.17.1 and up)



 The channels with at least one integrated chat cannot be deleted. If the channel is no longer valid, deactivate the channel.
 


### 
 Add Facebook Messenger channel





 ATTENTION.
 
 Before you start setting up the Facebook messenger channel, make sure the “Identity server Url (IdentityServerUrl), “Identity server client id” (IdentityServerClientId) and “Identity server client secret” (IdentityServerClientSecret) system settings are populated. If the values of these system settings are not populated, contact support assistance.
 



1. Open the
 **System Designer** 
 by clicking
 ![btn_system_designer.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/btn_system_designer.png)
 .
2. Click
 
 Chat settings
 
 .
3. In the
 
 Channels
 
 area, click
 ![chapter_minicards_add_connections.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/chapter_minicards_add_connections.png)
 . In the menu that appears, select “Facebook messenger”. Facebook login window opens.
4. In the opened Facebook window:
	1. Log in to Facebook.
	2. Select the checkboxes for the pages that you want to synchronize with Creatio. Note that you can only set up synchronization for public pages and not for personal profiles.
	3. Click
	 
	 Next
	 
	 .
	 
	
	 Select a public Facebook page to synchronize with Creatio
	 
	
	![synchronize_creatio_with_facebook_page_enu.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/synchronize_creatio_with_facebook_page_enu.png)
	4. Permit Creatio to manage your public page. This will allow the application to send and receive messages on behalf of your brand using the Facebook Messenger channel. If you restrict Creatio from managing the page, the chat functionality may not work properly.
	5. Click
	 
	 Done
	 
	 .
	   
	
	 As a result, a separate channel will be created for each of the selected pages. The channel name will match the name of the corresponding Facebook page.
	 
	
	 Set up access to managing the page
	 
	
	![setup_administrating_rights_for_page_enu.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/setup_administrating_rights_for_page_enu.png)
5. To process the messages from the created channel in the communication panel, activate the channel, and link it to the queue.
	1. In the
	 
	 Channels
	 
	 detail list, click the created channel name.
	2. On the mini page that opens:
		* Set the switch to “
		 **Active** 
		 .”
		* Select the chat
		 **queue** 
		 to process the messages that come via this channel.
		* Click
		 
		 Apply
		 
		 .
6. Repeat step 5 for all created channels if needed.


### 
 Add a Telegram channel





 Note.
 
 This functionality is available for Creatio version 7.17.1 and up.
 



1. Open the
 **System Designer** 
 by clicking
 ![btn_system_designer.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/btn_system_designer.png)
 .
2. Click
 
 System settings
 
 .
3. In the “Website URL” (SiteUrl) system setting, specify the URL of your Creatio application that will be synchronized with Telegram. To specify the URL, use the following format: https://yoursite.domain.com/0.
4. Go back to the
 **System Designer** 
 by clicking
 ![btn_system_designer.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/btn_system_designer.png)
 .
5. Click
 
 Chat settings
 
 .
6. In the
 
 Channels
 
 area, click
 ![chapter_minicards_add_connections.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/chapter_minicards_add_connections.png)
 . In the menu that appears, select “Telegram.” A mini page with channel parameters opens.
7. Populate the
 **channel parameters** 
 :
	1. Specify the
	 **token** 
	 for your chatbot. The token is generated on the Telegram side.
	2. Set the switcher to the “
	 **Active** 
	 ” position to enable processing chat messages in the communication panel.
	3. Select the chat
	 **queue** 
	 to process the messages that come via this channel.
	 
	
	
	 Note.
	 
	 To ensure the correct channel operation, make sure the telegram bot you are integrating with is only used on a single resource. If you are not sure whether the bot you are adding is integrated with any other websites or applications, generate a new bot token before you set up the channel in Creatio.
8. Click
 
 Apply
 
 .
 

 Example of setting up a Telegram channel
 

![telegram_chat_settings_enu.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/telegram_chat_settings_enu.png)



 Set up the chat actions
-------------------------



 Chat actions simplify and automate the processing of messages. A pre-configured “Create case” action (available for the Service Creatio products) triggers the “Create case from chat” (CreateCaseFromChat) business process. You can set up a list of actions that will be available for the agent when processing the chat, e.g., “Create order”, “Notify a manager about invoice payment” or “Notify system administrator.” To implement this, create a corresponding process to run when working in the chat. Learn more about creating and setting up processes in the
 [Business process setup (BPMN)](https://academy.creatio.com/docs/taxonomy/term/273) 
 block of articles. When the process is ready, add a corresponding chat action:
 


1. Open the
 **System Designer** 
 by clicking
 ![btn_system_designer.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/btn_system_designer.png)
 .
2. Click
 
 Chat settings
 
 .
3. In the
 
 Chat actions
 
 area, click
 ![chapter_minicards_add_connections.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/chapter_minicards_add_connections.png)
 .
4. On the “Chat action” mini page, specify:
	1. Caption
	 
	 – the action title that will display for the agent when working with the chat.
	2. Chat queue
	 
	 – select the chat queue. The agents of the selected queue will have access to this action.
	3. Process
	 
	 – select the process that will be triggered by the action.
	4. Click
	 
	 Apply
	 
	 .
	 
	
	 Set up a chat action
	 
	
	![setup_chat_actions_enu.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/setup_chat_actions_enu.png)
	
	
	
	
	
	 Note.
	 
	 The business process is connected to the current chat through the incoming “ChatId” and/or “ContactId” parameters that are passed to the process when running the chat action. Read more in the
	 [Process parameters](/docs/7-17/user/bpm_tools/business_process_setup/parameters/process_parameters) 
	 article.



 Set up third-party chatbot integration
----------------------------------------



 Creatio allows you to integrate third-party chatbots that will process common user requests, reducing the load on the agents. This option is only available for Facebook Messenger chats. The chatbot setup and Facebook integration procedure depend on the bot platform. These instructions are usually available in the bot platform's vendor documentation.
 



 This functionality requires:
 


* A Facebook Page.
* A working Creatio
 [Facebook Messenger channel](#title-3019-3) 
 .
* A third-party bot platform that supports the
 [Handover Protocol](https://developers.facebook.com/docs/messenger-platform/handover-protocol/) 
 and is integrated with your Facebook Page.



 To integrate Creatio with the chatbot:
 


1. Go to the “Settings” section of your Facebook page → “Advanced Messaging.”
2. Configure the “Messenger receiver” parameters in the “Connected Apps” block:
	* Primary Receiver for Handover Protocol – your bot platform
	* Secondary Receiver for Handover Protocol – Creatio Social application
	 
	
	 Fig. 3 Configuring the Messenger receiver
	 
	
	![scr_facebook_chatbot_integration_settings.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/scr_facebook_chatbot_integration_settings.png)
 As a result, the chatbot will process messages sent to your Facebook Page. Creatio will display them in the
 
 Chats
 
 section. The
 
 Agent
 
 field will be left empty for bot-processed chats.



 Additional chat settings
--------------------------


### 
 Restrict the number of active chats in the communication panel



 You can set up restrictions for the number of active chats that agents can process at a time. By default, the number of chats is restricted by 2. To change the active chat settings:
 


1. Open the
 **System Designer** 
 by clicking
 ![btn_system_designer.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/btn_system_designer.png)
 .
2. Click
 
 System settings
 
 .
3. Open the “
 **Simultaneous Chats** 
 ” (SimultaneousChats) system setting.
4. In the
 
 Default value
 
 field, specify the number of chats that the agent can process at a time. For example, 5. If an agent has a maximum number of chats in progress, they will not see any new chats until they terminate at least one of their chats. This restriction is valid for all chat channels available to the operator.
5. Click
 
 Save
 
 .


### 
 Change the chat notification alert



 You can change the standard notification alerts about new chat messages to make them easily recognizable by the agents. To do so:
 


1. Open the
 **System Designer** 
 by clicking
 ![btn_system_designer.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/btn_system_designer.png)
 .
2. Click
 
 System settings
 
 .
3. Open the “
 **Omni chat notification sound** 
 ” (OmniChatNotificationSound) system setting.
4. Click
 
 Clear value
 
 to delete the standard alert.
5. Select a local audio file
 
 .
6. Click
 
 Save
 
 .




