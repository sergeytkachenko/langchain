


 Set up the UTM codes
----------------------



 If you are already using web analytics tools, for example, Google Analytics, you are likely to have established tracking rules for the source and channel classification as well as UTM code you use. In this case, we recommend saving the website URLs and UTM codes you use to Creatio. To do this, use the following lookups:
 


* Lead channels
 
 . Contains the index of all resource types that provided new leads, e. g., “Social accounts,” “Search-based advertising,” or “Email.” The
 
 Lead channel code
 
 field of the lookup page contains the “utm\_medium” code values that match the channel. For example, “display,” “cpm,” and “banner” for the “Media advertising” channel. Creatio uses these values to identify the channel.
* Lead sources
 
 . Contains the index of specific resources from which the user was redirected, e. g., “Twitter,” “Google,” or “Creatio marketing.” The
 
 Lead source code
 
 field of the lookup page contains the “utm\_source” code values that match the source. For example, “facebook,” “facebook.com,” “fb,” and “fb.com” for the “Facebook” source. Creatio uses these values to identify the source. Here you can also set up the default channel for the selected source. For example, the “Social accounts” channel for “Facebook” and “Search-based advertising” channel for “Google AdWords.”
* Lead source URL
 
 . Contains the list of source websites (referrers) Creatio can identify. Here you can also set up the default source for the selected referrer. For example, the lookup contains the following URLs by default: “facebook.com” (“Facebook” source), “twitter.com” (“Twitter” source), “linkedin.com” (“Linkedin” source), etc.



 The lookups above have the most common website URLs and codes preconfigured. You can expand the lookups with the values your company uses.
 



 Since Creatio version 8.0.3, when a lead is registered from a landing page, the UTM codes that the landing page URL uses are passed to the “utm\_campaign”, “utm\_content”, “utm\_medium”, “utm\_source,” “utm\_term” Creatio columns as strings. Creatio does not display these columns on the lead page, but you can use the columns for customization, for example, in charts and pivot tables. This functionality also lets you utilize UTM codes not included in the lookups. For example, codes from emails sent by your partners.
 



 Add a lead channel
--------------------


1. Open the
 **System Designer** 
 , for example, by clicking
 ![btn_system_designer](/docs/sites/en/files/inline-images/btn_system_designer_8.png)
 in the top right. Go to the
 
 System setup
 
 block →
 
 Lookups
 
 .
2. Go to the
 
 Leads
 
 folder and open the
 
 Lead channels
 
 lookup.
3. Click
 
 New lead channel
 
 to add a record to the lookup. Enter the channel name in the row that appears, for example, “Partner sale,” and click
 ![btn_com_apply](/docs/sites/en/files/inline-images/btn_com_apply_2.png)
 on the toolbar.
4. Click
 ![btn_edit](/docs/sites/en/files/inline-images/btn_edit_3.png)
 on the toolbar to open the page of the record you created.
5. Click the
 
 Add
 
 button on the
 
 Lead channel code
 
 tab. This opens a page. Enter the “utm\_medium” code by which to identify the channel, for example, “affiliate.” Save the page.
   

 Similarly, you can add other “utm\_medium” codes by which to identify the channel.
 


 Note.
 
 Learn more about the rules that identify the lead source and channel in a separate article: Rules for determining lead sources (with examples).



 As a result, Creatio will save the channel to the lookup. The lookup will be used to identify the channel during lead tracking. In this example, when Creatio receives the “http://site.com/page?utm\_medium=affiliate” redirection URL, the lead channel will be set to “Partner sale.”
 



 Add a lead source
-------------------


1. Open the
 **System Designer** 
 , for example, by clicking
 ![btn_system_designer](/docs/sites/en/files/inline-images/btn_system_designer_8.png)
 in the top right. Go to the
 
 System setup
 
 block →
 
 Lookups
 
 .
2. Open the
 
 Lead sources
 
 lookup.
3. Click
 
 New lead source
 
 button to add a record to the lookup. Take the following steps in the row that appears:
4. Enter the source name, for example, “Admitad.com.”
5. Click
 ![btn_com_lookup](/docs/sites/en/files/inline-images/btn_com_lookup_2.png)
 in the
 
 Default channel
 
 field and select a channel in the dialog that opens, for example, “Partner sale.” The lead channel will be set to this value if Creatio cannot retrieve the “utm\_medium” code value from the redirection URL but can retrieve the “utm\_source” code value.
6. Click
 ![btn_com_apply](/docs/sites/en/files/inline-images/btn_com_apply_3.png)
 on the toolbar to save the record.
7. Click the toolbar button to open the page of the record you created.
8. Click the
 
 Add
 
 button on the
 
 Lead source code
 
 tab. This opens a page. Enter the “utm\_medium” code by which to identify the channel, for example, “admitad.” Save the page.
   

 Similarly, you can add other “utm\_source” codes by which to identify the source.



 As a result, Creatio will save the source to the lookup. The lookup will be used to identify the channel and source during lead tracking. In this example, when Creatio receives the “http://site.com/page?utm\_source=admitad” redirection URL, the lead source and channel will be set to “Admitad.com” and “Partner sale,” respectively.
 



 Add a source website
----------------------


1. Open the
 **System Designer** 
 by clicking
 ![btn_system_designer](/docs/sites/en/files/inline-images/btn_system_designer_8.png)
 in the top right. Go to the
 
 System setup
 
 block →
 
 Lookups
 
 .
2. Open the
 
 Lead sources
 
 lookup.
3. Add a record to the lookup. Take the following steps in the row that appears:
	1. Enter the source URL in the
	 
	 URL
	 
	 field, for example, “mysite.com.”
	2. Click
	 ![btn_com_lookup](/docs/sites/en/files/inline-images/btn_com_lookup_2.png)
	 in the
	 
	 Lead source
	 
	 field and select a source in the dialog that opens, for example, “Admitad.com”. The lead source will be set to this value if Creatio cannot retrieve the UTM codes from the redirection URL but can retrieve the referrer.
4. Click
 ![btn_com_apply](/docs/sites/en/files/inline-images/btn_com_apply_3.png)
 on the toolbar to save the record.
   

 Similarly, add other referrers by which to identify the lead sources.



 As a result, Creatio will save the referrer to the lookup. The lookup will be used to identify the channel and source during lead tracking. In this example, when Creatio receives the “http://mysite.com/” referrer, the lead source and lead channel will be set to “Admitad.com” and “Partner sale,” respectively.
 



 Embed a cookie tracking script into your website
--------------------------------------------------



 To ensure lead source tracking operates as intended, insert a special code snippet that tracks cookies into the source code of each page on your website.
 





 Attention.
 
 The setup of lead source tracking is done by the website administrator. To insert the tracking code, you need access to the HTML source code of your website and permission to edit it.
 



1. Copy the following code snippet that tracks cookies:
 



```

<script src="https://webtracking-v01.creatio.com/JS/track-cookies.js"></script>

```
2. Insert the tracking code into the HTML source code of each page on your website. You can paste the code anywhere before the closing tag at the end of the page. If you do not insert the code into each page on your website, Creatio will be unable to track every resource from which prospects were redirected to the website.



 After you set up lead source tracking for your website, the lead source and channel will become available in Creatio. You will be able to view tracking data in the
 
 History
 
 tab on the lead and connected contact page.
 




