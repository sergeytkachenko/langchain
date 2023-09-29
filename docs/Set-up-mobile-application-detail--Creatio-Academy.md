


 There are two types of details in the mobile application:
 


* **embedded details** 
 display all their records on the section record page regardless of the amount of data on the detail (
 [Fig. 1](#XREF_94977_445)
 );





 Fig. 1
 

 Embedded detail
 
 Contact address
 
 on the section page
 

![scr_mobile_wizard_mplemented_detail.png](/guides/sites/en/files/documentation/user/en/mobile_app_setup/BPMonlineHelp/mobile_app_setup_detail/scr_mobile_wizard_mplemented_detail.png)


* **standard details** 
 do not display their records on the section page (
 [Fig. 2](#XREF_61007_241)
 ). Tap a standard detail to view its records on a separate page.





 Fig. 2
 

 The
 
 Contacts
 
 and
 
 Activities
 
 standard details
 

![scr_mobile_wizard_standart_detail_list.png](/guides/sites/en/files/documentation/user/en/mobile_app_setup/BPMonlineHelp/mobile_app_setup_detail/scr_mobile_wizard_standart_detail_list.png)



 You can add new details and configure the existing ones via the mobile application wizard.
 







 Add detail
----------------


### 


 To add an embedded detail:


1. Open the System Designer by clicking
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/mobile_app_setup/BPMonlineHelp/mobile_app_setup_detail/btn_system_designer.png)
 .
2. Click
 
**Mobile application wizard** 

 in the “System setup” block.
3. Select the workplace to edit and click
 **Open** 
 .
4. Click the
 **Set up sections** 
 button.
5. Select a section in the list and click
 **Page setup** 
 ().
6. On the section page, select the
 **Embedded detail** 
 in the
 **New** 
 button menu (
 [Fig. 1](#XREF_79181_228)
 ).
 





 Fig. 1
 

 Adding an embedded detail
 

![scr_mobile_wizard_add_detail_inside.png](/guides/sites/en/files/documentation/user/en/mobile_app_setup/BPMonlineHelp/mobile_app_setup_detail/scr_mobile_wizard_add_detail_inside.png)
7. In the detail setting window:
 


	1. Select a detail to add.
	   
	
	 Some of the existing details are designed for specific sections. Be sure to select the version of a detail whose name specifically indicates that the detail was designed for this particular section. For example, when adding the
	 
	 Attachments
	 
	 detail to the
	 
	 Contacts
	 
	 section page, select the “Contact’s attachments” detail.
	2. Specify the detail title.
	3. In the
	 **Detail column** 
	 field, select the column that connects detail records to the current record in the section. For example, records on the
	 
	 Attachments
	 
	 detail in the
	 
	 Contacts
	 
	 section are connected to the
	 
	 Contacts
	 
	 section by the
	 
	 Contact
	 
	 column.
	4. In the
	 **Object column...** 
	 field, specify the column – section identifier. By default, it is “Id”.
	5. Save the detail setup parameters.
	 
	
	
	
	 As a result, a new detail will be added to the section page. For some details, the default columns may not be configured. In this case, you must add the displayed columns manually. Adding columns to a detail is similar to
	 
	[adding columns](/docs/7-16/user/customization_tools/mobile_app_setup/page/set_up_mobile_application_section_page#HT_chapter_mobile_wizard_section_page) 
	
	 to a section page.
8. Save the detail (
 [Fig. 2](#XREF_77160_229)
 ).
 





 Fig. 2
 

 Setting up an embedded detail
 

![scr_mobile_wizard_section_built-in_detail_setup.png](/guides/sites/en/files/documentation/user/en/mobile_app_setup/BPMonlineHelp/mobile_app_setup_detail/scr_mobile_wizard_section_built-in_detail_setup.png)


### 
 To add a standard detail:



 To display data correctly on the standard detail, add the corresponding section in the mobile application. For example, to display data on the
 
 Documents
 
 detail of the contact’s page, add the
 
 Documents
 
 section in the mobile application.
 



 To add a standard detail:
 


1. Open the mobile wizard and open the section page for editing (perform steps
 **1-4** 
 listed in the “
 [To add an embedded detail:](#XREF_16341)
 ” block).
2. On the page that opens, click
 **Set up details** 
 .
3. On the section detail setup page (
 [Fig. 1](#XREF_38521_116)
 ), click the
 **New detail** 
 button.
 





 Fig. 1
 

 Section detail settings page
 

![scr_mobile_wizard_section_detail_setup.png](/guides/sites/en/files/documentation/user/en/mobile_app_setup/BPMonlineHelp/mobile_app_setup_detail/scr_mobile_wizard_section_detail_setup.png)
4. The page of a newly added standard detail will contain only required fields (
 [Fig. 2](#XREF_82477_235)
 ).
 





 Fig. 2
 

 Required fields on a detail page
 

![scr_mobile_required_fields.png](/guides/sites/en/files/documentation/user/en/mobile_app_setup/BPMonlineHelp/mobile_app_setup_detail/scr_mobile_required_fields.png)



 Thus, if you add the
 
 Documents
 
 standard detail to any of the sections in the mobile application, the detail page will contain only required fields (
 [Fig. 3](#XREF_46561_33)
 ).
 





 Fig. 3
 

 Detail page with required fields
 

![scr_mobile_wizard_fields_required.png](/guides/sites/en/files/documentation/user/en/mobile_app_setup/BPMonlineHelp/mobile_app_setup_detail/scr_mobile_wizard_fields_required.png)
5. Add the corresponding section to mobile application and configure it for the correct operation and display of details.
 



 For example, add the
 
 Documents
 
 section in the mobile application wizard to display additional fields on the
 
 Documents
 
 detail page And
 
[set up fields on the edit page](https://academy.bpmonline.com/documents?product=mobile&ver=7&id=1394) 

 .







 Edit detail
-----------------


### 
 Edit an embedded detail



 To edit embedded details, use the buttons next to the detail name (
 [Fig. 1](#XREF_59339_230)
 ).
 





 Fig. 1
 

 Embedded detail editing buttons
 

![scr_mobile_wizard_set_detail_edit.png](/guides/sites/en/files/documentation/user/en/mobile_app_setup/BPMonlineHelp/mobile_app_setup_detail/scr_mobile_wizard_set_detail_edit.png)



 Click the
 **Set** 
 button to edit the detail. In the
 **Detail setting** 
 window (
 [Fig. 2](#XREF_77160_229)
 ), make your changes and click
 **Save** 
 .
 



 Use the
 ![btn_move_down_detail.png](/guides/sites/en/files/documentation/user/en/mobile_app_setup/BPMonlineHelp/mobile_app_setup_detail/btn_move_down_detail.png)
 and
 ![btn_move_up_detail.png](/guides/sites/en/files/documentation/user/en/mobile_app_setup/BPMonlineHelp/mobile_app_setup_detail/btn_move_up_detail.png)
 buttons to modify the location of the detail on the section page.
 



 To delete the embedded detail from the section page, click the
 **Delete** 
 button.
 


### 
 Edit standard detail



 To do this, move to the detail configuration page (
 [Fig. 1](#XREF_69202_460)
 ).
 





 Fig. 1
 

 Section detail settings page
 

![scr_mobile_wizard_section_detail_setup00001.png](/guides/sites/en/files/documentation/user/en/mobile_app_setup/BPMonlineHelp/mobile_app_setup_detail/scr_mobile_wizard_section_detail_setup00001.png)



 To delete a standard detail from a section page, click the
 **Delete** 
 button next to the detail name.
 



 To modify the parameters of existing standard details, click the
 **Set** 
 button next to the detail name. Setting up parameters of the standard detail is identical to setting up parameters described in the “” (
 [Fig. 2](#XREF_91053_245)
 ) block.
 





 Fig. 2
 

 Setting up a detail
 

![scr_mobile_wizard_standart_detail_option.png](/guides/sites/en/files/documentation/user/en/mobile_app_setup/BPMonlineHelp/mobile_app_setup_detail/scr_mobile_wizard_standart_detail_option.png)



 You can specify a column of a connected object detail and configure data filtering by this object. For example, on the activity page, you can display the contacts connected to the account, which is specified in the activity. To do this, add the
 
 Contacts
 
 detail to the activity record page and specify “Account” in both the
 
 Detail column
 
 and
 
 Object column
 
 fields
 




