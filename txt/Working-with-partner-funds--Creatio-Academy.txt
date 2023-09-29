


 Creatio can credit a specific percentage of interest to the funds of partners. Use this logic to automate working with the marketing funds. Creatio can automatically credit a percentage from  the amount of an opportunity that the partner successfully closed –  to special “marketing funds.” The partner can use the marketing fund to initiate promotions and other marketing activities. Creatio will then deduct the activity budget from the partner’s marketing funds.
 



 You can also add custom partnership funds and manually credit or debit them.
 





 Set up the funds
--------------------



 In the Creatio main application, perform the following actions:
 


1. Click
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/channel_sales/BPMonlineHelp/channel_sales_funds/btn_system_designer.png)
 in the main Creatio application.
2. Go to the
 
 System setup
 
 block → click
 
 Lookups
 
 .
3. Open the
 
 Level partnership parameters
 
 lookup.
4. Set parameters of fund credits as per the partner levels (
 [Fig. 1](#XREF_98467_49)
 ).
 





 Fig. 1
 

 Parameters of crediting the marketing funds for a “Bronze” level partner
 

![scr_chapter_portal_setup_bronze_level_parameters_fund.png](/guides/sites/en/files/documentation/user/en/channel_sales/BPMonlineHelp/channel_sales_funds/scr_chapter_portal_setup_bronze_level_parameters_fund.png)
5. Add a partnership. You can learn more in the “
 
[Example of setting up a partner program](/docs/8-0/user/sales_tools/channel_sales/partner_program_example/example_of_setting_up_a_partner_program#HT_create_new_partnership) 

 ” article. Note that the
 
 Active
 
 checkbox on the partnership page must be selected to be able to work with funds.
 



 As a result, the specified parameters for crediting the marketing funds will automatically display on the partner page in the main application (
 [Fig. 2](#XREF_39154_50)
 ), as well as on the
 
 Partnership parameters
 
 detail on the portal. A
 
 Marketing fund
 
 record will be added on the
 
 Funds
 
 detail. When an opportunity is closed with the “Closed won” result, the marketing funds will be credited with the percentage of the amount from the opportunity budget. This percentage depends on the partner level.
 



 You can add another fund manually by clicking
 ![btn_add_ke.png](/guides/sites/en/files/documentation/user/en/channel_sales/BPMonlineHelp/channel_sales_funds/btn_add_ke.png)
 on the
 
 Funds
 
 detail.
 





 Fig. 2
 

 Partner program page in the main application
 

![scr_chapter_portal_setup_parner_program_main.png](/guides/sites/en/files/documentation/user/en/channel_sales/BPMonlineHelp/channel_sales_funds/scr_chapter_portal_setup_parner_program_main.png)



 You can view the remaining sum of the funds on the partnership page under
 
 General info
 
 →
 
 Funds
 
 . Partners can access this information by opening the partnership page on the portal.
 





 Credit or debit the funds
-----------------------------



 The funds are credited automatically when a partner opportunity is closed with the “Closed won” status. The amount of funds is recalculated based on the opportunity sum, opportunity stage, or the partner. When an opportunity is deleted, the corresponding sum is debited from the amount of the marketing funds. These actions display on the partner page →
 
 General info
 
 →
 
 Operations
 
 of the partnership page in the main application, as well as on the portal.
 



 You can also credit or debit funds manually. Manual operations are available for marketing funds as well as for other types of funds.
 



 To charge or write-off funds:
 


1. Open the partnership page in the main application.
2. Go to the
 
 General info
 
 tab →
 
 Operations
 
 detail → click
 ![btn_add_ke00001.png](/guides/sites/en/files/documentation/user/en/channel_sales/BPMonlineHelp/channel_sales_funds/btn_add_ke00001.png)
 .
3. Populate the fields on the opened page:
 


	1. Type
	 
	 – select the type of operation: credit or debit.
	2. Fund
	 
	 – specify the name of the fund.
	3. Amount
	 
	 – specify the sum for crediting or debiting.
	4. Description
	 
	 – add comments to the operation. This field is optional.
4. Click
 
 Save
 
 (
 [Fig. 1](#XREF_98348_51)
 ).
 





 Fig. 1
 

 Example of a credit operation to the fund
 

![scr_chapter_portal_setup_parner_program_operation.png](/guides/sites/en/files/documentation/user/en/channel_sales/BPMonlineHelp/channel_sales_funds/scr_chapter_portal_setup_parner_program_operation.png)



 The changes will display in the main application, as well as on the portal. The partners only have permission to view the
 
 Operations
 
 and
 
 Funds
 
 details.
 





 Budgetg partner activities from the funds
---------------------------------------------



 When a partner adds a new marketing activity in the
 
 Marketing activities
 
 section on the portal, the partnership page of the main application displays a record with the “Partner activity” type on the
 
 Marketing activities
 
 tab. The partner will be specified as the portal organization account.
 



 If you open the record, you can specify the portal user as the activity owner and set the marketing activity budget (
 [Fig. 1](#XREF_12598_52)
 ).
 





 Fig. 1
 

 Partner program page in the main application
 

![chapter_portal_setup_partner_marketing_activity.png](/guides/sites/en/files/documentation/user/en/channel_sales/BPMonlineHelp/channel_sales_funds/chapter_portal_setup_partner_marketing_activity.png)



 If you specify a marketing fund in the
 
 Fund
 
 field of the record, the corresponding sum will be automatically debited from the specified fund once you save the record. If you edit or delete a record, Creatio will update the transaction and recalculate the funds. The recalculated funds display on the
 
 Operations
 
 detail of the partner program.
 



 You can also create partner activities in the main application. The funds will be debited similarly.
 




