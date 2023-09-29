


 Creatio automatically calculates contact age based on the value in the
 
 Birthdate
 
 field for customer database segmentation. If the
 
 Birthdate
 
 field is empty on the contact page, the value in the
 
 Age
 
 field will be “0.” Please take this into account when setting up filters that use this field.
 



 Creatio updates the value in the
 
 Age
 
 column in the following instances:
 


* Whenever a new contact record
 **is saved** 
 or the value in the
 
 Birthdate
 
 field is updated. In this case, the value in the
 
 Age
 
 field is updated only for the current contact.
* On
 **running** 
 the
 
 Update the values in the “Age” column
 
 action in the
 
 Contacts
 
 section. In this case, the age will update all contacts.
* **Daily** 
 , at a specific time. The age is calculated only for those contacts whose birthday is on the current day.



 Set up age calculation
------------------------



 The following age calculation settings are available:
 


* set up a time for daily updating of contact ages
* disable daily update of contact age
* disable any automatic updates of contact age.



 Use the
 [system settings](/docs/7-17/user/setup_and_administration/system_settings_and_lookups/system_setting_reference/description_of_system_settings#title-3082-3) 
 in the “Contact age” folder.
 





 Note.
 
 The list of system settings is available in a
 
 separate article
 
 . Be sure to specify the system setting code (as opposed to its localizable title).
   

 Users require permission to the “Can run actualize contact age process” (the “CanRunActualizeContactAgeProcess” code) system action.
 




 To
 **set up regular automatic updates of contact age** 
 , go to the
 
 Contacts
 
 section and run
 
 Actions
 
 >
 
 Schedule daily update of the “Age” column
 
 . If you change the time using the action in the
 
 Contacts
 
 section, the modifications will apply during the next age update.
 



 To
 **disable daily updating** 
 of the
 
 Age
 
 column, clear the checkbox in the “Enable automatic daily update of the contact ages” (the “RunAgeActualizationDaily” code) system setting. After this, the age calculation function will be performed only on saving contact records.
 



 To
 **disable age calculation completely** 
 , clear the checkbox in the “Enable updating contact ages” (the “ActualizeAge” code) system setting. This disables the age calculation functionality, regardless of the values of other system settings in the “Contact age” folder. If the age calculation functionality is disabled, the
 
 Age
 
 field on the contact page becomes editable.
 




