


 Use tags to segment your records manually. For example, you can tag records in the
 
 Contacts
 
 section to mark your VIP-customers or the “blacklisted” customers. Each record is tagged individually. You can quickly search and filter tagged records. For example, you can use tags to find the necessary article in the
 
 Knowledge base
 
 section.
 



 A section record can have several tags at a time. Also, you can assign either tags that will be displayed only to you or will be available to other Creatio users or customers on the self-service portal.
 








 Work with tags
---------------------



 You can assign tags to any record in Creatio. Records are tagged manually. You can tag a record directly from the record page. Use the section filter area to filter the records by tags. Creatio  uses separate tag lists for each section.
 



 The following types of tags are used in Creatio :
 


* **Private** 
 tags are only visible and accessible to the user who created them. Any user can create any number of private tags. Private tags are not visible to managers and system administrators. Private tags in Creatio  are marked green.
* **Corporate** 
 – tags that are visible to all the company employees. Any employee can add or remove a corporate tag. Corporate tags can be created by all employees/roles who are permitted to perform the “Corporate tag management” operation. Corporate tags in Creatio  are marked blue.
* **Public** 
 – tags that are visible for all the company employees and for the self-service portal users. Any employee can add or remove a public tag. Public tags can be created by all employees/roles that are permitted to perform the “Public tag management” operation. Public tags in Creatio  are marked red.





 Note.
 
 By default, the permission to create public and corporate tags is only granted to the “System administrators” role.
 









 Create a tag
-------------------


1. Open a record that you want to tag, for example, a contact page, and click the
 ![btn_com_tag_on_the_record_page.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_tags/btn_com_tag_on_the_record_page.png)
 button.
2. In the opened window, enter the name of your new tag. The drop-down menu will display the tag types that you can create. Select tag type to finish creating a tag (Fig. 1).
 





 Fig. 1
 

 Creating a tag
 

![scr_groups_add_new_tag.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_tags/scr_groups_add_new_tag.png)



 As a result, a new tag will be created in Creatio . The currently opened record will be tagged with this new tag.
 





 Note.
 
 When creating a tag, use the
 
 +
 
 button in the window or the “Down”, “Up” and “Enter” keys.
 






 Note.
 
 If the combination of the type and the name of your new tag already exists, Creatio will not create new tags. In this case, the existing tag will be assigned to the section record.
   

 The names of personal tags created by different users may coincide.
 









 Tag a record
-------------------


1. Open a record that you want to tag, for example, a contact page, and click the
 ![btn_com_tag.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_tags/btn_com_tag.png)
 button.
2. In the opened window, start entering the name of the existing tag that you want to assign to the selected record. The drop-down list will show the tag search results. Select your tag (Fig. 1).
 





 Fig. 1
 

 Tagging a record
 

![scr_groups_tagging.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_tags/scr_groups_tagging.png)



 As a result, the selected contact will be tagged.
 





 Note.
 
 To view the full list of tags, press the “Down” key while the cursor is in the empty
 
 Tags
 
 window string.
 




 To filter records by tags, click the
 ![btn_com_tag_in_section.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_tags/btn_com_tag_in_section.png)
 button in the filter area. Place the cursor in the opened window and select your tag from the list (Fig. 2). You can also enter the tag name manually.
 





 Fig. 2
 

 Selecting a tag to filter section records
 

![scr_groups_tags_filtration_select.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_tags/scr_groups_tags_filtration_select.png)



 As a result, the section records will be filtered by the selected tag.
 








 Remove a tag
-------------------


1. Open a record that you want to remove a tag from, for example, a contact page, and click the
 ![btn_com_tag00001.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_tags/btn_com_tag00001.png)
 button.
2. In the opened window, click
 
 X
 
 next to the tag to remove (Fig. 1). The tag will be removed from the section record. Removing the tag from the record will not result in deleting the tag itself.
 





 Fig. 1
 

 Removing a tag
 

![scr_groups_clear_tagging.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_tags/scr_groups_clear_tagging.png)








 Set up advanced filter for a tagged record
-------------------------------------------------



 Use the advanced filter function to apply several parameters or filter conditions to tagged records.
 





 Example.
 
 Display the accounts tagged with “Pay attention” whose profile completion is less than 50%.
 




 To do this:
 


1. From the
 
 Filters/folders
 
 menu, select the
 
 Switch to advanced mode
 
 option.
2. In the filter condition setup area perform the following:
 


	1. Click
	 
	 Add condition
	 
	 .
	2. Press the
	 ![btn_com_expand.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_tags/btn_com_expand.png)
	 button next to the “Account” object title.
	3. In the added field, select the “Accounts section record tag (by column Object)” reverse connection object.
	4. In the
	 
	 Column
	 
	 field, specify the “Quantity” column of the connected object.
	5. Change the “count” condition type to “exists”.
	6. Add additional “Tag” condition and select the “Pay attention” tag.
	7. Add the “Data entry compliance” condition.
	8. Select the “<” condition and specify 50.
3. Click the
 
 Apply
 
 button (Fig. 1).
 





 Fig. 1
 

 – Setting up the advanced filter for a record tagged with “Pay attention”
 

![scr_groups_tags_applying_filter_to_tagged_record.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_tags/scr_groups_tags_applying_filter_to_tagged_record.png)



 As a result, all accounts tagged with “Pay attention” and with profile completion of less than 50% will be displayed.
 





 Note.
 
 Save the filter conditions as a folder for further use.
 









 Tags FAQ
---------------


### 



 How to view a list of available tags?



 Open a section page. In the filter area, click the
 ![btn_com_tag_in_section00002.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_tags/btn_com_tag_in_section00002.png)
 button. Hover the mouse cursor over the displayed field. A list of all tags available in current section will be displayed (Fig. 1).
 





 Fig. 1
 

 A list of available tags
 

![scr_groups_tags_filtration_list.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_tags/scr_groups_tags_filtration_list.png)



 A system administrator has permission to display a list of all section tags. One way to manage an object record is to create and edit a lookup based on that object (e.g., to edit the existing tags in the
 
 Activities
 
 section, create a lookup based on the “Activity section tag” object). All tags of the corresponding section will be viewable as records of that lookup. Users with system administrator privileges will have access to all tags of all users (including private tags) this way.
 


### 



 How to edit and delete existing tags?



 Tags can be edited and deleted by modifying records in the corresponding section tag object (e.g., “Contacts section tag”, “Accounts section tag”, etc.). One way to manage an object record is to create and edit a lookup based on that object (e.g., to edit the existing tags in the
 
 Activities
 
 section, create a lookup based on the “Activity section tag” object). Standard access permissions apply.
 


### 



 How to delete a tag?



 A user with access to the
 
 Lookups
 
 section has permission to delete tags. Create a lookup with a tag of the specific section as an object (for example, “Activity section tag”). Find the tag to delete in the created lookup and click the
 ![btn_delete_record.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_tags/btn_delete_record.png)
 button.
 




