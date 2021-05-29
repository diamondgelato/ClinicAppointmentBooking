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
        query = "SELECT * FROM appointment WHERE datetime LIKE ?"
        cur.execute (query, (stringDate, ))
        # print (date)
        result = cur.fetchall()
        # if rec in result:
        # hour=int(rec)   
        print (result)
        conn.commit()
        #need to complete this.
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
            message = "You have your appointment at "+ str(hour+1)+":"+str(minutes)+"\nPlease be there 15 minutes prior to the appointment.\nStay Healthy and Take care."
            query = "SELECT phone_no FROM patient WHERE patient_id=?;"
            cur.execute (query, (id, ))
            result = cur.fetchall()
            print (result)
            conn.commit()
            #need to complete this.
            number="+91"+str(result[0][0])
            kit.sendwhatmsg(number, message, hour, minutes)
            conn.close()


# notification("2021-05-04 04:26:00",1, 1)