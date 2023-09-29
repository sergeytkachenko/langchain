


 Why will the visual elements not open, even though the business process keeps running according to the log?
-------------------------------------------------------------------------------------------------------------



 Creatio uses WebSocket protocol to run user processes, notifications, and phone integrations. If the process log shows that the business process is being executed, but the visual elements do not open, check the websocket settings. Learn more about configuring Creatio to use the WebSocket protocol:
 [Set up WebSockets](https://academy.creatio.com/documents?id=1631) 
 .
 



 Why does a process not continue to run automatically?
-------------------------------------------------------



 If a business process does not continue to run, check the following system settings:
 


* Check the websockets.
* Your business process might be waiting for a signal. Therefore, the process can not continue running until it receives a signal.
* If during the execution of the business process a page needs to be opened, check the process parameters in the Designer. A parameter or a contact might be set in the
 
 Owner
 
 field and might not be able to display the page to the current user. For example, if the user lacks access permissions to the required page.
* Rarely, the incorrect “Maximum number of working processes” setting in the JIS pool can cause a bug. If a value greater than 1 is set, then opened processes accumulate and stop responding.



 How do I advance a case to the next stage automatically?
----------------------------------------------------------



 Currently, dynamic cases have no automatic stage transitions. To advance a case to the next stage, click the corresponding stage on the workflow bar on the opportunity, case or lead page. All tasks of the current stage will appear on the action panel and will be added to the calendar of the corresponding contacts.
 



 Where and how the cases are saved?
------------------------------------



 The cases are saved as configuration schemas, similar to processes, objects and pages. The schema name is specified in the
 
 Name
 
 field.
 



 Can I set up multiple cases for a single section?
---------------------------------------------------



 You can set up multiple cases for a single section. For example, you can use individual cases that have different number of stages for the “Small business” and “Medium business” categories in the
 
 Opportunities
 
 section.
 



 To do this:
 


1. Fill out the
 
 Which column determines which case to use with a record?
 
 field on the case setup page.
2. Specify the corresponding value in the
 
 Use this case with records where
 
 field when setting up the case.



 How do business process or case pages interact with pages I have open?
------------------------------------------------------------------------



 Pages that are
 **run in the background** 
 do not interrupt your workflow. Creatio only posts a notification in the notification panel that lets you open the page at any convenient time.
 



 Pages that
 **are not run in the background** 
 interact with pages you have open as follows:
 


1. After the process or case page closes, Creatio brings you back to the original page you had open. For example, if a process page opens from a contact form page, Creatio brings you back to the form page after the process page closes.
2. If the process or case page opens another process or case page, Creatio opens that page after the first page closes. After the second page closes, Creatio brings you back to the original page you had open. For example, if a process page opens from a contact form page and a case page opens from the process page, Creatio opens the case page after the process page closes, then brings you back to the form page once the case page closes.





 Note.
 
 Creatio preserves any unsaved data you entered on the page you had open.
 





