


 Merge duplicate records in a Creatio object automatically using the
 
 Find and merge duplicates
 
 element.
 





 Note.
 
 Before you set up the element, make sure
 [bulk duplicate search](https://academy.creatio.com/documents?id=1959) 
 and
 [global search](https://academy.creatio.com/documents?id=1712) 
 features are configured, and the relevant section has active duplicate search rules.
 




 The resulting record is based on the earliest-created record and populated as follows:
 


* The populated fields of the earliest-created record remain unchanged.
* The empty fields of the earliest-created record contain data of the latest-created record.
* The details contain data from details of all duplicate records.



 Configure the duplicate search parameters in the element setup area (Fig. 1).
 




 Fig. 1 The
 
 Find and merge duplicates
 
 element setup area
 

![scr_element_find_duplicates.png](/docs/sites/en/files/images/BPM_Tools/find_and_merge_duplicates/scr_element_find_duplicates.png)



 Fill out the fields using the parameter value menu:
 


1. Specify the object to search for duplicates in the
 
 Object
 
 field. You can select only the objects that have active duplicate search rules.
2. Select the ID of the record whose duplicates to search in the
 
 Record identifier
 
 field.
3. Specify the search rules in the
 
 Duplicate search rules
 
 field in one of the following ways:
	* Select
	 
	 All rules
	 
	 to use all active rules. Default option.
	* Select
	 
	 Selected rules
	 
	 and click the
	 
	 Add rule
	 
	 button to choose specific active rules. If you select this option but do not choose any rules, the element will revert to the
	 
	 All rules
	 
	 option after you close the setup area.



 If you deactivate a duplicate search rule specified in the element, the element will no longer use it. If you deactivate all specified rules, the process that contains the element will fail to complete. You will be able to see the reason for failure in the process log.
 





 Note.
 
 Creatio warns you that a business process might use the duplicate search rule when you deactivate it. However, Creatio does not check whether any
 
 Find and merge duplicates
 
 element is using it currently.
 





