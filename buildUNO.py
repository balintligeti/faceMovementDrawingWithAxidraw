from pyaxidraw import axidraw  
import time 

print("test")

time.sleep (10) 
ad = axidraw.AxiDraw()
ad.plot_setup("g6.svg")
ad.options.port = "East"
ad.options.model = 2
ad.options.pen_pos_up = 98
ad.options.speed_pendown = 35
ad.options.const_speed = True
ad.options.pen_pos_down = 2
ad.plot_run()
print('done 1/11')
