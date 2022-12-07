'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import arcade
arcade.open_window(900,900,"The Tie Fighter by Andrew Donoho")
arcade.set_background_color(arcade.color.WHITE)

# offset amounts
y=-75
x=500

arcade.start_render()

#Right wing Connection
arcade.draw_polygon_filled(((440,355),(440,540),(575,440),(575,365)),arcade.color.BLACK)

# draw Wings
arcade.draw_polygon_filled(((76,135),(35,450),(65,805),(250,855),(280,550),(260,243)),arcade.color.GRAY)
arcade.draw_polygon_filled(((76+x,135+y),(35+x,450+y),(65+x,805+y),(250+x,855+y),(280+x,550+y),(260+x,243+y)),arcade.color.GRAY)

# points for wing sections
polygon_points = [
 [[55,430],[140,460],[155,425],[90,170]]
,[[50,460],[75,765],[155,550],[143,500]]
,[[95,790],[240,830],[190,580],[176,568]]
,[[205,570],[250,825],[270,560],[230,545]]
,[[100,155],[175,422],[190,420],[245,240]]
,[[250,265],[270,525],[240,510],[200,425]]
       ]

# draw wing sections
for p1 in polygon_points:
    arcade.draw_polygon_filled(p1,arcade.color.BLACK)

    # draw wing sections offsets
    p2 = []
    for points in p1:
        p2.append([points[0]+x,points[1]+y])
    arcade.draw_polygon_filled(p2,arcade.color.BLACK)

# draw wing centers
arcade.draw_ellipse_filled(190,490,120,175,arcade.color.GRAY,0,-1)
arcade.draw_ellipse_filled(690,420,120,175,arcade.color.GRAY,0,-1)

# draw cockpit and connectors
arcade.draw_polygon_filled(((370,380),(370,530),(175,520),(175,465)),arcade.color.BLACK)
arcade.draw_circle_filled(415,450,100,arcade.color.GRAY)
arcade.draw_circle_filled(415,450,75,arcade.color.BLACK_OLIVE)
arcade.draw_line(415,487,415,550,arcade.color.GRAY,10)
arcade.draw_line(415,413,415,375,arcade.color.GRAY,10)
arcade.draw_line(468,397,362,503,arcade.color.GRAY,10)
arcade.draw_line(468,503,362,397,arcade.color.GRAY,10)
arcade.draw_line(340,450,400,450,arcade.color.GRAY,10)
arcade.draw_line(490,450,350,450,arcade.color.GRAY,10)
arcade.draw_ellipse_filled(415,450,75,75,arcade.color.GRAY)
arcade.draw_ellipse_filled(415,450,50,50,arcade.color.BLACK_OLIVE)
arcade.draw_circle_filled(370,370,5,arcade.color.NEON_GREEN)
arcade.draw_circle_filled(440,362,5,arcade.color.NEON_GREEN)

arcade.run()
