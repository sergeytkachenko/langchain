


 Since Creatio 8.0 Atlas, Creatio adds the required dependencies automatically for elements created or modified using Freedom UI Designer. I. e., you can use the functionality of all app packages when working with Freedom UI pages, sections, objects, business processes, web services, and configuration elements. This makes no-code development easy and comfortable for users.
 



 A
 **cyclic dependency** 
 is a dependency that occurs when the same package is dependent on the current package and is part of a index of packages on which the current package depends directly or via a dependency chain. Cyclic dependency chains lead to app runtime errors.
 



 Consider an app with
 
 A
 
 ,
 
 B
 
 , and
 
 C
 
 packages where the
 
 B
 
 package depends on the
 
 A
 
 package, and the
 
 C
 
 package depends on the
 
 B
 
 package. Using an element of the
 
 C
 
 package in the
 
 A
 
 or
 
 B
 
 package the
 
 C
 
 package to be their dependency. Creatio will not execute an operation with such a requirement since it will cause a cyclic chain (Fig. 1).
 




 Fig. 1 Cyclic chain
 

![scr_example_cyclic_sequences.png](/docs/sites/en/files/images/Platform_basics/cyclic_sequences/scr_example_cyclic_sequences.png)



 Using apps that have cyclic dependencies can cause Creatio runtime issues. To avoid this, Creatio checks the app elements used and dependencies configured while saving the app changes. If cyclic dependency chains are detected as part of the check-up, Creatio saves the changes but does not save new package dependencies. You will receive a recommendation to check and fix the dependencies configured. The notification will contain more information about the error as well (Fig. 2):
 


* Source
 
 is a part of the schema that refers to the error-causing element.
* Reference
 
 is a name of the element that causes the error.
* Package
 
 is a name of the package that contains the element.




 Fig. 2 Error message for a cyclic dependency
 

![scr_error_cyclic_sequences.png](/docs/sites/en/files/images/Platform_basics/cyclic_sequences/scr_error_cyclic_sequences.png)



 We recommend fixing cyclic dependencies before you configure the app further to ensure its operability.
 



 Cyclic chain examples
-----------------------



 This section covers several example solutions that cause cyclic chain errors.
 





 Example 1.
 
 If you use an existing configuration element from the
 
 Custom
 
 package (Fig. 3) in the “UserApplication” custom app, this will cause a cyclic chain error. Cause: the
 
 Custom
 
 package depends on every configuration package by default, including the “UserApplication” package. However, the “UserApplication” package must depend on the
 
 Custom
 
 package to access its elements.
 





 Fig. 3 Package hierarchy
 

![scr_hierarchy_cyclic_sequences.png](/docs/sites/en/files/images/Platform_basics/cyclic_sequences/scr_hierarchy_cyclic_sequences.png)





 Example 2.
 
 You have created “Application1” and “Application2” apps. If you use “Application1” elements in “Application2,” Creatio adds “Application1” to “Application2” as a dependency automatically. If you use the functionality of the “Application2” app in the “Application1” app to improve the latter, this will cause a cyclic chain error.
 




 Prevent cyclic chains
-----------------------



 To avoid cyclic chains, we recommend the following:
 


* If you configure an app using elements from another app, mind the app's resulting dependencies. Transfer both apps into a different environment to the app works as intended.
* Only save the improvements that the app uses to the app package. After creating an app but before setting it up, find its package and change the default package. To
 **change the default package** 
 :


1. Click
 ![](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/btn_system_designer_8_shell.png)
 in the top right → “System setup” → “System settings.”
2. Select the “Current package” (“CurrentPackageId” code) system setting.
3. Make sure that the package name from the
 
 Advanced settings
 
 tab in the Application Hub matches the package name in the
 
 Default value
 
 field. If a different package is specified, change it to the app package and save the changes.



 Resolve the cyclic chain issue
--------------------------------



 View examples that resolve the cyclic chain issue in the table below.
 




 Examples that resolve the cyclic chain issue
 


| 
 Way to eliminate cyclic chains
  | 
 Example
  |
| --- | --- |
| 
 If you use the wrong elements by mistake, which caused a cyclic chain, you can delete them or replace them with new elements that do not cause a cyclic chain. After that, save the changes to readd the dependencies.
 

 Objects or business processes that use methods and
 
 Script task
 
 element cannot be published before you eliminate the cyclic chain issue.
  | 
 The
 
 Read data
 
 business process element reads a redundant column or uses it in filtering conditions. To eliminate the cyclic chain, simply delete the column and save the business process.
  |
| 
 If the elements that cause a cyclic chain are not critical to the app operation or you made the changes by mistake, simply revert the changes to eliminate all newly introduced cyclic chains.
  | 
 You replaced the
 
 UsrObject
 
 object both in the “UserApplication” app package and the
 
 Custom
 
 package. The
 
 Column
 
 object column created in the
 
 Custom
 
 package has a different
 
 Name
 
 property in the “UserApplication” package. Since you made the changes in the dependent package, this caused a cyclic chain. To eliminate it, simply return the property to its original state and save the updated object.
  |
| 
 If you cannot edit or delete the elements that caused a cyclic chain, move them:
 * to the package that contains the dependent schemas of the elements
* to the package from which the package that contains the schemas inherits


 Learn more in a different section:
 [Move the functionality between packages](https://academy.creatio.com/documents?id=2419&anchor=title-2534-8) 
 .
  | 
 A cyclic chain was made when you used the
 
 UsrLookup
 
 lookup of the
 
 Custom
 
 package in the “UserApplication” app. The lookup is the data source for the
 
 UsrEntity
 
 object’s lookup column. To fix the error, move the
 
 UsrLookup
 
 lookup to the “UserApplication” app package.
  |






 Attention.
 
 Do not replace a single object in a single package more than once. If the cyclic chain is caused by two replacements of a single object in two different packages, move the schema that causes the cyclic chain to a third package. The package where you configure the app must inherit from the package to which you moved the schema.
 





