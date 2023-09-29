


 Mini pages in Creatio are “light” versions of regular record edit pages. They show a limited number of fields from regular record pages and provide better control over the UX of your users who work with the section records.
 



 Mini pages enable your users to perform the following operations with fewer clicks:
 


* preview section records without having to open standard record pages;
* quickly add and edit section records;
* run certain actions right from a record mini page (e.g., making a call or sending an email message);
* open the linked records displayed on the mini page in one click, etc.





 Note.
 
 Learn more about working with mini pages of different records in the “
 
[Mini pages](https://academy.bpmonline.com/documents?product=base&ver=7&id=1622) 

 ” article.
 




 After you set up your regular section pages in the Section Wizard, you can start configuring mini pages.
 



 To configure a mini page in Creatio:
 


1. Open the section, where you need to set up mini pages.
2. In the section, click
 
 View
 
 →
 **Open Section Wizard** 
 .
3. In the
 
 Mini page
 
 area, select the functions for the mini pages in this section (
 [Fig. 1](#XREF_23934_335)
 ):
 


	1. **Add record** 
	 – the mini page will open when a user clicks
	 
	 Add
	 
	 in the section. The user can then open the complete record page by clicking
	 ![chapter_minicards_expand.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_mini_pages/chapter_minicards_expand.png)
	 on the mini page.
	2. **Edit record** 
	 – this will enable the users to edit existing records via the mini page. This option adds an “edit” button to the mini page. The user can click
	 ![chapter_minicards_edit.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_mini_pages/chapter_minicards_edit.png)
	 in the top right corner of the mini page to edit the record.
	3. **View record** 
	 – this will enable the users to preview the record data without opening the standard record edit page. The mini page will pop up when the user hovers their cursor over the record link shown in a list.
	 
	
	
	
	
	
	 Fig. 1
	 
	
	 Enabling mini pages for adding and viewing section records
	 
	
	![scr_section_wizard_minicard_checkbox.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_mini_pages/scr_section_wizard_minicard_checkbox.png)
4. Click
 **Edit mini page** 
 to switch to Mini Page Designer.
5. In the Mini Page Designer, select the mini page mode (
 **Add mode/Edit mode/View mode** 
 ) for the function(s) selected on step 3.
 





 Note.
 
 The “HeaderContainer” element at the top of the field setup area of the Mini Page Designer is non-editable. It is used to display the mini page caption correctly.
6. Set up the layout of the corresponding mini pages:
 


	1. Drag the necessary columns from the
	 
	 Page elements
	 
	 area to the field setup area (
	 [Fig. 2](#XREF_57630_Fig_363_Adding)
	 ).
	2. Click
	 ![btn_set_columns_edit.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_mini_pages/btn_set_columns_edit.png)
	 to modify column properties (
	 [Fig. 3](#XREF_64801_337)
	 )
	 
	
	
	
	
	
	 Fig. 2
	 
	
	 Setting up the layout of a mini page
	 
	
	![section_wizard_drag_column_mini_page.gif](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_mini_pages/section_wizard_drag_column_mini_page.gif)





 Note.
 
 Working with column properties on mini pages is similar to that of the regular section page.
 




 Read more >>>
 







 Fig. 3
 

 Editing the mini page columns
 

![scr_section_wizard_minicard_columns.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_mini_pages/scr_section_wizard_minicard_columns.png)


1. To configure the behavior of the fields on the mini page, you can use business rules.
 





 Note.
 
 Working with business rules for mini page fields is similar to that of the regular section page fields.
 
 Read more >>>
 







 Note.
 
 You can use the
 
 Source code
 
 tab to edit the source code of the mini page and customize it even further. The tab displays the source code of the page view module that was generated based on the changes you made during the previous steps. Learn more about working with the source code of Creatio modules in the
 

 “
 
[Module designer](https://academy.creatio.com/documents/technic-sdk/7-16/module-designer) 

 ” article.
2. Click
 ![btn_section_wizard.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_mini_pages/btn_section_wizard.png)
 to return to the Section Wizard.
3. Save the changes.
 



 As a result, mini pages will become available in the section for selected functions. For example, if you enabled and set up the “Add mode” - a mini page will open when a user clicks
 
 New…
 
 in the section (
 [Fig. 4](#XREF_52570_338)
 ). If you enabled and set up the “View mode” - the preview mini page will pop up when a cursor hovers over the section record link in any list that shows the records of this section (
 [Fig. 5](#XREF_48266_Fig_366_Mini_page)
 ).
 





 Fig. 4
 

 Example of a mini page for adding a section record
 

![scr_section_wizard_add_application_minicard.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_mini_pages/scr_section_wizard_add_application_minicard.png)





 Fig. 5
 

 Example of a mini page for previewing a section record
 

![chapter_section_wizard_preview_mini_page.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_mini_pages/chapter_section_wizard_preview_mini_page.png)




