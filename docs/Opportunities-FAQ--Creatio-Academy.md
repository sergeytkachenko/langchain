





 Can you work with opportunities not by a process?
------------------------------------------------------



 If your company's approach to sales management is different from the one in Creatio, you can work with the
 
 Opportunities
 
 section without using the pre-defined sales process.
 



 In this case, do not start the corporate sales process and just change the stage on the opportunity page manually. Fill in the required fields, enter information in the tabs and details.
 



 For the process to not run automatically when transferring a lead to the
 
 Awaiting sale
 
 stage, disable the “Start sales process” system setting.
 






 How to change the standard sales process?
----------------------------------------------



 You can delete, change or add process stages, and change the list of activities in accordance with your needs.
 



 To change the process:
 


1. Open the
 
 Process library
 
 section.
2. Find the default process that you want to change. The corporate sales process consists of several subprocesses with each referring to a particular opportunity stage. When searching for a subprocess, pay attention to the name and the 7.8 prefix. For example, if you need to change the “Qualification” stage, find a process called “Opportunity qualification v7.8.0”.
3. Create a copy of the basic corporate sales process by clicking the
 
 Copy
 
 button record in the process record.
4. Make the required changes in the copy. You can change the elements, remove elements or add new ones.
5. Save the edited copy and publish.
6. Go to the original version of the corporate sales process and disable it by clicking the
 
 Actions
 
 →
 
 Disable
 
 .
 





 Note.
 
 Detailed descriptions of business process management are available in the Creatio business process documentation.
 




 After performing the settings, the system will use the custom corporate sales process.







 How to change basic tasks that are created to custom tasks?
-----------------------------------------------------------------



 To change the list of basic activities, which are formed during the corporate sales process, you need to replace the basic sales process with a custom copy. More information about changing a default process:
 
[How to change the standard sales process?](#HT_specs_opp_fiq_edit_process) 





 After you have made the necessary adjustments at each stage of the updated sales process, the system will form the activities that you have added/changed.
 






 Under what conditions is the [DM] field filled in on the opportunity page?
-------------------------------------------------------------------------------



 The
 
 DM
 
 field in the "BANT” profile of the opportunity page contains the name of the contact who is the decision maker for the opportunity. The field is filled in automatically. To specify the decision maker on the opportunity page, add the contact and in the
 
 Role
 
 field enter "DM” on the
 
 Contacts
 
 details of the
 
 Opportunity data
 
 tab.
 



 Note that the
 
 DM
 
 field pulls the data from the opportunity page, not from the page of the contact that also contains the
 
 Role
 
 field. This field denotes the decision maker for the whole company At the same time a different person may make decisions about the sale.
 






 How to set up different processes for different opportunity types?
-----------------------------------------------------------------------



 This functionality can be implemented by the developer means.
 






 Why is the amount calculated incorrectly after changing currency?
----------------------------------------------------------------------



 When you change the currency of the
 
 Amount
 
 multi-currency field, the value in the field and in the multi-currency edit pop-up are different (
 [Fig. 1](#XREF_31430_169)
 ).
 





 Fig. 1
 

 Different values in a multi-currency field and the corresponding multi-currency edit pop-up
 

![scr_sec_opp_faq_currency_change.png](/guides/sites/en/files/documentation/user/en/opportunities/BPMonlineHelp/opportunities_faq/scr_sec_opp_faq_currency_change.png)



 After changing currency in a filled-in multi-currency field, the specified amount will be automatically converted to the new value according to currency exchange rates. At the same time, the
 
 Amount
 
 field on the multi-currency edit pop-up displays the amount in base currency. This is a non-editable field. Learn more in the “
 
[Working with currencies](https://academy.creatio.com/documents?product=base&ver=7&id=1584) 

 ” article.
 







 What happens if one of the activities is skipped
------------------------------------------------------



 If one or more of the stage activities were not completed, and the opportunity was advanced to the next stage with the workflow bar, then the activity will be canceled automatically. Creatio will generate a new list of activities corresponding to the current opportunity stage.
 



 The uncompleted tasks that were created manually will not be canceled when advancing to the next stage. Uncompleted tasks do not affect transition to next stages.
 




