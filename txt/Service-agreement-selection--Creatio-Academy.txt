


 The service agreements are available in Service Creatio, enterprise edition. Creatio selects applicable service agreement automatically, based on the values in the
 
 Contact
 
 and
 
 Account
 
 fields. Only active service agreements whose expiration date exceeds or is equal to the current date can be selected. Service agreements in the statuses that are marked as
 
 Active
 
 in the
 
 Service agreement statuses
 
 lookup are considered open.
 



 The list of agreements available for selection depends on the values in the
 
 Contact
 
 and the
 
 Account
 
 fields of the case page, as well as on information on the
 
 Service recipients
 
 detail that is located on the
 
 Contract provisions
 
 tab on the service agreement page. The list of service agreements will display only the ones that have the specified contact and/or account added to the
 
 Service recipients
 
 detail. So the field is filled in with one of the agreements according to the following priorities:
 


1. If the
 
 Contact
 
 field is filled in, the
 
 Service agreement
 
 field fills in with the agreement that meets one of the requirements:
 


	1. A contact specified on the case page is found on the
	 
	 Service recipients
	 
	 detail of the service agreement.
	2. A department of the account that the specified contact is connected to is found on the
	 
	 Service recipients
	 
	 detail of the agreement.
	3. An account that the specified contact is connected to is found on the
	 
	 Service recipients
	 
	 detail of the agreement.
2. If the
 
 Contact
 
 field is empty and the
 
 Account
 
 field is filled in, the
 
 Service agreement
 
 field will be filled in with the one that has the specified account added to the
 
 Service recipient
 
 detail.
3. If no service agreements meet the required conditions, the
 
 Service agreement
 
 field is filled in with the base service agreement. The base service agreement provides the minimum number of services. You can set it up using the "Default service agreement" system setting.



 If several service agreements meet the required conditions, the one with the higher priority will be specified in the
 
 Service agreement
 
 field. The rest of the service agreements are available in the list. If multiple service agreements apply to the case, the following is selected as the primary agreement:
 


1. Contact’s service agreement (the contact is specified on the
 
 Service objects
 
 detail of the service agreement).
2. The service agreement of the contact’s department.
3. The account’s service agreement.
 



 When you change the value in the
 
 Contact
 
 ,
 
 Account
 
 or any other field that govern the process of selecting a service agreement, the list of available service agreements is reconsidered.
 





 Note.
 
 Information about the account and department that the contact is connected to can be found on the contact page. The portal user’s account and department are specified on the
 
 Service objects
 
 detail.
 




 The
 
 Service agreement
 
 field is available for editing at any case processing stage.




