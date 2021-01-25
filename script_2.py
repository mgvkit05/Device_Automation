'''
Automating adb commands on netcomm CPE.

'''

import subprocess
import time

subprocess.call('adb devices', shell=True)

option = input("Enter option\n 1.SIM Status\n 2.IMEI\n 3.IMS Status\n 4.Data Profile\n 5.Change and Enable APN Name\n 6.Change APN IP Type\n 7.Disable APN State\n 8.Signal Strength\n 9.Registration Status\n 10.Cell Signal Measurements\n 11.Show cell Scanned\n 12. Q to exit\n WAITING FOR USER INPUT: ")


def sim_status():
    subprocess.call('adb shell rdb dump sim', shell=True)

def imei():
    subprocess.call('adb shell rdb dump imei', shell=True)

def ims_status():
    subprocess.call('adb shell rdb dump wwan.0.ims', shell=True)

def data_profile():
    print('########################################################')
    subprocess.call('adb shell rdb dump link.profile.1', shell=True)
    print('########################################################')
    subprocess.call('adb shell rdb dump link.profile.2', shell=True)
    print('########################################################')
    subprocess.call('adb shell rdb dump link.profile.3', shell=True)
    print('########################################################')
    
    subprocess.call('adb shell rdb dump link.profile.1.apn', shell=True)
    subprocess.call('adb shell rdb dump link.profile.2.apn', shell=True)
    subprocess.call('adb shell rdb dump link.profile.3.apn', shell=True)
    subprocess.call('adb shell rdb get link.profile.1.pdp_type', shell=True)
    subprocess.call('adb shell rdb get link.profile.2.pdp_type', shell=True)
    subprocess.call('adb shell rdb get link.profile.3.pdp_type', shell=True)

def change_and_enable_apn():
    subprocess.call('adb shell rdb set link.profile.1.apn apn1_name', shell=True)
    time.sleep(1)
    subprocess.call('adb shell rdb set link.profile.1.writeflag 1', shell=True)
    time.sleep(1)
    subprocess.call('adb shell rdb set link.profile.1.enable 1', shell=True)
    time.sleep(1)

    subprocess.call('adb shell rdb set link.profile.2.apn apn2_name', shell=True)
    time.sleep(1)
    subprocess.call('adb shell rdb set link.profile.2.writeflag 1', shell=True)
    time.sleep(1)
    subprocess.call('adb shell rdb set link.profile.2.enable 1', shell=True)
    time.sleep(1)

    
    subprocess.call('adb shell rdb set link.profile.1.apn apn3_name', shell=True)
    subprocess.call('adb shell rdb set link.profile.1.writeflag 1', shell=True)
    time.sleep(1)
    
def change_ip_type():
    subprocess.call('adb shell rdb set link.profile.4.pdp_type ipv4v6', shell=True)
    time.sleep(1)
    subprocess.call('adb shell rdb set link.profile.4.writeflag 1', shell=True)
    time.sleep(1)
    subprocess.call('adb shell rdb set link.profile.1.enable 1', shell=True)
    time.sleep(1)
    
    
def disable_apn():
    subprocess.call('adb shell rdb set link.profile.1.enable 0', shell=True)
    subprocess.call('adb shell rdb set link.profile.2.enable 0', shell=True)
    subprocess.call('adb shell rdb set link.profile.3.enable 0', shell=True)

def signal_strength():
    subprocess.call('adb shell rdb dump signal', shell=True)

def registration_status():
    subprocess.call('adb shell rdb dump network_status', shell=True)

def cell_signal_measurements():
    subprocess.call('adb shell rdb dump cell_measurement', shell=True)

def cell_scanned():
    subprocess.call('adb shell rdb dump rrc_info.cell', shell=True)
    

        
if option == '1':
    sim_status()
    
elif option == '2':
    imei()
    
elif option == '3':
    ims_status()
    
elif option == '4':
    data_profile()
    
elif option == '5':
    print("**WARNING**")
    print("This will set APN. Press Enter to continue or Press Q to quit")
    change_and_enable_apn()
    
elif option == '6':
    print("**WARNING**")
    print("This will set the IP type to IPV4V6 by default. Press Enter to continue or Press Q to quit")
    change_ip_type()
    
elif option == '7':
    print("**WARNING**")
    print("This will disable all APNs")
    disable_apn()
    
elif option == '8':
    signal_strength()
    
elif option == '9':
    registration_status()
    
elif option == '10':
    cell_signal_measurements()

elif option == '11':
    cell_scanned()

elif option == 'q' or 'Q':
    print("Exit")
    exit()

else:
    print("Input Error.Exiting...")
    exit()



