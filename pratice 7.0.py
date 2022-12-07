#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(600,600,"my drawling")
arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

arcade.start_render()
arcade.draw_lrtb_rectangle_filled(200,300,200,0,arcade.color.AIR_SUPERIORITY_BLUE)
arcade.draw_rectangle_filled(300,300,400,400,(255,255,0),45)
#drawling stuff
arcade.draw_rectangle_outline(300,300,400,400,(0,0,0),3,45)
arcade.draw_line(100,100,500,500,(255,0,0),4)
arcade.draw_circle_filled(300,300,50,(255,255,255),200)
arcade.draw_circle_outline(300,300,50,(255,255,255),200)

arcade.draw_ellipse_filled(400,400,100,50,arcade.color.BATTLESHIP_GREY)
point_list=((100,100),(120,400),(200,400),(300,150))
arcade.draw_polygon_filled(point_list,arcade.color.FRENCH_RASPBERRY)

arcade.draw_text("pycasso",200,550,arcade.color.CARROT_ORANGE,20)

mypic = arcade.load_texture("images/pmg")
arcade.draw_texture_rectangle(550,100,mypic.height,mypic,45,200)
#command i
arcade. finish_render()


arcade.run()

