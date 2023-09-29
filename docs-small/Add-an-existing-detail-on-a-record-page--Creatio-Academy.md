


 You can change the details on section pages and add existing details to a page. An “existing detail” is a page element that has been created and configured in the Detail Wizard. Learn more:
 [Create a detail to add it to a record page](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/page_layout/create_a_detail/create_new_detail#title-150-3) 
 .
 





 Add an existing detail to a record page.
--------------------------------------------





 Example.
 
 Display the out-of-the-box
 
 Activities
 
 detail in the custom
 
 Requests
 
 section.
 






 Note.
 
 Learn more about creating and configuring a section in the
 [Add a new section](https://academy.creatio.com/documents?product=base&ver=7&id=1245) 
 article.
 




 To add a detail to a section page:
 


1. Open the relevant section, e. g.,
 
 Requests
 
 .
2. Click
 
 View
 
 →
 
 Open Section Wizard
 
 .
3. In the
 
 Section pages
 
 block of the Section Wizard:
 


	1. click
	 
	 Edit page
	 
	 if you have only one edit page in your section
	2. click
	 **the link to the relevant page** 
	 if there are several pages in the section (Fig. 1).
	 
	
	
	
	
	 Fig. 1 Selecting a section page from the list
	 
	
	![scr_section_wizard_multiple_section_pages.png](/docs/sites/en/files/images/NoCode_Customization/page_layout/scr_section_wizard_multiple_section_pages.png)
4. Open the tab where you would like to place the detail. For example,
 
 Processing
 
 .
5. Click
 
 New detail
 
 .
6. Specify the detail settings in the dialog box (Fig. 2):
 




 Fig. 2 Detail dialog box
 

![scr_section_wizard_add_detail_window_activity.png](/docs/sites/en/files/images/NoCode_Customization/page_layout/scr_section_wizard_add_detail_window_activity.png)


	1. In the
	 
	 Detail
	 
	 field, select the detail to add to the page.
	 
	
	
	
	
	
	 Note.
	 
	 If the relevant detail is not available, the object you would like to use might not be registered as a detail yet. Use the
	 
	 Advanced settings
	 
	 section to check if the detail schema and related configuration elements exist. If not, create the detail. Learn more:
	 [Add a detail based on an existing object](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/page_layout/create_a_detail/create_new_detail#title-150-1) 
	 .
	2. Use the
	 
	 Title
	 
	 field to specify the detail’s title to display on the page.
	3. Use the
	 
	 Where detail column
	 
	 field to specify the detail object’s column to filter the detail records. This is a lookup column that uses the current section’s object as a lookup. The name of this column usually matches that of the section object. For example, select “Request” in the
	 
	 Where detail column
	 
	 to connect the
	 
	 Equipment request
	 
	 detail to the
	 
	 Requests
	 
	 section.
	4. Use the
	 
	 Equals to page column
	 
	 field to specify the section object’s column to filter the detail records. Normally, this is the
	 
	 Id
	 
	 column. That way, a detail will only display the records where the value of the
	 
	 Request
	 
	 column matches that of the current section record’s Id column. In other words, the detail will only display the equipment connected to the current request.
	 
	
	
	 Note.
	 
	 If the object can only be connected to the current section’s object via a single column, Creatio populates the field with the value of that column.
7. Click
 
 Save
 
 →
 
 Section wizard
 
 →
 
 Save
 
 .
 



 As a result, a new
 
 Activity
 
 detail will be added to the request page.







 Edit an existing detail on a record page
----------------------------------------------


### 
 Change a detail’s settings



 To
 **change a detail’s settings** 
 or
 **edit its name** 
 on the record page:
 


1. Open the relevant section, e. g.,
 
 Requests
 
 .
2. Select any record in the section list and click
 
 Open
 
 .
3. Click
 
 View
 
 →
 
 Open Section Wizard
 
 .
4. Open the tab with the detail to edit.
5. Select the detail and click
 ![btn_chapter_content_designer_htlm_element_edit.png](/guides/sites/default/files/documentation/user/ru/ui_business_logic_customization/BPMonlineHelp/add_existing_detail_on_page/btn_chapter_content_designer_htlm_element_edit.png)
 . You can edit the detail’s title displayed on the record page and the detail’s record display parameters (Fig. 3).
 




 Fig. 3 Editing an existing detail on a record page
 

![gif_detail_wizard_edit_detail_properties.gif](/docs/sites/en/files/images/NoCode_Customization/page_layout/gif_detail_wizard_edit_detail_properties.gif)





 Note.
 
 The title changed in the
 
 Title
 
 field on the Section Wizard’s edit page will be available only on the pages of the corresponding section.
 



### 
 Set up the detail’s appearance


1. Open the relevant section, e. g.,
 
 Requests
 
 .
2. Select any record in the section list and click
 
 Open
 
 .
3. Open the tab with the detail to set up.
4. Click
 ![btn_com_roles_actions_menu.png](/guides/sites/default/files/documentation/user/ru/ui_business_logic_customization/BPMonlineHelp/add_existing_detail_on_page/btn_com_roles_actions_menu.png)
 next to the detail’s title and select
 
 Detail setup
 
 to open the Detail wizard (Fig. 4):
 




 Fig. 4 Navigating to the Detail wizard
 

![chapter_section_wizard_add_detail_record.png](/docs/sites/en/files/images/NoCode_Customization/page_layout/chapter_section_wizard_add_detail_record.png)





 Note.
 
 You can also edit a detail in the Section wizard. To do this, open the tab with the detail to set up and click
 ![btn_chapter_content_designer_htlm_element_edit.png](/guides/sites/default/files/documentation/user/ru/ui_business_logic_customization/BPMonlineHelp/add_existing_detail_on_page/btn_chapter_content_designer_htlm_element_edit.png)
 . In the page that opens, click
 ![btn_chapter_content_designer_htlm_element_edit.png](/guides/sites/default/files/documentation/user/ru/ui_business_logic_customization/BPMonlineHelp/add_existing_detail_on_page/btn_chapter_content_designer_htlm_element_edit.png)
 to the right of the detail’s title.
5. Select the
 
 Make the list editable
 
 checkbox to make the detail’s data editable directly from the list without the need to open a new page. The checkbox may be greyed out if the detail was created or edited in the
 
 Advanced settings
 
 section and its configuration is different from the Detail wizard’s base configuration.
6. Open the
 
 Pages
 
 tab to set up the detail fields.
7. Click
 
 Save
 
 after editing the detail.
 



 As a result, the detail will change. The updated detail will be displayed on all the pages of the relevant section.



 Delete a detail from the record page
--------------------------------------


1. Open the relevant section, e. g.,
 
 Requests
 
 .
2. Select any record in the section list and click
 
 Open
 
 .
3. Click
 
 View
 
 →
 
 Open Section Wizard
 
 .
4. Open the tab with the detail to delete.
5. Click
 ![btn_delete_record_on_dtl.png](/guides/sites/default/files/documentation/user/ru/ui_business_logic_customization/BPMonlineHelp/add_existing_detail_on_page/btn_delete_record_on_dtl.png)
 next to the detail’s title (Fig. 5).
 




 Fig. 5 Deleting a detail from the record page
 

![chapter_section_wizard_delete_detail.png](/docs/sites/en/files/images/NoCode_Customization/page_layout/chapter_section_wizard_delete_detail.png)



 As a result, the detail will be deleted from the section page. The detail will still be available in the Section wizard's detail list and in the advanced settings.




