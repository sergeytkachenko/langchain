


 The
 
 Validation
 
 process element is used in the processes that manage the verification of loan applications by underwriters. This process element is available only in Financial Services Creatio. Use the
 
 Validation
 
 element to create a validation checklist that an underwriter must complete to approve or deny a loan application. The general purpose of the
 
 Validation item
 
 element is to automate the credit loan review. by determining the process flow based on the validation results.
 





 Note.
 
 More details on the application review automation are available in the “
 [Validation item case element](https://academy.creatio.com/documents?id=7131) 
 ” article.
 




 Specify the validation parameters on the element setup page (Fig. 1).
 




 Fig. 1 The
 
 Validation
 
 element settings
 

![chapter_process_designer_verification.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/chapter_process_designer_verification.png)




 Which validation item to execute?
 
 – select an item from the
 
 Validation items
 
 lookup. The lookup contains the list of actions that include validation questions and additional information that the employee may need during the validation process. This is a required field.
 




 Application
 
 – specify the loan application to validate. Use the parameter value window to specify where the element is supposed to get the application Id. You can populate this parameter using the parameter value window. By default, it is the application that the process was run for. This is a required field.
 




 Execute on page
 
 – specify the page where the validation item must be performed. By default, a pre-set Creatio
 [validation item page](https://academy.creatio.com/documents?id=1666) 
 is used. This is a required field.
 




 How to perform validation?
 
 – select what exactly the underwriter will validate: the loan application itself or its participants. Depending on the selected method, additional parameters become available. It is a required field.
 


* Select “Single participant validation” if the underwriter will be validating a specific participant. In this case, the
 
 Participant role
 
 field becomes available where you specify the application participant, whose profile the underwriter will validate during this step. This is a required field.
 
 Participant application form
 
 – specify the application form of the participant. (optional).
* Select “Multiple participant validation” if the underwriter will be validating application participants of a specific role. Select the role in the
 
 Participant role
 
 field.
* Select “Application approval” if the underwriter will be validating the loan application itself.




 Who performs the task?
 
 – select an employee or a group of employees who perform the validation. For example, the loan manager or the verification group. This is a required field.
 


* Select “Group of employees” if the validation can be performed by any employee of a specific role. Select the corresponding role in the
 
 Role of employees
 
 field.
* Select “Responsible employee” if the validation can be performed by a specific employee only. Select the employee in the
 
 Owner
 
 field.




 How to display on Validation detail?
 
 – select a method for displaying the validation result on the
 
 Validation
 
 detail of the application page.
 


* Select “Add new record”, Creatio will add a new record on the
 
 Validation
 
 detail.
* Select “Edit existing record” to update a specific record on the
 
 Validation
 
 detail. In this case, you will need to specify the record to update in the
 
 Record identifier
 
 field.




 After Validation Saved
 
 – in addition to the standard settings available in the
 [advanced mode](https://academy.creatio.com/documents?id=7003) 
 , the
 
 Validation
 
 element has a field where you can specify C# code with the use of .NET Framework classes. The code will be executed after the business process creates and saves the validation item.
 




