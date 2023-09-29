


**Creatio portal** 
 is a component that provides a way to open up various parts of your system to external users, such as customers, partners, contractors, stakeholders, or teams within your company.
 



 A portal is a workplace with different permissions for various types of users. The portal UI is similar to the UI of the primary application. Use the portal to create a limited subset of Creatio with restricted access to data and only the necessary functionality. The list of sections available in Creatio portal depends on its configuration.
 



 Through a portal, users can access certain Creatio sections and their associated data. Additionally, they can view, edit, or create records, as well as add notes and attachments.
 





 Note.
 
 Since Creatio version 8.0.9 “Portal user” user type and “All portal users” root role were renamed to “External user” and “All external users,” respectively.
 




 The Creatio portal is provided in the following configurations:
 **self-service portal** 
 ,
 **customer portal** 
 , and
 **partner portal** 
 . They are suitable for a variety of use cases, the most common being:
 


* **Customer self-service** 
 , such as in technical support. Give a self-service option to your customers and focus the time and expertise of your support agents on more important tasks. Allow your customers to submit support cases and track the resolution progress directly on the portal. Provide them access to your knowledge base articles, helping them to find answers quickly. Service multiple customers at once, avoiding queues and productivity loss.
 [Read more >>>](#title-1638-1)
* **Interaction with internal and external customers** 
 , for instance, an HR portal. Configure the ability to service external employees and contractors who do not use Creatio regularly: create applications, submit them for approval and track their progress. An HR portal can act as a central hub for all the important company documents and policies that are available freely.
 [Read more >>>](#title-1638-2)
* **Interaction with external users** 
 (clients, dealers, and partners) at all stages of the sales process. Create partner programs, process leads, and close opportunities along with your partners by using lead and corporate sales management processes. Keep track of the partner tiers, training sessions, and the partners’ certified experts.
 [Read more >>>](#title-1638-3)



 Both the range of problems the portal solves and its customization possibilities differ based on your portal configuration. Each configuration includes a specific number of base sections and additional objects (lookups, details, etc.). It might also include the option to add custom sections. Learn more in a separate article:
 [Customize Portal Creatio](https://academy.creatio.com/documents?id=2002) 
 . View major parameters of various portal configurations in the table below.
 





| 
 Portal configuration
  | 
 Base sections
  | 
 Custom sections
  | 
 Number of objects
  |
| --- | --- | --- | --- |
| 
 Self-service portal
  | 

 Portal cases
 
 ,
 

 Portal knowledge base
 
 | 
 0
  | 
 ≤ 300
  |
| 
 Customer portal
  | 
 Portal cases
 
 ,
 

 Portal knowledge base
 
 ,
 

 Applications
 
 (for Financial Services Creatio, Customer Journey edition),
 

 Documents
 
 (if available in the main Creatio application)
  | 
 ≤ 3
  | 
 ≤ 1500
  |
| 
 Partner portal
  | 
 Portal cases
 
 ,
 

 Portal knowledge base
 
 ,
 

 Partner program
 
 ,
 

 Leads
 
 ,
 

 Opportunities
 
 ,
 

 Marketing activities
 
 ,
 

 Orders
  | 
 ≤ 3
  | 
 ≤ 3000
  |




 In Creatio, the portal functionality is licensed separately.
 



 The following licenses are required for each user of different portal editions:
 


* customer portal on-site/cloud for the customer portal
* self-service portal on-site/cloud for the self-service portal
* partner portal on-site/cloud for the partner portal



 Learn more:
 [Creatio licensing](/docs/7-18/user/setup_and_administration/licensing/licensing_overview/creatio_licensing) 
 .
 



 Self-service portal
---------------------



 The self-service portal is available in Service Creatio customer center, Service Creatio, enterprise edition, and Financial Services Creatio, customer journey products. The portal can act as a primary means of user support or as an extension of your service system.
 



 The self-service portal eases the load on your employees by freeing up various communication channels (e. g., phone or email) and routing incoming requests On the self-service portal, users can find answers to their questions in the knowledge base, create and track the progress of their support cases, or communicate with the support staff via the feed. Unlike support agents, self-service capabilities and information are available to your customers 24/7. The self-service portal configuration allows you to add the following sections to the portal:
 


* The
 
 Portal Cases
 
 section, where portal users can register support cases on their own, as well as track the case resolution progress and communicate with support employees. The
 
 Portal Cases
 
 section is a counterpart to the
 
 Cases
 
 section in the main Creatio application. You can choose which fields and details from the
 
 Cases
 
 section to display in the
 
 Portal Cases
 
 section via the Section Wizard.
* The
 
 Portal Knowledge base
 
 section, where portal users can look up the reference information, search for answers to frequently asked questions, find rules, regulations, document templates, or advertising materials.



 You cannot add custom sections to the self-service portal. However, you can customize the base sections.
 



 Customer portal
-----------------



 The customer portal configuration provides portal capabilities to all Creatio products and is designed for process automation, e. g., providing services, confirming applications and service requests, etc. You can add custom sections to the customer portal to automate any internal process. All custom logic in these sections will be available to the portal users. Configure business processes and cases on the portal to automate routine administrative tasks. For example, customer portal users can:
 


* Initiate processes, e. g., create applications, requests, etc.
* Participate in processes, e. g., approve requests.



 You can add up to three custom sections to the customer portal. Configure the custom sections in the Section Wizard and add them to the “Portal” workplace to display them on the portal.
 



 Create custom sections from scratch with no or minimal connection to base Creatio sections.
 



 The customer portal configuration in Financial Services Creatio, customer journey edition allows you to add the
 
 Applications
 
 section to the portal. Additionally, you can add the
 
 Documents
 
 section if your Creatio product supports it.
 





 Note.
 
 You can use the self-service and customer portals together to set up a support service channel with up to 3 custom sections.
 




 Partner portal
----------------



 The partner portal is available in Sales Creatio, enterprise edition, and Creatio CRM Bundle.
 



 The partner portal is designed for companies that work with customers via partner networks. This portal is a platform for communication and collaboration on leads and sales with your partners.
 



 A
 [partner](/docs/glossary_page#title-2089-110) 
 can work with your customers on your behalf using the partner portal.
 





 Note.
 
 Add the partner organization to the “Partner portal users” functional role to let the organization access the “Partner portal” configuration. Learn more:
 [Manage users and access permissions on the portal](/docs/7-17/user/more_apps/portal/manage_portal_in_the_main_application/manage_portal_in_main_application) 
 .
 




 Find the data about your company’s partners and related partnerships, their conditions, and status in the
 
 Partnership
 
 section of the main application. This section is best suited for your employees in charge of partner interaction. You can use it to set up the cooperation conditions and add as many
 [partnerships](/docs/glossary_page#title-2089-112) 
 as needed, but no more than one per partner (Fig. 1). The partner portal displays the conditions of an individual partnership as a partner program.
 




 Fig. 1 The
 
 Partnership
 
 section in the main application
 

![scr_chapter_portal_partnership_register_example.png](/docs/sites/en/files/images/More_Apps/portal/portal_overview/scr_chapter_portal_partnership_register_example.png)



 Manage the partner performance and set up the cooperation conditions in the main Creatio application.
 



 The
 
 Partner program
 
 section will display the partnership conditions you configure in the main application. Partner portal users can view only the profile of their organization and cannot edit the data. Your partners and their employees can access the
 
 Partner program
 
 section. This section contains all information relevant to your partners and their work (Fig. 2):
 


* Current partner tier.
* Partner program conditions for the current tier, including the partner reward, such as a percentage of the partner’s profits (profit margin) and performance indicators required for a level-up.
* Partner training sessions and certifications.
* Lead and opportunity analytics.




 Fig. 2 A partner program page on the portal
 

![scr_chapter_portal_partner_programme_page_example_0.png](/docs/sites/en/files/images/More_Apps/portal/portal_overview/scr_chapter_portal_partner_programme_page_example_0.png)



 You can only bind a single partner program to each partner.
 



 When working on the partner portal, your partners can register new leads and opportunities in the corresponding portal sections. A partner program page displays lead and opportunity details by default. You can also find them on the partnership page in the primary application. This data is used to keep track of how partners fulfill their partnership conditions and how they progress through partnership tiers. Set up and view partner sales analytics in the dashboards on the portal main page. Learn more:
 [Channel sales](https://academy.creatio.com/docs/user/sales_tools/channel_sales) 
 .
 




