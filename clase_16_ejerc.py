from datetime import datetime, timedelta

print("=======================")
dt = datetime.now()
print(dt)

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)

print("=======================")
dt_custom = datetime(2000, 1, 1)
print(dt_custom)

print(dt_custom.year)
print(dt_custom.month)
print(dt_custom.day)
print(dt_custom.hour)
print(dt_custom.minute)
print(dt_custom.second)


print("=======================")
print(dt.strftime("%A %d of %B %Y, %I:%M hours"))
print(dt.strftime("%A %d of %B %Y, %I hours %M min"))
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)

print("=======================")
td = timedelta(days=45)
fecha_modif = dt + td
print(dt.strftime("%A %d of %B %Y, %I hours %M min"))
print(fecha_modif.strftime("%A %d of %B %Y, %I hours %M min"))

print("=======================")
bida = datetime(1978, 12, 20, 1, 00, 00)
hoy = datetime.now()

y = hoy.year - bida.year 
mo = int(bida.month - hoy.month)
d = int(bida.day - hoy.day) 
h = int(bida.hour - hoy.hour)
mi = int(bida.minute - hoy.minute)
print(y)
print(mo)
print(d)
print(h)
print(mi, "\n"*3)

deltadias = y*3600 + mo*30 + d
print(deltadias)


añosx = int(deltadias/3600)
mesesx = int((deltadias - añosx*3600)/30)
diasx = int(deltadias - añosx*3600 - mesesx*30)
print(añosx)
print(mesesx)
print(diasx)

print(f"Mi edad es: {añosx}años, {mesesx} meses y {diasx} dias")

print("********************************************************")
print("********************************************************")