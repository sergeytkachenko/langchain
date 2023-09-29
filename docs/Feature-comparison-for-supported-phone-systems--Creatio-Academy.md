


 The telephony features in Creatio vary depending on the connected phone system. By default, Creatio is integrated with Webitel telephone service. If necessary, you can connect a different system.
 



 Below is a feature comparison table for different phone systems:
 





| 

 TAPI
 
 | 

 Cisco Finesse
 
 | 

 Avaya
 
 | 

 Webitel
 
 | 

 Asterisk
 
 | 

 CallWay
 
 |
| --- | --- | --- | --- | --- | --- |
| 
**“Search by caller ID” phone system functionality** 
 |
| 
[Note 1](#title-2356-1) 
 | 
 +
  | 
 +
  | 
 +
  | 
 +
  | 
 +
  |
| 
**“Make outgoing calls” phone system functionality** 
 |
| 
 +
  | 
 +
  | 
 +
  | 
 +
  | 
[Note 2](#title-2356-2) 
 | 
[Note 3](#title-2356-3) 
 |
| 
**“Receive incoming calls” phone system functionality** 
 |
| 
 +
  | 
 +
  | 
 +
  | 
 +
  | 
 -
  | 
[Note 4](#title-2356-5) 
 |
| 
**“Place calls on hold, unhold calls” phone system functionality** 
 |
| 
 +
  | 
 +
  | 
 +
  | 
 +
  | 
 +
  | 
 +
  |
| 
**“End calls” phone system functionality** 
 |
| 
 +
  | 
 +
  | 
 +
  | 
 +
  | 
 +
  | 
 +
  |
| 
**“Manage agent status” phone system functionality** 
 |
| 
[Note 5](#title-2356-6) 
 | 
 +
  | 
 +
  | 
 +
  | 
 -
  | 
 +
  |
| 
**“Transfer calls” phone system functionality** 
 |
| 
 +
  | 
 +
  | 
 +
  | 
 +
  | 
 +
  | 
 +
  |
| 
**“Save the information to
 
 Calls
 
 section” phone system functionality** 
 |
| 
 +
  | 
 +
  | 
 +
  | 
 +
  | 
 +
  | 
 +
  |
| 
**“Call from browser” phone system functionality** 
 |
| 
 -
  | 
 -
  | 
 -
  | 
 +
  | 
 -
  | 
 -
  |
| 
**“Replay calls” phone system functionality** 
 |
| 
 -
  | 
 -
  | 
 -
  | 
 +
  | 
 -
  | 
 -
  |
| 
**Telephone system versions** 
 |
| 
 All phone systems that use TAPI 2.X
  | 
 Cisco Finesse 11.5+
  | 
 AES v5.2-10.1
  | 
 | 
 13, 16, 18
  | 
 |



### 
 Notes


#### 
 1



 Due to TAPI limitations, caller identification is unavailable for calls routed through UCCX while using CUCM.
 


#### 
 2



 The user might have to respond to an incoming system call to initiate an outgoing call from Creatio. The call flow depends on the software/hardware phone version/model.
 


#### 
 3



 CallWay software phones are fully supported. If the agent uses a different IP or software phone, they have to respond to an incoming “system” call to initiate an outgoing call from Creatio.
 


#### 
 4



 Only CallWay software phones are fully supported.
 


#### 
 5



 The following 2 statuses are available: “Ready” and “Do not disturb” (DND). Cisco is currently not supported.
 




