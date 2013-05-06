//
// box for Night Sky Orb LED clock
//   designed by: Terry Nielsen
//
//   Parameter File
//

//
// box parameters
//

// Square box of this size in mm

// test: box_width = 70;
box_width = 160;

// box is this deep in mm

// test: box_depth = 20;
box_depth = 40;

// box has walls this thick in mm
wall_thickness=5;

// box has corner braces this size in mm
corner_size = 15;

// make lip on decorative frame of front of panel
lip_width = 10;
lip_thickness = 3;

// front panel is this thick in mm
panel_thickness=5;

// back panel is this thick in mm
back_panel_thickness = 3;

// corner braces are recessed from the back
corner_recess=back_panel_thickness + 2;

//
// LED parameters
//

// number of LEDs in row:

// test: led_row_count = 2;
led_row_count = 8;
led_col_count = led_row_count; // make it a square grid

// LED hole resolution

led_resolution = 20;

// LED holes have this diamter in mm
led_hole_back_dia=5;

// make this bigger to make hole wider at front of panel
led_hole_front_dia=led_hole_back_dia*2;

// LED holes are spaced this far apart in the grid in mm
led_hole_spacing=15;

// LED grid hole pattern is offset from the sides this far:
led_hole_pattern_offset = 
    (box_width-led_hole_spacing*(led_row_count-1))/2;

//
// End of parameters
//
