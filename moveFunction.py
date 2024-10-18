from pyaxidraw import axidraw  
ad = axidraw.AxiDraw()
ad.interactive()
ad.options.speed_pendown = 20
connected = ad.connect()
if not connected:
    quit()
ad.move(1, 1)
ad.line(1, 1)
ad.move(-2, -2)  # Pen-up move back to origin
ad.disconnect()