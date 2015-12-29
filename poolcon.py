import datetime
import smtplib

# LOGGING METHODTOBE
def logdat(subject, gpioout, count, countdown):
    f=open('/var/log/gpio.log','a')
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y/%m/%d %H:%M:%S")
    datastring = 'GPIOOUT='+str(gpioout)+', COUNT='+str(count)+', COUNTDOWN='+str(countdown)
    outstring = str(timestamp)+"\t"+subject+': '+datastring+"\n"
    f.write(outstring)
    f.close()

