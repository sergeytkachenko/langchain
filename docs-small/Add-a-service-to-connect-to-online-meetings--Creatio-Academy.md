


 Creatio users can join online meetings from the activity calendar if the activity page contains a video conference link. Learn more in a separate article:
 [Link an online meeting](https://academy.creatio.com/documents?id=2391&anchor=title-2168-2) 
 . The button to join a meeting appears if the activity contains a link that follows the URL pattern of the online meeting service. The
 
 Meeting services links
 
 lookup contains the URL patterns for the most popular services:
 


* Microsoft Teams
* Zoom
* Cisco Webex
* Join.Me
* AnyMeeting
* GoToMeeting
* Google Meet



 If your company uses a different online meeting service or corporate account of any of the listed services, the generated URLs will differ from the patterns specified in the lookup. In this case, add a new URL pattern to the
 
 Meeting services links
 
 lookup.
 





 Example.
 
 Add a Zoom URL pattern for Our Company corporate account.
 



1. Click
 ![btn_system_designer.png](/docs/sites/en/files/images/Setup_and_Administration/online_meetings_services/btn_system_designer.png)
 in the top right →
 
 Lookups
 
 .
2. Open the content of the
 
 Meeting services links
 
 lookup.
3. Click
 
 New
 
 .
4. Fill out the fields of the new record:
 


	1. Enter the service name in the
	 
	 Name
	 
	 field. For example, “Zoom Our Company.”
	2. Enter the brief service description in the
	 
	 Description
	 
	 field. For example, “Corporate Zoom account.”
	3. Enter the universal pattern that lists the mandatory components included in each link the service generates in the
	 
	 Link mask
	 
	 field. For example, (http
	 
	 s
	 
	 ?:\/\/(www\\.)?|www\\.){1}.OurCompany?zoom.us/j/.+?\b
5. Click
 ![btn_save_record.png](/docs/sites/en/files/images/Setup_and_Administration/online_meetings_services/btn_save_record.png)
 .
6. Repeat steps 3-5 for each relevant service if needed.




