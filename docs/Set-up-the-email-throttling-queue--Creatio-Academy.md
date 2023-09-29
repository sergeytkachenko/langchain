


**Throttling** 
 balances the outgoing email flow in Creatio.
 



 Use throttling to split a large email into multiple parts and send the parts to the email provider one by one during the specified time frame. This approach improves the delivery rate and prevents the emails from being flagged as spam or rejected by email providers. Use throttling when:
 


* Sending multiple emails during a short period.
* Sending emails to new subscribers.
* Sending emails to subscribers you have not contacted by email for a long time.
* Sending first emails from a new domain.
* Sending emails after changing the sender’s IP address.
* Sending a test email that has to be changed or canceled during the mailing process.
* Sending emails likely to increase the activity of users.



 In these situations, sending emails gradually enhances the domain’s reputation. The throttling mechanism also lets you control the outgoing email flow, which can be useful in cases like balancing the load on contact center agents who process the feedback (leads).
 



 Creatio provides the following throttling modes:
 


* “
 **Warmup cold audience** 
 ” to send the emails using the pre-configured schedule. Learn more:
 [Warm up cold audience](#title-2016-1) 
 .
* “
 **Manual limit** 
 ” – Creatio will send the emails based on the specified daily limit. Learn more:
 [Manual limit](#title-3298-10) 
 .



 Warm up cold audience
-----------------------



 “Warmup cold audience” is a throttling mode where Creatio sends a limited number of emails daily after the email starts. There is a fixed delay before each email. The daily limit and the delay help to emulate manual emailing, which is essential to enhance the reputation of the sender’s domain.
 



 The pre-configured warm-up schedule is based on the best throttling practices, such as emailing daily for 2 weeks and longer with a gradual increase in the number of emails per day.
 



 To change this schedule, contact Creatio support and specify the new daily limit and delay. After the support team applies the changes, click the
 ![btn_info.png](/docs/sites/en/files/images/Marketing_Tools/email_additional_settings_throttling/btn_info.png)
 button in the
 
 Delivery schedule
 
 field on the email page to view the updated schedule. We recommend that you only change this schedule for urgent reasons and with a basic understanding of warm-up strategies.
 




**Note.** 
 If the email has more than 1 sender address (for example, set by a macro), Creatio will apply the schedule for each address individually. Learn more:
 [Warm-up examples](/docs/8-0/user/marketing_tools/email_marketing/additional_setup/throttling/email_throttling_queues#title-2016-3) 
 .
 



### 
 Enable the warm-up mode



 Configure the warm-up cold audience parameters before starting the email.
 


1. Go to the
 
 Email
 
 section and open the needed record.
2. Go the
 
 Parameters
 
 tab.
3. Select the “
 **Warmup cold audience** 
 ” value in the
 
 Throttling settings
 
 field. Click the
 ![btn_info.png](/docs/sites/default/files/images/Marketing_Tools/email_additional_settings_throttling/btn_info.png)
 button in this field to view the email delivery schedule.
4. Select one of the shared queues in the
 
 Throttling queue
 
 field. Creatio sends all emails in a queue independent of the other throttling queues. Learn more:
 [Set up a distribution queue](#title-2016-5) 
 and
 [Warm-up examples](/docs/8-0/user/marketing_tools/email_marketing/additional_setup/throttling/email_throttling_queues#title-2016-3) 
 . The “General” value is selected by default (Fig. 1). This is a required field.
 




 Fig. 1 Setting up a throttling queue
 

![email_additional_settings_throttling.png](/docs/sites/en/files/images/Marketing_Tools/email_additional_settings_throttling/email_additional_settings_throttling.png)
5. Click
 
 Save
 
 .



 As a result, Creatio will send the emails using the selected throttling mode.
 


### 
 Set up a throttling queue



 A throttling queue is a tool to segment cold contacts. Throttling queues let you group several bulk or trigger emails to segment different pools of cold contacts for individual warm-ups. For example, a part of the audience originates from social networks and another part from a webinar. In this case, we recommend dividing the audience into different segments and create a dedicated throttling queue for each segment to keep the email marketing strategies separate. Learn more:
 [Warm-up examples](/docs/8-0/user/marketing_tools/email_marketing/additional_setup/throttling/email_throttling_queues#title-2016-3) 
 . Configure the queues in the
 
 Throttling queues
 
 lookup. To add a new queue:
 


1. Open the system designer by clicking
 ![system_designer00001.png](https://academy.creatio.com/sites/default/files/documents/docs/product/bpm'online%20marketing/marketing/7.16.0/BPMonlineHelp/section_employees/system_designer00001.png)
 in the top right.
2. Click the “Lookups” link in the “System setup” block.
3. Open the
 
 Throttling queues
 
 lookup.
4. Click
 
 New
 
 .
5. Enter the queue name, for example, “New queue.” Fill out the
 
 Description
 
 column if necessary.
6. Fill out the
 
 Code
 
 field with an alphanumeric code (Fig. 2). Creatio will use the code to segment bulk emails. You can use arbitrary names.
 




 Fig. 2 Adding a new throttling queue
 

![email_additional_settings_queues_lookup.png](/docs/sites/en/files/images/Marketing_Tools/email_additional_settings_throttling/email_additional_settings_queues_lookup.png)




 Attention.
 
 We recommend against modifying codes of existing lookup entries since this can affect the active bulk and trigger emails. To specify another code, add a new lookup entry and select this throttling queue when creating an email record.


### 
 Warm-up examples



 Find detailed examples of the warm-up mode in action below.
 





| 
 Day
  | 
 Daily email limit
  | 
 The delay between emails, sec
  |
| --- | --- | --- |
| 
 1
  | 
 25
  | 
 400
  |
| 
 2
  | 
 25
  | 
 400
  |
| 
 3
  | 
 25
  | 
 400
  |
| 
 4
  | 
 50
  | 
 400
  |
| 
 5
  | 
 50
  | 
 400
  |
| 
 6
  | 
 75
  | 
 400
  |
| 
 7
  | 
 75
  | 
 400
  |



#### 
 Example 1




 Send the “Newsletter” bulk email to 100 recipients. Use the “General” throttling queue. Two sender addresses will be used: sender1@example.com (75 recipients) and sender2@example.com (25 recipients).
 




 Creatio will use a separate schedule for each sender's
 **email address** 
 .
 



 The bulk email will start from the Day 1 schedule for the “Warmup cold audience” mode. Emails from sender1@example.com will be sent in 3 days (25 emails per day). Emails from sender2@example.com will be sent in 1 day (25 emails per day).
 


#### 
 Example 2




 Send a “Webinar invitation” bulk email to the same contacts. Add a new sender address. Split the audience between the senders as follows: sender1@example.com (50 recipients), sender2@example.com (25 recipients), and sender3@example.com (25 recipients).
 




 Emails to
 **new sender addresses** 
 always start from the Day 1 schedule. If you have already used an email address for sending bulk emails, its schedule will start from the day where the previous bulk email stopped:
 


* All emails from sender3@example.com will be sent in 1 day (25 emails per day) according to the schedule, starting from Day 1.
* All emails from sender2@example.com will be sent in 1 day (25 emails per day) according to the schedule, starting from Day 2.
* All emails from sender1@example.com will be sent in 2 days (50 emails per day) according to the schedule, starting from Day 4.


#### 
 Example 3




 Add 100 new recipients to the “Webinar invitation” bulk email contact audience and create the “New” throttling queue. Use 2 sender addresses: sender1@example.com (75 recipients) and sender2@example.com (25 recipients).
 




 When
 **changing the throttling queue** 
 , the email delivery always starts from the Day 1 schedule, even if you have already used the addresses in this bulk email:
 


* All emails from sender1@example.com will be sent in 3 days (25 emails per day).
* All emails from sender2@example.com will be sent in 1 day (25 emails per day), starting from Day 1.





 Attention.
 
 Create a new throttling queue for each new audience segment to avoid disrupting the audience warm-up procedure.
 




 Manual limit
--------------



 “Manual limit” is a throttling mode that lets you specify the uniformly distributed email sending parameters. Use it to balance the load on the website or your support agents who process the email’s responses (leads).
 



 Select this mode to send the specified number of emails daily. You can limit the mode’s sending period by selecting the required values in the
 
 Delivery schedule
 
 field group. On the last delivery day, Creatio sends the rest of the messages, as long as their number is less than the
 
 Daily limit
 
 value.
 



 Configure the manual limit parameters before starting the email.
 






 Note.
 
 Starting from Creatio 7.18.2, you can edit the manual limit parameters for active emails. You can use this to set up a custom warm-up schedule with arbitrary limits, similarly to the cold audience warmup mode.
 







 Example.
 
 Send a promo email to 100 recipients. The agents can process up to 16 responses daily (from 9:00 AM to 6:00 PM). Processing each response takes 30 minutes.
 




 To set up these limits:
 


1. Go to the
 
 Email
 
 section and open the needed record.
2. Go to the
 
 Parameters
 
 tab.
3. Select “
 **Manual limit** 
 ” in the
 
 Throttling mode
 
 field.
4. Use the
 
 Daily limit
 
 field to specify the number of email responses the agents can process daily. For example, “16.” The field is required.
5. Use the
 
 Delay between emails
 
 field to set up an interval between emails based on the time an agent requires to process a lead, in seconds. For example, “1800.”
6. Use the
 
 Delivery schedule
 
 detail to specify the agents’ work schedule.
	1. Select “Every day” in the
	 
	 Delivery schedule
	 
	 field.
	2. Specify the period between 9:00 AM and 6:00 PM in the
	 
	 Delivery time range
	 
	 field.
	 
	
	
	 Note.
	 
	 The
	 
	 Daily limit
	 
	 and
	 
	 Delay between emails
	 
	 fields, as well as the
	 
	 Delivery schedule
	 
	 settings are connected. The specified delivery time range must be longer than the period during which Creatio sends the daily number of emails, including the delays. If erroneous limits are specified, you will be unable to save and send the email. Should that happen, change the distribution settings according to the tooltips.
	 
	
	
	
	
	
	 Fig. 3 Example of manual limit setup
	 
	
	![email_additional_settings_throttling_manual_limits_example.png](/docs/sites/en/files/images/Marketing_Tools/email_additional_settings_throttling/email_additional_settings_throttling_manual_limits_example.png)
7. Click
 
 Save
 
 .



 As a result, Creatio will take 7 days to finish the email. During the first 6 days, Creatio will send 16 emails daily. The remaining 4 emails will be sent on day 7.
 




