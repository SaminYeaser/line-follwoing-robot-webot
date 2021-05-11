from controller import Robot


def run_robot(robot):
    time_step = 32
    max_speed = 6.28

    
    wheels = []
    wheelsNames = ['wheel1', 'wheel2','wheel3','wheel4']
    for i in range(4):
            wheels.append(robot.getDevice(wheelsNames[i]))
            wheels[i].setPosition(float('inf'))
            wheels[i].setVelocity(1.0)
            
    left_ir = robot.getDevice('lf')
    left_ir.enable(time_step)
                    
    right_ir = robot.getDevice('rt')
    right_ir.enable(time_step)
    while robot.step(time_step)  != -1:

                        #read ir sensors
                        

                       left_ir_value = left_ir.getValue()
                       right_ir_value = right_ir.getValue()
                
                       print("left: {} right: {}".format(left_ir_value, right_ir_value))
                
                
                       left_speed = max_speed * 0.25
                       right_speed = max_speed * 0.25
                
                       if (left_ir_value > right_ir_value) and (left_ir_value > 450):
                                print("Go left")
                                left_speed = -max_speed * 0.25
                       elif (right_ir_value > left_ir_value) and (right_ir_value > 490):
                                print("Go right")
                                right_speed = -max_speed * 0.25
                           
                       wheels[0].setVelocity(left_speed)
                       wheels[1].setVelocity(right_speed)
                       wheels[2].setVelocity(left_speed)
                       wheels[3].setVelocity(right_speed)
    
       
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)