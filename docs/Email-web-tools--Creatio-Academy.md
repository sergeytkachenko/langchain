


 Before sending emails, you can access their deliverability rates and the probability of getting marked as spam using services covered in this article. This approach can increase the ratio of delivered emails to sent emails.
 



 Copy content services
-----------------------



 After checking an email’s content manually, run the copy through dedicated editor services. They can pinpoint errors and typos, and help you improve the text generally by identifying overly complex sentences, slang, generalizations, split infinitives, overuse of passive constructions, and more.
 


* [Hemingway App](http://www.hemingwayapp.com/) 
 checks for readability and provides tips for imrpoving the text.
* [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen/) 
 checks for grammar, syntax, and complexity. The service is avavilable as a sepearate application and as a Google Chrome extension.
* [Coschedule’s Headline Analyzer](http://coschedule.com/headline-analyzer) 
 evaluates the title from the POV of the user’s interests. Essentially, assesses the probable open rate.



 Reputation control services
-----------------------------



 The sender’s reputation is one of the vital factors affecting the email deliverability rates. Monitoring the reputation can reveal a decrease in it early on and take measure to prevent the emails from getting marked as spam.
   

 To check for various health markers of your reputation, you can use the following server types:
 


* audience validation tools
* IP address check-up tools
* postmaster tools
* blacklist check-up tools.


### 
 Email check-up tools



 The recipients in your base can grow inactive as a result of a change of employment, loss of the password, or migration to another email provider. Inactive email addresses in the contact base can damage the domain’s reputation. We recommend to check the base regularly and purge inactive addresses. You can use the following services:
 


* [Email address validation connector for Creatio](https://marketplace.creatio.com/app/email-address-validation-connector-creatio) 
 check email addresses for validity and availability.
* [MailboxValidator](https://www.mailboxvalidator.com/) 
 assesses the validity of the email addresses, assigns points and status for each address based on the check-up.
* [QuickEmailVerification](https://quickemailverification.com/) 
 assesses the validity of the email addresses, calculates the percentage of valid and invalid addrsses, as well as groups the totals by category. Good for checking bases collected without double-opt-in or with a significant number of typos.
* [MillionVerifier](https://www.millionverifier.com/) 
 assesses the validity of the email addresses and generates a report and chart after the check-up.
* [ZeroBounce](https://www.zerobounce.net/) 
 assesses the validity of the email addresses and generates a detailed and exhaustive report whose fields can be exported.


### 
 IP address check-up tools



 The IP address reputation affects the deliverability directly. To check the reputation of an IP address, use the following services:
 


* [SenderScore](https://senderscore.org/index.php) 
 evaluates the reputation of IP addresses and domains from 1 to 100 points. The higher the score, the better the reputation. The indicators are calculated based on the sender’s average activity for the last 30 days compared to the activity of other senders. A high score means you have a good reputation. A low score means a poor reputation.
 

 Fig. 1 Example SenderScore
 

![sender_score_metric.png](/docs/sites/default/files/images/Marketing_Tools/email_recommendations/sender_score_metric.png)




 Fig. 2 Example SenderScore chart
 

![sendes_score_chart.png](/docs/sites/default/files/images/Marketing_Tools/email_recommendations/sendes_score_chart.png)
* [TallosInteligense](https://talosintelligence.com/) 
 evaluates the reputation as good, neutral, or poor.
 

 Fig. 3 TallosInteligense check-up example
 

![TallosInteligense.png](/docs/sites/default/files/images/Marketing_Tools/email_recommendations/TallosInteligense.png)
* [MXToolbox](https://mxtoolbox.com/SuperTool.aspx) 
 provides aggregated reports with domain or IP details.


### 
 Domain check-up tools (postmaster tools)



 These services provide stats for sent emails: the number of delivered emails, complaints, unsubscribes, read and deleted messages. Major email providers offer their own postmaster tools:
 


* [Gmail](https://postmaster.google.com/managedomains) 
 ,
* [Yahoo](https://help.yahoo.com/kb/postmaster/) 
 .


### 
 Blacklist check-up tools



 A blacklist (spam filter, DNSBL) is a list of Ip-addresses or domains known to send spam. Such lists are available for email providers on the servers. We recommend to track blacklists for your IP address to prevent your emails from getting marked as spam for certain.
 



 As a rule, a domain or Ip-address is temp-banned (for 24-72 hours, depending on the spam filter settings). After that time, the address is unblocked automatically, and you can repeat the sending. In most cases, you can request for an early removal of your address from the blacklist. The support can do that after considering your ticket.
 



 Thee most popular blacklists include:
 


* **Spamhaus** 
 lists problem addresses and is considered by Google, Microsoft (Hotmail, AOL, MSN, Live), Yahoo. To remove an address from the list, resolve the issue that got the address listed, and make a request for removal.
* **Spamcop** 
 is a service for making spam complaints. When a complaint is made, the email provider will request to solve the issue.
* **URIBL** 
 lists problem domains. It is considered by manny email providers. It is impossible to get an address removed from the list if it was listed there multiple times.
* **Proofpoint** 
 lists problem addresses. It is considered by Apple. If an IP-address is listed by ProofPoint, its outbound emails will no longer be delivered to @icloud.com and @me.com.



 Use the following tools to check if an address is blacklisted:
 


* [Dnsbl.info](http://www.dnsbl.info/) 
 checks an IP-address or domain’s blacklist status on multiple blacklists.
 

 Fig. 4 Check using Dnsbl.info
 

![dnsbl.png](/docs/sites/default/files/images/Marketing_Tools/email_recommendations/dnsbl.png)


* [MXToolbox](https://mxtoolbox.com/emailhealth) 
 checks a domain’s blacklist status on multiple blacklists using the “Email Health” menu. It can also assess the DNS domain’s health.
 

 Fig. 5 MXToolobox check-up example
 

![MXToolbox.png](/docs/sites/default/files/images/Marketing_Tools/email_recommendations/MXToolbox.png)



 Services for checking emails before sending.
----------------------------------------------



 You can check where you email may end up with popular email providers using either manual testing or dedicated services.
 


* [Glockapps](https://glockapps.com/) 
 predicts where the email will end up. It also provides tips for improving poor deliverability and covers the factors causing it.
 

 Fig. 6 Clockapps check-up example
 

![glockapps.png](/docs/sites/default/files/images/Marketing_Tools/email_recommendations/glockapps.png)
* The
 [Litmus](https://litmus.com/spam-filter-tests) 
 and
 [Email on Acid](https://www.emailonacid.com/spam-testing/) 
 services let you see how the content of your email will look with different email providers, in different browsers, or on different devices.
 

 Fig. 7 Email on Acid check-up example
 

![email_on_acid.png](/docs/sites/default/files/images/Marketing_Tools/email_recommendations/email_on_acid.png)
* [Mail-tester](https://www.mail-tester.com/) 
 is a versatile service for checking an email using a number of parameters:
	+ blacklist status
	+ email authentication setup
	+ errors or broken links.

 Fig. 8 Mail-tester check--up example
 

![mail_tester.png](/docs/sites/en/files/images/Marketing_Tools/email_recommendations/mail_tester.png)



 You can unfold each check-up parameter to get more details.




