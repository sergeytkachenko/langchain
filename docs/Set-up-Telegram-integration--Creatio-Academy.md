


 Set up Telegram integration to let contact center agents process messages sent to your Telegram chatbot in Creatio.
 



 Create and set up a Telegram chatbot before configuring a Telegram channel in Creatio. Read more about creating and setting up bots in
 [Telegram documentation](https://core.telegram.org/bots) 
 .
 





 Note.
 
 Before you set up the integration in Creatio version 8.0.2 Atlas and earlier, make sure that the format of Creatio URL in the “Website URL” (“SiteUrl” code)
 [system setting](https://academy.creatio.com/documents?id=269) 
 is https://yoursite.domain.com/0.
 



 If the system setting is empty, leave it as is. In this case, Creatio will populate it when you add the channel.
 



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
 
 Channels
 
 area. Select “Telegram” in the pop-up menu. This will open a mini page with channel parameters.
4. Fill out the
 **channel parameters** 
 :
	1. Specify the
	 **token** 
	 for your chatbot. The token is generated on Telegram's end.
	2. Set the switch to “
	 **Active** 
	 ” to enable the chat message processing in the communication panel.
	3. Select the
	 **chat queue** 
	 that will process the messages that come via this channel.
	 
	
	
	 Note.
	 
	 To ensure the correct channel operation, make sure your Telegram bot is only used in a single resource. If you are not sure whether the bot is integrated with any other websites or applications, generate a new bot token before you set up the channel in Creatio.
	4. Select the expected channel message
	 **language** 
	 . This will let the agents use quick reply templates in the customer language.
5. Click
 
 Apply
 
 .
 

 Fig. 1 Setting up a Telegram channel
 


![telegram_chat_settings.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/telegram_chat_settings.png)




