import getpass
from datetime import datetime
from zoneinfo import ZoneInfo
import os
from pathlib import Path
# ========================================= Functions ==================================================
def encrypt(data, key):
  encrypted = ''
  for i in data:
      encrypted += chr(ord(i)^int(key))
  return encrypted

def decrypt(data, key):
  decrypted = ''
  for i in data[:len(data)]:
      decrypted += chr(ord(i)^int(key))
  return decrypted

def Read_all(File, key):
  File.seek(0)
  File.readline()
  print('')
  for i in File.readlines():
    print(decrypt(i[:len(i)-1], key))

def write(timestamp_path, File, key):
  
  date = str(datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S"))
  
  timestamp = open(timestamp_path,'a')
  timestamp.write(encrypt(date, key)+'\n')
  timestamp.close()
  
  File.write(encrypt(date, key)+'\n')
  
  print('')
  print("Enter blank to finish writing")
  data = input('What is in your mind? : ')
  while data != "":
    File.write(encrypt(data, key)+'\n')
    data = input()
  File.write(encrypt('----------------------------------------',key)+'\n')

#================================================ Code ======================================================
# 1. Define the folder path first
folder = Path.home() / "Documents" / "My_Diary_Data"
if not os.path.exists(folder):
    os.makedirs(folder)

name = input("Enter your Name: ")

# 2. Create full paths for your files
file_path = os.path.join(folder, name)
timestamp_path = os.path.join(folder, name + "_timestamp")


flag = 'N'

try:
    File = open(file_path,'x')
    open(timestamp_path,'x')
    key = getpass.getpass('Enter the secret key: ')

    enc = ''
    for i in key:
      enc += chr(ord(i)^10)

    File.write(enc+'\n')

    File.close()

except:
    File = open(file_path,"a+")

    File.seek(0)

    key = getpass.getpass('Enter the secret key: ')

    dec = ''
    for i in File.readline():
      dec += chr(ord(i)^10)

    if key == dec[:len(dec)-1]:
      flag = "Y"
    else:
      print("Wrong secret key")

if flag == "Y":
  while True:
    print('')
    print('My Diary'.center(30,'-'))
    print('1.Read all content \n2.Read specific content \n3.Write \n4.exit')
    choice = int(input("Enter your choice: "))
    match choice:
      case 1:
        Read_all(File, key)
      case 2:
        
        file1 = open(timestamp_path,'r')
        
        dict1 = {}
        j = 1
        for i in file1.readlines():
          dict1[j] = decrypt(i[:len(i)-1], key)
          j += 1
        
        print('')
        for key1,value in dict1.items():
          print(f"{key1}.{value}")
        
        if len(dict1) == 0:
          continue
            
        
        print('')
        choice = int(input("Choose the option: "))
        print('')

        File.seek(0)
        dat = File.readline()
        while dict1[choice] != decrypt(dat[:len(dat)-1], key):
          dat = File.readline()
        

        while decrypt(dat[:len(dat)-1], key) != '----------------------------------------':
          print(decrypt(dat[:len(dat)-1], key))
          dat = File.readline()

      case 3:
        write(timestamp_path, File, key)
      case 4:
        print("Thank you for using My Diary")
        break
      case _:
        print('Invalid choice')

