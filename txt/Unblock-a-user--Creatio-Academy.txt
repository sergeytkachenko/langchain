


 If the user
 [mistypes their credentials](/docs/8-0/user/setup_and_administration/user_and_access_management/user_management/unblock_a_user_shortcut/unblock_a_user#title-2108-5) 
 several times in a row, their account will be blocked for some time.
 



 The system administrator can
 [set up the blocking conditions](/docs/8-0/user/setup_and_administration/user_and_access_management/user_management/unblock_a_user_shortcut/unblock_a_user#title-2108-1) 
 :
 


* the number of attempts after which the user account is blocked
* the period after which the user account is unblocked.



 User account blocking principles
----------------------------------



 Several
 [system settings](/docs/7-17/user/setup_and_administration/system_settings_and_lookups/system_setting_reference/description_of_system_settings#title-1880-28) 
 are considered when blocking a user account:
 


* “Number of logon attempts” (“LoginAttemptCount” code).
* “Quantity of login attempts for warning message” (“LoginAttemptBeforeWarningCount” code).
* “User locking time” (“UserLockoutDuration” code).



 The user account blocking
 **mechanism** 
 is as follows:
 


* If the number of failed login attempts does not exceed the value of the
 **“Number of logon attempts”** 
 (“LoginAttemptCount” code) system setting, Creatio displays a failed login attempt message (Fig. 1).
 

 Fig. 1 A failed login attempt message
 

![scr_incorrect_password_message.png](/docs/sites/en/files/images/Setup_and_Administration/unblock_user/scr_incorrect_password_message.png)
* If the number of failed login attempts exceeds the value of the
 **“Number of logon attempts”** 
 (“LoginAttemptCount” code) system setting, Creatio displays a lockout warning message (Fig. 2).
 

 Fig. 2 A lockout warning message
 

![scr_warning_message.png](/docs/sites/en/files/images/Setup_and_Administration/unblock_user/scr_warning_message.png)
* If the number of failed login attempts equals the value of the
 **“Quantity of login attempts for warning message”** 
 (“LoginAttemptBeforeWarningCount” code) system setting, Creatio displays a lockout message (Fig. 3).
 

 Fig. 3 A lockout message
 

![scr_block_message.png](/docs/sites/en/files/images/Setup_and_Administration/unblock_user/scr_block_message.png)



 As a result, the user will be blocked for the period specified in the
 **“User locking time”** 
 (“UserLockoutDuration” code) system setting. The user account will be unblocked after the specified period. To unblock a user account earlier, use the following instruction:
 [Unblock a user account](/docs/8-0/user/setup_and_administration/user_and_access_management/user_management/unblock_a_user_shortcut/unblock_a_user#title-2108-2) 
 .
 



 Specify the user account blocking conditions
----------------------------------------------


### 
 Set the number of login attempts


1. Click
 ![btn_system_designer.png](/guides/sites/default/files/documentation/user/ru/licensing/BPMonlineHelp/licensing_creatio/btn_system_designer.png)
 to open the System Designer.
2. Click
 **“System settings”** 
 in the “System setup” block.
3. Open the
 **“Number of logon attempts”** 
 system setting (“LoginAttemptCount” code).
 
 Specify the acceptable number of failed login attempts in the
 
 Default value
 
 field. The recommended system setting value is 5.
4. Open the
 **“Quantity of login attempts for warning message”** 
 system setting (“LoginAttemptBeforeWarningCount” code).
 
 Specify the number of failed login attempts after which Creatio displays the lockout warning message in the
 
 Default value
 
 field. The user will be blocked after the next failed login attempt. The recommended system setting value is 3.





 Note.
 
 The value of the “Number of logon attempts” system setting (“LoginAttemptCount” code) must not exceed that of the “Quantity of login attempts for warning message” system setting (“LoginAttemptBeforeWarningCount” code).
 



### 
 Set up the user lockout period


1. Click
 ![btn_system_designer.png](/guides/sites/default/files/documentation/user/ru/licensing/BPMonlineHelp/licensing_creatio/btn_system_designer.png)
 to open the System Designer.
2. Click
 **“System settings”** 
 in the “System setup” block.
3. Open the
 **“User locking time”** 
 system setting (“UserLockoutDuration” code).
 
 Specify the user account blocking time (in minutes) after a number of failed login attempts in the
 
 Default value
 
 field. The recommended system setting value is 15.



 As a result, Creatio will set the account blocking conditions for all system users.
 



 Unblock a user account
------------------------




 You can unblock a user account in Creatio version 7.17.3 and later.
 




 To
 **unblock a user account** 
 before the lockout period expires, do the following:
 


1. Click
 ![btn_system_designer.png](/guides/sites/default/files/documentation/user/ru/licensing/BPMonlineHelp/licensing_creatio/btn_system_designer.png)
 to open the System Designer.
2. Click
 **“System users”** 
 in the “Users and administration” block.
3. Open the user page.
4. Click
 
 Unblock
 
 (Fig. 4).
 

 Fig. 4 Unblock a user
 

![scr_unblock_user.png](/docs/sites/en/files/images/Setup_and_Administration/unblock_user/scr_unblock_user.png)



 As a result, the user account will be unblocked.
 




