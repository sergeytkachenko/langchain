


 The
 
 Start timer
 
 event enables you to run the process either once at a specified time, or regularly with a specified frequency.
 



 You can select the frequency in the
 
 Process launch frequency
 
 field. The parameters of the
 
 Start timer
 
 event will differ depending on the selected option.
 



 The base settings of the element are different depending on the frequency. Additional parameters are available for all frequency options (Fig. 1).
 




 Fig. 1
 

 Start timer
 
 element setup area with common parameters
 




![scr_chapter_process_designer_start_timer_universal.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_start_timer_universal.png)





 Process start time
 
 – the time at which the process will start.
 




 Timer validity
 
 – the life cycle of the
 
 Start timer
 
 event, i.e., a time period during which the event is considered relevant and can be triggered. Populate these fields if you need to limit the period during which the
 
 Start timer
 
 event can be triggered for a process e.g., if you need the process to run every Friday for the next five weeks only).
 




 Repeat on misfire
 
 – select this checkbox to ensure that the process launches even if the
 
 Start timer
 
 element cannot be triggered at the intended time, e.g., due to a server reboot.
 




 Time zone
 
 – the time zone of the
 
 Start timer
 
 element. By default, the element time zone is set according to:
 


* The time zone of the user who created a campaign.
* The time zone specified in the
 
 Default TimeZone
 
 system setting (if no time zone has been set in the user profile).



 If the time zone cannot be set according to the rules above, the
 
 Time zone
 
 field of a new campaign will have the “(GMT) UTC Time Format” default value.
 




 Parameters of the “Once” frequency option
--------------------------------------------



 Select the "Once” frequency option in the
 
 Process launch frequency
 
 to run the business process only once at a specified time (Fig. 2).
 




 Fig. 2
 
 The
 
 Start timer
 
 event setup for one-time process launch
 




![scr_chapter_process_designer_start_timer_once.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_start_timer_once.png)





 Launch on
 
 – the time at which the process will start.
 




 Parameters of the “Minute/hour” frequency option
---------------------------------------------------



 Select the "Minute/Hour” option in the
 
 Process launch frequency
 
 field to launch the process several times a day (e.g., working hours) (Fig. 3).
 




 Fig. 3
 
 The
 
 Start timer
 
 event setup for running the process every hour from 8 am till 8 pm
 




![scr_chapter_process_designer_start_timer_m_h.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_start_timer_m_h.png)





 Run every
 
 – a process launch frequency in minutes or hours, as well as a time frame the process will be limited to. For example, you can run the process every hour from 8 am till 8 pm.
 




 Parameters of the “Day” frequency option
-------------------------------------------



 If you select the "Day” option in the
 
 Process launch frequency
 
 field to launch the business process once a day at a certain time with specific intervals (e.g., every three days) (Fig. 4).
 




 Fig. 4
 
 The
 
 Start timer
 
 event setup for running the process every three days at 11 am
 




![scr_chapter_process_designer_start_timer_day.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_start_timer_day.png)





 Run every
 
 – a launch frequency in days and a launch time. For example, you can run a process every three days at 11 am.
 




 Parameters of the “Week” frequency option
--------------------------------------------



 Select the "Week” option in the
 
 Process launch frequency
 
 field to repeat the business process weekly on specified days at the specified time (Fig. 5).
 




 Fig. 5
 
 The
 
 Start timer
 
 event setup for running the process every Tuesday and Thursday at 9 am
 




![scr_chapter_process_designer_start_timer_week.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_start_timer_week.png)





 Launch on
 
 – the time at which the process will be launched (e.g., 9:00 am).
 




 Which days of the week to run?
 
 – select weekdays on which the process must start.
 




 Parameters of the “Month” frequency option
---------------------------------------------



 Select the "Month” option in the
 
 Process launch frequency
 
 field to launch the business process monthly at certain days (Fig. 6).
 




 Fig. 6
 
 The
 
 Start timer
 
 event setup for running the process monthly
 




![scr_chapter_process_designer_start_timer_month.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_start_timer_month.png)





 Run every
 
 – enter a time gap in months between each process launch. For example, you can automatically run the process every third month.
 




 Start day
 
 – specify the launch day of the process. You can choose from the following options:
 


* "Day of the month" is a specific day of month (e.g., every tenth of the month). For example, every tenth of the month.
* "Day of the week" is the number and the day of the week of the month (e.g., every third Friday of the month).
* "First / last work day" is the first or last business/regular day of the month.




 Parameters of the “Year” frequency option
--------------------------------------------



 Select the "Year” option in the
 
 Process launch frequency
 
 field to run the business process every year on a certain date at the specified time (Fig. 7).
 




 Fig. 7
 
 The
 
 Start timer
 
 event setup for running the process every third Monday of October every year
 




![scr_chapter_process_designer_start_timer_year.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_start_timer_year.png)





 Start day
 
 – select the day and the month when the process will start. For example, 8th of March or every third Monday of October.
 




 Launch on
 
 – the time at which the process will be launched (e.g., 9:00 am).
 




 Timer validity
 
 – the life cycle of the
 
 Start timer
 
 event, i.e., a time period during which the event is considered relevant and can be triggered.
 




 Repeat on misfire
 
 – select this checkbox to ensure that the process launches even if the
 
 Start timer
 
 element cannot be triggered at the intended time, e.g., due to a server reboot.
 




 Parameters of the “Other frequency” option
---------------------------------------------



 Select the "Other frequency” option in the
 
 Process launch frequency
 
 field to set a custom process frequency via a cron-expression (Fig. 8).
 




 Fig. 8
 
 The
 
 Start timer
 
 event configured to launch a process from 14:00 to 14:59 and from 18:00 to 18:59 daily
 




![scr_chapter_process_designer_start_timer_cron.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_start_timer_cron.png)






 Note.
 
 Cron is a planning utility widely used in UNIX-based operating systems. You can configure a more flexible launch date of a process using cron-expressions. We recommend consulting with your company’s system administrators before working with cron-expressions.
 




 A cron-expression consists of numbers, words and symbols placed in a strictly defined order to specify the time, date, and year of the process launch. The following table shows a basic structure of cron-expressions:
 





| 
 TIME UNITS
  | 
 ACCEPTABLE VALUES
  | 
 SPECIAL CHARACTERS
  |
| --- | --- | --- |
| 
 Second
  | 
 0
  | 
 , - \* /
  |
| 
 Minute
  | 
 0-59
  | 
 , - \* /
  |
| 
 Hour
  | 
 0-23
  | 
 , - \* /
  |
| 
 Day of the month
  | 
 1-31
  | 
 , - \* ? / L W
  |
| 
 Month
  | 
 1-12 or JAN-DEC
  | 
 , - \* /
  |
| 
 Day of the week
  | 
 1-7 or SUN-SAT
  | 
 , - \* ? / L #
  |
| 
 Year
  | 
 empty value or 1970-2099
  | 
 , - \* /
  |






 Note.
 
 If the cron-expression is correct, you will see the time/date of the process launch in the traditional format in the
 
 Cron-expression
 
 field. If the expression is incorrect, Creatio will display an error.
 




 Examples of cron-expressions
------------------------------




 0 \* 14 \* \* ?
 
 – launches the process every minute from 14:00 to 14:59 daily.
 




 0 0/5 14,18 \* \* ?
 
 – launches the process every 5 minutes from 14:00 to 14:59 and from 18:00 to 18:59 daily.
 




 0 10,44 14 ? 3 WED
 
 – launches at 14:10 and 14:44 every Wednesday of March.
 




 0 0 12 1/5 \* ?
 
 – launches the process at 12:00 every 5 days, starting from the first day of the month on a monthly basis.
 



 Learn more about cron expressions in the
 [QARTZ documentation](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html) 
 .
 




