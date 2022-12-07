#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500,400,"my drawling")
arcade.set_background_color(arcade.color.ALMOND)



arcade.start_render()
for X_offset in range (0,501,20):
    arcade.draw_line(X_offset,0,X_offset,500,arcade.color.BLACK)
for Y_offset in range (0,401,20):
    arcade.draw_line(0,Y_offset,600,Y_offset, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(20,80,380,360,arcade.color.PHLOX)

arcade.draw_line(10,10,10,10,arcade.color.GREEN,1)

#arcade.draw_circle_filled(400,320,60,arcade.color.GOLD)

arcade.draw_ellipse_filled(100,100,120,40,arcade.color.GOLD)

arcade.draw_line(120,60,80,20,arcade.color.BLUE,3)

#arcade.draw_triangle_filled(400,320,450, 340,340,300,arcade.color.BLUE)
arcade.draw_arc_filled(400,320,120,120,arcade.color.YELLOW,30,330)
arcade.draw_circle_filled(250,200,40,arcade.color.WISTERIA)
arcade.draw_rectangle_filled(200,260,40,20,arcade.color.BLUSH,-45)
#arcade.draw_rectangle_outline(200,200,100,10,arcade.color.BLUE,20,30)

arcade.draw_text("I love you. I know.",20,160,arcade.color.BRICK_RED,20)
arcade.draw_rectangle_filled(460,10,8,8,arcade.color.RED)
#command i


arcade. finish_render()





arcade.run()


