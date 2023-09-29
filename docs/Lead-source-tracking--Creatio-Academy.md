


 You can track lead sources and channels. Analyzing the lead channel performance enables choosing the most prospective channels for further development.
   

 Information collected by the tracking code displays in the
 
 Lead engagement
 
 field group on the lead page. The lead source tracking provides the following information about potential customers:
 




 Lead page with channel information and lead engagement origin
 



![""](/docs/sites/en/files/2020-12/chapter_tracking_lead_source.png)


* Lead channel. The [Channel] field displays the resource type that delivered the lead: “Social accounts,” “Search-based advertising” or “Direct traffic.”
* Lead source. The [Source] field displays the name of the resource, e.g., “Twitter.”
* Name of the website domain that redirected the user to the tracked website. It will be displayed in the [Redirection website] field, e.g., “facebook.com.”
* Name of the landing page on which a potential customer submitted the web form. It will be displayed in the [Landing] field.
* Name of the marketing email that redirected the user to your website, and also the name of the campaign that includes the corresponding email. This information displays in the [Bulk email] and [Campaign] fields accordingly. The fields are only available in Marketing Creatio.



 Lead source tracking operation
--------------------------------


1. Every time the tracking code redirects a potential customer to your website, two URLs will be written to the cookie files:
	* URL of the website that redirected the user to your webste (referrer)
	* Redirection URL containing tracking parameters (e.g., UTM marks).
2. When a potential customer populates the form on your landing page, the information about the referrer and the redirection URL will be sent to Creatio. The system will analyze the URLs and identify the lead channel and the source website.
3. After the customer completes the landing page form, Creatio will add a new lead and write the URL analysis result in it. Based on the redirection URL, Creatio will also link the generated leads to the marketing emails that originated them. Similarly, Creatio will link leads to the corresponding campaigns.



 Using cookie files in the lead source tracking
------------------------------------------------



 The lead source tracking creates two cookies containing the following data:
 


* The [BpmRef] cookie contains the name of the website domain (referrer) that redirected the users to your website. Redirection URL will display in the [Redirection address] field of the [History] tab on the lead page.
* The [BpmHref] cookie contains the URL of the website that redirected the user to your website. The redirection URL might contain tracking parameters (e.g., the UTM marks) used by the tracking code to determine the lead attraction channel. For example,
   

 http://www.?reatio.com?utm\_source=facebook&utm\_medium=social&utm\_campaign=c1. The redirection link is stored in the [BpmHref] database column and is not available in the application UI.


### 
 Determining the external, internal, and direct traffic



 The following rules are applied for the redirections from external links to your website and for your website's internal redirections. These rules define the way the data is written to the
 
 BpmRef
 
 and
 
 BpmHref
 
 cookie files regardless of the initial values they contain:
 


* Each external redirection from a new source will result in overwriting the referrer and the redirection URL in the corresponding cookies.
* Your website's internal redirections will not result in data overwriting in any of the cookie files.



 When a direct link is used to access your website, the direct link to your website page is saved in the
 
 BpmHref
 
 cookie file, while the referrer value remains blank. This occurs regardless of the previously used website redirection source.
   

 Thus, Creatio takes into consideration only the last source and the redirection link to your website.
 



 Using the UTM marks
---------------------



 In Creatio, UTM marks are used in bulk and trigger emails. These marks enable obtaining additional information about lead sources and analyzing the efficiency of marketing emails and campaigns. UTM marks are variables that are added to all URLs in a bulk email. The marks are added sequentially, at the end of each URL, and are separated with the “&” character.
   

 The following UTM marks are used to determine lead sources:
 


* The
 **utm\_medium** 
 mark determines the lead source channel, or the type of resource used to attract the lead, such as a search engine, social network, etc.
* The
 **utm\_source** 
 mark determines the specific information resource used to attract the lead, for example, Facebook, Google, etc.
* The
 **utm\_campaign** 
 mark determines the campaign that involved the bulk email. If the bulk email was not conducted as part of a Creatio campaign, specify the trigger email subject in the mark name.
* The
 **utm\_term** 
 mark determines a keyword in the campaign and is used mostly for search-based advertising.
* The
 **utm\_content** 
 mark is used to distinguish similar content or links in the same email. For example, if an email contains two links with a call to action, you can use the utm\_content parameter to assign different values and perform split tests.



 Rules for determining lead sources (with examples)
----------------------------------------------------


### 
 Using tracking to determine the lead source and the lead channel



 Creatio analyzes your website visits and identifies the lead sources using the tracking code and landing pages. Tracking results can be obtained from the page of the lead sent to Creatio from your landing page. The results are generated using the data contained in the
 
 Channel
 
 and
 
 Source
 
 fields on the
 
 History
 
 tab. The
 
 Channel
 
 field displays the lead traffic type, for example, “Social accounts”, and the
 
 Source
 
 field displays the advertising system used, for example, “Twitter”. Use the
 
 Leads
 
 section analytics to obtain the performance indicators for a certain lead channel or source.
   

 Creatio uses the following information to analyze the lead sources:
 


* UTM marks: “utm\_medium” (lead channel) and “utm\_source” (lead source);
* Unique identifiers of redirections from Google that are added automatically (“gclid”). For example, if you post an advertisement in this search engine.
* Source website (referrer) URL that redirected your customer to your website.



 The
 
 Lead channels
 
 ,
 
 Lead sources
 
 , and
 
 Lead source URL
 
 lookup values are used for the analysis of the redirection URL and the source website.
 





 Note
 
 If you already use tracking rules for channel classification, sources, and used marks, we recommend that you supplement the contents of the mentioned lookups.
 




 Below are the rules used by Creatio to identify the lead source and channel.
 


#### 
 Lead channel identification rules



 The rules are listed by priority. This means that if rule 1 is satisfied, then rules 2 – 5 will not be checked, and so on.
 





| 
 Channel identification rule
  | 
 Case example
  |
| --- | --- |
| 
 1. utm\_medium mark
  |  |
| 
 If the redirection URL contains the “utm\_medium” mark value, the channel will be populated with the value corresponding to that mark (1).
  | 
 For example, the redirection URL value is “http://site.com/page?utm\_medium=social”.
 
 In this case, the channel will be populated with the “Social accounts” value.
  |
| 
 2. utm\_source mark
  |  |
| 
 If the redirection URL contains the “utm\_source” mark value, the channel will be populated with the found source default value (2).
  | 
 For example, the redirection URL value is “http://site.com/page?utm\_source=creatio”, which means the customer clicked the link in the Creatio bulk email. In this case, the channel will be populated with the “Email” value.
  |
| 
 3. Google AdWords redirection ID. Direct
  |  |
| 
 If the redirection URL obtains the value from Google (“gclid”)  redirection, then the “Search-based advertising” will be specified as the lead channel.
  | 
 For example, if the redirection URL is “http://site.com/?gclid=123xyz".
  |
| 
 4. Referrer
  |  |
| 
 If the redirection URL does not contain UTM mark values, then the source website (referrer) will be analyzed. To do this:
 * If the referrer of the found source website is included in the [Lead source URL] lookup (source website sub-domains are also included in the search), then the lead channel will be populated with the site URL value (4);
* If the found referrer is not included in the [Lead source URL] lookup, then the channel will be populated with the “Redirected from another website” value.
 | 
 For example, the referrer is “mobile.twitter.com”. In this case, the source will be populated with the "Twitter” value and the channel – with the “Social account”.
  |
| 
 5. Direct traffic
  |  |
| 
 If the redirection URL does not contain UTM mark values and the referrer is not identified, then the channel will be populated with the “Direct traffic” value.
  |  |



#### 
 Lead source identification rules



 The rules are listed by priority. This means that if rule 1 is satisfied, then rules 2 – 5 will not be checked, and so on.
 





| 
 Source identification rule
  | 
 Case example
  |
| --- | --- |
| 
 1. utm\_source mark
  |  |
| 
 If the redirection URL contains the “utm\_source” mark value, the lead source will be populated with the value corresponding to that mark (3).
  | 
 For example, the redirection URL value is “http://site.com/page?utm\_medium=social&utm\_source=linkedin”. In this case, the source will be populated with the “LinkedIn” value.
  |
| 
 2. utm\_medium mark
  |  |
| 
 If the redirection URL contains the “utm\_medium” mark value, the lead source will be populated with the “Other source” value.
  | 
 For example, if the redirection URL value is “http://site.com/page?utm\_medium=social”.
  |
| 
 3. Google AdWords redirection ID. Direct
  |  |
| 
 If the redirection URL obtains the value from Google (“gclid”)  redirection, then the “Google AdWords”  will be specified as the lead source accordingly.
  | 
 For example, if the redirection URL value is “site.com/?gclid=123xyz”, then the source will be populated with the “Google AdWords” value.
  |
| 
 4. Referrer
  |  |
| 
 If the redirection URL does not contain UTM mark values, then the source website (referrer) will be analyzed. To do this:
 * If the referrer of the found source website is included in the [Lead source URL] lookup (source website sub-domains are also included in the search), then the lead source will be populated with the site URL value(4);
* If the found referrer is not included in the [Lead source URL] lookup, then the lead source will be populated with the “Other website” value.
 | 
 For example, if the source website value is “mobile.twitter.com”, then the lead source will be populated with the “Twitter” value.
  |
| 
 5. No source
  |  |
| 
 If the redirection URL does not contain UTM mark values and the referrer is not identified, then the lead source will not be specified.
  |  |



#### 
 Notes



 (1) – use the [Lead channels] lookup to link the “utm\_medium” mark to a lead channel. Possible values of the UTM marks for each channel are displayed on the
 
 Lead channel code
 
 tab of the lookup page.
   

 (2) – use the [Lead sources] lookup to set the default channel for the lead source.
   

 (3) – use the [Lead sources] lookup to link the “utm\_source” mark to a lead source. Possible values of the UTM marks for each source are displayed on the
 
 Lead source code
 
 tab of the lookup page.
   

 (4) – use the
 
 Lead source URL
 
 lookup to link the source to a website URL.
 


### 
 Using tracking to determine a campaign and a bulk email



 You can estimate the efficiency of your bulk emails and campaigns using the lead tracking for the leads generated from landing pages. While analyzing the redirection URLs, Creatio identifies the bulk email and the campaign that redirected the customer to the landing page of your website and where they submitted the landing page form.
   

 On the lead page, you can find out the bulk email and the campaign connected to the lead. To do this, use the
 
 Bulk email
 
 ,
 
 Campaign
 
 fields, and the
 
 Lead engagement
 
 field group on the
 
 History
 
 tab. You can get the summary information about the efficiency of the bulk emails and campaigns using the analytics in the
 
 Leads
 
 and
 
 Campaigns
 
 sections.
 



 A campaign is identified based on matching of the “utm\_campaign” marks in the redirection URL and on the campaign page. If there are several campaigns found for the “utm\_campaign” value, the lead page will display the last campaign (by creation date).
   

 A bulk email is identified using the bulk email unique Id contained in the redirection URL (“bulk\_email\_rid”).
 


#### 
 Using tracking to set up determining of a campaign and a bulk email



 To start tracking
 **campaigns** 
 , enter the “utm\_campaign” mark value on the
 
 Properties
 
 page of the campaign.
   

 To start tracking
 **bulk emails** 
 and the connected campaigns, go to the
 
 Parameters
 
 tab of the bulk email page and do the following:
 


1. Select the [Use UTM tracking codes] checkbox.
2. Select the marks: “utm\_source,” “utm\_campaign,” “utm\_medium,” additionally – “utm\_content” and “utm\_term”.
3. Enter the list of domains to generate the redirection URL for using the marks entered.



 Apart from the UTM marks, the redirection URL will also contain the unique Id of the bulk email (“bulk\_email\_rid”). Its value is generated in Creatio automatically and is added to all the redirection URLs in the email. The unique Id of each bulk email is stored in the
 
 RId
 
 system column.
   

 For example, a campaign page will include the following values:
 


* [utm\_source] – “creatio”
* [utm\_campaign] – “crm\_day”
* [utm\_medium] – “email”
* [utm\_content] – “active\_users”
* The domain list will include the “http://www.creatio.com/event-crm” website.



 In this case, the website redirection URL will look like this: “http://www.creatio.com/event-crm/?utm\_source=creatio&utm\_medium=email&utm\_campaign=crm\_day&utm\_content=active\_users&bulk\_email\_rid=17”
 




