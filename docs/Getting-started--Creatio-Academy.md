


 The partner portal is designed for companies that work with customers via partner networks. This portal is a joint communication platform for passing leads between partners, partner cross-sales, and marketing campaign team-ups.
 



 The partner portal functionality is available in Sales Creatio enterprise and CRM Creatio.
 



 Your partners can work with these sections:
 


* Leads
* Opportunities
* Orders
 
 .



 These sections are duplicates of the main application sections of the same name. You can choose which fields and details from the
 
 Cases
 
 section to display in the
 
 Portal Cases
 
 section via the Section Wizard. Lead and opportunity details are available in the
 
 Partner program
 
 portal section and on the partnership page in the main application. These data are used to keep track of how the partnership conditions are fulfilled, how higher partnership tiers are achieved and how marketing funds are credited.
 



 Portal users can access the basic portal functionality – main page, user profile settings, knowledge base search, feed communications, etc.
 



 You can set up partner sales analytics in the dashboards on the portal main page. More information about setting up the portal main page is available in the “
 
[Set up the portal main page](https://academy.creatio.com/documents?product=portal&ver=7&id=1477) 

 ” article.
 



 You can add up to three custom sections on the customer portal. Custom sections are
 
[configured via the Section Wizard](https://academy.creatio.com/documents?product=portal&ver=7&id=1968) 

 and are added to the “Portal” workplace.
 





 Partner organization access permissions
-------------------------------------------



 To access the “Partner portal” configuration, add the partner organization to the “Partner portal users” functional role. You can read more about the types of portal users in the “
 
[Users and permissions on the portal](https://academy.creatio.com/documents?product=portal&ver=7&id=2014) 

 ” article.
 





 Portal licensing
--------------------



 Each portal user “consumes” a special “portal license” (as opposed to using regular Creatio licenses). The name of the partner portal license must contain the “partner portal on-site/cloud” string. Read more about licensing in the “
 
[Creatio licensing](https://academy.creatio.com/documents?product=administration&ver=7&id=1264) 

 ” article.
 









 Prepare the partner portal for work
-------------------------------------------



 You can find the data about your company’s partners and related partnerships (their conditions and status) in the
 
 Partnership
 
 section of the main application. This section is best suited for use by your employees responsible for interaction with your partners. You can use it to set up the cooperation conditions and add as many partnerships as needed but no more than one per each partner (
 [Fig. 1](#XREF_63077_1)
 ). The partner portal displays the conditions of a partnership as a partner program.
 





 Fig. 1
 

 The
 
 Partnership
 
 section in the main application
 

![scr_chapter_portal_partnership_register_example.png](/guides/sites/en/files/documentation/user/en/channel_sales/BPMonlineHelp/channel_sales_getting_started/scr_chapter_portal_partnership_register_example.png)





 Note.
 
 You can manage partners performance and set up the cooperation conditions in the main Creatio application.
 




 The partner programs are configured in the main application. Partner portal users can only access the profile of their own organization. The partner program access on the portal is read-only. The
 
 Partner program
 
 section is available for access by your partners and their employees. This section contains all information relevant to your partners and their work (
 [Fig. 2](#XREF_60454_367)
 ):
 


* Current partner tier and performance indicators required for a level-up.
* Partner reward, such as a percentage of their profits.
* Partner training sessions and certifications.
* Funds and amount of funds.
* Credit and debit operations.
* Marketing activities of the partner.
* Partnership parameters history.
* Partner lead and opportunity analytics.
* Additional information.





 Fig. 2
 

 A partner program page on the portal.
 

![scr_chapter_portal_parner_program.png](/guides/sites/en/files/documentation/user/en/channel_sales/BPMonlineHelp/channel_sales_getting_started/scr_chapter_portal_parner_program.png)





 Note.
 
 You can only bind a single partner program to each partner.
 




 To prepare the partner portal for work:
 


1. [Outline your partner program](/docs/8-0/user/sales_tools/channel_sales/partner_program_example/example_of_setting_up_a_partner_program#HT_partner_program_parameters_table) 

 . Setting up a partner program is a one-time procedure.
 



 We recommend that you capture your partner program parameters on paper or in a spreadsheet. Specify the types of partners you work with. For example, a “reseller”, “consultant”, etc. Set forth the partner tiers and requirements to achieve a new tier. For instance, “Bronze,” “Silver,” and “Platinum” tiers for a “Reseller” partner. You can define the cooperation conditions (parameters) for each tier individually. Such parameters can include the number or amount of opportunities, the number of leads, interest debit payable to the marketing funds, etc.
2. [Transfer the parameters](/docs/8-0/user/sales_tools/channel_sales/partner_program_example/example_of_setting_up_a_partner_program#HT_partner_program_parameters_transer_to_lookups) 


 of the partner program to the main Creatio application. The parameters are entered once.
 



 Make sure to populate the
 
 Type of partner
 
 ,
 
 Level of partner
 
 ,
 
 Level partnership parameters
 
 and
 
 Category of partnership parameter
 
 lookups with your parameters.
3. [Set up personal price lists](/docs/8-0/user/sales_tools/channel_sales/partnership_conditions/set_up_special_conditions_of_partner_cooperation#HT_partners_personal_pricelists) 

 to take into consideration special conditions for working with partners. This action is run for each partner individually.
4. [Add a new partnership](/docs/8-0/user/sales_tools/channel_sales/partner_program_example/example_of_setting_up_a_partner_program#HT_create_new_partnership) 


 in the
 
 Partnership
 
 section in the main application.
 



 Adding an active partnership in the main application means that you have reached an agreement with the partner and they officially begin participating in your partner program. The newly created partnership will be available to the partner as a partner program.
5. [Create a portal organization](/docs/8-0/user/sales_tools/channel_sales/partner_program_example/example_of_setting_up_a_partner_program#HT_create_partner_portal_organization) 


 for an account of the “Partner” type. Bind partner portal users to the organization and set up corresponding permissions.
6. [Send a portal invitation email](https://academy.creatio.com/documents?product=portal&ver=7&id=2012) 


 to the employees of the partner.




