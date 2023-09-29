


 You can integrate your business processes with standard sections. As a result, the section users will be able to run integrated business processes in two modes (
 [Fig. 1](#XREF_23249_278)
 ):
 





 Fig. 1
 

 Running a process integrated into a section
 


![scr_section_wizard_run_process_from_the_record.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_BPMN_process_to_section/scr_section_wizard_run_process_from_the_record.png)



* **Regardless of section records** 
 (1). You can add any business process to the
 
 Run process
 
 menu of any standard section.
* **For a specific record** 
 (2), using the record’s data in the process flow.





 Note.
 
 To be able to run a business process, a user must have access to the
 
 Can run business processes
 
 (CanRunBusinessProcesses)
 
[system operation](https://academy.creatio.com/documents?product=administration&ver=7&id=2000) 

 .
 




 To add a business process that runs by a specific record, you need to modify the process by adding a parameter that would receive the unique identifier of the section record by which the process is run. The instructions on how to do this are available in the “
 
[Run business processes for section records](https://academy.creatio.com/documents?product=BPMS&ver=7&id=7152) 

 ” article of the Business process management guide.
 



 To integrate a business process in a section:
 


1. Open the needed section.
2. Click
 
 View
 
 >
 
**Open section wizard** 

 .
3. Click
 
**Business process** 

 .
4. Under
 
 Run business process from section
 
 , click
 
![btn_chapter_mobile_wizard_new_role.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_BPMN_process_to_section/btn_chapter_mobile_wizard_new_role.png)

 (
 [Fig. 2](#XREF_40697_Fig_430_Adding_a)
 ).
 





 Fig. 2
 

 Adding a business process to a section
 


![chapter_section_wizard_add_process.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_BPMN_process_to_section/chapter_section_wizard_add_process.png)
5. Select the necessary process in the
 
 Which process to run
 
 field (
 [Fig. 3](#XREF_12578_280)
 ).
6. In the opened pop-up, select how the process should run:
 


	1. To run the process regardless of section record, select
	 
	 Regardless of record
	 
	 .
	2. To run the process for separate section records, select the
	 
	 For selected record
	 
	 .
7. If you chose
 
 For selected record
 
 , select the parameter where Creatio should pass the unique Id of the selected section record in the
 
 Process parameter where the record is passed
 
 field.
 





 Note.
 
 If the process already has a lookup parameter that uses the section object as a lookup, it will be selected automatically. If there are two or more parameters, you will need to select the correct one.
 






 Fig. 3
 

 Configuring the launch of a business process
 


![scr_section_wizard_choose_process_parameter.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_BPMN_process_to_section/scr_section_wizard_choose_process_parameter.png)
8. Save all changes in the Section Wizard and clear the cache to apply changes in Creatio.
 



 As a result, the process will become available in the
 
 Run process
 
 menu of the section next time you log in.




