


 Let’s walk through the steps of preparing a partner portal and creating a partner program to start working with the partner.
 





 Case.
 
 Set up a partner program. Under its conditions, you grant a discount to a reseller partner. The discount sum depends on the number of registered leads and the sum of closed opportunities. Additionally, the partner program provides your partners with the ability to achieve a new tier: from the Bronze tier to the Platinum tier. Your partners can also have extra discounts. The amount of such discounts grows as your partner reaches new tiers.
 







 Specify your and your partner’s cooperation parameters
-----------------------------------------------------------



 If you are already working with your partner under certain conditions, you can streamline your cooperation parameters and capture them on paper or a spreadsheet. For instance, the parameters of a reseller partnership can be represented as in
 [Fig. 1](#XREF_11319_412)
 :
 





 Fig. 1
 

 Table with partnerships parameters
 

![scr_chapter_portal_setup_table_with_parameters.png](/guides/sites/en/files/documentation/user/en/channel_sales/BPMonlineHelp/channel_sales_example/scr_chapter_portal_setup_table_with_parameters.png)



 Based on this, you will need to populate the lookups as follows:
 


* Type of partner
 
 – “Reseller.”
* Level of partner
 
 – “Bronze,” “Silver,” “Platinum.”
* Category of partnership parameter
 
 – number of leads, opportunity amount, partner discount, percentage of credits to the marketing fund.
* Type of partnership parameter
 
 – “Obligation,” “Benefit.”






 Set up partner program parameters
--------------------------------------



 The partnership parameters in
 [Fig. 1](#XREF_11319_412)
 are available in Creatio out of the box. You only need to add the partnership parameters required for the cooperation with your partner if they are not yet available in the lookups.
 






 Add new partnership
------------------------


1. Open the
 
**Partnership** 

 section in the main application. This section is available in Sales Creatio enterprise and CRM Creatio. You may need to add the
 
 Partnership
 
 section to at least one workplace before it becomes available in the left menu.
2. Click the
 
**New partnership** 

 button.
3. Populate the fields in the mini page that pops up. Refer to the partnership parameters table when populating the fields.
 


	1. Select your company’s partner in the
	 
	 Account
	 
	 lookup.
	2. Specify the type of your partner in the
	 
	 Type
	 
	 field.
	3. Specify the time frame of the partner program using the
	 
	 Start date
	 
	 and
	 
	 Due date
	 
	 fields. The period is 1 year by default.
	4. Leave the
	 
	 Active
	 
	 check box selected if you want the portal page to display the partnership as a partner program. At the same time, you can uncheck this checkbox when needed and make the partner program unavailable to your partner (e.g., when creating different programs for different periods).
4. Save the changes (
 [Fig. 1](#XREF_98436_414)
 ).
 



 As a result, the specified partner parameters in the lookups, including the partner funds, will automatically display in the main application, as well as in the partner program on the portal.
 





 Note.
 
 Only users with the “Partner portal users” role may have access to the partner program.
 






 Fig. 1
 

 Adding a new partnerships and partner program
 

![chapter_portal_setup_adding_partnership.gif](/guides/sites/en/files/documentation/user/en/channel_sales/BPMonlineHelp/channel_sales_example/chapter_portal_setup_adding_partnership.gif)






 Prepare the partner organization for working on the portal
---------------------------------------------------------------


1. Create a partner portal organization and bind it to portal users. This process is covered in the “
 
[Add portal users](https://academy.creatio.com/documents?product=portal&ver=7&id=2010) 

 ” article. Please note that you need to choose the “Partners” role in the
 
 Parent role
 
 field on the profile organization page when creating a partner portal organization.
2. Configure access permissions for the portal users of the partner organization. To access the partner portal functionality and work in the partner program, a portal user must be assigned the “
 **Partner portal users** 
 ” functional role. More information on the portal user roles is available in the “
 
[Manage portal user roles](https://academy.creatio.com/documents?product=portal&ver=7&id=2004) 

 ” article.
3. Send portal invitation emails to partner portal users to enable them to log in to the partner portal and participate in the partner program. The procedure for sending portal invitation is available in the “
 
[Send portal invitations](https://academy.creatio.com/documents?product=portal&ver=7&id=2012) 

 ” article.
 



 As a result, users with the “Partner portal users” functional role will be able to access the
 
 Partner program
 
 section (
 [Fig. 1](#XREF_35339_417)
 ), which stores all conditions and the current status of each partnership.
 





 Fig. 1
 

 The
 
 Partner program
 
 section
 

![scr_chapter_portal_setup_parner_program.png](/guides/sites/en/files/documentation/user/en/channel_sales/BPMonlineHelp/channel_sales_example/scr_chapter_portal_setup_parner_program.png)




