from wpilib import DigitalInput

class LineFollower:
   def __init__(self, drivetrain):
      self.drivetrain=drivetrain
      self.left_sensor= DigitalInput(8)
      self.right_sensor= DigitalInput(9)
   def run(self):
      left_data= self.left_sensor.get()
      right_data= self.right_sensor.get()
      print(f"left:{left_data} right:{right_data}")
      if left_data and not right_data:
         self.drivetrain.move(-0.5, 0)
         print(left_data)
      elif right_data and not left_data:
         self.drivetrain.move(0.5,0)
         print(right_data)
      else:
         self.drivetrain.move(0, -0.5)





