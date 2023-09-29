


 If you use several types of content in your marketing emails, for example, newsletters, special offers and invitations, we recommend enabling subscriptions for particular content types. As a result, your customers will receive only the content that they are interested in. For example, a customer may sign up for special offers, but not give consent to receive news and invitations.
 





 Attention.
 
 Subscriptions to different types of marketing emails are not available in the base Creatio configuration. An additional setup by a software developer is required.
 




 Custom unsubscribe page must meet the following criteria:
 


* There must be a single page for the subscription setup. Users must not open additional pages to manage subscriptions to different types of marketing emails or unsubscribe from them.
* There must be an option to unsubscribe from all emails.



 Additional recommendations:
 


* Brand the page by adding corporate name an logo.
* The page should have an option to provide comments as to the reason for unsubscribing.
* Make user authentication optional.



 Below is a general description of the setup process for subscriptions to different emails.
 


1. Create a list of the email types in the
 **Email type** 
 lookup.
2. Create pages on your website where the customer can express their consent to receive particular materials from your company. Set them up as the forwarding pages on your landings.
3. Clear the checkbox for the “
 **Unsubscribe user from all emails** 
 ” (UnsubscribeFromAllMailings) system setting. This is required to avoid automatic unsubscribes from all emails when a recipient only unsubscribes from a particular type of email.
 





 Note.
 
 The "Unsubscribe user from all emails” (UnsubscribeFromAllMailings) system setting is used for adding the automatic unsubscribe block to the email template and the correct functioning of the unsubscribe link. It is recommended to clear the value of this system setting unless you set up different types of emails as part of developer customization.
4. Specify the address of the unsubscribe page in the “Website to redirect unsubscribed” system setting.
5. Set up the integration of the created page with Creatio. Such integration is performed by Creatio development tools.
 



 After the setup is complete, information about subscription limitations for different types of email will be displayed on the
 **Email subscription** 
 detail of the contact page. You can also use the
 
 Email subscription
 
 detail to manually specify the email types that the user has unsubscribed from on the
 
 Email subscription
 
 detail of the contact page.




