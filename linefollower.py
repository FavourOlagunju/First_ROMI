
from wpilib import DigitalInput

class LineFollower:
   def __init__(self, drivetrain):
      self.drivetrain=drivetrain
      self.left_sensor= DigitalInput(8)
      self.right_sensor= DigitalInput(9)
   def run(self):
      left_data= self.left_sensor.get()
      right_data= self.right_sensor.get()
      if left_data== True:
         self.drivetrain.move(0.5,5)
      elif right_data== True:
         self.drivetrain.move(0.5,-5)
      elif left_data== True and right_data == True:
         self.drivetrain.move(0,90)

      else:
         self.drivetrain.move(1,0)





