# smart-attendance
This project is for marking the Attendance in the office/college....

the image of the person is capture from the pi camera and sends  for comparision.

the main rekog.py runs and the comparission takes place with the dataset already available.
     -If it matches the attendance is marked and the greetings are generated.
                     EX- hello shiva
                     
     - IF the person does not match then the details are gathered by the lex bot with the help of the speaker and microphone .
     and stored in the database along with the image.
     
later the real task starts  AWS LEX service is iniated and a sequence of questions are generated for the person 
to know the purpose of visit and the reason is stored and informed to the higher officials.

