# Modbus_Film69

### install  
```sh
pip install git+https://github.com/WATCHARAPHON6912/Modbus_Film69.git
```
### example
```python
from Modbus_Film69 import Modbus_Film69
ser=Modbus_Film69("COM3")
while 1:
    rec,len_Bytes=ser.send("01 03 20 00 00 04")
    print(rec,len_Bytes)
```
