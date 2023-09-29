


 Lead predictive scoring enables minimizing the amount of working time that your managers spend on low potential leads and increasing the number of leads converted to opportunities. The prediction is performed for every qualified lead. It takes into account the lead parameters and the working history.
 



 Predictive score – a
 
[machine learning](https://academy.creatio.com/documents?product=administration&ver=7&id=1825) 

 tool that displays the probability of lead conversion to a new opportunity on a scale from 1 to 100 points (
 [Fig. 1](#XREF_83999_196)
 ).
 





 Note.
 
 In case the predictive score is not displayed in the lead profile, you need to verify if lead predictive scoring is enabled and a trained model instance exists in the
 
 ML models
 
 section of Creatio.
 






 Fig. 1
 

 Lead profile with a predictive score
 

![scr_chapter_predicting_lead_profile_with_score.png](/guides/sites/en/files/documentation/user/en/leads/BPMonlineHelp/leads_scoring/scr_chapter_predicting_lead_profile_with_score.png)



 Depending on the probability of lead conversion to opportunity Creatio determines general likelihood of lead conversion:
 


* ![lead_strong_prediction.png](/guides/sites/en/files/documentation/user/en/leads/BPMonlineHelp/leads_scoring/lead_strong_prediction.png)
 – high predictive score (80-100 points)
* ![lead_middle_prediction.png](/guides/sites/en/files/documentation/user/en/leads/BPMonlineHelp/leads_scoring/lead_middle_prediction.png)
 – medium predictive score (50-79 points)
* ![lead_weak_prediction.png](/guides/sites/en/files/documentation/user/en/leads/BPMonlineHelp/leads_scoring/lead_weak_prediction.png)
 – low predictive score (1-49 points)



 Predictive scoring is not performed for non-qualified leads and the predictive score for such leads is set to “0”
 ![lead_no_prediction.png](/guides/sites/en/files/documentation/user/en/leads/BPMonlineHelp/leads_scoring/lead_no_prediction.png)
 .
 



 The predictive score is regularly recalculated since lead nurturing process is having a constant impact upon the probability of its conversion to opportunity. The score can either be raised or decreased if the lead information has not been updated for a long time. Learn more about predictive scoring in the “
 

[Predictive scoring](https://academy.creatio.com/documents?product=administration&ver=7&id=1863) 

 ” article.
 





 Launch of predictive scoring
--------------------------------



 You can launch lead predictive scoring for a single record as well as for all the lead records being nurtured. You can launch it automatically or manually for a selected record.
 


### 
 Set up automatic predictive scoring



 Predictive scoring is initiated
 **automatically** 
 :
 


* During lead qualification. In this case the score prediction is only performed for the qualified lead.
* Every day, when Creatio is not excessively used. In this case the score prediction is performed for all the leads being nurtured.



 To set up the automatic launch of the predictive scoring process for all nurtured leads:
 


1. Click
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/leads/BPMonlineHelp/leads_scoring/btn_system_designer.png)
 to open the System Designer.
2. Click
 
 ML models
 
 in the “System setup” block.
3. Open the lead scoring page.
4. Navigate to the
 
 Setting up background update of prediction results
 
 detail on the
 
 Parameters
 
 tab and switch the
 
 Perform background update of prediction results daily during the maintenance window
 
 slider to the right.
 





 Note.
 
 You can set up the period when Creatio is least loaded (to run resource-heavy processes) in the
 
 Maintenance periods
 
 lookup.


### 
 Launch predictive scoring manually



 To
 **manually** 
 launch predictive scoring for any lead, highlight the record whose score needs to be displayed in the
 
 Leads
 
 section, and select the
 
 Evaluate predictive score
 
 command from the
 
 Actions
 
 menu (
 [Fig. 1](#XREF_55524_196)
 ).
 





 Fig. 1
 

 Manually launching lead predictive scoring
 

![scr_chapter_predicting_score_lead_manually.png](/guides/sites/en/files/documentation/user/en/leads/BPMonlineHelp/leads_scoring/scr_chapter_predicting_score_lead_manually.png)





 Data processed during predictive scoring calculation
--------------------------------------------------------



 To evaluate the lead predictive scoring, the machine-learning model analyses the data of the lead and its linked records. We recommend populating Creatio with maximum information about the lead for its processing during the predictive scoring.
 



 During the scoring process, the machine-learning model processes the following data of the lead and the connected objects.
 


* Lead need type.
* Availability of a qualified contact and contact details (role, type, department, job title, mobile phone, business phone).
* If there are no contact details on the lead page, Creatio verifies if these details are populated on the corresponding contact page.
* Availability of a qualified account and account details (category, industry, type, number of employees, web site, country).
* If there are no account details on the lead page, Creatio verifies if these details are populated on the corresponding account page.
* Lead engagement data (source, channel, website events, landing).
* + Lead aggregated indicators:
	+ number of days after lead qualification
	+ number of leads per contact
	+ number of leads per contact registered within the last 2 weeks
	+ number of phone calls and emails per lead (monthly, quarterly, total)
	+ number of days after the last phone call
	+ number of days after the last email



 Lack of one or several parameters from the list might have considerable impact upon the lead predictive score accuracy.
 




