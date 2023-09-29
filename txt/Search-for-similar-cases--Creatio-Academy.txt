


 Predictive search for similar cases increases the support team efficiency. The information about similar cases helps to streamline the solution of the current case.
 



 This
 [ML tool](https://academy.creatio.com/documents?product=administration&ver=7&id=1825) 
 finds similar cases by analyzing the unstructured text data and displays them on the case page. The probability score is displayed in the
 
 Score
 
 field (Fig. 1).
 




 Fig. 1 The
 
 Similar cases
 
 detail on a case page
 

![case_page_similar_cases.png](/docs/sites/en/files/images/Service_Tools/similar_cases/case_page_similar_cases.png)



 If you have more than 100 processed cases, Creatio will train the out-of-the-box recommendation model automatically. This model will predict recommendations for all new cases. If necessary, you can adapt and train the ML model to suit your business needs. Read more:
 [Set up searching for similar texts](/docs/8-0/user/customization_tools/ai_tools/similar_texts/similar_text_search) 
 .
 



 To see the prediction, go to the
 
 Closure and feedback
 
 tab on the case page. The search results will display on the
 
 Similar cases
 
 detail. Should the case subject or description change, you can perform a new search for similar cases by clicking
 
 Refresh
 
 .
 



 Rate the relevance of the found cases in the
 
 Prediction quality
 
 field. Your feedback will improve the accuracy of future predictions.
 





 Note.
 
 If Creatio stores more than 100 processed cases but will not display the similar case search results, check if the search for similar cases is active and there is a trained ML model in the
 
 ML Models
 
 section.
 



 Additionally, Creatio will not display the prediction if the search yields no relevant results. In this case you can change the text similarity threshold manually on the ML model’s advanced options page. Read more:
 [Set up searching for similar texts](/docs/8-0/user/customization_tools/ai_tools/similar_texts/similar_text_search) 
 .
 












 Run the search for similar cases
----------------------------------



 You can search for cases that are similar to either a single record or  all the records in the
 
 Cases
 
 section. You can launch the search automatically or manually.
 


### 
 Set up an automatic search



 Creatio will search for similar cases
 **automatically** 
 :
 


* When creating a new case.
* When changing an existing case.
* Daily when Creatio is loaded the least.



 To set up the automatic prediction for all cases:
 


1. Open the
 
 ML models
 
 section in the
 
 Studio
 
 workplace.
2. Open the “Similar case search” model.
3. Toggle on
 
 Perform background update of prediction results daily during the maintenance window
 
 in the
 
 Setting up background update of prediction results
 
 field group on the
 
 Parameters
 
 tab
 *.* 






 Note.
 
 If you need to run resource-heavy processes, such as the search for similar cases, it is better to do it when Creatio is loaded the least. You can specify the relevant time period  in the
 
 Maintenance periods
 
[lookup](/docs/8-0/user/setup_and_administration/system_settings_and_lookups/lookup_values/manage_lookup_values) 
 .


### 
 Run a manual search



 To start a
 **manual** 
 search for similar cases, go to the
 
 Cases
 
 section, open the needed record and click
 
 Refresh
 
 on the
 
 Similar cases
 
 detail (Fig. 2).
 




 Fig. 2 Searching for similar cases manually
 

![search_for_cases_again.png](/docs/sites/en/files/images/Service_Tools/similar_cases/search_for_cases_again.png)



 How predictive search for similar cases works
-----------------------------------------------



 To find similar cases, the ML model compares the text in the
 
 Subject
 
 and
 
 Description
 
 fields of the current case to the corresponding values of the other cases in the section. The model takes into account the matching text parameters,  as well as the “weight” (importance) of certain words and phrases. The model considers the cases  similar if the text exceeds the similarity threshold. The threshold  is set to 0.3 by default, however you can alter this value and retrain the model. Read more:
 [Set up searching for similar texts](/docs/8-0/user/customization_tools/ai_tools/similar_texts/similar_text_search	) 
 .
 




