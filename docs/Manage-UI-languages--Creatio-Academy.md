


 Creatio supports localization into multiple languages. You can manage the list of languages in the system designer of the
 
 Languages
 
 section.
 





 Note.
 
 Access to the list of languages and translation is configured using the “Access to “Languages” section” and “Access to “Translation” section” system operations. Setting up permissions for various operations is described in a separate
 [article](https://academy.creatio.com/documents?product=administration&ver=7&id=258) 
 .
 





 Creatio interface is translated into following languages:
 





|  |  |
| --- | --- |
| 
english_US.png
 English (United States)
  | 
dutch.png
 Dutch (The Netherlands)
  |
| 
portuguese.png
 Portuguese (Brazil)
  | 
Portuguese_Portugal.png
 Portuguese (Portugal)
  |
| 
arabian.png
 Arabic (Saudi Arabia)
  | 
romanian.png
 Romanian (Romania)
  |
| 
Korean.png
 Korean (Korea)
  | 
Portuguese_Portugal.png
 Russian
  |
| 
hebrew.png
 Hebrew (Israel)
  | 
thailand.png
 Thai (Thailand)
  |
| 
spanish.png
 Spanish (Spain)
  | 
ukrainian.png
 Ukrainian (Ukraine)
  |
| 
italian.png
 Italian (Italy)
  | 
french.png
 French (France)
  |
| 
german.png
 German (Germany)
  | 
czech.png
 Czech (Czech Republic)
  |
| 
polish.png
 Polish (Poland)
  | 
sweden.png
 Swedish (Sweden)
  |
| 
Portuguese_Portugal.png
 Albanian (Albania)
  | 
Vietnamese.png
 Vietnamese (Vietnam)
  |




 All localization tools are built-in, there is no need to install or set up additional software in Creatio. Translation of the interface and other elements is performed in the
 
 Translation
 
 section.
 





 Note.
 
 If the needed language is present in the list above but is not available in the
 
 Languages
 
 section, contact Creatio technical support. Indicate Creatio version and product you use in your request.
 




 Enable UI language
--------------------



 Only English language is available in the user profile by default. You need to enable the needed languages in the
 
 Languages
 
 section to add them to the list of languages in the user profile.
 





 Note.
 
 If you use a load balancer to ensure fault tolerance of your Creatio application, perform the setup on one Creatio instance, then transfer settings to other instances. The setup process applies to Marketplace apps, custom packages, and other settings that require compilation. Learn more in a separate article:
 [Compile an app on a web farm](https://academy.creatio.com/documents?id=2410) 
 .
 



1. Go to the
 
 Languages
 
 section in the system designer.
2. In the list of languages, locate the language you need and click
 
 Open
 
 .
3. On the language page, select the
 
 Active
 
 checkbox (Fig. 1).
 




 Fig. 1 Enabling additional language
 

![scr_chapter_multilanguage_enable.png](/guides/sites/en/files/documentation/user/en/custom_localization/BPMonlineHelp/manage_UI_languages/scr_chapter_multilanguage_enable.png)
4. Save the changes.
 



 As a result, Creatio compilation will start and you will see the enabled language appear in your Creatio user profile after the compilation is finished.
 





 Attention.
 
 Compilation is a required step when enabling additional languages. If a language is enabled, but the application is not compiled, the user who selected this language will not be able to log in.
 






 Note.
 
 If you cannot access Creatio after switching languages, you can quickly access the
 
 Configuration
 
 section by adding “/dev” after Creatio application URL and initiate compilation from there.



 Change UI language
--------------------



 You can change the system interface language in the user profile. These settings apply individually to the users who changed their language.
 


1. Click the profile picture at the top right corner and select
 
 Your profile
 
 .
2. On the profile page, select the needed language from the available list and save the changes (Fig. 2).
 




 Fig. 2 Changing the interface language
 

![change_language.png](/guides/sites/en/files/documentation/user/en/custom_localization/BPMonlineHelp/manage_UI_languages/change_language.png)



 After changing language, you will need to log in again.
 





 Note.
 
 If you do not see the needed language in the list, it may be disabled. You can find more information about enabling additional languages in a separate
 [article](https://academy.creatio.com/documents?product=base&ver=7&id=1844) 
 .
 






 Note.
 
 System administrators can change interface language for different users in the
 [System users
 
 section](https://academy.creatio.com/documents?product=administration&ver=7&id=1426) 
 .
 




 Creatio interface, including sections, columns, pages and lookups will be displayed in the language specified in the user profile (if the corresponding translation is available). The actual section data, such as account or contact names, notes and knowledge base articles are not localized and will always be displayed in the language they were entered.
 





 Note.
 
 If a value has s a translation for the currently selected language, it will be displayed in that language. If no translations are found, the value will be displayed in the language it was originally added.
 




 Set default UI language
-------------------------



 After adding a new user account, system administrator specifies user’s interface language (culture) on the
 [user page of the
 
 System users
 
 section](https://academy.creatio.com/documents?product=administration&ver=7&id=1426) 
 . You can set default interface language for all users. This will help when adding large numbers of users at once (i.e., by importing users, when using SSO, etc.).
 



 To set the default language:
 


1. Go to the
 
 Languages
 
 section in the system designer.
2. Select a language and click
 
 Open
 
 .
3. Select the
 
 Use by default
 
 checkbox on the opened page (Fig. 3).
 




 Fig. 3 Setting the default language
 

![default_language_setting.png](/guides/sites/en/files/documentation/user/en/custom_localization/BPMonlineHelp/manage_UI_languages/default_language_setting.png)





 Note.
 
 The
 
 Use by default
 
 checkbox can be enabled only for one language.
4. Save the changes.
 



 When you create a new user, the default language will be automatically selected in the user’s profile.
 





 Note.
 
 If the culture is not specified for the user, the interface language and localized data will be displayed in the language, specified in the
 
 Primary culture
 
 system setting. More information about system settings is available in a separate
 [article](https://academy.creatio.com/documents?product=administration&ver=7&id=269) 
 .
 




 Users can change language in their profile after logging in to the system. After changing the language, the interface will be displayed in that language next time the user logs in.



 Add new UI language
---------------------



 If you are localizing your Creatio application to one of the languages that are not yet available, you will need to add that language in the
 
 Languages
 
 section first.
 


1. Go to the
 
 Languages
 
 section in the system designer.
2. Click the
 
 New language
 
 button. A new language page opens.
3. In the
 
 Name
 
 field, select the language you want to add.
 





 Note.
 
 The list of languages is located in the system lookup, and is non-editable.
4. Select an image to be used as an icon for that language.
5. Save the changes.




