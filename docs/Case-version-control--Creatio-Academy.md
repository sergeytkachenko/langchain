


 Case version control enables you to track the history of changes and eliminate possible disruptions in launched case instances when editing the case schema.
 



 Changes made in the case schema can be saved as a separate version. All case versions are saved in Creatio and can be viewed on the case properties page. The case version  that is launched in the section according to the set conditions is considered as actual. Usually, this is the last saved case version. You can switch to any other saved case version as actual. Only one actual case version can exist at a time.
 



 Save a new case version
-------------------------



 When saving the case select whether to save the changes as a new version or update the current version (Fig. 1).
 




 Fig. 1. Selecting the case saving method
 

![scr_case_versions_save_new_version.png](/docs/sites/en/files/images/BPM_Tools/dcm_case_versioning/scr_case_versions_save_new_version.png)



 If you click
 
 Save
 
 without selecting any options, Creatio will check the following:
 


* whether there are case instances in progress
* whether the package that stores the original case version is open for modification.



 If there are
 **no case instances in progress** 
 and the
 **case package is open for modification** 
 , all changes will be saved to the current case version.
 



 If there are
 **case instances in progress** 
 , Creatio will suggest creating a new version. If you choose not to, Creatio will attempt to save the changes to the current version. However, this may trigger errors in the case instances that are in progress.
 



 If the
 **case package is closed for modification** 
 , Creatio will suggest saving a new version of the case. After confirmation, the new version will be saved in the package specified in the “Current package” system setting.
 





 Note.
 
 If you save the case package as an archive, and install the package in a different environment, the actual version of the case will be transferred with the package. Creatio will always determine the final current version of the case based on which package is higher in the hierarchy.
 




 View the case version
-----------------------



 The case versions are available on the case properties page on the
 
 Case versions
 
 tab (Fig. 2).
 




 Fig. 2. Viewing the list of case versions
 

![gif_case_versions_open_case_properties.gif](/docs/sites/en/files/images/BPM_Tools/dcm_case_versioning/gif_case_versions_open_case_properties.gif)



 Click the case title to open the current case version in the case designer.
 



 Set the actual case version
-----------------------------



 You can change the actual case version on the case properties page on the
 
 Case versions
 
 tab. To do this, select the needed version and select “Set as actual version” in the
 ![btn_detail_menu.png](/docs/sites/default/files/images/BPM_Tools/dcm_case_versioning/btn_detail_menu.png)
 button menu (Fig. 3).
 




 Fig. 3. Changing the actual case version
 

![scr_case_versions_change_active_version.png](/docs/sites/en/files/images/BPM_Tools/dcm_case_versioning/scr_case_versions_change_active_version.png)



 Run the new case version
--------------------------



 After saving a new version, all new case instances will run using that version. However, all unfinished case instances will proceed using their original case version. You can switch such an instance to the new version using the
 
 Change case
 
 button on the record page (Fig. 4). After confirmation, the current case instance will be canceled. A new case instance will run using the actual case version.
 




 Fig. 4. Switching a running case to the new version.
 

![scr_case_versions_change_launched_case_version.png](/docs/sites/en/files/images/BPM_Tools/dcm_case_versioning/scr_case_versions_change_launched_case_version.png)








