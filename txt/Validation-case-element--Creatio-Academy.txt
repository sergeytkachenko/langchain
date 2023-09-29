



 This element is available only in Financial Services Creatio, lending edition.
 




 Use the
 
 Validation
 
![chapter_case_designer_icon_verification.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/chapter_case_designer_icon_verification.png)
 case element to verify applications as part of the case. You can create a validation checklist that an underwriter must complete to approve or deny a loan application, streamlining the decision-making process.
 





 Note.
 
 Learn more about the
 
 Validation
 
 business process element:
 [Validation
 
 process element](/docs/7-18/user/bpm_tools/process_elements_reference/user_actions/validation/validation_item_process_element) 
 .
 




 Set up the
 
 Validation
 
 case element
------------------------------------------



 Specify the validation parameters in the element setup area (Fig. 1).
 




 Fig. 1 The
 
 Validation
 
 element setup area
 

![chapter_process_designer_verification_7.18.png](/docs/sites/en/files/images/BPM_Tools/dcm_elements/chapter_process_designer_verification_7.18.png)



 The element caption is displayed at the top of the element setup area. This makes the element easy to find on the case diagram.
 



 Fill out the following fields:
 


1. Which validation item to execute?
 
 – select an item from the
 
 Validation items
 
 lookup. The lookup contains the list of actions that include validation questions and additional information that the employee may need during the validation process. This is a required field.
2. Application
 
 – specify the application to validate. Use the parameter value window to specify where the element is supposed to get the application Id. You can populate this parameter using the parameter value window. By default, it is the application for which you ran the case. This is a required field.
3. Execute on page
 
 – specify the page where the underwriter must perform the validation. By default, Creatio uses a pre-configured
 [validation item page](/docs/7-18/user/finance_and_banking/financial_services/set_up_verification_actions_shortcut/set_up_verification_actions) 
 . This is a required field.
4. How to perform validation?
 
 – select what exactly the underwriter will validate: the loan application itself or its participants. Depending on the selected method, additional parameters will become available. This is a required field.
	* Select “Single participant validation” if the underwriter will validate a specific participant. In this case, the
	 
	 Participant role
	 
	 field will become available. Specify the role of the application participant in it. This is a required field.
	 
	 Participant application form
	 
	 – specify the application form of the participant if it exists. This is an optional field.
	* Select “Multiple participant validation” if the underwriter will validate the application participants of a specific role. Specify the role in the
	 
	 Participant role
	 
	 required field.
	* Select “Application approval” if the underwriter will validate the loan application itself.
5. Who performs validation?
 
 – select an employee or a group of employees who must perform the validation. For example, the loan manager or the verification group. This is a required field.
	* Select “Group of employees” if the validation can be performed by any employee of a specific role. Select the corresponding role in the
	 
	 Role of employees
	 
	 field.
	* Select “Responsible employee” if the validation can be performed by a specific employee only. Select the employee in the
	 
	 Owner
	 
	 field.
6. How to display on Validation detail?
 
 – select a method for displaying the validation result on the application page.
	* Select “Add new record” to add a new record to the
	 
	 Validation
	 
	 detail.
	* Select “Edit exist record” to update an existing validation record. Specify the record to update in the
	 
	 Record identifier
	 
	 additional field.
7. When is the step performed?
 
 – indicates whether to activate the element at the start of the stage or after a case step.




 Validation
 
 element advanced settings
------------------------------------------



 In addition to the standard settings, the
 [advanced mode](/docs/7-18/user/bpm_tools/business_process_setup/overview/process_designer#title-1624-8) 
 of the
 
 Validation
 
 element settings displays the
 
 After Validation Saved
 
 field. It accepts C# code with .NET Framework classes. Creatio will execute the code after the case creates and saves the validation item.
 




