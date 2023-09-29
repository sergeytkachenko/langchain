


 Set up chats to let your company's contact center agents process messages from popular chat applications in Creatio. The general chat setup procedure is as follows:
 


1. **Add and set up a chat queue** 
 . Create a list of agents who will process chat messages, set up the message routing rules, and modify the chat completion timeout time on this step.
2. **Set up the chat actions** 
 . Set up a list of actions an agent can take after talking to the customer on this step. For example, create a case, issue an order, or send an email with more information.
3. **Limit the number of active chats** 
 . Specify the maximum number of active chats agents can see on the communication panel on this step.
4. **Change the notification alert** 
 for new chat messages (optional). Set up a new chat message alert agents can easily recognize on this step.
5. **Add the chat channels** 
 . A chat channel displays a message feed from specific sources, e. g., a Facebook Page. The following chat integrations are available as channel sources in Creatio:
 


	* [Facebook messenger](https://academy.creatio.com/documents?id=2384)
	* [Telegram](https://academy.creatio.com/documents?id=2354)
	* [WhatsApp](https://academy.creatio.com/documents?id=2355)
 The channels with at least one chat in Creatio cannot be deleted. If the channel is no longer relevant, deactivate the channel.



 Use the
 
 Chat settings
 
 section of the System Designer to set up Creatio chat and messenger integration. Chat setup is performed by the system administrator or by a user with the “Access to "Chat settings" section” (“CanManageChats” code) operation permission.
 




 Fig. 1 Set up chat
 

![chats-setup_page_enu.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/chats-setup_page_enu.png)



 Add a chat queue
------------------



 To process chat messages, you need to set up chat queues. A chat queue determines the team of agents that will be processing the chat. The number of queues does not depend on the number of channels. For example, set up a “Support service” chat queue to process messages coming from the brand page. Set up a “Sales assistants” chat queue to process online store requests. Use the
 
 Chat settings
 
 section of the System Designer to create queues for chat agents. To add a chat queue:
 


1. Click the
 ![btn_system_designer.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/btn_system_designer.png)
 button to open the
 **System Designer** 
 .
2. Click
 
 Chat settings
 
 .
3. Click the
 ![](/docs/sites/en/files/images/Setup_and_Administration/Chats/chapter_minicards_add_connections.png)
 button in the
 
 Chat queues
 
 area.
4. Fill out the parameters of the new queue in the window that opens.
	1. Enter a name that implies the queue purpose and the target role in the
	 
	 Name
	 
	 parameter. For example, “1st-line support.”
	2. Set how to determine the agent to process the chat in the
	 
	 Routing rule
	 
	 parameter.
		* Select “
		 **To all agents** 
		 ” to make the new chat available to all agents of the current queue.
		* Select “
		 **To an available agent** 
		 ” to automatically assign the chat to an available agent. The available agent is the one with the least number of chats in progress. If several agents have the same number of chats in progress, the new chat will be assigned to the agent who has not taken any chats longer than others. If an agent does not take the chat within 5 minutes, the chat will be assigned to the next agent. The current agent will become “Inactive.” You can change this time using the “
		 **Omni chat operator accept chat timeout** 
		 ” (“OmniChatOperatorAcceptChatTimeout” code) system setting. The agent must change their status to “Active” in the communication panel to continue processing chats.
	3. Set the maximum waiting time from the moment of the last chat message to automatic chat closure in the
	 
	 Chat completion timeout, minutes
	 
	 parameter. When the specified time expires, the chat closes automatically. When the chat closes due to timeout, the subsequent messages are processed as new chats and redistributed to the active agents. If you do not specify any value in the field, the chat does not close.
	4. Click the
	 ![](/docs/sites/en/files/images/Setup_and_Administration/Chats/btn_chapter_mobile_wizard_new_role.png)
	 button in the
	 
	 Queue agents
	 
	 detail. Specify the users and roles that will be processing chat messages. For example, you can use the “CC agents” organizational role. You can add several users or roles to the list of agents. Similarly, the same user can be added as an agent to several chat queues.




 Fig. 2 Set up a chat queue
 

![chat_queue_enu.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/chat_queue_enu.png)



 Set up the chat actions
-------------------------



 Chat actions streamline and automate message processing. A preconfigured “Create case” action (available for the Service Creatio products) triggers the “Create case from chat” (CreateCaseFromChat) business process. You can set up a list of actions that will be available to the agent when processing the chat, e. g., “Issue an order,” “Notify a manager about invoice payment,” or “Notify the system administrator.” To implement this, create a corresponding process to run when working in the chat. Learn more about creating and setting up processes in the
 [Business process setup (BPMN)](https://academy.creatio.com/docs/user/bpm_tools/business_process_setup) 
 block of articles. When the process is ready, add a corresponding chat action:
 


1. Click the
 ![btn_system_designer.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/btn_system_designer.png)
 button to open the
 **System Designer** 
 .
2. Click
 
 Chat settings
 
 .
3. Click the
 ![btn_chapter_mobile_wizard_new_role.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/btn_chapter_mobile_wizard_new_role.png)
 button in the
 
 Chat actions
 
 area.
4. Specify the following on the “Chat action” mini page:
	1. Enter the action title the agent sees when working with the chat in the
	 
	 Caption
	 
	 parameter.
	2. Select the queue whose agents can use the action in the
	 
	 Queue
	 
	 parameter.
	3. Select the process the chat action triggers in the
	 
	 Process
	 
	 parameter.
	4. Click
	 
	 Apply
	 
	 .
	 
	
	 Fig. 3 Set up a chat action
	 
	
	
	![setup_chat_actions_enu.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/setup_chat_actions_enu.png)
	
	
	
	
	
	
	 Note.
	 
	 The business process is connected to the current chat via the incoming “ChatId” and/or “ContactId” parameters that are passed to the process when running the chat action. Learn more in a separate article:
	 [Process parameters](https://academy.creatio.com/documents?id=7054) 
	 .



 Restrict the number of active chats in the communication panel
----------------------------------------------------------------



 You can set up restrictions for the number of active chats that agents can process at a time. By default, the number of chats is restricted by 2. To change the active chat settings:
 


1. Click the
 ![btn_system_designer.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/btn_system_designer.png)
 button to open the
 **System Designer** 
 .
2. Click
 
 System settings
 
 .
3. Open the “
 **Simultaneous Chats** 
 ” (“SimultaneousChats” code) system setting.
4. Specify the number of chats that the agent can process at a time in the
 
 Default value
 
 field. The number is 5 by default. If an agent has a maximum number of chats in progress, they will not see any new chats until they terminate at least one of their chats. This restriction is valid for all chat channels available to the agent.
5. Click
 
 Save
 
 .



 Change the chat notification alert
------------------------------------



 You can change the standard notification alert about new chat messages to help the agents easily recognize them. To do so:
 


1. Click the
 ![btn_system_designer.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/btn_system_designer.png)
 button to open the
 **System Designer** 
 .
2. Click
 
 System settings
 
 .
3. Open the “
 **Omni chat notification sound** 
 ” (“OmniChatNotificationSound” code) system setting.
4. Click
 
 Clear value
 
 to delete the standard alert.
5. Click
 
 Select file
 
 and upload a file from your computer.
6. Click
 
 Save
 
 .




