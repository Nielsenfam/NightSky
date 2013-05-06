//
// box for Night Sky Orb LED clock
//   designed by: Terry Nielsen
//

include <NSParams.scad>

//
// draw back panel
//

cube(size=[(box_width-wall_thickness*2)-0.5,
           (box_width-wall_thickness*2)-0.5,
           back_panel_thickness]);

