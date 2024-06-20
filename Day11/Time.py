""" ip: 7262sec
      op: 2hr:1min:2sec
"""
ip= 7262
minutes=0
hrs=0
sec=0
hrs=ip//3600
mins=(ip-3600*hrs)//60
sec=(ip-3600*hrs)-(60*mins)
print(hrs,"hrs :",mins,"min :",sec,"sec")

