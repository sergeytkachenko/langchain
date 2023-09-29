


 WhatsApp is a Facebook product. Due to this, you need the following to integrate this messenger:
 


* A
 **Facebook Business Manager** 
 account. If you have not signed up yet, follow the
 [Facebook instructions](https://www.facebook.com/business/help/1710077379203657?id=180505742745347) 
 .
* Integration with a Facebook partner platform that provides access to WhatsApp Business API. You can use
 **Twilio** 
 .



 You can sign up for a trial account with limited functionality to
 **get acquainted** 
 with the WhatsApp integration features.
 **Verify your accounts** 
 to take full advantage of WhatsApp integration. This will help you secure your and your customers' data. In general, the WhatsApp integration setup consists of the following steps:
 


1. Set up a Twilio free trial account to get acquainted with the integration (optional).
 [Read more >>>](/docs/7-17/user/setup_and_administration/base_integrations/set_up_chats/set_up_whatsapp/set_up_whatsapp_integration#title-2025-1)
2. Set up a Twilio business account.
 [Read more >>>](/docs/7-17/user/setup_and_administration/base_integrations/set_up_chats/set_up_whatsapp/set_up_whatsapp_integration#title-2025-4)
3. Set up a WhatsApp chat channel in Creatio.
 [Read more >>>](/docs/7-17/user/setup_and_administration/base_integrations/set_up_chats/set_up_whatsapp/set_up_whatsapp_integration#title-2025-5)



 File transfer in WhatsApp channel is
 **limited** 
 to:
 


* **Receiving files** 
 . At the moment, Creatio only works with incoming files, sending files is not available.
* **File size** 
 up to 16 Mb.
* **File formats** 
 :
 


	+ Images: \*.jpg, \*.jpeg, \*.png.
	+ Audio files: \*.mp3, \*.ogg, \*.amr.
	+ Documents: \*.pdf.
	+ Videos: \*.mp4.



 Learn more about supported file formats in
 [Twilio documentation](https://www.twilio.com/docs/whatsapp/guidance-whatsapp-media-messages) 
 .
 





 Note.
 
 Twilio is partnered with telecom service providers in a limited number of countries. View the country list in
 [Twilio documentation](https://support.twilio.com/hc/en-us/articles/115000781088-International-Porting-Process) 
 . Besides the specified countries, Twilio has no restrictions on US phone numbers. If your number is not eligible, follow
 [Twilio instructions](https://support.twilio.com/hc/en-us/articles/360052171393-Can-I-activate-my-own-phone-number-for-WhatsApp-on-Twilio-) 
 .
 




 Step 1. Set up a trial account (optional)
-------------------------------------------



 You can set up a Twilio free trial account without verification and subscription to paid platform services. This will let you test Creatio WhatsApp integration, including messaging and file transfer. To set up the test integration:
 


1. Set up a Twilio free trial account.
 [Read more >>>](/docs/7-17/user/setup_and_administration/base_integrations/set_up_chats/set_up_whatsapp/set_up_whatsapp_integration#title-2025-2)
2. Set up a WhatsApp chat channel in Creatio
 [Read more >>>](/docs/7-17/user/setup_and_administration/base_integrations/set_up_chats/set_up_whatsapp/set_up_whatsapp_integration#title-2025-3)


### 
 Set up a Twilio free trial account


1. Sign up on https://www.twilio.com/try-twilio. You will be able to set up a test integration after the signup. Twilio will grant you limited virtual funds to help you review the functionality.
 





 Note.
 
 Should you decide to convert the account to a full-fledged business account, the trial features and virtual funds will become unavailable. We recommend using separate accounts for working and testing purposes.
2. Specify the endpoint URL for transferring chats to Creatio. To do this, navigate to the sandbox settings in Twilio:
 



[Twilio Console](https://www.twilio.com/console) 
 → Programmable Messaging → Settings → WhatsApp Sandbox Settings → Sandbox Configuration and enter the “https://sm-receiver.creatio.com/api/webhook/LeadGen/whatsapp” value in the
 
 WHEN A MESSAGE COMES IN
 
 field.
3. Set up the Twilio sandbox:
 [Twilio Console](https://www.twilio.com/console) 
 → Programmable Messaging → Try it out → Send a WhatsApp message.
4. Twilio will generate a code. Send the code from your phone number to your trial account number using WhatsApp. Twilio will notify you upon success. As a result, Twilio will add your number to Sandbox Participants.
5. If you would like to use several test numbers, repeat step 3 for each of them. To review the test numbers in the Sandbox Participants list, go to Twilio Console → Programmable Messaging → Settings → WhatsApp Sandbox Settings → Sandbox Participants. After that your trial account number will be able to receive messages from the numbers you added in the previous step.


### 
 Set up a test WhatsApp channel in Creatio



 Before you start setting up the WhatsApp channel, make sure the “Identity server Url” (“IdentityServerUrl” code), “Identity server client id” (“IdentityServerClientId” code), and “Identity server client secret” (“IdentityServerClientSecret” code) system settings are populated. If the values of these system settings are not populated, contact Creatio support.
 


1. Click the
 ![btn_system_designer.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/btn_system_designer.png)
 button to open the
 **System Designer** 
 .
2. Click
 
 Chat settings
 
 .
3. Click
 ![btn_chapter_mobile_wizard_new_role.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/btn_chapter_mobile_wizard_new_role.png)
 button in the
 
 Channels
 
 area. Select “WhatsApp” in the pop-up menu. This will open a mini page with the channel parameters.
4. Fill out the
 **channel parameters** 
 :
	1. Phone number
	 
	 – your Twilio free trial account phone number.
	2. Verification phone number
	 
	 – a phone number included in the Sandbox Participants list in Twilio.
	3. Application Id
	 
	 – the Twilio free trial account SID specified in the
	 
	 ACCOUNT SID
	 
	 field of the Twilio Console.
	4. Token
	 
	 – the token Twilio generates for the trial account. Specified in the
	 
	 AUTH TOKEN
	 
	 field of the Twilio Console.
5. Click
 
 Connect
 
 .
6. Activate the chat channel. In the mini page that opens:
	1. Set the switch to
	 
	 Active
	 
	 .
	2. Select the
	 **chat queue** 
	 that will process the messages that come via this channel.
	3. Click
	 
	 Apply
	 
	 .



 As a result, Creatio will connect a test WhatsApp channel. You will be able to receive and process test messages and files.
 



 Step 2. Set up a business account
-----------------------------------



 Sign up for Twilio and complete the verification to take advantage of all Twilio business features. Learn more in
 [Twilio documentation](https://www.twilio.com/docs/whatsapp/tutorial/connect-number-business-profile) 
 .
 



 The general setup procedure is as follows:
 


1. Sign up for
 [Facebook Business Manager](https://business.facebook.com/overview) 
 .
	1. If your company
	 **already has an account** 
	 , proceed to step 2.
	2. If your company
	 **does not have an account yet** 
	 , follow the instructions in
	 [Facebook documentation](https://www.facebook.com/business/help/1710077379203657?id=180505742745347) 
	 .
2. Sign up for
 [Twilio](https://www.twilio.com/) 
 .
3. Specify the endpoint URL for transferring chats to Creatio. To do this, navigate to the sandbox settings in Twilio:
 



[Twilio Console](https://www.twilio.com/console) 
 → Programmable Messaging → Settings → WhatsApp Sandbox Settings → Sandbox Configuration and enter the “https://sm-receiver.creatio.com/api/webhook/LeadGen/whatsapp” value in the
 
 WHEN A MESSAGE COMES IN
 
 field.
4. Verify your Twilio number with WhatsApp.
 
	1. [Request WhatsApp](https://www.twilio.com/whatsapp/request-access) 
	 to enable your Twilio number.
	 Select “
	 **No** 
	 ” in the
	 
	 Are you working with an ISV, SI, or third party
	 
	 field. After you send the request, Twilio will send an initial confirmation email describing your further steps to the email address specified in the form.
	2. Add the
	 **phone number** 
	 :
	 
	
	
	
	 Go to Twilio Console → Programmable Messaging → Senders → WhatsApp Senders and click the
	 
	 New WhatsApp Sender
	 
	 button.
	 
	
	
	
	 You can use
	 [your own phone number](https://support.twilio.com/hc/en-us/articles/360052171393-Can-I-activate-my-own-phone-number-for-WhatsApp-on-Twilio-) 
	 or buy a
	 [Twilio number](https://www.twilio.com/console/phone-numbers/search) 
	 .
	 
	
	
	
	
	
	 Note.
	 
	 Follow WhatsApp
	 [display name guidelines](https://developers.facebook.com/docs/whatsapp/guides/display-name/) 
	 when filling out your profile.
	3. Allow Twilio to
	 **send messages** 
	 on your behalf. To do so, go to Facebook Business Manager and approve Twilio's request to send messages on your company's behalf. To approve the request:
		* Go to business.facebook.com → Settings → Business Settings → Requests
		* Follow the link in the initial phone number confirmation email
	4. **Verify the company** 
	 with Facebook Business Manager. If you have already verified your company, proceed to the next step. To verify your company:
	 
	
	
	
	 Go to Facebook Business Manager → Settings → Business Settings → Security Center and click the
	 
	 Start verification
	 
	 or
	 
	 Continue
	 
	 button in the
	 
	 Business Verification
	 
	 section.
	 
	
	
	
	 Learn more about verifying the business in
	 [Facebook documentation](https://www.facebook.com/business/help/2058515294227817?id=180505742745347) 
	 .
	5. Follow the link in the email from Twilio to confirm the registration.



 As a result, you will be able to communicate with customers using WhatsApp via the registered number within 24 hours after the verification.
 



 Step 3. Add a WhatsApp channel to Creatio
-------------------------------------------



 Before you start setting up the WhatsApp channel, make sure the “Identity server Url” (“IdentityServerUrl” code), “Identity server client id” (“IdentityServerClientId” code), and “Identity server client secret” (“IdentityServerClientSecret” code) system settings are populated. If the values of these system settings are not populated, contact Creatio support.
 


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
 
 area. Select “WhatsApp” in the pop-up menu. This will open a mini page with channel parameters.
4. Fill out the
 **channel parameters** 
 :
	1. Phone number
	 
	 – the phone number connected to and verified with Twilio.
	2. Verification phone number
	 
	 – the phone number to which Creatio will send the channel verification message.
	3. Application Id
	 
	 – the Twilio account SID specified in the
	 
	 ACCOUNT SID
	 
	 field of the Twilio Console.
	4. Token
	 
	 – the token Twilio generated for your account. Specified in the
	 
	 AUTH TOKEN
	 
	 field of the Twilio Console.
5. Click
 
 Connect
 
 .
 

 Fig. 1 Setting up a WhatsApp channel
 

![scr_setup_chat_channel_whatsapp.png](/docs/sites/en/files/images/Setup_and_Administration/Chats/scr_setup_chat_channel_whatsapp.png)
6. If the channel is verified successfully, Creatio will open a channel edit mini-page. To process messages from the new channel in the communication panel, activate the channel and link it to a queue. To do so:
 


	1. Set the switch to
	 
	 Active
	 
	 .
	2. Select the
	 **chat queue** 
	 that will process the messages that come via this channel.
	3. Select the expected channel message
	 **language** 
	 . This will let the agents use quick reply templates in the client language.
	4. Click
	 
	 Apply
	 
	 .



 This will connect a WhatsApp channel to Creatio. Contact center agents will be able to process messages received via this channel in the communication panel and view the chat history in the
 
 Chats
 
 section.
 





 Note.
 
 Keep in mind that you can only connect a single WhatsApp number to a single Creatio application. If you add the number to several applications, e.  g., development, testing, and production environments, only the last integrated instance will receive messages.
 





