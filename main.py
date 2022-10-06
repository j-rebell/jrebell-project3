#Allows use of the arcade library for this program.
import arcade
#Setting my own variable to save keystrokes
ac = (arcade.color)
#Create window in a classic 4x3 format and set background color to something representing the sky
arcade.open_window(1024,768, "Art Class in CompSci")
arcade.set_background_color(ac.DARK_SKY_BLUE)
#Allows everything to be shown on screen
arcade.start_render()
#Stem of flower
arcade.draw_lrtb_rectangle_filled(0, 1024, 128, 0, ac.LAWN_GREEN)
#Pedals and center of flower
arcade.draw_lrtb_rectangle_filled(384, 416, 320, 64, ac.FERN_GREEN)
arcade.draw_arc_filled(400, 352, 64, 96, ac.PARADISE_PINK, -180, 360)
arcade.draw_arc_filled(368, 320, 96, 64, ac.PARADISE_PINK, -180, 360)
arcade.draw_arc_filled(432, 320, 96, 64, ac.PARADISE_PINK, -180, 360)
arcade.draw_arc_filled(400, 280, 64, 96, ac.PARADISE_PINK, -180, 360)
arcade.draw_circle_filled(400, 320, 32, ac.GOLDEN_YELLOW)
#Draw bee body
arcade.draw_ellipse_filled(512, 384, 64, 32, ac.CANARY_YELLOW)
arcade.draw_circle_filled(480, 384, 16, ac.CANARY_YELLOW)

arcade.draw_arc_outline(512, 400, 8, 16, ac.HONEYDEW, -180, 360, 4)
#Draw bee eye and antenna
arcade.draw_circle_filled(476, 390, 4, ac.BLACK)
arcade.draw_line(476, 400, 474, 408, ac.BLACK, 1)
#Bee stripes
arcade.draw_xywh_rectangle_filled(496, 370, 8, 28, ac.BLACK)
arcade.draw_xywh_rectangle_filled(512, 370, 8, 28, ac.BLACK)
arcade.draw_xywh_rectangle_filled(528, 374, 8, 20, ac.BLACK)
#Stinger
arcade.draw_triangle_filled(544, 380, 544, 388, 552, 384, ac.BLACK)
#Text at top right
arcade.draw_text("Jacob Rebell", 768, 640, ac.HONEYDEW, 16)
#Finshes rendering the window so it can be shown
arcade.finish_render()
#Keeps window alive
arcade.run()