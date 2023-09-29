


 Landing page is a standalone website page that is designed for a call to action, a specific goal usually related to a marketing campaign. Creatio can connect to your landing pages and use the captured visitor data to add new records. For example, this lets you generate a prospect database and nurture leads before handing them off to sales.
 



 You can use landing pages to set up the registration of any Creatio object related to sales funnel or customer service. For example, you can use a page that contains special subscription offers, shopping cart page, user registration page, or multimedia download page as landing page. Creatio can add cases, leads, contacts, accounts, orders, and other records based on data retrieved from the submitted web form.
 



 Since version 8.0.5 you can pass data from a landing page to Creatio in multiple ways:
 


* Integrate Creatio with external webhook service. For example, Landingi, Instapage, Elementor.
* Customize HTML code of the landing page and integrate the page with a record in the
 
 Landing pages and web-forms
 
 section.





 Note.
 
 The instructions below are based on a common way to use landing pages and web forms to gather leads. Register other Creatio objects similarly.
 




 Integrate with landing pages via external webhook service
-----------------------------------------------------------



 This integration is available for Creatio 8.0.5 and later. You can integrate landing pages created in any builder that supports webhooks. We recommend using Landingi service. Learn more in a separate article:
 [Landingi service integration](https://academy.creatio.com/documents?id=2414) 
 .
 



 You can connect Matomo to landing page that integrates to Creatio via external webhook service to add tracked data to Creatio. For example, since Creatio 8.0.7, you can add data with events tracked on a landing pages to contact.
 



 The general procedure to integrate Creatio with a landing page includes the following steps:
 


1. **Get API key** 
 .
2. **Create a landing page** 
 .
3. Set up OAuth authentication if you use Creatio
 **on-site** 
 . This is a one-time procedure. Learn more in a separate article:
 [Set up OAuth 2.0 authorization for integrated applications](https://academy.creatio.com/documents?id=2396) 
 .
4. **Connect your landing page to Creatio** 
 and set up field mapping between the page and Creatio lead.
5. **Set up tracking** 
 to enrich the customer profile with website events (optional). Learn more about tracking setup on the
 [Creatio Marketplace](https://marketplace.creatio.com/app/matomo-connector-creatio) 
 .



 This procedure differs based on your webhook service. To integrate an external webhook service with Creatio, follow the instructions in separate articles:
 [Set up external webhook service integration](https://academy.creatio.com/documents?id=2412) 
 ,
 [Landingi service integration](https://academy.creatio.com/documents?id=2414) 
 .
 



 Integrate with landing pages via web-to-object mechanism
----------------------------------------------------------



 The general procedure to integrate Creatio with a landing page includes the following steps:
 





 Attention.
 
 Creatio supports integration with CMS that let you add custom HTML and JavaScript code. You need an additional connector to integrate with other CMS, for example, WordPress. Learn more on
 [Creatio Community](https://community.creatio.com/) 
 and
 [Marketplace](https://marketplace.creatio.com/) 
 .
 



1. **Create landing pages** 
 based on
 [general rules and recommendations](https://academy.creatio.com/documents?id=1522) 
 .
2. **Connect your landing page to Creatio and set up field mapping between the lead page and landing page form.** 
 To
 [connect](https://academy.creatio.com/documents?id=1083) 
 the landing page to Creatio, copy the unique code snippet generated in Creatio for your landing page and paste it into page code. The fields are mapped between the landing page and lead page through the embedded code snippet. As a result, each lead generated via the landing page will automatically be saved to the
 
 Leads
 
 section for further nurturing in Creatio.
3. **Set up the landing forms processing.** 
 The form your customers fill out only provides part of the information required for lead nurturing. Depending on the purpose of the landing page, you can set up
 [autofill](https://academy.creatio.com/documents?id=1523) 
 for some of the lead page fields. For example, the subscription form for a special offer on hardware can automatically be connected to the “Hardware” need type. You can also streamline the process of filling out the registration form on the landing page for bulk email recipients by
 [autofilling](https://academy.creatio.com/documents?id=1625) 
 the required fields that have Creatio data available, for example, name, email, phone number, etc.
4. **Set up tracking** 
 to enrich the customer profile with the website events and track lead channels and sources. Learn more about setting up tracking in a separate article:
 [Track contact data](https://academy.creatio.com/documents?id=2372) 
 .




