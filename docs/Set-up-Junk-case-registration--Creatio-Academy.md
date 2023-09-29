


 Creation can process incoming “junk” emails, e.g., spam, auto-replies, and internal emails so that the agents do not spend time on them.
 



 The setup procedure is as follows:
 


1. Specify email addresses, address strains or email domains of “junk” emails in the
 **Blacklist of email addresses and domains for case registration** 
 lookup. By default, the lookup contains the following values commonly used in the bulk emails: postmaster, noreply, no-reply, mail-daemon, mailer-daemon.
2. Specify the processing routine for “junk” emails in the “
 **Create cases from junk emails** 
 ” (CreateCasesFromJunkEmails) system setting.
 


	1. Clear the
	 
	 Default value
	 
	 checkbox to
	 **disable creating cases based on “junk” emails** 
	 .
	2. Select the
	 
	 Default value
	 
	 checkbox to
	 **create cases based on “junk” emails** 
	 .
3. If you select the
 
 Default value
 
 checkbox in the “Create cases from junk emails” system setting,  populate the
 
 Default value
 
 field of the “
 **Junk case default status** 
 ” (JunkCaseDefaultStatus) system setting. For instance, select “Canceled” to automatically cancel any cases created from “junk” emails.








