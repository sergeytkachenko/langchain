


 Use Creatio chat integration functionality to communicate with customers and process service cases through the communication channels that are convenient to your customers. The company employees can send messages through the customer's communication channel of choice from the action panel in any section. Chat agents process incoming cases in the communication panel. During a chat, agents can provide consultations, share files, and run business processes using the communication panel. The chat logs are saved on the contact page.
 



 Creatio creates
 **new chats** 
 in the following cases:
 


* An incoming private message from a new customer in Facebook Messenger, WhatsApp, or Telegram (bot-only).
* A new message from an existing customer if there are no current active chats for this customer.



 In other cases, Creatio displays new messages in the active chat.
 



 Creatio adds
 **new contacts** 
 based on incoming chats if the following conditions are met:
 


* A customer sent their first message using a company page, Telegram bot, or WhatsApp.
* There are no Creatio contacts with a Facebook user ID, Telegram user ID, or WhatsApp number from the incoming message.



 When a new contact is created based on an incoming chat, Creatio will populate the following contact fields:
 


* A Facebook user's name, profile picture, and ID.
* A Telegram user's name, profile picture, and ID.
* A WhatsApp user's name, profile picture, and phone number.



 Change the agent status
-------------------------



 The agent status determines whether they can receive and process chats in the Creatio communication panel.
 


* **Active** 
 . An active agent can see new messages and chats on the communication panel, process them, and send responses.
* **Inactive** 
 . An inactive agent can only see previously received chats on the communication panel, process them, and send responses. Creatio does not distribute new chats among inactive agents.



 By default, the agent's status is “Inactive.” Change it in the communication panel or the user profile menu (Fig. 1).
 




 Fig. 1 Agent's status in the user profile
 

![set_operator_status_enu.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/set_operator_status_enu.png)



 When an agent logs out (i. e., closes the session), their status will be changed to “Inactive” automatically and new chats will not be distributed to this agent. When the agent logs back in, their status will be the same as before the logout.
 



 Process chat messages
-----------------------



 Agents can process chats using the
 
 Chats
 
 tab of the communication panel. Agents can access:
 


* **Active** 
 chats that are in progress.
* **New** 
 chats that are awaiting acceptance.
 


 Note.
 
 The time for taking a chat into processing, as well as the time limit for replying to an active chat, may be limited. Learn more in a separate article:
 [Add a chat queue](https://academy.creatio.com/documents?id=2382&anchor=title-2022-1) 
 .




 Fig. 2 Chats on Creatio communication panel
 

![chats_enu.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/chats_enu.png)



 If you permit Creatio to send you desktop notifications in your browser, you will receive a desktop alert whenever a new chat is assigned to you.
 



 To
 **start processing the chat** 
 , click
 
 Accept chat
 
 . You will become the owner of this chat. After this, you will have the following options available:
 


* Text chat messages.
* Files attached to the chat.
* Contact details.
* Chat source.
* Chat actions.



 To use a
 **quick reply template** 
 , click the
 ![btn_com_view_chat_templates.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/btn_com_view_chat_templates.png)
 button or type “//” in the reply field and proceed to enter the name or text of the template. A box with the list of
 [pre-configured chat templates](https://academy.creatio.com/documents?id=2357&anchor=title-2116-3) 
 will open (Fig. 3).
 




 Fig. 3 Quick reply template search
 

![scr_chat_templates.png](/docs/sites/en/files/images/Platform_basics/work_with_chats/scr_chat_templates.png)



 If you leave the chat without sending the reply, Creatio will save a
 **draft** 
 of your message automatically. You can get back to editing the reply at any moment after you open the chat again. The draft will appear in the reply field.
 



 To
 **run a chat action** 
 , for example, create a case, click the
 ![btn_menu.png](/docs/sites/default/files/images/2020-12/btn_menu.png)
 button in the top right corner of the communication panel, and select the action to perform (Fig. 4).
 





 Note.
 
 Learn more about setting up chat actions in a separate article:
 [Set up the chat actions](https://academy.creatio.com/documents?id=2382&anchor=title-2022-5) 
 .
 





 Fig. 4 Run a chat action
 

![perform_chat_actions_enu.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/perform_chat_actions_enu.png)



 When the conversation is over, click the
 ![btn_com_end_open_chat.png](/docs/sites/default/files/images/Platform_basics/working_with_chats/btn_com_end_open_chat.png)
 button at the top of the communication panel. Alternatively, click the
 ![btn_com_end_chat.png](/docs/sites/default/files/images/Platform_basics/working_with_chats/btn_com_end_chat.png)
 button on the communication panel to complete any active chat. You can complete a chat at any time without waiting for the timeout. If a customer sends a new message after the chat has been completed, Creatio will create a new chat and add it to the corresponding processing queue.
 



 Initiate a chat conversation
------------------------------



 In Creatio, you can not only process incoming cases but also initiate chat conversations with customers. Your company employee can contact the customer through any available chat channel as part of their workflow. This functionality is available on the
 [action panel](https://academy.creatio.com/documents?id=1765&anchor=title-2141-5) 
 of any section. For example, message the case contact, lead contact, opportunity participants, or account contacts.
 



 Click the channel button to fetch the connected contact or list of contacts you can message through the channel.
 



 You can message the customer as long as the following conditions are true:
 


* There is an active provider channel in Creatio.
* The contact messaged you through the channel at least once.
* The customer sent their last message through the channel within the last 24 hours (only for Facebook Messenger and WhatsApp).




 Fig. 5 Initiate the chat in the
 
 Opportunities
 
 section
 

![scr_start_chat_from_opportunity_page.png](/docs/sites/en/files/images/Platform_basics/work_with_chats/scr_start_chat_from_opportunity_page.png)



 If one or more conditions are false and you click the channel button, Creatio will notify you that it is not possible to message the contact.
 



 Find similar contacts
-----------------------



 Customers can reach out to you through different channels. If the same person uses multiple channels, there is a chance of creating several contact records for the same customer in Creatio. When a new chat is added, Creatio performs an automatic search for similar contacts.
 



 The search for similar contacts is performed based on the active
 [duplicate search rules](https://academy.creatio.com/documents?id=1591&anchor=title-747-10) 
 . After the search is complete, the chat window displays information about similar contact records. This enables minimizing the number of duplicates in Creatio.
 



 Click the link with the number of the detected duplicates to open the list of potential duplicate contacts on a separate page. The contact from the active chat is labeled as “Current.” Should you decide to merge the duplicates, the chat contact will be changed for a resulting record.
 




 Fig. 5 Duplicate search results
 

![merge_duplicates_enu.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/merge_duplicates_enu.png)



 Create a case from a chat
---------------------------



 The “Create case” chat action is available for the following Creatio products:
 


* Service Creatio, enterprise edition
* Service Creatio, customer center edition
* Financial services Creatio, bank customer journey edition



 If you run the action, Creatio will add a new case with the following fields populated:
 


* Subject
 
 : text of the first chat message.
* Description
 
 : text of all incoming messages received before the agent answered in the chat.
* Source
 
 : “Chat.”
* Registration date
 
 : the case creation date.
* Status
 
 : “New.”
* Contact
 
 : contact from the chat.
* Account
 
 : the account of the contact.
* Assignee
 
 : chat agent.



 Transfer the chat to another agent or queue
---------------------------------------------



 Customers might ask questions that are out of the channel scope. For example, a customer who is experiencing issues with placing an online order and wants an alternative way to place it may contact you via the tech support channel. In these cases, the agent can assist the customer with the issue and transfer the chat to a different queue. For example, the sales department. Alternatively, they can transfer the chat to a specific employee. For example, the customer’s account manager. To transfer the chat:
 


1. Open the relevant chat in the communication panel.
2. Click the
 ![](/docs/sites/default/files/images/Platform_basics/working_with_chats/btn_transfer_chat.png)
 button at the top. This will open the list of available chat queues and agents.
3. Select the queue or the agent to whom to transfer the chat in the list (Fig. 6). The list displays the status of each agent: “Active” (green indicator), “Inactive” (red indicator), or “Chats exceeded” (gray indicator). You can transfer the chat:
 


	* to active agents whose status is “Active” or “Inactive”
	* to queues that have one or more agents besides you


 Note.
 
 Creatio sets the “Chats exceeded” status automatically if the number of chats an agent is processing equals the value of the “Simultaneous Chats” (“SimultaneousChats” code)
 [system setting](https://academy.creatio.com/documents?id=1259) 
 . The default value is 5 chats. This status is displayed only in the agent list during chat transfer and cannot be set manually.
 





 Fig. 7 Transfer the chat to another agent or queue
 

![scr_transfer_chat.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/scr_transfer_chat.png)



 After the transfer, Creatio completes the current chat and automatically creates a child chat. The status of the new chat depends on the way you transfer it:
 


* If you transfer the chat to a specific employee, Creatio adds the new chat to the agent’s active chat list and sets the chat status to “In progress.”
* If you transfer the chat to a queue, Creatio sets the chat status to “Waiting for processing” and distributes the chat among the queue agents based on the queue routing rules. The chat appears in the
 
 New chats
 
 list until a specific agent accepts the chat. After the chat is accepted, Creatio changes its status to: “In progress.” After the agent opens the chat, they can access the parent chat messages and carry on the conversation.



 View chats and analytics
--------------------------



 The agent can access chat messages in the communication panel. Users that have
 [permission to read](https://academy.creatio.com/documents?id=262) 
 the “Chats” object can view both live and complete chats in the
 
 Chats
 
 section. For example, this helps managers to provide assistance without chat escalation or understand the context of issues that take multiple chats to troubleshoot. After the chat is complete, all sent messages and files become available on the
 
 Timeline
 
 tab of the corresponding contact pages as well.
 



 The
 
 Chats
 
 section also lets you view detailed information about the chats, group the chats by different parameters, view the customer communication history, analyze the customer case dynamics for a specific period, view the agent workload as well as chat processing rate.
 



 Process chats using an external chatbot
-----------------------------------------



 Use chatbots to pre-process messages incoming via the Facebook Messenger channel and reduce the load on your agents. The chatbot will provide answers to frequently asked questions, as well as pre-process requests before Creatio passes the chat to an agent. The chatbot platform can integrate with your public Facebook page and upload the processed customer requests to Creatio.
 



 Chatbots can only be used with Facebook Messenger chats. Learn more about setting up a chatbot in a separate article:
 [Set up third-party chatbot integration](https://academy.creatio.com/documents?id=2384&anchor=title-2023-14) 
 .
 



 The chatbot will process messages customers send to your public page via Facebook Messenger. Depending on the chatbot settings, the message exchange can be saved to Creatio after the chat is over or distributed to an agent.
 


### 
 Pre-process a request with the chatbot



 This logic implies that the chatbot passes the customer request to a Creatio agent who decides if further work with this chat is needed. You can use this setting for chats where customers ask non-standard questions or require access to non-public data. For example, sales contracts.
 



 Generally, the chatbot request processing looks as follows:
 


1. A new chat with the “Bot processing” state is created. The chat is available in the
 
 Chat
 
 section but is not displayed on the communication panel.
2. After Creatio takes over, it completes the chat and automatically creates a child chat with the “Waiting for processing” state.
3. The new chat is routed to an agent according to the channel settings.
4. When processing the child chat on the communication panel, the agent can access the parent chat messages. The agent can use them to decide to continue or complete the chat.
5. After the agent chat is over, Creatio hands over the chat to the prime recipient of the transfer protocol (the chatbot platform). If the customer sends a new message, a new chat will be created.


### 
 Process a request with the chatbot



 This logic implies that the chatbot processes Facebook Messenger customer requests without passing them to agents. You can use this setting to provide answers for frequently asked questions or process typical messages. For example, quote requests.
 



 Generally, the chatbot request processing looks as follows:
 


1. A new chat with the “Bot processing” state is created. The chat is available in the
 
 Chat
 
 section but is not displayed on the communication panel.
2. The chat completes automatically after the last message is sent/received. Manage the chat autocompletion time in the channel settings:
	* **At the end of the waiting time** 
	 if the queue's
	 
	 Chat completion timeout
	 
	 field is populated. Learn more in a separate article:
	 [Add a chat queue](https://academy.creatio.com/documents?id=2382&anchor=title-2022-1) 
	 .
	* **After 60 minutes** 
	 if no timeout is specified in the queue settings.
3. After the chat is over, Creatio hands over the chat to the prime recipient of the transfer protocol (the chatbot platform). The customer and bot's message history is available in the
 
 Chat
 
 section.




