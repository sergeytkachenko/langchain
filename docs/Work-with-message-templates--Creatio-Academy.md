


 In Creatio, you can design the message content from scratch or tailor an existing template to the recipient. Use templates to send emails as part of business processes, automatic notifications, and quick replies in chats. Configure all templates in the
 
 Message templates
 
 section. By default, the templates are created in the default application language. If you want to localize your templates, set up a template in the default language first. You can copy the base template settings to other languages when you add localizations later.
 



 Set up a message template
---------------------------


### 
 Set up an email template


1. Go to the
 
 Studio
 
 workplace and click
 
 Message templates
 
 .
2. Click
 
 New
 
 and select “Email template” in the menu.
3. Specify the template name on the opened page. For example, “Date and time of the meeting.”
4. Specify the macro source. For example, “Activity.”
5. Click
 
 Edit
 
 on the
 
 Email template
 
 detail. The Content Designer will open. By default, the templates are created in the default application language. If you want to localize your template,
 [add localizations](#title-2050-4) 
 to the template after the initial setup.
6. Fill out the email subject in the Content Designer.
7. Drag the
 
 Block
 
 element to the working area.
8. Drag the
 
 Text
 
 element to the block.
9. Replace the
 
 Text
 
 element's placeholder content with the desired message.
10. If necessary, insert macros to personalize the message with the sender or recipient’s data.
 


	1. Place the cursor where you want to insert the macro.
	2. Click
	 ![btn_text_macros.png](/docs/sites/en/files/images/Platform_basics/template_setup/btn_text_macros.png)
	 →
	 
	 Basic macro
	 
	 .
	3. In the popup, pick a macro and click
	 
	 Select
	 
	 .
11. Save the template.



 As a result, Creatio will create a new “Date and time of the meeting” email template. Learn more about using email templates:
 [Send a template-based email](/docs/7-17/user/platform_basics/communications/emails/working_with_emails#title-749-2) 
 .
 





 Note.
 
 Learn more about the Content Designer and working on complex templates:
 [Email templates](https://academy.creatio.com/docs/user/marketing_tools/email_marketing/email_templates) 
 .
 



### 
 Set up a chat template


1. Go to the
 
 Studio
 
 workplace and click
 
 Message templates
 
 .
2. Click
 
 New
 
 and select “Chat template” in the menu.
3. Specify the template’s name on the opened page. For example, “Greeting.”
4. Make sure that the macro source is “Chat.”
5. Enter the message in the
 
 Chat template
 
 detail. If you want to localize your template,
 [add localizations](#title-2050-4) 
 to the template after the initial setup.
6. If necessary, insert macros to personalize the message with the sender or recipient’s data.
 


	1. Place the cursor where you want to insert the macro.
	2. Click
	 ![btn_text_macros.png](/docs/sites/en/files/images/Platform_basics/template_setup/btn_text_macros.png)
	 →
	 
	 Basic macro
	 
	 .
	3. In the popup, pick a macro and click
	 
	 Select
	 
	 .
7. Save the template.



 As a result, Creatio will create a new chat message template. Learn more about using chat templates:
 [Work with chats](/docs/7-17/user/platform_basics/communications/chats/work_with_chats#title-1814-2) 
 .
 



 Set up template localization
------------------------------



 Use localized templates to send messages to your customers in their preferred language. You can use this functionality:
 


* in chats
* when sending template-based emails from the action panel or communication panel
* when sending notifications about business processes



 Take the following steps to set up localized messages:
 


1. Set up the languages that will be used for your communication with customers.
 [Read more >>>](#title-2050-5) 
 <
2. Create localized templates.
 [Read more >>>](#title-2050-6)



 To determine the language of an template sent to a customer, Creatio verifies:
 


1. Whether the
 
 Preferred language
 
 field is filled out on the contact page.
 


	1. If the field is filled out, Creatio will send the template in the specified language to the recipient.
	2. If the field is not filled out, Creatio will switch to the next verification stage.
2. Whether the language of the chat channel or mailbox is specified (only for Service Creatio products).
 


	1. If the chat (mailbox) language is specified, Creatio will send the template in this language to the recipient.
	2. If the chat (mailbox) language is not specified, Creatio will switch to the next verification stage.
3. Whether the “Default language for messages” (“DefaultMessageLanguage” code) system setting is filled out.
 


	1. If the system setting is filled out, Creatio will send the template in the specified language to the recipient.
	2. If the system setting is not filled out, Creatio will send the email in the default Creatio language to the recipient.





 Note.
 
 If you specify contacts with different languages or contacts without the preferred language in the
 
 To
 
 field when sending multilingual messages as part of a business process, Creatio will send the template in the default language to all recipients.
 



### 
 Set up preferred languages



 Specify the preferred language on the contact page in the
 
 Contacts
 
 section. Creatio will send email notifications in this language to the contact. The preferred language does not depend on the UI languages configured for user operation or the default Creatio language.
 



 The
 
 Customer languages
 
 lookup values are used to specify languages and generate multilingual templates.
 


* Only the languages with the
 
 Is used
 
 checkbox selected in the
 
 Customer languages
 
 lookup are available for selection on the contact page.
* By default, all languages listed in the lookup are available for use in message templates. If you add an inactive language to a template, the
 
 Active
 
 checkbox will be selected for this language in the
 
 Customer languages
 
 lookup.



 The deactivated language becomes unavailable in the
 
 Preferred language
 
 field menu on the contact page but is still displayed if it was specified earlier. The chat or email template tab in such language is hidden, but messages will still be sent if this language is specified on the contact page.
 



 If you reactivate a language, all the earlier created templates will be displayed in the lookup.
 


### 
 Create a localized message template



 You can set up a localized chat or email message template in the
 
 Message templates
 
 lookup.
 



 To create a localized template:
 


1. Go to the
 
 Studio
 
 workplace and click
 
 Message templates
 
 .
2. Select the template to which you want to add localizations.
3. Click the
 ![btn_com_menu_gear.png](/docs/sites/en/files/images/Platform_basics/template_setup/btn_com_menu_gear.png)
 button. In the menu, you will see all languages with the
 
 Active
 
 checkbox selected in the
 
 Languages
 
 lookup. Select a template language you want to add.
 



 If there are no active languages in Creatio yet or you want to add a tab with the language that has not been activated, select the
 
 Add language
 
 option (Fig. 1) and select the template language you want to add in the opened window. The
 
 Active
 
 checkbox for this language will be selected automatically.
 




 Fig. 1 Add a language to the template
 

![chapter_emails_add_template_language.png](/docs/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/chapter_emails_add_template_language.png)
4. After you select a language, Creatio will prompt you to copy the content of an existing template to the new tab. Select this option if you need to use the configured layout for the added localization.
5. If you need to add several languages into a template, take steps 3 and 4 for each localization. As a result, several tabs for creating messages in the selected languages will be displayed on the template page (Fig. 2).
 




 Fig. 2 A localized template
 

![chapter_emails_empty_multilanguage_template.png](/docs/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/chapter_emails_empty_multilanguage_template.png)
6. Select the needed tab and edit the content. Create a message in each of the languages in a similar way.
7. Save the changes.
 





 Note.
 
 If you copy a multilingual template, Creatio will copy all of its saved localizations.




