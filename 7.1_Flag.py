'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
'''


import arcade
Flag_Height = 260
Flag_Width = round(1.9 * Flag_Height)
print(Flag_Width)
Union_Height = round(Flag_Height * 7 / 13)
Union_Width = round(Flag_Width * 2 / 5)
print(Union_Width)
Stripe_Height = round(Flag_Height/13)
starcount = [6,5,6,5,6,5,6,5,6]

arcade.open_window(Flag_Width,Flag_Height,"The Stars and Stripes")
arcade.set_background_color(arcade.color.CARDINAL)
starx = round(Union_Width/12)
stary = round(Union_Height/10)

arcade.start_render()

Stripe_Center = round(Stripe_Height/2) + Stripe_Height
while Stripe_Center < Flag_Height:
    arcade.draw_line(0, Stripe_Center, Flag_Width, Stripe_Center, arcade.color.WHITE, Stripe_Height)
    Stripe_Center += (Stripe_Height * 2)

arcade.draw_lrtb_rectangle_filled(0,Union_Width,Flag_Height,Flag_Height-Union_Height,arcade.color.SAPPHIRE)

x=0
for count in starcount:
    i = 1
    if count == 5:
        str_pos = starx * 2
    else:
        str_pos = starx
    while (i <= count):
        arcade.draw_text("*",str_pos + (starx * (i-1) *2) - 4 , Flag_Height- Union_Height + (stary * x),arcade.color.WHITE,20)
        i += 1
    x += 1
arcade.run()