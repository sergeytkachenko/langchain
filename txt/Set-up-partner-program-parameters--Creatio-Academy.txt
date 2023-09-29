


 Creatio comes with a set of tools for configuring partner programs, such as special lookups with pre-set partnership parameters. You will need to examine these pre-set parameters and modify them to suit your specifics. You can also come up with your own partnership parameters and add them to Creatio
 
[lookups](https://academy.creatio.com/documents?product=administration&ver=7&id=271) 

 .
 



 To set up custom partnership parameters, populate the
 
 Type of partner
 
 ,
 
 Level of partner
 
 ,
 
 Level partnership parameters
 
 , and
 
 Category of partnership parameter
 
 lookups accordingly.
 





 Attention.
 
 When you edit the content of lookups, do not delete base content. Otherwise, essential functionality failure may occur.
 



1. **Type of partner** 
 is the type of your company and your partner company’s cooperation. The
 
 Type of partner
 
 lookup contains the following default types: “Reseller,” “Consultant,” “Reference,” and “Integrator.” If you work with partners of other types, you must add these types to the this lookup.
2. **Level of partner** 

 is the tier for each type of partner, as well as the target number of points needed to reach that tier. The partners get their points for reaching the performance indicators specified in the
 
 Category of partnership parameter
 
 lookup. When a partner collects the target number of points, they get to the next tier, and their collected points reset. For example, a “Reseller” partner has three tiers: bronze, silver, and platinum.
3. **Category of partnership parameter** 

 is a lookup with a list of parameters to evaluate the performance of a partner. This can be the number of leads, the sum of opportunities, the number of certified experts, the marketing budget, and so on.
4. **Level partnership parameters** 

 is a lookup that is used to make the rules and conditions of a partnership for each individual tier of the partner program. It uses the values of all lookups specified above.
 



 In
 [Fig. 1](#XREF_40205_412)


 , you can see an example of partnership conditions for a “Bronze” reseller. In this example:
 


	1. The “Leads number” and “Opportunity amount” parameters are required for a partner to reach the Bronze level. Parameter type – “
	 **Obligation.** 
	 ”
	2. The “Margin” parameter type is the reward of the partner. As soon as the partner reaches the Bronze level, they will have a 10% discount. Parameter type – “
	 **Benefit.** 
	 ”
	3. The “Price list” parameter determines special prices for partners of a specific level. Parameter type – “
	 **Benefit.** 
	 ”
	4. The “Marketing funds” parameter determines the percentage of the opportunity sum that will be paid to the partner marketing funds when a partner closes the opportunity with the “Closed won” status. Parameter type – “
	 **Benefit** 
	 ”.
	 
	
	
	
	 For example, by closing opportunities with the total sum of 100,000 and registering 10 leads, the partner will get 80 points for fulfilling the criteria of each of the parameters. As a result, they will get the Bronze level and a 10% discount. 1% of each successful opportunity will be credited to the marketing funds.
	 
	
	
	
	
	
	 Fig. 1
	 
	
	 Partnership parameters for a Bronze-tier reseller.
	 
	
	![scr_chapter_portal_setup_bronze_level_parameters.png](/guides/sites/en/files/documentation/user/en/channel_sales/BPMonlineHelp/channel_sales_lookups/scr_chapter_portal_setup_bronze_level_parameters.png)



 As a result, the partnership program will be based on the values specified in the lookups.  Learn more about setting up a partnership program in the “
 
[Example of setting up a partner program](/docs/8-0/user/sales_tools/channel_sales/partner_program_example/example_of_setting_up_a_partner_program#HT_partner_program_setup_example) 

 ” article.
 




