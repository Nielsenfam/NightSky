//
// box for Night Sky Orb LED clock
//   designed by: Terry Nielsen
//

include <NSParams.scad>

// A simple decorative frame to go on front panel

// draw box lip
difference() {
   cube(size=[box_width,box_width,lip_thickness]);
   translate([lip_width,lip_width,0])
      cube(size=[box_width-lip_width*2,
                 box_width-lip_width*2,
                 lip_thickness]);
}
