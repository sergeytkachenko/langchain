


 Adding an
 **unsubscribe link** 
 in each email is important to ensure its successful delivery. Emails that do not contain unsubscribe links can be blocked by the marketing email provider.
 



 The unsubscribe link is required in the email template. If you try to save a template without an unsubscribe link, it will be added to the template automatically.
 



 After clicking the unsubscribe link, recipients are forwarded to the URL of the
 **unsubscribe page** 
 . You can either generate it on your web site or use the Creatio pre-configured page. If you decide to use your own page, make sure you specify its URL in Creatio. Before the unsubscribe page is displayed, a recipient is automatically forwarded to the Creatio server, where the information about the canceled subscription is stored.
 



 Set up a redirection page for the recipients who unsubscribed
---------------------------------------------------------------



 You can use the following options for an unsubscribe page:
 


* Auto-generated Creatio unsubscribe page containing text: “You have unsubscribed from further emails. Your email was successfully deleted from our mailing list."
* any other page configured on your web site. There are no specific requirements for the design of this page. The recipient unsubscribes upon clicking the unsubscribe link. The “Do not use email” checkbox is selected automatically on the contact page.



 If you have your own unsubscribe page, you need to specify the address in Creatio. To do so:
 


1. Open the system designer by clicking the
 ![btn_system_designer.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_emails_unsubscribe/btn_system_designer.png)
 button.
2. Click “
 **System settings** 
 ” in the “System setup” block.
3. Select the “Email section settings” folder and open the “
 **Website to redirect the unsubscribed** 
 ” (“RedirectUnsuscribersTo” code)) system setting.
4. Specify the URL of your unsubscribe page in the
 
 Default value
 
 field, e. g., http://www.mysite.com/act/unsubscribe/ and save the setting.
 



 The value of this system setting is empty by default. To redirect the unsubscribed, Creatio uses the auto-generated unsubscribe page.
 



 If you clear the value in the "Website to redirect the unsubscribed” system setting, the unsubscribed link will open a default auto-generated page without any additional settings.



 Add an unsubscribe link to a template
---------------------------------------



 You can add an unsubscribe link to a template in multiple ways:
 


* Use a default unsubscribe link in the template. Creatio asks whether you want to add the link when you save a template that has no unsubscribe link (Fig. 1).
 

 Fig. 1 Saving a template without an unsubscribe link
 

![gif_saving_a_template_without_an_unsubscribe_link.gif](/sites/en/files/images/Marketing_Tools/set_up_an_unsubscribe_link_in_emails/gif_saving_a_template_without_an_unsubscribe_link.gif)
* Add an existing block that has an unsubscribe link to the template (Fig. 2).
 

 Fig. 2 Block that has an unsubscribe link
 

![section_email_unsubscribe_link_macros.png](/sites/en/files/images/Marketing_Tools/set_up_an_unsubscribe_link_in_emails/scr_block_that_has_an_unsubscribe_link.png)
* Add a custom unsubscribe macro to a content block.



 You can save the content block that has a custom unsubscribe macro for use in other emails. Learn more in a separate article:
 [Save a content block for use in other emails](https://academy.creatio.com/documents?id=2067) 
 .
 


### 
 Add a custom unsubscribe macro as a URL


1. Open the email template in the Content Designer.
2. Set the cursor where you want to place an unsubscribe link.
3. Click
 ![btn_chapter_content_designer_macros.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_emails_unsubscribe/btn_chapter_content_designer_macros.png)
 and select
 
 Basic macro
 
 .
4. Select the “URL” unsubscribe macro and click the
 
 Select
 
 button (Fig. 3).
 




 Fig. 3 Add an unsubscribe macro
 

![section_email_unsubscribe_link_macros.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_emails_unsubscribe/section_email_unsubscribe_link_macros.png)
5. Save the template.
 



 As a result, the URL unsubscribe macro will be added to the email template. When sending emails, the unsubscribe macro is converted into an unsubscribe link, e.g., http://www.mysite.com/act/unsubscribe/.


### 
 Add a custom unsubscribe macro as a hypertext link


1. Open the email template in the Content Designer.
2. Select the text that serves as a hyperlink to the unsubscribe page. This brings up a toolbox.
3. Click the
 ![btn_chapter_content_designer_image_element_link.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_emails_unsubscribe/btn_chapter_content_designer_image_element_link.png)
 button.
4. Specify the
 
 #Unsubscribe.URL#
 
 macros in the
 
 Link
 
 field and click
 
 OK
 
 (Fig. 4).
 




 Fig. 4 Add an unsubscribe macro as a hypertext link
 

![section_email_unsubscribe_link_text_hyperlink.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_emails_unsubscribe/section_email_unsubscribe_link_text_hyperlink.png)



 As a result, the selected text will serve as a hyperlink to the unsubscribe page.
 



 You can also import templates as HTML elements into the Content Designer if a complex HTML layout is used. You need to specify the unsubscribe link as a text macro
 
 #Unsubscribe.URL#
 
 . When sending emails, the unsubscribe macro is converted into an unsubscribe link, e.g., http://www.mysite.com/act/unsubscribe/.
 




