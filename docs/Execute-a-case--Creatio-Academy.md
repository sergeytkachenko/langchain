


 You can add a case to most Creatio sections. Some sections, e. g.,
 
 Opportunities
 
 ,
 
 Leads
 
 ,
 
 Cases
 
 , come with pre-configured cases out of the box. Learn more:
 
[Set up cases in sections](/docs/8-0/user/bpm_tools/dynamic_case_setup/case_designer_workflows/set_up_a_case/set_up_cases_in_sections) 

 .
 





 Note.
 
 We recommend disabling the section's business process before running the section case. Otherwise, the case and the process will run in parallel.
 




 Advance through case stages
-----------------------------



 The section case launches automatically when a new record that matches the launch conditions is created. The case also creates activities and launches sub-processes included in the first stage automatically.
 



 By default, cases execute the stage elements immediately upon transitioning to the stage. If you set the
 
 When is the setup performed?
 
 field in the element settings to “After the previous step is complete,” the case will execute the element only after the step specified in the
 
 Perform after step
 
 field.
 



 Use the workflow bar on the action panel to advance through the case stages. Creatio displays all activities created as part of the case on the action panel.
 



 You can set the case to transition to a specific stage depending on the results of the task or the conditions of the subprocess at the current stage.
 



 The case owner will see case steps on the action panel. Complete tasks and advance through the stages to achieve the goal of the case. Completing all the steps on a stage is not required. Users must complete only the required steps to advance through the case.
 



 If you attach a hint to a case step, the
 ![btn_playbook.png](/docs/sites/en/files/images/CRM_Tools/playbook/btn_playbook.png)
 button will appear on the action panel (Fig. 1). Click the button to open the box with the knowledge base article that will help the employees to work on the case. Learn more about how to set up hints:
 [Set up case Playbook hints](/docs/8-0/user/crm_tools/knowledge_base/playbook/set_up_case_playbook_hints) 
 .
 





 Fig. 1
 
 Opening a Playbook hint
 

![gif_playbook_open.gif](/docs/sites/en/files/images/CRM_Tools/playbook/gif_playbook_open.gif)





 Note.
 
 Users can advance to the final “unsuccessful” stage from any stage without completing the required steps.
 




 Change case
-------------



 If the record page's field value that triggered the case changes, and there is a more suitable case for the new value, the action panel will display the
 
 Change case
 
 button (Fig. 2).
 





 Fig. 2
 
 The
 
 Change case
 
 button
 

![chapter_case_designer_change_case.png](/docs/sites/en/files/images/BPM_Tools/dcm_perform/chapter_case_designer_change_case.png)



 To launch a new case:
 


1. Click the
 
 Change case
 
 button.
2. Select the “Launch” command.
3. Click
 
 Proceed
 
 in the dialog box to confirm the case change.



 As a result, the record page will display the stages and activities of the new case.
 




