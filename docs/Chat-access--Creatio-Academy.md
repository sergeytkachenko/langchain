


 To manage Facebook Messenger and WhatsApp chat channels in Creatio on-site:
 


* Switch Creatio from HTTP to HTTPS. Learn more in a separate article:
 [Switch a Creatio website from HTTP to HTTPS](https://academy.creatio.com/docs/node/272) 
 .
* Set up access to the chat service at https://sm-account.creatio.com/ on the application server.
* Set up an incoming connection to HTTPS protocol and protection by a valid certificate for the sm-account.creatio.com chat service on the application server.



 To manage Telegram chat channels, make sure the application server has internet access.
 



 If your Creatio application uses two-factor authentication, grant FacebookOmnichannelMessagingService, TelegramOmnichannelMessagingService, WhatsappOmnichannelMessagingService services access to incoming requests.
 




