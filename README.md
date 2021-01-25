# Device_Automation

## Abstract:
The goal is to trigger 'AT Commands' and 'Android Debug Commands (ADB commands)' to the device from the laptop to control device operations.

## Context:
1. In order to evaluate device performance for its ability to reliably attach to the netwrok, repeated airplane mode on/off test is performed.
The manual process is tediuos especially when thousands of attach/detach process needs to be trigerred.
2. Need for retrieving/configuring device parameters using ADB commands in a seamless manner. 

## Scritp Description:
PC connected to the Phone over USM cable.
The script is able to trigger attach/detach commands to the device. User is prompted for options to detach/attach to the network.
Several Android Debug commands can be trigerred from the laptop to retrieve and configure changes/settings on the device.


## Tools
- Python programming
- Serial library 
- Subprocess library

## Diagram

![final](https://user-images.githubusercontent.com/77254370/105671825-2f81ae80-5e98-11eb-8cb6-4c6583d75702.JPG)
