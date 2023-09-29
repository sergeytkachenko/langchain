


 Auto numbering of records
---------------------------



 The following settings are available in Creatio products that have the corresponding sections.
 



 System settings of this group facilitate automatic numbering of records, for example, invoice codes or account numbers. There are two types of settings: one specifies the static text (mask) of a number, and another one is used for saving the last generated number. For example, to generate a knowledge base article code like “Article-23,” where 23 is the current number of the invoice, enter the following mask: Knowledge base article-{0}.
 



 Auto numbering is enabled for the following objects:
 


* “Document” – via the “Document number mask” (DocumentCodeMask) and “Current number of document” (DocumentLastNumber) system settings.
* “Contract” – “Contract number mask” (ContractCodeMask) and “Current contract” (ContractLastNumber) settings.
* “Account” – via the “Account code mask” (AccountCodeMask) and “Current number of account” (AccountLastNumber) system settings.
* “Knowledge base article” – via the “Knowledge base article number mask” (KnowledgeBaseCodeMask) and “Current number of knowledge base article” (KnowledgeBaseLastNumber) system settings.
* “Invoice” – via the “Invoice number mask” (InvoiceCodeMask) and “Current number of invoice” (InvoiceLastNumber) system settings.
* “Case” – via the “Case number mask” (CaseCodeMask) and “Current number of case” (CaseLastNumber) system settings.
* “Service contract” – “Service agreement number mask” (ServicePactCodeMask) and “Current number of service agreement” (ServicePactLastNumber) settings.
* “Operation” – via the “Cash flow number mask” (CashflowCodeMask) and “Current number of operation” (CashflowLastNumber) system settings.
* “Problem” – via the “Problem number mask” (ProblemCodeMask) and “Current number of problem” (ProblemLastNumber) system settings.
* “Change” – via the “Change number mask” (ChangeCodeMask) and “Current number of change” (ChangeLastNumber) system settings.
* “Release” – via the “Release number mask” (ReleaseCodeMask) and “Current number of release” (ReleaseLastNumber) system settings.
* “Order” – via the “Order number mask” (OrderCodeMask) and “Current number of order” (OrderLastNumber) system settings.



 The
 **“Mask number...”** 
 system setting is used during the process of generating the number or code of record when it is created. With the help of this setting you can specify a static text (mask) preceding or following the numeric value of number or code.
 



 Type: text (500 characters).
 



 The
 **“Current number of…”** 
 system setting is used for generating the number or code of record when it is created. Stores the numeric component of the last created record.
 



 Type: integer.
 



 Updating contact ages
-----------------------



 Use the settings below to manage the contact age calculation in Creatio. Read more:
 
[Updating contact ages](/docs/8-0/user/crm_tools/accounts_and_contacts/calculate_contact_age_shortcut/calculate_contact_age) 

 .
 



**Enable updating contact ages** 
 (ActualizeAge) – manages the functionality of automatic update of contact ages. Disabling this system setting will disable all functionality for automatic contact age calculation. The functionality includes: automatic updating of contact ages on saving a contact record, a regular scheduled update of contact ages on their birthdays, contact age update triggered by the
 
 Update the values in the 'Age' column
 
 action in the
 
 Contacts
 
 section.
 



 Type: Boolean. Default value: “True.”
 



**Enable automatic daily update of the contact ages** 
 (RunAgeActualizationDaily) – manages the daily operation of updating the contact ages. If you enable this system setting, Creatio will run a daily check for contacts who have their birthday today and update their
 
 age
 
 . If you disable this system setting, Creatio will still use the general age calculation functionality, but without the automatic daily updates.
 



 Type: Boolean. Default value: “True.”
 



**Time of automatic daily update of the contact ages** 
 (AutomaticAgeActualizationTime) – determines the time of performing the age updates for the contacts whose birthday falls on the current day. Users can set the value manually or by running the
 
 Schedule daily update of the “Age” column
 
 action in the
 
 Contacts
 
 section.
 





 Note.
 
 For large contact databases, we recommend scheduling the daily update of contact ages on the non-business hours.
 




 By default, the system setting value is set in the “UTC” format. However, if a user runs the
 
 Schedule daily update of the “Age” column
 
 action in the
 
 Contacts
 
 section and does not change the run time, the system setting value will be updated automatically – the time will be recalculated based on the user's time zone. For example, a user in the UTC+1 time zone runs the
 
 Schedule daily update of the “Age” column
 
 action but does not change the value in the system setting. In this case, Creatio will display the default time as “02:30 AM” instead of 01:30 AM and change the displayed time zone from “UTC” to “UTC+1.”
 



 Type: time. Default value: “01:30 (UTC).”
 





 Note.
 
 Note that if you change the time using the system setting and not via the action in the
 
 Contacts
 
 section, the new value will only apply after the next already scheduled age update, i. e., in 24 hours after modifying the system setting value. For example, if you change the system setting value from 01:30 AM to 04:30 AM on Monday at 3 PM, the nearest age update will occur at 01:30 AM on Tuesday and then – at 04.30 AM on Wednesday. If you change the time using the action in the
 
 Contacts
 
 section, the modifications will apply during the next age update.
 




**Date of the last update of the contact ages** 
 (LastAgeActualizationDate) – use this setting to view the date of the last age update (performed as per schedule or by running the section action).
 



 Administration
----------------



**Licensing company Id** 
 (CustomerId) – stores the unique identifier of your company used for licensing purposes. Company Id is provided when purchasing licenses.
 



 Type: text (500 characters).
 



**Joined objects administering** 
 (QueryJoinRightLevel) – manages access to viewing information from one of the joined objects. For example, when viewing information about primary contact (like job responsibility or birth date) from the
 
 Accounts
 
 section.
 



 Type: integer. Default value: “0.” This system setting can have one of the following values:
 


* “0” – show data only from those records in the joined object for which the current user has access;
* “1” – show data only from those records in the joined object for which the current user has access. In case the user does not have access to a record, show data from the primary displayed column;
* “2” – show data from all records of joined object, regardless of whether or not the user has access to them.





 Attention.
 
 If the current user does not have access to the “Read” operation for the object that contains the connected record, then the data of the connected object will not be displayed regardless of the value of the ”Joined objects administering” system setting.
 




**Term of expired license notification** 
 (ExpireLicenseNotificationTerm) – determines when to notify the users about the need to extend Creatio licenses, in days before the expiration date. If there are no licenses for the coming term or there are not enough licenses, system administrators will see this notification in the communication panel.
 



 Type: integer. Default value: 14.
 



**Enable rights on service agreements and configuration items for portal users** 
 system setting (“EnableRightsOnServiceObjects” code) – grants the permission to view service agreements and configuration items to portal users and organizations.
 



 Specify the portal user contacts and organization accounts in the
 **service agreement’s** 

 Service recipients
 
 detail to enable them to view the agreement.
 



 Specify the portal user contacts and organization accounts in the
 **configuration item’s** 

 Users
 
 detail to enable them to view the item.
 



 Type: Boolean. Default value: “True.”
 



**MaxDopQueryHint** 
 system setting (“MaxDopQueryHint” code) lets you limit the number of threads used to execute a request to the database. This can help reduce the impact of resource-intensive operations on other users.
 


### 
 Audit log



**Log client IP range management events** 
 (UseAdminClientIPLog) – specifies whether to log the changes to or the deletion of the valid IP address ranges.
 



 Type: Boolean. Default value: “False.”
 



**Log entity schema columns access rights management events** 
 (UseAdminEntitySchemaColumnLog) – specifies whether to log the changes to object column permissions.
 



 Type: Boolean. Default value: “False.”
 



**Log external resources access rights management events** 
 (UseAdminEntitySchemaExternalServiceLog) – specifies whether to log the changes to access permissions for objects used to integrate Creatio with various external services via the OData protocol.
 



 Type: Boolean. Default value: “False.”
 



**Log users management events** 
 (UseAdminUserRoleLog) – specifies whether to log the addition of users to organization structure elements and the exclusion of users from roles.
 



 Type: Boolean. Default value: “False.”
 



**Enable rights on service agreements and configuration items for portal users** 
 system setting (“EnableRightsOnServiceObjects” code) – grants the permission to view service agreements and configuration items to portal users and organizations.
 



 Specify the portal user contacts and organization accounts in the
 **service agreement’s** 

 Service recipients
 
 detail to enable them to view the agreement.
 



 Specify the portal user contacts and organization accounts in the
 **configuration item’s** 

 Users
 
 detail to enable them to view the item.
 



 Type: Boolean. Default value: “True.”
 



**Audit log culture** 
 (AuditLogCulture) – the language of the audit log messages.
 



 Type: lookup. Default value: “en-US.”
 



**Log user authorization management events** 
 (UseUserAuthorizationLog) – specifies whether to log the user's login attempts, both successful and failed.
 



 Type: Boolean. Default value: “False.”
 



**Log denied operations management events** 
 (UseDeniedOperationLog) – specifies whether to log the attempts to execute denied operations.
 



 Type: Boolean. Default value: “False.”
 



**Log entity schema default records access rights management events** 
 (UseAdminEntitySchemaRecordDefRightLog) – specifies whether to logs the changes to access permissions for records of the default objects.
 



 Type: Boolean. Default value: “False.”
 



**Log user sessions management events** 
 (UseUserSessionLog) – specifies whether to log the end of user sessions.
 



 Type: Boolean. Default value: “False.”
 



**Log audit log operations management events** 
 (UseAdminOperationAuditLog) – specifies whether to log the audit log operations.
 



 Type: Boolean. Default value: “False.”
 



**Log operation access rights management events** 
 (UseAdminOperationLog) – specifies whether to log the changes to system operation access permissions.
 



 Type: Boolean. Default value: “False.”
 



**Log entity access rights management events** 
 (UseAdminEntitySchemaOperationLog) – specifies whether to log the changes to access permissions for reading, updating, and deleting data in the objects.
 



 Type: Boolean. Default value: “False.”
 



**Log system settings management events** 
 (UseAdminSettingsLog) – specifies whether to log the changes to system setting values.
 



 Type: Boolean. Default value: “False.”
 



**Log entity schema records access rights management events** 
 (UseAdminEntitySchemaRecordRightLog) – specifies whether to log the changes to access permissions for object records.
 



 Type: Boolean. Default value: “False.”
 



**Log administrated entities management events** 
 (UseAdminEntitySchemaLog) – specifies whether to log the changes to permitted ways to manage objects.
 



 Type: Boolean. Default value: “False.”
 



**Log organizational structure management events** 
 (UseAdminUnitAdminLog) – specifies whether to log the creation, update, and deletion of the organizational structure elements (user “roles”).
 



 Type: Boolean. Default value: “False.”
 



**Log users management events** 
 (UseAdminUserLog) – specifies whether to log the creation, update, and deletion of system users.
 



 Type: Boolean. Default value: “False.”
 



 Business processes
--------------------



 Creatio can use custom business processes in place of the out-of-the-box business processes. The following system settings that determine whether custom or OOTB processes run in different circumstances.
 



**Process of adding invoice based on order** 
 (CreateInvoiceFromOrderProcess) – process that starts when selecting the
 
 Add invoice based on order
 
 action on the order page.
 



 Type: lookup. Default value: “The setting is available in all Creatio products containing the
 
 Invoices
 
 and
 
 Orders
 
 sections.”
 



**Process of adding order based on opportunity** 
 (CreateOrderFromOpportunityProcess) – process that starts when selecting the
 
 Add order based on opportunity
 
 action on the opportunity page.
 



 Type: lookup. Default value: “Add order based on opportunity.” The setting is available for Sales Creatio, enterprise edition, Sales Creatio, commerce edition and Creatio CRM bundle.
 



**Corporate sale process** 
 (OpportunityManagementProcess) – process that starts when selecting the
 
 Run corporate sales process
 
 action on the opportunity page.
 



 Type: lookup. Default value: “Corporate sale.” Available in all Creatio products containing the
 
 Opportunity
 
 section.
 



 Lock a user account
---------------------



 The settings below manage the user account locking criteria.
 



 Read more:
 [Unlock a user account](/docs/8-0/user/setup_and_administration/user_and_access_management/user_management/unblock_a_user_shortcut/unblock_a_user) 
 .
 



**Number of login attempts** 
 (LoginAttemptCount) – the number of permitted failed login attempts.
 



 Type: integer. Default value: “0.”
 



**Quantity of login attempts for warning message** 
 (LoginAttemptBeforeWarningCount) – the number of failed login attempts after which Creatio will warn the user their account may be locked.
 



 Type: integer. Default value: “0.”
 



**User locking time** 
 (UserLockoutDuration) – the user account lockout duration after a number of failed login attempts, in minutes.
 



 Type: integer. Default value: “15.”
 



 Approvals
-----------



**Send email message if approval is required** 
 (SendVisaEmail) – service setting, may be used by add-ons and connectors.
 



 Type: Boolean. Default value: “False.”
 



**Mailbox for sending email with information on approval** 
 (VisaMailboxSettings) – email account used to send the notifications about approvals. You can select any email account registered in the system.
 



 Type: lookup.
 



**Invoice approval process** 
 (InvoiceVisaProcess) – the business process that is launched when an invoice is sent for approval.
 



 Type: lookup. Default value: “Invoice approving.” Available in all Creatio products containing the
 
 Invoices
 
 section.
 



**Order approval process** 
 (OrderVisaProcess) – business process that launches when an order is sent for approval.
 



 Type: lookup. Default value: “Order approving.” Available in all Creatio products containing the
 
 Invoices
 
 section.
 



**Contract approval process** 
 (ContractVisaProcess) – business process that launches when a contract is sent for approval.
 



 Type: lookup. Default value: “Contract approval.” Available in all Creatio products containing the
 
 Contracts
 
 section.
 



**Email template for sending invoice approval information** 
 (InvoiceVisaEmailTemplate) – template for the email that is automatically sent to the approver user or user group when an invoice is submitted for approval. To add and edit templates, use the “Email message templates” lookup.
 



 Type: lookup. Default value: “Template of new invoice approval notification.” Available in all Creatio products containing the
 
 Invoices
 
 section.
 



**Email template for sending information about order approval** 
 (OrderVisaEmailTemplate) – template for the email that is automatically sent to the approver user or user group when an order is submitted for approval. To add and edit templates, use the “Email message templates” lookup.
 



 Type: lookup. Default value: “Template of new order approval notification.” Available in all Creatio products containing the
 
 Orders
 
 section.
 



**Email template for sending contract approval information** 
 (ContractVisaEmailTemplate) – template for an email that is automatically sent to the approver user or user group when a contract is submitted for approval. To add and edit templates, use the “Email message templates” lookup.
 



 Type: lookup. Default value: “Template of new contract approval notification.” Available in all Creatio products containing the
 
 Contracts
 
 section.
 



 Global Search
---------------



**Global search default entity weight** 
 (GlobalSearchDefaultEntityWeight) – increasing the display priority of the search results that display records of the section where the search was performed. For example, if you enter a search query from the
 
 Contacts
 
 section, the records of this section will appear first in the list.
 



**Global search default primary column weight** 
 (GlobalSearchDefaultPrimaryColumnWeight) – increasing the display priority of the specific search results. It applies to records, whose primary column value matches the search query (for example,
 
 Full name
 
 is a primary column for the contact and
 
 Name
 
 is a primary column for the account). If the search query matches the value in the primary column of the record, this record will be displayed at the top of the list of search results.
 



**Display search results with partial match** 
 (UseInexactGlobalSearch) – displaying search results taking morphology, typos and fuzzy matches into account.
 



 Type: Boolean. Default value: “False.”
 



**Match threshold for displaying in search results (percent)** 
 (GlobalSearchShouldMatchPercent) – enables managing the number of displayed search results with partial match. For this system setting, you can set an integer value from 0 to 100. The lower the value is – the more results with partial match are displayed. This will increase the chances of finding the needed data for inaccurate search requests.
 



 Process log
-------------



 Use the system settings listed below to manage the Process Log operations in Creatio. Read more:
 
[Process log](/docs/7-18/user/bpm_tools/business_process_administration/process_execution/view_process_execution_data) 

 . These system settings are grouped in a “Process log” folder in the
 
 System settings
 
 section.
 



**Allowed time for process instances in the "Error" state (days)** 
 (AllowedTimeForProcessInErrorState) – number of days during which the process instances in the “Error” state stay active in Creatio. After the specified time expires, these process instances will be canceled automatically.
 



 Default value: 20. If you set the value to “0,” the process instances in the “Error” state will not be canceled at all (the system setting will be disabled).
 





 Note.
 
 The “Allowed time for process instances in the "Error" state (days)” system settings lets Creatio clear the process log from the outdated process instances in the “Error” state.
 




**Archive data on deletion from log** 
 (ArchiveProcessLogOnDeletion) – whether to archive or delete data that is removed from the process log. Available in Creatio version 8.0.3 and later.
 



 Type: Boolean. Default value: “False.”
 





 Note.
 
 The default value is “True” for Creatio instances originally deployed as version 8.0.2 and earlier.
 




**Archive data expiration term (days)** 
 (ArchiveDataExpirationTerm) – all archived process instances that are older than the specified term will be deleted automatically.
 



 Default value: “90.” If you set the value to “0,” the archived process instances will not be deleted at all (the system setting will be disabled).
 



**Log data expiration period (days)** 
 (ProcessLogExpirationPeriod) – number of days after which a new process log record is archived.
 



 Type: integer. Default value: “30 days.”
 





 Note.
 
 In Creatio version 8.0.2 and earlier, use the
 **Process log archiving period (days)** 
 (ProcessLogArchivingPeriod) system setting that functions identically instead.
 




**Maximum time for the process log maintenance execution (minutes)** 
 (ProcessMaintenanceJobTimeout) – time limit for process log maintenance. If the log data cannot be processed within the specified time, the operation will be paused and renewed as soon as the maintenance process runs again.
 



**Frequency of running operations for process log maintenance (minutes)** 
 (ProcessMaintenanceJobFrequencyMinutes) – specifies how often Creatio runs the process log maintenance operations, in minutes.
 



 Type: integer. Default value: “5 minutes.”
 



 Applications
--------------



 These settings are available in Financial Services Creatio, lending edition, and Creatio CRM-bundle.
 



**Main participant role in application** 
 (MainParticipantRole) – the role of a transaction participant specified in the
 
 Client
 
 field.
 



 Type: lookup. Default value: Borrower.
 



**Main registration document type** 
 (MainRegDocumentType) – the primary identity document for a contact.
 



 Type: lookup. Default value: “National passport.”
 



 Values by default
-------------------



 The following settings are available in Creatio products that have the corresponding sections.
 



**Attachments and notes default icon** 
 (FileDetailDefaultIcon) – icon used in the tile view on the
 
 Attachments and notes
 
 detail for the files, whose type is not specified in the
 
 File extensions
 
 lookup.
 



 Type: lookup Default value: “default.”
 



**Default case source** 
 (CaseOriginDef) – case type in the
 
 Source
 
 field on the case page.
 



 Type: lookup Default value: “Call.”
 



**Default portal case source** 
 (PortalCaseOriginDef) – the type for cases created via the portal.
 



 Type: lookup Default value: “Call.”
 



**Document status by default** 
 (DocumentStatusDef) – default status for new documents.
 



 Type: lookup. Default value: “Planned.”
 



**Invoice payment status by default** 
 (InvoicePaymentStatusDef) – default payment status for new invoices.
 



 Type: lookup. Default value: “Not issued.”
 



**Order delivery status** 
 (OrderDeliveryStatusDef) – default status for a new order delivery.
 



 Type: lookup. Default value: “Planned.”
 



**Order payment status** 
 (OrderPaymentStatusDef) – default payment status for new orders.
 



 Type: lookup. Default value: “Planned.”
 



**Order status** 
 (OrderStatusDef) – default status for new orders.
 



 Type: lookup. Default value: “Planned.”
 



**Default unit of measure** 
 (DefaultUnit) – default unit of measure for a new product.
 



 Type: lookup. Default value: “pieces.”
 



**Project status by default** 
 (ProjectStateDef) – default status for new projects.
 



 Type: lookup. Default value: “Planned.”
 



**Default city for employees** 
 (EmployeeCityDef) - default city used to build up routes for field sales employees if the current location is not defined.
 



**Default change source** 
 (ChangeSourceDef) – default source for new changes.
 



 Type: lookup. Default value: “Project.”
 



**Default change category** 
 (ChangeCategoryDef) – default category for new changes.
 



 Type: lookup. Default value: “Normal.”
 



**Case closure code by default** 
 (CaseClosureCodeDef) – default code for closed cases.
 



 Type: lookup. Default value: “Resolved successfully.”
 



**Default change priority** 
 (ChangePriorityDef) – default priority for new changes.
 



 Type: lookup. Default value: “Average.”
 



**Case default priority** 
 (CasePriorityDef) – default priority for new cases.
 



 Type: lookup. Default value: “Average.”
 



**Default release priority** 
 (ReleasePriorityDef) – default priority for new releases.
 



 Type: lookup. Default value: “Average.”
 



**Default service agreement** 
 (DefaultServicePact) – base service agreement used for the calculation of response and resolution time, if the case SLA cannot be determined by the case contact or account.
 



 Type: lookup. Default value: “Service contract by default.”
 



**Default change status** 
 (ChangeStatusDef) – default status for new changes.
 



 Type: lookup. Default value: “New.”
 



**CI default status** 
 (ConfigurationItemStatusDef) – default status for new configuration items.
 



 Type: lookup. Default value: “Active.”
 



**Case default status** 
 (CaseStatusDef) – default status for new cases.
 



 Type: lookup. Default value: “New.”
 



**Default problem status** 
 (ProblemStatusDef) – default status for new problems.
 



 Type: lookup. Default value: “New.”
 



**Default release status** 
 (ReleaseStatusDef) – default status for new releases.
 



 Type: Lookup: Default value: “Planned.”
 



**Default service status** 
 (ServiceItemStatusDef) – default status for new services.
 



 Type: lookup. Default value: “Active.”
 



**Default service agreement status** 
 (ServicePactStatusDef) – default status for new service contracts.
 



 Type: lookup. Default status: “Active.”
 



**Time for case overdue check, minutes** 
 (CaseOverduesCheckTerm) – determines the frequency of Creatio checks if cases are overdue. In an overdue case, the date of planned reaction or planned resolution is less than the current date, while the date of actual reaction or the actual resolution is not specified. As a result, the checkbox is selected in the
 
 Reaction overdue
 
 or
 
 Resolution overdue
 
 column on the case page. The value is set in minutes.
 



 Type: integer. Default value: “2.”
 



**Default release type** 
 (ReleaseTypeDef) – default type for new releases.
 



 Type: lookup. Default value: “Minor.”
 



**Default service agreement type** 
 (ServicePactTypeDef) – default type for new service contracts.
 



 Type: lookup. Default value: “SLA.”
 



**Default support line for case** 
 (CaseServiceLevelDef) – default support level for new cases.
 



 Type: lookup. Default value: “1st line.”
 



**Default change goal** 
 (ChangePurposeDef) – default purpose for new changes.
 



 Type: lookup. Default value: “Standard changes.”
 



**Base price list** 
 (BasePriceList) – price list that determines the product price.
 



 Type: lookup. Default value: “Base.”
 



 Integration with external resources
-------------------------------------



 The “Integration with external resources” system setting group is used to register Creatio for integration with
 
social networks

 and
 
[Google](https://academy.creatio.com/docs/user/setup_and_administration/base_integrations/google_mail_contacts_and_calendar) 

 . Three system settings are used for each registration:
 


* **Application registration page** 
 (FacebookRegistrationPage, GoogleRegistrationPage, TwitterRegistrationPage) – the address of the integrated external resource. For instance, “https://code.google.com/apis/console/.”
* **Key** 
 (FacebookConsumerKey, FacebookConsumerSecret, GoogleConsumerKey, GoogleConsumerSecret, etc.).
* **Secret key** 
 (FacebookConsumerSecret, GoogleConsumerSecret, TwitterConsumerSecret).



 The procedure of obtaining values for the “Access Key” and “Secret Access Key” system settings of this folder is explained when describing the procedure of signing up the application to social networks and Google.
 



 Configuration
---------------



**Repository URI by default** 
 (DefRepositoryUri) – path to the package repository that is used in the system by default. The default path is used if the path to the package repository has not been specified.
 



 Type: text (500 characters).
 



**Base lookup card page** 
 (DefLookupEditPageSchemaUId) – used for lookup registration. This system setting determines the page to be used as a base page for cards of standard lookups.
 



 Type: lookup. Default value: “Base lookup card page.”
 



**Base lookup card page** 
 (DefLookupGridPageSchemaUId) – base page used to display lists of records in standard lookups, as well as to open a window for any lookup in the system. The page is used for registering Creatio lookups.
 



 Type: lookup. Default value: Lookup page.
 





 Note.
 
 Lookups are registered in the
 
[Lookups](/docs/8-0/user/setup_and_administration/system_settings_and_lookups/create_a_lookup/create_new_lookups) 

 section.
 




**Current package** 
 (CurrentPackageId) – package that contains all changes made via the Section Wizard. These can be, for example, changes associated with adding columns to the section object or adding a new section to the system.
 



 Type: lookup. The “Custom” package is set as the current package by default. To migrate configuration settings made in the Section Wizard to another application, make sure you change the value of this system setting. Select the package to save your configuration changes in the
 
 Value by Default
 
 field (this package can later be exported and installed on a new application).
 



**Mobile application manifest** 
 (MobileApplicationManifest) –name of the XML file that contains the configuration of the mobile application. If multiple manifests are specified, their names are separated with the semicolon “;” symbol.
 



 Type: text (50 characters).
 



**Package repository path** 
 (UpdateRepositoryUri) – path to a repository folder that contains updated base packages. Use this system setting to update the application version. The value of this system setting is provided by the support service.
 



 Type: text (500 characters).
 



**Display C# compiler warnings when publishing configuration** 
 (CodeCompilerWarningLevel) – level of C# compiler warnings that will be displayed when compiling workspace files. The values can range from “0” to “4,” where “0” – do not display warnings, “1” – display the most important warnings, etc., in ascending order.
 



 Type: integer. Default value: “2.”
 



**Publisher** 
 (Maintainer) – used to identify a party that makes changes to the configuration. The publisher name is assigned to each package separately. You can edit only packages that have been published by your company. The setting is used for developing user workspaces for the third parties.
 



 Type: text (250 characters).
 



**Maximum quantity of data strings to be bound to package** 
 (MaxPackageSchemaDataRowsCount) – if the number of the bound records reaches the system setting value when binding the data to the package, the corresponding message will be displayed and the data binding should be confirmed.
 



 Type: integer. Default value: “100.”
 





 Note.
 
 Binding large volumes of records to a package can take a long time.
 




**Prefix for object name** 
 (SchemaNamePrefix) – sets the required prefix in the custom objects' names. This prefix makes it easier to find the custom configuration elements if you need to change these elements or move their data. Creatio adds the prefix to new configuration objects in the section wizard, detail wizard, and the
 
 Configuration
 
 section (Creatio IDE). For example, you can change the default prefix to the company acronym. The prefix name supports uppercase and lowercase Latin characters. You can also add numbers to the prefix, but the prefix cannot consist of numbers alone and it cannot start with a number.
 



 Type: text (50 characters). Default value: “Usr.”
 



**Calendar start time** 
 (SchedulerDisplayTimingStart) – the
 
 Calendar
 
 view of the
 
 Activities
 
 section will scroll to this time when loaded. The setting uses the 24-hour format, from 0 to 24. For example, specify “8” for “8:00 AM.”
 



**Calendar start date** 
 (SchedulerTimingStart) – the start date for the period in the
 
 Calendar
 
 view of the
 
 Activities
 
 section. The setting uses the 24-hour format, from 0 to 24. For example, set the period start to 7:00 AM instead of 12:00 AM by specifying “7” in the setting.
 



 Type: integer. Default value: “0.”
 



**Calendar end date** 
 (SchedulerTimingEnd) – the end date for the period in the
 
 Calendar
 
 view of the
 
 Activities
 
 section. The setting uses the 24-hour format, from 0 to 24. For example, set the period end to 6:00 PM instead of 12:00 AM by specifying “18” in the setting.
 



 Type: integer. Default value: “24.”
 



**Default main page** 
 (DefaultIntroPage) – the display schema for the main Creatio page. Specifies the page that opens when loading Creatio. Set the available values in the
 
 IntroPageUId
 
 field of the “ApplicationMainMenu” object.
 



 Type: lookup. The default value depends on the Creatio product.
 



**BuildType** 
 (BuildType) – the build type (“Softkey” or “Demo”).
 



 Type: lookup. Default value: “Softkey.”
 



**Debug mode** 
 (IsDebug) – enables the debug mode that helps you to locate, isolate, and solve Creatio configuration issues.
 



 Type: Boolean. Default value: “False.”
 



**Default form page in the Freedom UI shell** 
 (EditPagesUITypeForFreedomHost) – whether to use Classic UI or Freedom UI form pages in the Freedom UI by default. You can specify exceptions for specific objects in the
 
 Object-specific form page interface in the Freedom and Classic UI shell
 
 lookup.
 



 Type: lookup. Default value: “Freedom UI pages.”
 



**Default form page in the Classic UI shell** 
 (EditPagesUITypeForEXTHost) – whether to use Classic UI or Freedom UI form pages in the Classic UI by default. You can specify exceptions for specific objects in the
 
 Object-specific form page interface in the Freedom and Classic UI shell
 
 lookup.
 



 Type: lookup. Default value: “Classic UI pages.”
 





 Note.
 
 If the object has both form pages, Freedom UI sections always open Freedom UI form pages when you add, view, edit, or copy a record.
 




 Mobile application
--------------------



 Settings are available in Creatio enterprise and Creatio CRM-bundle.
 



**Check-in verification range** 
 (CheckInRadius) – a distance that is the allowable discrepancy (in meters) between the coordinates of the employee and the actual coordinates of the check-in. Specified distance will be used for check-in verification.
 



**Use last known location of user** 
 (UseMobileLastKnownLocation) – a system setting enabling a mobile device to use the latest cached employee's location and save it as check-in location if the actual check-in coordinates are unknown.
 



 Type: Boolean. Default value: “True.”
 



 Email section settings
------------------------



 The following settings are available in the Creatio products containing Marketing Creatio.
 



**Turn on logging for webhooks** 
 (EnableWebHooksLogging) – specifies whether to log recipient responses in Creatio. The log4net tool is used for logging. The log can be used by developers for debugging.
 



 Type: Boolean. Default value: “False.”
 



**App external URL that is used to receive webhooks** 
 (WebhooksApplicationUrl) – URL for receiving responses from the bulk email recipients (must be accessible from the Internet). The value of the system setting is specified, if during the system installation, the traffic routing has been configured using the firewall. Type: text (500 characters).
 



**App external URL used for bulk email unsubscribe queries** 
 (UnsubscribeApplicationUrl) – URL for receiving requests to unsubscribe from bulk emails (must be accessible from the Internet). When unsubscribing, a parameter with the key value that is used to unsubscribe is added to this address. For example, if the value of the system setting is “http://www.site.com/unsubscribe,” the actual unsubscribe link is “http://www.site.com/unsubscribe?key=0123456789.” The system setting value is specified, if during the system installation, the traffic routing has been configured using the firewall.
 



 Type: text (500 characters).
 



**Interval for stats collection in bulk email, hrs** 
 (BulkEmailHourlyStatisticPeriod) – period displayed in the Opens/clicks chart of the
 
 Email totals
 
 tab on the bulk email page. Specified in hours.
 



 Type: integer. Default value: “48.”
 



**Test email recipient** 
 (TestSendingBulkEmailContact) – contact, whose data will be substituted in the test emails as values for macros when running the
 
 Send test email
 
 action of the
 
 Email
 
 section.
 



 Type: lookup.
 



**Unsubscribe user from all bulk email** 
 (UnsubscribeFromAllMailings) – specifies whether to select the
 
 Do not use Email
 
 checkbox automatically for the contacts who have unsubscribed from bulk email.
 



 Type: Boolean. Default value: “True.”
 



**Time period (days) to update bulk emails statistics** 
 (MandrillStatisticUpdatePeriodDays) – the period during which the final response is recorded for each contact who participated in a bulk email. Any responses received from the contacts after the period is over will not affect the bulk email statistics. The value is specified in days.
 



 Type: integer. Default value: “30.”
 



**Website to redirect the unsubscribed** 
 (RedirectUnsuscribersTo) – URL, where users are redirected automatically, after they unsubscribe from a bulk email.
 



 Type: text (500 characters).
 



**Check interval for bulk email with "In progress" status, min** 
 (MandrillShedulerTimeStep) – determines how often Creatio checks whether all due bulk emails have been launched. The value of the system setting is specified in minutes.
 



 Type: integer. Default value: “1.”
 



**“Domains list" field default name in Email** 
 (GoogleAnalyticsTrackingDomains) – a list of URLs, whose statistics will be tracked with Google Analytics.
 



 The values are entered separated by commas. Type: text (250 characters).
 



**Enable option "System email”** 
 (SystemEmailIgnoreUnsubscribeFromAllMailings) – used to show/hide the
 
 System email
 
 checkbox on the
 
 Parameters
 
 tab of the bulk email page. This checkbox enables using bulk emails to send “system emails” – non-marketing notifications. System emails ignore the
 
 Do not use email
 
 checkbox value on the contact's
 
 Communication channels
 
 tab.
 



 Type: Boolean. Default value: “True.”
 



**Prevent to send duplicated emails to recipients with the same address** 
 (PreventDuplicatesSending) – if enabled, Creatio will identify duplicate email addresses in bulk email audiences and will send only one email per unique address. The contact for whom the email will be personalized is selected randomly among those with duplicate email addresses.
 



 Type: Boolean. Default value: “False.”
 



 Cases
-------



 The system settings are available in Service Creatio, customer center edition, Service Creatio, enterprise edition, Financial Services Creatio, bank customer journey edition, and Creatio CRM bundle.
 



**1st-line support** 
 (FirstSupportLine) – a user group that corresponds to the “1st-line support” value of the “Service team member roles” lookup. Used in the incident management process in case of incident escalation.
 



 Type: lookup. Default value: “1st-line support.”
 



**2nd-line support** 
 (SecondSupportLine) – a user group that corresponds to the “2nd-line support” value of the “Service team member roles” lookup. Used in the incident management process in case of incident escalation.
 



 Type: lookup. Default value: “2nd-line support.”
 



**3rd-line support** 
 (ThirdSupportLine) – a user group that corresponds to the “3rd-line support” value of the “Service team member roles” lookup. Used in the incident management process in case of incident escalation.
 



 Type: lookup. Default value: “3rd-line support.”
 



**Automatically create new contacts for unknown email addresses** 
 (CreateNewContactsForUnknownEmailAddresses) – manages creating new contacts when registering a case from an unknown email.
 



 Type: Boolean. Default value: “True.”
 



**Number of waiting days to reevaluate resolved case** 
 (FirstReevaluationWaitingDays) – after a case is resolved and the case evaluation email is sent, Creatio will wait for the customer to evaluate the case within the specified period before sending a second reminder.
 



 Type: integer. Default value: “1.”
 



**Number of waiting days after second reminder of resolved case** 
 (SecondReevaluationWaitingDays) – after a second case evaluation email, Creatio will wait for the specified number of days before closing the case.
 



 Type: integer. Default value: “1.”
 



**Automatically close resolved cases** 
 (CloseResolvedCases) — if enabled, Creatio will close resolved cases automatically after the evaluation waiting period specified in the “Number of waiting days to reevaluate resolved case” and “Number of waiting days after the second reminder of resolved case” system settings ends.
 



 Type: boolean. Default value: “True.”
 



 General
---------



**Base personal calendar** 
 (BaseUserCalendar) – sets the default calendar.
 


* The default calendar is used in Service Creatio, customer center edition and Financial Services Creatio, bank customer journey edition if another calendar is not specified on the service page.
* The default calendar is used in Service Creatio, enterprise edition if another calendar is not specified on the service page in the service agreement or on the service agreement page.



 Type: lookup. Default value: “Default calendar.”
 



**Configuration version** 
 (ConfigurationVersion) – the current workspace version.
 



 Type: text (50 characters).
 



**Caption for communication options block on login page** 
 (LoginPageCommunicationBlockCaption) – caption for the login page block that contains the communication options.
 



 Type: text (50 characters).
 



**Caption for useful links block on login page** 
 (LoginPageLinksBlockCaption) – caption for the login page block that contains the links.
 



 Type: text (50 characters).
 



**Notification monitor** 
 (RemindingsCheckInterval) – frequency of checking for new Creatio notifications. The value of this system setting is specified in milliseconds (ms).
 



 Type: integer. Default value: “300000 ms” (5 minutes).
 



**Number of records in Excel export batch** 
 (ExcelExportBatchSize) – changing this value affects the speed of exporting large numbers of records to Excel and the amount of memory used.
 



**Logo** 
 (LogoImage) – logo displayed on the login page. Creatio logo is displayed by default, but you can upload a different image. PNG is the recommended image format.
 



 Type: image.
 



**Upper panel logo** 
 (HeaderLogoImage) – image that will be displayed at the top of Creatio pages. Creatio logo is displayed by default, but you can upload a different image. PNG is the recommended image format.
 



 Type: image.
 



**Logo in main menu** 
 (MenuLogoImage) – image that will display at the top of the Creatio main menu page (opens by default upon first login). Creatio logo is displayed by default, but you can upload a different image. PNG is the recommended image format.
 



 Type: image.
 



**Product name** 
 (ProductName) – header of the browser tab with the opened Creatio application.
 



 Type: text (250 characters). Default value: “Creatio.”
 



**Domain to redirect** 
 (DomainToRedirect) – the URL where users are redirected automatically after they open the website in a browser.
 



 Type: text (250 characters).
 



**Case email body maximum length** 
 (EmailBodyForCaseMaxLength) – maximum number of characters from email, that will be displayed in the
 
 Description
 
 field of the case, created automatically from that email.
 



 Type: integer. Default value: “600 characters.”
 




**Maximum number of records to import from Excel** 
 (MaxImportExcelRecordCount) – maximum number of records that can be imported from an Excel file.
 



 Type: integer. Default value: “2000.”
 




**Maximum number of process item repetitions** 
 (MaxProcessLoopCount) – maximum number of times the same process item can be run during a process.
 



 Type: integer. Default value: “100.”
 



**Attachment max size** 
 (MaxFileSize) – maximum size of a file that can be added to the
 
 Attachments and notes
 
 detail in Creatio sections. The value of this system setting is specified in megabytes (MB).
 



 Type: integer. Default value: “10 MB.”
 



**Minimum characters necessary to filter list** 
 (StringColumnSearchMinCharCount) – minimum number of characters sufficient to filter records in the drop-down list of the “lookup” field. When you type the needed value directly in the lookup field (without opening the lookup), a drop-down list opens, containing the values that match the characters entered. The minimum number of characters sufficient to display the drop-down list is defined by this system setting.
 



 Type: integer. Default value: “3.”
 



**Display pop-up window message** 
 (ShowBrowserPopupWindowToolbars) – used to manage the display of browser toolbars in the Creatio pop-up windows. In Creatio, pop-up windows are used in system setup window to open designers, pages, lookup windows, etc.
 



 Type: Boolean. Default value: “False.”
 



**String columns filter** 
 (StringColumnSearchComparisonType) – the type of search operator used to filter records of the “lookup” field.
 



 Type: integer. Default value: “1.” The setting can have one of two values:
 


* “0” – searched record must begin with the specified string.
* “1” – searched record must contain the specified string.



**Emails to connect our technical support** 
 (SupportEmailDef) – the recipient addresses for emails sent via the
 
 Need help
 
 action on the communication panel. For example, specify the internal support service email. Separate the emails with semicolons.
 



 Type: text (50 characters). Default value: “support@creatio.com.”
 



 Send emails
-------------



 The system settings are available in Service Creatio, customer center edition, Financial Services Creatio, bank customer journey edition calendar, and Creatio CRM bundle.
 



**Customer service email** 
 (SupportServiceEmail) – email address that receives automatic notifications of new cases created on the self-service portal. It is also used to send notifications to customers about the status of their case.
 



 Type: text (250 characters).
 



**Website Url** 
 (SiteUrl) – the addres of the Creatio instance, formatted as https://yoursite.domain.com/0. Creatio uses it:
 


* To redirect the user to the relevant web page after they provide feedback on the case service quality.
* To synchronize with Telegram when adding a chat.



 Type: text (250 characters).
 



**SMTP server login** 
 (SmtpUserName) – full email address used to send customer notifications about case statuses.
 



 Type: Unlimited length string.
 



**SSP registration mail box** 
 (SSPRegistrationMailbox) – email address used to send notifications about self-service portal registration.
 



 Type: lookup.
 



**SMTP server password** 
 (SmtpUserPassword) – password of the email specified in the
 
 SMTP server login
 
 system setting.
 



 Type: Unlimited length string.
 



**SMTP server name or IP** 
 (SmtpHost) – SMTP server coordinates used to send the outgoing emails. To populate this setting, please see your mail provider's documentation.
 



 Type: Unlimited length string.
 



**SMTP server port** 
 (SmtpPort) – SMTP server port used to send emails. To populate this setting, please see your mail provider's documentation.
 



 Type: integer.
 



**Use SSL** 
 (SmtpEnableSsl) – used for the support of the Secure Sockets Layer protocol. For more information on using SSL protocol please see your mail provider's documentation.
 



 Type: Boolean.
 



**Logo - Feedback value not found** 
 (ImageRaitingNotFound) – sets the logo on the web page that opens after a user evaluates the quality of service. The logo is displayed if the settings of the rating range are incorrect. Standard logo is displayed by default, but you can upload a custom one. PNG is the recommended image format.
 



 Type: image.
 



**Logo - Case not found** 
 (ImageCaseNotFound) – sets the logo on the web page that opens after a user evaluates the quality of service. The logo is displayed if the case number is invalid or if the case was deleted. Standard logo is displayed by default, but you can upload a custom one. PNG is the recommended image format.
 



 Type: image.
 



**Logo - Feedback has been already received** 
 (ImageRaitingAlredyExist) – sets the logo on the web page that opens after a user evaluates the quality of service. The logo is displayed if the case is closed or if the case
 
 Rating
 
 field is already populated. Standard logo is displayed by default, but you can upload a custom one. PNG is the recommended image format.
 



 Type: image.
 



**Logo - Thank you for your feedback** 
 (ImageThanksForRaiting) – sets the logo on the web page that opens after a user evaluates the quality of service. PNG is the recommended image format.
 



 Type: image.
 



 Duplicate search
------------------



**Date of last duplicate search by contacts** 
 (LastContactDuplicatesSearch) – date and time of the last search for duplicate records in the
 
 Contacts
 
 section.
 



 Type: date/time.
 



**Date of last duplicate search by accounts** 
 (LastAccountDuplicatesSearch) – date and time of the last search for duplicate records in the
 
 Accounts
 
 section.
 



 Type: date/time.
 



 LDAP synchronization
----------------------



 The settings in this group are used to synchronize users with the LDAP server.
 





 Attention.
 
 We recommend that you use the LDAP synchronization setup window for
 
[LDAP synchronization setup](https://academy.creatio.com/documents?id=513) 

 .
 



### 
 Licenses during the LDAP synchronization



**License packages for LDAP user** 
 (LdapUserLicPackages) – licenses that will be granted to users created upon LDAP synchronization. If the system setting is not filled out, the users will be provided with all licenses. The values are entered separated by semicolons.
 



 Type: text.
 


### 
 LDAP connection settings



**LDAP server name or IP** 
 (LDAPServer) – address used to connect to the LDAP server.
 



 Type: text (50 characters).
 



**LDAP authentication type** 
 (LDAPAuthType) – authentication type that is used when authorizing the LDAP users. For example, Ntlm, Anonymous, Basic, etc.
 



 Type: lookup.
 



**LDAP server user login** 
 (LDAPServerLogin) – user login for connecting to the LDAP server. For example, it could be the system administrator domain name.
 



 Type: text (50 characters).
 



**LDAP server user password** 
 (LDAPServerPassword) – user password for connecting to the LDAP server. For example, the system administrator's domain password. The password data is encrypted.
 



 Type: encrypted string.
 


### 
 User synchronization settings



**Name of attribute containing LDAP user full name** 
 (LDAPUserFullNameAttribute) – an attribute of entry in the LDAP directory that contains the full name of a user. For example, this can be the “name” attribute.
 



 Type: text (50 characters).
 



**Name of attribute containing LDAP user login** 
 (LDAPUserLoginAttribute)– an attribute of entry in the LDAP directory that contains the domain login of a user. For example, “AccountName.”
 



 Type: text (50 characters).
 



**Name of attribute to identify LDAP user** 
 (LDAPUserIdentityAttribute) – any attribute of entry in the LDAP directory, whose value is unique for each entry. The value of this attribute is used as a unique identifier of records, when synchronizing users. For example, in Active Directory it could be “objectSid.”
 



 Type: text (50 characters).
 



**LDAP entry, which contains list of LDAP users** 
 (LDAPUsersEntry) – unique name (distinguishedName, DN) of an entry in the LDAP directory organization structure (folders, groups, etc) that contains user-type entries. For example, “CN=Users,DC=example,DC=com.” If the directory contains a number of such entries, specify the unique name of their mutual parent entry. Type: text (50 characters).
 



**Condition to form list of LDAP users** 
 (LDAPUsersFilter) – filter used to select LDAP entries for user synchronization. For example, for Active Directory this filter expression can be as follows:
 




 “(&(objectClass=user)(objectClass=person)(!objectClass=computer)(!userAccountControl:1.2.840.113556.1.4.803:=2)).”
 




 Type: text (50 characters).
 



**Name of attribute containing LDAP current employment** 
 (LDAPUserCompanyAttribute) – an attribute of entry in the LDAP directory that contains the place of work of the user. Used when importing users from LDAP to automatically fill in the
 
 Account
 
 field in the contact page.
 



 Type: text (250 characters).
 



**Name of attribute containing LDAP user email** 
 (LDAPUserEmailAttribute) – an attribute of entry in the LDAP directory that contains the email of the user. Used when importing users from LDAP directory to automatically fill in the
 
 Email
 
 field on the contact page.
 



 Type: text (250 characters).
 



**Name of attribute containing LDAP user phone number** 
 (LDAPUserPhoneAttribute) – an attribute of entry in the LDAP directory that contains the phone number of the user. Used when importing users from LDAP directory to automatically fill in the
 
 Business phone
 
 field in the contact page.
 



 Type: text (250 characters).
 



**Name of attribute containing LDAP user job title** 
 (LDAPUserJobTitleAttribute) – an attribute of entry in the LDAP directory that contains the job title of the user. Used when importing users from LDAP directory to automatically fill in the
 
 Job title
 
 field in the contact page.
 



 Type: text (250 characters).
 


### 
 Folder synchronization settings



**Name of attribute containing LDAP group name** 
 (LDAPGroupNameAttribute) – an attribute of entry in the LDAP directory that contains the name of the user group. For example, the “cn” attribute in Active Directory.
 



 Type: text (50 characters).
 



**Name of attribute to identify LDAP group** 
 (LDAPGroupIdentityAttribute) – an attribute of entry in the LDAP directory whose value is unique for all entries. The value of this attribute is used as a unique identifier of records, when synchronizing groups. For example, in Active Directory it could be “objectSid.”
 



 Type: text (50 characters).
 



**LDAP entry containing list of LDAP groups** 
 (LDAPGroupsEntry) – unique name (distinguishedName, DN) of an organization structure item in the LDAP directory containing user group entries. For example, “CN=Groups,DC=example,DC=com.” If the directory contains a number of such entries, specify the unique name of their mutual parent entry.
 



 Type: text (50 characters).
 



**Condition to form list of LDAP groups** 
 (LDAPGroupsFilter) – filter used to select LDAP entries for group synchronization. For example, for Active Directory this filter expression can be as follows:
 




 “(&(objectClass=group)(!userAccountControl:1.2.840.113556.1.4.803:=2))”
 




 Type: text (50 characters).
 



**Condition to form list of LDAP users in group** 
 (LDAPUsersInGroupFilter) – search filter that determines what users belong to which groups. Use the following variables to specify filter parameters:
 


* #LDAPGroupDN# – unique name (Distinguished Name) of the group being searched;
* #LDAPGroupName# – name of the group. This variable will contain the value specified in the Group name field in the synchronization setup window;
* #LDAPGroupIdentity# – unique id of the searched folder. The variable will contain the value of the attribute specified in the Unique identifier of group field of the LDAP synchronization setup window.



 Type: text (50 characters).
 


### 
 Additional LDAP synchronization settings



**Name of attribute containing LDAP entry modification date** 
 (LDAPEntryModifiedOnAttribute) – an attribute of entry in the LDAP directory, which contains the date and time of the last modification of the entry in the “generalized time” format. Used for identifying new users in the LDAP group during the synchronization.
 



 Type: text (50 characters). Default value: “whenChanged.”
 



**LDAP synchronization interval, hours** 
 (LDAPSynchInterval) – time between LDAP synchronization sessions, specified in hours.
 



 Type: integer. Default value: “1.”
 



**Date of last synchronization with LDAP** 
 – date and time of the last synchronization session. The value of this system setting is updated automatically. It is not recommended to edit it manually. This system setting is used for the automatic LDAP synchronization.
 



 Type: date/time.
 



 Phone
-------



**Default message exchange library** 
 (SysMsgLib) – the telephony integration library used by default.
 



 Type: lookup.
 



**Close telephony connection on logout** 
 (CloseTelephonyConnectionOnLogout) – balances the load on telephony. If turned on, users will be automatically logged out of the telephony agent when logging out of Creatio, freeing the line and the workplace for other employees.
 



 Type: Boolean. Default value: “False.”
 



 Managing passwords
--------------------



**Show message about locking account during logging in** 
 (DisplayAccountLockoutMessageAtLogin),
 **Show message about incorrect password during logging in** 
 (DisplayIncorrectPasswordMessageAtLogin) – the settings manage the message displayed if a user enters an incorrect username or password. The displayed message depends on both settings.
 



 Type: Boolean. Default value: “False.”
 



 If the “false” value is set for both settings, then when entering an incorrect password or username, the standard message is displayed: “Either invalid username or password specified, or your user account is inactive.”
 



 If the “on” value is set for both settings:
 


* If a user enters an incorrect username, the message will be “You have entered incorrect username.”
* If a user enters an incorrect password, the message will be “You have entered incorrect password.”
* If a locked user tries to authorize to the system, the message will be “Your user account is locked.”



 If only the “Show message about locking account during logging in” setting is on:
 


* If a user enters an incorrect username or password, the message will be “You have entered incorrect username or password.”
* If a locked user tries to authorize to the system, the message will be “Your user account is locked.”



 If only the “Show message about incorrect password during logging in” system setting is on:
 


* If a user enters an incorrect username, the message will be “You have entered incorrect username or your user account is locked.”
* If a user enters an incorrect password, the message will be “You have entered incorrect password.”
* If a locked user tries to authorize to the system, the message will be “You have entered incorrect username or your user account is locked.”



**Quantity of login attempts for warning message** 
 (LoginAttemptBeforeWarningCount) – number of failed attempts to enter the password before displaying the message about the number of remaining attempts before the user account is locked. If the “0” value is set for the system setting, the message is not displayed.
 



 Type: integer. Default value: “0.”
 



**Number of login attempts** 
 (LoginAttemptCount) – number of unsuccessful attempts to enter the correct password. If the number of login attempts exceeds specified threshold, the user account will be locked for the period specified in the “User locking time” (UserLockoutDuration) system setting. If the “0” value is set for the system setting, the number of attempts is unlimited.
 



 Type: integer. Default value: “0.”
 



**Password validity term, days** 
 (MaxPasswordAge) – number of days since the password was created or edited after which the user must change the password. The password is changed when logging in to the system. If the “0” value is set for the system setting, the password never expires.
 



 Type: integer. Default value: “0.”
 



**Reminder about password change, days** 
 (PasswordChangeReminding) – number of days remaining before the password expires. If there remains the specified number of days or fewer days, Creatio displays a corresponding message upon the login attempt and suggests opening the password change page. If the “0” value is set for the system setting, the message is not displayed.
 



 Type: integer. Default value: “0.”
 



**Quantity of analyzed passwords** 
 (PasswordHistoryRecordCount) – number of previous user passwords. Note that the new password must not match any of the previous passwords. When you enter a password that matches one of the previous passwords, Creatio will display the number of previous passwords that must not match the new password. Once the password is changed, the previous password will be saved in Creatio. If the “0” value is set for the system setting, the new password can be identical to the previous one.
 



 Type: integer. Default value: “0.”
 



**User locking time** 
 (UserLockoutDuration) – time period (in minutes) during which the user will not be allowed to log in to the system once the number of failed attempts to enter the password exceeds the set threshold. If the “0” value is set for the system setting, the user will not be locked.
 



 Type: integer. Default value: “0.”
 



 Password strength settings set the requirements that must be met by new passwords. The following settings define these requirements:
 


* **Password complexity: Minimum length** 
 (MinPasswordLength) – minimum number of characters in the password.
 



 Type: integer. Default value: “0.”
* **Password complexity: Minimum quantity of lower case characters** 
 (MinPasswordLowercaseCharCount) – minimum number of lowercase letters in the password.
 



 Type: integer. Default value: “0.”
* **Password complexity: Minimum quantity of upper case characters** 
 (MinPasswordUppercaseCharCount) – minimum number of uppercase letters in the password.
 



 Type: integer. Default value: “0.”
* **Password complexity: Minimum quantity of digits** 
 (MinPasswordNumericCharCount) – minimum number of digits in the password.
 



 Type: integer. Default value: “0.”
* **Password complexity: Minimum quantity of special characters** 
 (MinPasswordSpecialCharCount) – minimum number of special symbols that are not letters or digits (#, %, &, !, ?, etc.) .
 



 Default value: “0.”



 Manage files
--------------



 Use the settings below to manage restrictions for uploading third-party files to Creatio.
 



**File Security Mode** 
 (FileSecurityMode) – method of restricting the upload of third-party files to the application.
 



 Type: lookup Default value: “File extensions DenyList.”
 



**File extensions DenyList** 
 (FileExtensionsDenyList) – a list of potentially malicious files prohibited for uploading to Creatio. The list of extensions is separated by commas, without blank spaces.
 



 Type: text. Default value:
 






```

“ade,adp,apk,app,appx,appxbundle,asp,aspx,asx,bas,bat,bin,cab,cer,chm,cmd,cnt,com,command,conf,cpl,crt,csh,der,diagcab,dll,dmg,elf,exe,fxp,gadget,grp,hlp,hpj,hta,htc,html,inf,inf1,ins,inx,ipa,iso,isp,isu,its,jar,jnlp,job,js,jse,ksh,lib,lnk,mad,maf,mag,mam,maq,mar,mas,mat,mau,mav,maw,mcf,mda,mdb,mde,mdt,mdw,mdz,msc,msh,msh1,msh1xml,msh2,msh2xml,mshxml,msi,msix,msixbundle,msp,mst,msu,nsh,ops,osd,osx,out,paf,pcd,pif,pl,plg,prf,prg,printerexport,ps1,ps1xml,ps2,ps2xml,psc1,psc2,psd1,psdm1,pst,py,pyc,pyo,pyw,pyz,pyzw,rb,reg,rgs,run,scf,scr,sct,sh,shb,shs,sys,theme,tmp,u3p,url,vb,vbe,vbp,vbs,vbscript,vhd,vhdx,vsmacros,vsw,vxd,webpnp,website,workflow,ws,wsc,wsf,wsh,xbap,xll,xnk,xml.”
```





**File extensions AllowList** 
 (FileExtensionsAllowList) – list of file extensions most frequently used by company employees and allowed for uploading to Creatio. The list of extensions are entered separated by commas, without blank spaces.
 



 Type: text. Default value:
 






```

“doc,docx,rtf,odt,pages,pdf,xls,xlsx,xlsm,xlsb,csv,ods,ppt,pptx,ppsx,txt,log,json,md,config,zip,rar,7z,gz,pjp,pjpeg,jfif,webp,tif,bmp,png,jpeg,jpg,gif,ico,xbm,dib,emz,jfif,heic,ai,eps,jpe,cod,ief,ras,cmx,pnm,pbm,pgm,ppm,rgb,xpm,xwd,mp3,wav,mp4,mov,wmv,bpmn,frx,msg,vcf,ics,p7s,p7m,wmz,mso,dwg,mpp,step,vsd,vsdx,psd,gbt,prn,stp,rdp,dtf.”
```





**Allow processing files of unknown type** 
 (AllowFilesWithUnknownType) – rules of system behavior when uploading files of unknown type. The file types are defined by the extension. If the extension is not specified, the type is defined by the file content.
 



 Type: Boolean. Default value: “True.”
 



**Active file content storage** 
 (ActiveFileContentStorage) – determines where to store the content uploaded to Creatio. You can connect external, e. g. cloud, storage to Creatio via the file API and place the content there. This will allow you to reduce the Creatio database size without introducing file restrictions. Once you register the new storage in the
 
 File content storages
 
 lookup, you will be able to select this location in the system setting's
 
 Default value
 
 field. If you change the active storage, the content added prior to the change will remain in its original location.
 



 Type: Lookup: Default value: “Database.”
 



 Junk case filter
------------------



 The system settings are available in Service Creatio, customer center edition, Service Creatio, enterprise edition, Financial Services Creatio, bank customer journey edition, and Creatio CRM bundle.
 



**Create Cases From Junk Emails** 
 (CreateCasesFromJunkEmails) – manages creating cases by emails from the addresses and domains specified in the
 
 Blacklist of email addresses and domains for case registration
 
 lookup.
 



 Type: Boolean. Default value: “False.”
 



**Junk case default status** 
 (JunkCaseDefaultStatus) – default status for cases registered by emails and domains specified in the
 
 Blacklist of email addresses and domains for case registration
 
 lookup.
 



 Type: lookup. Default value: “Canceled.”
 



 Finances
----------



**Base currency** 
 (PrimaryCurrency) – base currency used for financial calculations in Creatio.
 



 Type: lookup. Default value: “US Dollar.”
 



**Tax by default** 
 (DefaultTax) – default tax to use when adding a product.
 



 Type: lookup. Default value: “VAT.” The system setting is available for Sales Creatio products.
 



**Price includes tax** 
 (PriceWithTaxes) – taxation method used when calculating product cost.
 



 Type: Boolean. Default value: “True.” The system setting is available for Sales Creatio products and the CRM bundle lineup.
 



 Chats
-------



**Omni chat notification sound** 
 (OmniChatNotificationSound) – the notification alert for new chat messages.
 



 Type: BLOB.
 



**Simultaneous chats** 
 (SimultaneousChats) – the number of active chats an agent can process simultaneously. If an agent has a maximum number of chats in progress, they will not see any new chats until they terminate at least one of their chats. This restriction is valid for all chat channels available to the agent.
 



 Type: integer. Default value: “5.”
 



**Omni chat operator accept chat timeout** 
 (OmniChatOperatorAcceptChatTimeout) – the period for an agent to take the chat, in minutes. If the agent does not take the chat within this period, the chat will be assigned to the next agent.
 



 Type: integer. Default value: “5.”
 




