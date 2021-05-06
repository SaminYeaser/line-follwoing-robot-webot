"""line_follower controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
time_step = 32
max_speed = 6.28

#motor
left_motor = robot.getMotor('left wheel motor')
right_motor = robot.getMotor('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

#ir sensor

right_ir = robot.getDevice('rt')
right_ir.enable(time_step)

mid_ir = robot.getDevice('md')
mid_ir.enable(time_step)

left_ir = robot.getDevice('lf')
left_ir.enable(time_step)



while robot.step(timestep) != -1:
   right_ir_val = right_ir.getValue()
   mid_ir_val = mid_ir.getValue()
   left_ir_val = left_ir.getValue()
   
   print("left: {} mid:{} right: {}".format(left_ir_val,mid_ir_val,right_ir_val))
   
   left_speed = max_speed
   right_speed = max_speed
   
   if left_ir_val<700 and right_ir_val<700 and mid_ir_val>=700:
       left_motor.setVelocity(-left_speed)
       right_motor.setVelocity(-right_speed)
   if left_ir_val<700 and right_ir_val>=700 and mid_ir_val>=700:
       left_motor.setVelocity(-left_speed)
       right_motor.setVelocity(0)
   if left_ir_val>=700 and right_ir_val<700 and mid_ir_val>=700:
       left_motor.setVelocity(0)
       right_motor.setVelocity(-right_speed) 
   if left_ir_val>=700 and right_ir_val<700 and mid_ir_val<700:
       left_motor.setVelocity(0)
       right_motor.setVelocity(-right_speed)
   if left_ir_val<700 and right_ir_val>=700 and mid_ir_val<700:
       left_motor.setVelocity(-left_speed)
       right_motor.setVelocity(0)
   if left_ir_val<700 and right_ir_val<700 and mid_ir_val<700:
       left_motor.setVelocity(-left_speed)
       right_motor.setVelocity(-right_speed)
   pass

