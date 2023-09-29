


 Use folders to organize and segment your records. Setting up folders will assist you to easily find the necessary records among multiple data. For example, in the
 
 Contacts
 
 section, you can create a “New customers” folder that will filter records by the contact type (“Customer”) and the record date (“Current month”). If you select a folder within a section, only the records that match folder filter conditions will be displayed. You can add your most frequently used folders in favorites.
 



 A section record can be included in one or more folders.
 



 The folders can have a tree-like structure and contain both parent and subordinate folders. The folder structure does not affect the contents of the folders. For example, if a record is included in one of the subordinate folders, it does not necessarily mean it is included in the parent folder.
 



 You can create the necessary folder structure and specify your own rules for the folder contents. The procedures for creating static and dynamic folders are different. Deleting a folder will not result in deleting the records contained in it.
 





 Static folders
------------------



**Static folders** 
 (indicated with the
 ![icn_basis_static_group.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_groups/icn_basis_static_group.png)
 icon) include only those section records that have been added to these folders manually or via converting from the dynamic folder. “VIP” or “Blacklist” are examples of static folders because the decision to include certain customers into such folders is made for each record individually. Static folders can be used to group other folders.
 





 Attention.
 
 Static folders are only available in some Creatio sections.
 



### 
 Create a static folder



 Static folders are only available in some Creatio sections. You can create a static folder in the following ways:
 


* Add a folder and fill it with records manually.
* Copy the folder content from a dynamic folder.



 To add a static folder manually:
 


1. In the
 
 Filter
 
 menu, select the
 
 Show folders
 
 option. The folder area will be displayed.
2. In the
 
 Add folder
 
 menu, select the
 
 Static
 
 command.
 

 Fig. 1
 
 Creating a static folder
 




[![scr_folders_act_add_static_folder.png](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_act_add_static_folder.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_act_add_static_folder.png)






 Note.
 
 The
 
 Add folder
 
 button menu is only displayed for sections where you can create a static folder.
3. Enter the folder name and click
 
 OK
 
 on the opened page.




 As a result, the new static folder will be added in the section. You need to populate this folder manually by selecting the required records and running the [Add to folder] action Read more in the "
 [Add records to a static folder](#title-753-7) 
 " article.
 








 To convert a dynamic folder into a static folder:
 




 Fig. 2
 
 Converting the dynamic folder to static
 




[![scr_folders_convert_to_static.png](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_convert_to_static.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_convert_to_static.png)



1. In the
 
 Filter
 
 menu, select the
 
 Show folders
 
 option.
2. In the folder tree, select a dynamic folder which content you need to include in a static folder.
3. From the
 ![btn_lookups_add_type.png](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/btn_lookups_add_type.png)
 menu, select the
 
 Convert folder
 
 option.
4. Enter the new folder name and click
 
 OK
 
 in the opened page.



 As a result, the static folder will appear as a subfolder of the selected dynamic folder. The content of the folders will be identical at the moment of conversion. Further, you can manually include or exclude records using the
 
 Add to folder
 
 action. Read more in the "
 [Add records to a static folder](#title-753-7) 
 " article.
 





 Note.
 
 The
 
 Convert folder
 
 action does not affect the content of the original dynamic folder.
 



### 
 Add records to a static folder


1. In the
 
 Actions
 
 menu, select the [Select multiple records] command (
 [Fig. 3](https://academy.creatio.com/documents/base/7-16/how-create-static-folder?document=marketing#XREF_64388_100) 
 ).
 

 Fig. 3
 
 Switching to the multiple selection mode
 




[![scr_folders_select_multiple_records.png](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_select_multiple_records.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_select_multiple_records.png)






 Note.
 
 Switching to the multiple selection mode is not required for adding a single record to the static folder.
 





 Fig. 4
 
 Adding a record to a static folder
 




[![scr_folders_include_in_folder.png](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_include_in_folder.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_include_in_folder.png)
2. Check the boxes next to the records you want to include in the static folder.
3. In the
 
 Actions
 
 menu, select the
 
 Include in folder
 
 command.
4. In the opened window, select the needed folder and click the
 
 Select
 
 button (or double-click the needed folder).



 As a result, the records selected in the section will be included in this static folder.
 


### 
 Remove records from a static folder


1. In the section
 
 Filter
 
 menu, select the
 
 Show folders
 
 command.
2. Select a static folder whose records must be excluded.
3. In the
 
 Actions
 
 menu, select the
 
 Select multiple records
 
 command.
4. Select the records that must be excluded from the selected folder.
5. In the
 
 Actions
 
 menu, select the
 
 Exclude from folder
 
 command.




 Fig. 5
 
 Excluding records from the selected static folder
 




[![scr_folders_remove_from_folder.png](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_remove_from_folder.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_remove_from_folder.png)




 As a result, the selected records will be excluded from the selected static folder.
 



 Dynamic folders
-----------------



**Dynamic folders** 
 (indicated with the
 ![icn_basis_dynamic_group.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_groups/icn_basis_dynamic_group.png)
 icon) contain only those section records that match the specified filter conditions. For example, you can create a dynamic folder “New customers“ for records filtered by the date they were created on.
 



 Records cannot be manually included in or excluded from dynamic folders. A record will be displayed in a dynamic folder only if it matches the folder filter. If the record no longer meets the folder filter, it will automatically be excluded from that folder.
 



 For example, your “Competitors” folder filters the records by the account type (“Competitors”). Thus, the companies for which the “Competitor” value is specified will be automatically included in the folder. If the company type changes, the record will automatically be excluded from that folder.
 


### 
 Create a dynamic folder



 To create a dynamic folder with the corresponding filter conditions:
 


1. In the
 
 Filter
 
 menu, select the
 
 Show folders
 
 command.
 

 Fig. 1
 
 [Show folders] command
 




[![scr_folders_act_show_folders.png](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_act_show_folders.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_act_show_folders.png)
2. Click the
 
 Add folder
 
 button. In the sections where the static folders are available, select the
 
 Dynamic
 
 command in the button menu.
3. Populate the opened window with the folder name and click
 
 OK
 
 – you will see a filter condition setup area appear.
 

 Fig. 2
 
 Folder filter setup area
 




[![scr_folders_mnu_setup_filter.png](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_mnu_setup_filter.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_mnu_setup_filter.png)
4. Set the needed filter conditions and click the
 
 Save
 
 button.




 Fig. 3
 
 Saving a folder filter
 




[![scr_folders_dynamic_folder_filtering_conditions.png](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_dynamic_folder_filtering_conditions.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_dynamic_folder_filtering_conditions.png)






 Note.
 
 Filter condition setup is identical to the
 [advanced filter](/docs/7-18/user/platform_basics/business_data/filters_shortcut/filters#title-1755-10) 
 setup.
 




 As a result, all the records that meet the filter conditions appear automatically in the section list when you select the folder.
 





 Note.
 
 You can also save an advanced filter as a dynamic folder. To do this, click the [Save as] button in the filter area.
 




 You can copy the necessary folder if you need to create a folder whose filter conditions are partially identical to one of the existing folders. You can also copy the original folder access rights if necessary. To do this, select
 
 Copy
 
 in the
 ![btn_com_folder_filter.png](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/btn_com_folder_filter.png)
 button menu of the necessary folder.
 



 Add folders to favorites
--------------------------



 You can add the most frequently used folders to the list of favorites.Both static and dynamic folders can be added to the list.
 



 To add a folder to favorites, select it and click the
 ![btn_com_folder_favorite.png](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/btn_com_folder_favorite.png)
 button (
 [Fig. 1](https://academy.creatio.com/documents/base/7-16/how-manage-favorite-folders?document=marketing#XREF_51148_129) 
 ).
 




 Fig. 1
 
 Adding a folder to favorites
 




[![scr_folders_mark_as_favorite.png](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_mark_as_favorite.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_mark_as_favorite.png)




 All added folders are displayed as subordinate to the “Favorite“ folder in the folder area. In addition, the favorite folders become available in the [Filter] menu (
 [Fig. 2](https://academy.creatio.com/documents/base/7-16/how-manage-favorite-folders?document=marketing#XREF_88241_130) 
 ).
 




 Fig. 2
 
 Selecting the favorite folder in the [Filter] menu
 




[![scr_folders_menu_favorite.png](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_menu_favorite.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/product/bpm'online%20base/base/7.16.0/BPMonlineHelp/chapter_groups/scr_folders_menu_favorite.png)





