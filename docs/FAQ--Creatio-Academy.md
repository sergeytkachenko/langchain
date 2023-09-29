


 Why is the number of contacts in Creatio different from an external service?
------------------------------------------------------------------------------



 Creatio calculates the number of contacts based on the UTM parameters in the contact submissions. Contacts can submit forms on a website or Facebook lead form that has UTM parameters. Other services can use different means of tracking that can also be customizeable further. As such, discrepancies can occur. The most common reasons for them are as follows:
 


* Contact clicked on an ad Creatio did not track. For example, the ad account is not connected to Creatio, the contact clicked the ad before Creatio started tracking it, or the ad has a tracking error.
* Columns of UTM marks in the linked contact records of the “Submitted forms” object were updated manually. If this occurs, Creatio cannot match contact data to the contact and does not display the contact in the Digital Ads app.
* Creatio has not yet calculated the number of contacts. This is done in intervals rather than real time.



 Why will my Facebook Ads account not connect?
-----------------------------------------------



 Make sure you meet the connection requirements and are using the correct Facebook user. Learn more:
 [Connect Facebook Ads to Creatio](https://academy.creatio.com/documents?id=2462) 
 . If the issue persists, update Creatio Ads app permissions and reset Creatio app permissions in Facebook.
 



 Why will my Google Ads account not connect?
---------------------------------------------



 Make sure you meet the connection requirements and are using the correct Google user. Learn more:
 [Connect Google Ads to Creatio](https://academy.creatio.com/documents?id=2463) 
 . If the issue persists, reset Creatio app permissions in Google Ads.
 




