


 You can configure cases in any Creatio section. Several cases can be used simultaneously in each section. However, a section record will use only one of the cases, depending on a specific column value. For example, for the “Medium business” and “Small business” opportunity categories, you can configure different cases.
 



 There are several ways to access the Case Designer:
 


* The
 
 Cases
 
 tab in the section wizard
* The
 
 Set up section cases
 
 button in the
 
 View
 
 section menu.



 The case setup page displays a list of all cases configured for a section (
 [Fig. 1](#XREF_59743_205)
 ).
 





 Fig. 1
 

 Section case setup page
 


![scr_chapter_case_designer_cases_list.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_set_up_cases/scr_chapter_case_designer_cases_list.png)




 The
 
 Which column to build the stages by?
 
 and
 
 Which column to set initial case condition by?
 
 fields determine the basic case properties (
 [Fig. 2](#XREF_21377_206)
 ):
 


1. Which column to build the stages by?
 
 – the values of the column specified in this field will be used to determine case steps.
2. Which column to set initial case condition by?
 
 – Creatio will use the column specified in this field to determine which case to run for which record. Populate this field if the section has several cases.





 Fig. 2
 

 Configuring section case columns
 


![scr_case_designer_case_columns.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_set_up_cases/scr_case_designer_case_columns.png)






 Create a case
---------------



 Click
 
 New case
 
 to add a section case. The
 
[Case Designer](/docs/8-0/user/bpm_tools/dynamic_case_setup/case_designer_workflows/overview/case_designer#HT_chapter_case_designer_workspace) 

 will open. In the designer, configure the sequence of steps (case elements) that are performed at each case stage. A new case will appear in the list of section cases after you save changes in the Case Designer.
 





 Note for implementation specialists.
 
 In the pre-production environment, if you configure the case for the section with the default case disabled, then before transferring the created case to the production environment, bind the data of the disconnected case.
 




 Activate a case
-----------------



 Cases that are not currently in use can be deactivated by selecting the case record and clicking the
 
 Deactivate case
 
 button in the
 
 Actions
 
 drop-down menu. The case will continue running for all records created before its deactivation. Several cases can be activated simultaneously in each section.
 





 Note.
 
 You can run only those cases that correspond to the columns specified in the
 
 Which column to build the stages by?
 
 and
 
 Which column to set initial case condition by?
 
 fields. If the values of the
 
 Which column to build the stages by?
 
 and
 
 Which column to set initial case condition by?
 
 fields are changed, all cases that have incompatible column values will be deactivated.
 





