


 Creatio provides two out-of-the-box business processes to handle cases received by a call. The processes start when an agent receives a call from a customer.
 




 Attention.
 
[Telephony setup](https://academy.creatio.com/documents?product=administration&ver=7&id=1028) 
 is needed to work by the processes. Furthermore, the processes are available only for the users included in the folder specified in the
 
 Folder – Contact Center agents
 
 system setting.
 

 When taking a call, an agent can choose to run one of the Creatio business processes, depending on the call purpose: create a new case or start consultation for an existing case.
 



 The process flow depends on whether the subscriber is identified or not. The system allows identifying the contact or creating a new one. According to the customer's request, a new case will be created or the contact page will open. On this page, the agent will be able to see the history of communication with the customer and provide consultations regarding the existing cases.
 



 When a call is received, the
 
 Calls
 
 tab becomes active on the communication panel. On the
 
 Processes
 
 detail of the
 
 Call
 
 tab, the following actions become available:
 
 Add new case
 
 and
 
 Advice on existing case
 
 . Each action starts the corresponding business process.
 




 Case registration process
----------------------------



 To register a new case when taking a call, select the
 
 Add new case
 
 action. This action will trigger the corresponding process. The process can have different flows based on different conditions. These flows and conditions can be summarized in the following table.
 





|  |  |
| --- | --- |
| 
 Condition
  | 
 Agent actions
  |
| 
 The contact is uniquely identified by a phone number registered in the system.
  | 
 Clicking the
 
 Add new case
 
 button opens a new case page where you should enter the information provided by the customer. On the case page, the
 
 Contact
 
 field is automatically populated.
  |
| 
 The system detected multiple contacts with the same phone number from which the call has been received
  | 
 The call panel displays the
 
 Search results
 
 detail that contains the list of contacts with the phone number from which the call has been received. Click the record of the right contact and then click the
 
 Add new case
 
 button, so a new case page will open. The
 
 Contact
 
 field on the page will be automatically populated.
  |
| 
 The contact is not identified by the phone number, but the call has been received from a customer already registered in the system
  | 
 Clicking the
 
 Add new case
 
 button opens the contact identification page. On this page, you can search for the contact by name, by communication options, or by the name of the company where the employee works. Select proper contact and then click the
 
 Add new case
 
 button, so a new case page will open. The
 
 Contact
 
 field on the page will be automatically populated. The phone number from which the call has been received will be added to the
 
 Communication options
 
 detail of the selected contact.
  |
| 
 The contact is not identified by the phone number and the call has been received from a new customer
  | 
 Clicking the
 
 Add new case
 
 button opens a contact identification page where you should select the
 
 Add case and contact
 
 action. On the opened page, enter contact data. Click the
 
 Next
 
 button, so a new case page will open. The
 
 Contact
 
 field on this page will be automatically filled in. If needed, you can edit the record of the new contact after saving the record of the new case.
  |





 Advising on an existing case process
---------------------------------------



 To advice a customer on an existing case, select the
 
 Advice on existing case
 
 action. This action will trigger the corresponding process. The process can have different flows based on different conditions. These flows and conditions can be summarized in the following table.
 





|  |  |
| --- | --- |
| 
 Condition
  | 
 Agent actions
  |
| 
 The contact is uniquely identified by a phone number registered in the system.
  | 
 Clicking the
 
 Advice on existing case
 
 button opens the page of the caller contact. Open the
 
 History
 
 tab to view the list of cases connected to the given contact.
  |
| 
 The system detected multiple contacts with the same phone number from which the call has been received
  | 
 The call panel displays the
 
 Search results
 
 detail that contains the list of contacts with the phone number from which the call has been received. Click the record of the needed contact and then click the
 
 Advice on existing case
 
 button. The page of the selected contact will open. Open the
 
 History
 
 tab to view the list of cases connected to the given contact.
  |
| 
 The contact is not identified by the phone number, but the call has been received from a customer already registered in the system
  | 
 Clicking the
 
 Advice on existing case
 
 button opens the contact identification page. On this page, you can search for the contact by name, by communication options, by the number of the registered case, or by the name of the company where the employee works. Select proper contact and then click the
 
 Add new case
 
 button, The page of the selected contact will open. Open the
 
 History
 
 tab to view the list of cases connected to the given contact.
  |
| 
 The contact is not identified by the phone number and the call has been received from a new customer for whom registered cases have not been found
  | 
 You will need to proceed to the process of creating a new case. Clicking the
 
 Advice on existing case
 
 button opens a contact identification page where you should select the
 
 Add case and contact
 
 action. On the opened page, enter contact data. Click the
 
 Next
 
 button, so a new case page will open. The
 
 Contact
 
 field on this page will be automatically filled in. If needed, you can edit the record of the new contact after saving the record of the new case.
  |





