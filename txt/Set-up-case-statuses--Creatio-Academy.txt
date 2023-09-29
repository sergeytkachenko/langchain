


 You can manage the statuses of cases in Creatio using the
 
 Case statuses
 
 lookup. The
 
 Case statuses
 
 lookup functions:
 


* Create a list of possible states of service cases, e.g., “New,” “In progress,” “Closed,” etc.
* Set the final state, from which a case cannot transition to other states.
* Set states indicating that a case has been resolved.
* Set states that stop the case processing.



 The setup procedure is as follows:
 


1. Open the system designer by clicking the
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_statuses_settings/btn_system_designer.png)
 button.
2. Go to the
 
 System setup
 
 block → click
 **Lookups** 
 .
3. Open the contents of the
 **Case statuses** 
 lookup.
4. Edit the properties of case statues directly in the list.
5. Click
 ![btn_edit.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_statuses_settings/btn_edit.png)
 and go to additional parameters and conditions for going from one state to another.



 The lookup fields are as follows:
 





|  |  |
| --- | --- |
| 
 Name
  | 
 Case status name, that is displayed in the
 
 Status
 
 field, for example, “In progress“.
  |
| 
 Description
  | 
 Additional information about the case status, that cannot be specified in other fields.
  |
| 
 Is final
  | 
 Indicates that cases in this status have finished processing. By default, the final statuses are “Cancelled” and “Closed”. Closed or cancelled cases cannot be assigned any other statuses.
  |
| 
 Is resolved
  | 
 Indicates that a solution or an answer has been sent to the user. By default this checkbox is selected for the “Resolved” status. If a case is assigned this status, the timer for the resolution deadline stops.
  |
| 
 Is paused
  | 
 Indicates that cases in this status are suspended for some reason, usually because a response or an action from the user is expected. By default, this checkbox is selected for the “Pending” status. The resolution timer is paused for cases that have this status.
  |
| 
 Button caption
  | 
 The caption of the button that changes the case status to the current one. This button is displayed in the list of the
 
 Cases
 
 section as well as on the case page.
  |
| 
 Close on save
  | 
 If this checkbox is selected, then, whenever the user saves a case in this status, the case page will be automatically closed.
  |




 The lookup contents will be used on the case page.
 




