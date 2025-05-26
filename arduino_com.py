import serial
import time


class Arduino():
    def __init__(self):
        self.arduino = serial.Serial("/dev/ttyACM0", baudrate=9600)
        time.sleep(2)
        print("Init DOne")
        
    def send_message(self, msg):
        print(msg)
        msg = msg + '\n'
        while True:
            self.arduino.write(msg.encode('utf-8'))
            print("Message sent")
            # time.sleep(0.2)
            rec_msg = self.rec()

            if rec_msg == f"ACK{msg.strip()}":
                print("✅ ACK received: ", rec_msg)
                break
            else:
                print("❌ ", rec_msg)
                # time.sleep(0.5)
    def rec(self):
        print("Message reader started")
        msg_decoded = self.arduino.readline().decode('utf-8').strip() 
        print(f"Message received: {msg_decoded}")
        return msg_decoded
