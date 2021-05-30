from datetime import datetime
import pywhatkit as kit
import sqlite3 as sql
import ProgramVar as pv
#if the date is today's date then you send reminders for the appointments an hour before the appointment and 10 mins before the appointment

def notification(dat,i,id):
    conn = sql.connect(pv.databasePath)
    cur = conn.cursor()
    if(i==0):
        #db connection
        now=datetime.now().date().isoformat()
        stringDate = '%' + now + '%'
        query = "SELECT appointment.app_id, appointment.datetime, appointment.status, patient.phone_no FROM appointment JOIN scheduled_app ON scheduled_app.app_id = appointment.app_id JOIN patient ON patient.patient_id =scheduled_app.patient_id WHERE appointment.datetime LIKE ?"
        cur.execute (query, (stringDate, ))
        # print (date)
        result = cur.fetchall()
        # if rec in result:
        # hour=int(rec)   
        print (result)
        conn.commit()
        count=0
        for record in result:
            print(record[1])
            res=record[1].split(" ")
            print(res)
            times=res[1].split(":")
            hour=int(times[0])-1
            minutes=int(times[1])
            print(hour)
            print(minutes)
            message = "You have your appointment at "+ str(hour+1)+":"+str(minutes)+"hours today. \nPlease be there 15 minutes prior to the appointment.\nStay Healthy and Take care."
            number="+91"+str(record[3])
            kit.sendwhatmsg(number, message, hour, minutes)
            count+=1

        conn.close()
        
    else:
        now1=datetime.now().date().isoformat()
        #an hour before the message will be sent to the person
        # now1="2021-05-04"
        res=dat.split(" ")
        print(res)
        if(res[0]==now1):
            times=res[1].split(":")
            hour=int(times[0])-1
            minutes=int(times[1])
            print(hour)
            print(minutes)
            message = "You have your appointment at "+ str(hour+1)+":"+str(minutes)+"hours today. \nPlease be there 15 minutes prior to the appointment.\nStay Healthy and Take care."
            query = "SELECT phone_no FROM patient WHERE patient_id=?;"
            cur.execute (query, (id, ))
            result = cur.fetchall()
            print (result)
            conn.commit()
            number="+91"+str(result[0][0])
            kit.sendwhatmsg(number, message, hour, minutes)
            conn.close()


# notification("2021-05-30 05:54:00",1, 2) 