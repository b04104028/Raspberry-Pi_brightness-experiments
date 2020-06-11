# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# TSL2561
# This code is designed to work with the TSL2561_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Light?sku=TSL2561_I2CS#tabs-0-product_tabset-2

# Enable I2C clock stretching
dtparam=i2c_arm_baudrate = 10000

import smbus
import time
import pandas as pd
import datetime

with open(r'/home/pi/Desktop/LightSensor//' +str(datetime.date.today()) + '_170_.txt','a', newline = '') as f:
    f.write('date,       time,      fullSpec,   infra,  visi' + '\n')
           # 2020-04-14,  01:02:46,  95,       19,    76

while True:
    # Get I2C bus
    bus = smbus.SMBus(1)
    
    # TSL2561 address, 0x29(from i2cdetect -y 1)
    # Select control register, 0x00(00) with command register, 0x80(128)
    #       0x03(03)    Power ON mode
    bus.write_byte_data(0x29,0x00|0x80,0x03)
    # TSL2561 address, 0x39(57)
    # Select timing register, 0x01(01) with command register, 0x80(128)
    #       0x02(02)    Nominal integration time = 402ms
    bus.write_byte_data(0x29, 0x01 | 0x80, 0x02)
    
    time.sleep(0.5)
    
    # Read data back from 0x0C(12) with command register, 0x80(128), 2 bytes
    # ch0 LSB, ch0 MSB
    data = bus.read_i2c_block_data(0x29, 0x0C | 0x80, 2)
    
    # Read data back from 0x0E(14) with command register, 0x80(128), 2 bytes
    # ch1 LSB, ch1 MSB
    data1 = bus.read_i2c_block_data(0x29, 0x0E | 0x80, 2)
    
    # Convert the data
    ch0 = data[1] * 256 + data[0]
    ch1 = data1[1] * 256 + data1[0]
    
    # Output data to screen
    print (datetime.datetime.strftime(datetime.datetime.now(), "%H: %M: %S"))
    print ("Full Spectrum(IR + Visible) :%d lux" %ch0)
    print ("Infrared Value :%d lux" %ch1)
    print ("Visible Value :%d lux" %(ch0 - ch1))
    
    i = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
    j = datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S")
    k = '%d' %ch0
    l = '%d' %ch1
    m = '%d' %(ch0-ch1)
    
    
    with open(r'/home/pi/Desktop/LightSensor//' +str(datetime.date.today()) + '_170_.txt','a', newline = '') as f:
        f.write(i + ',  '+j+',  '+k+',       '+l+',    '+m+'\n')
               # 2020-04-14,  01:02:46,  95,       19,    76   
    
    time.sleep(60)
     


