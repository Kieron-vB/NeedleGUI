#main test folder
#In the GUI the user can initialize the connection to gpredict or to the serial port

#Data to/from gpredict will come through socket_attachment to the datahandler
#Data to/from the arduino will come through serial_connector to the datahandler

#All the active data will get held onto by the datahandler  landline error

import data_handler
import gui_main
import serial_connector #REMOVE LATER
import socket_attachment #REMOVE LATER

if __name__ == "__main__":
    
    #Start the gui and initialize the data handler
    core_info = data_handler.CoreInfo()
    window = gui_main.MainWindow(core_info)

    #Testing the serial connection:
    #ser = serial_connector.SerialHandler(PORT="/dev/ttyUSB0")
    #ser.manual_input()
    #ser.close_connection()
    
    #Testing the socket connection:
    #sock = socket_attachment.SocketGrabber()
    #sock.blocking_recv()

    #MAIN LOOP:
    while True:
        core_info.update()
