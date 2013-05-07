//
// box for Night Sky Orb LED clock
//   designed by: Terry Nielsen
//

include <NSParams.scad>


//
// Build Walls of Box
//
difference() 
{
   cube(size=[box_width,
              box_width,
              box_depth],center=false);
   translate( [wall_thickness,wall_thickness,0]) 
      cube(size=[box_width-wall_thickness*2,
                 box_width-wall_thickness*2,
                 box_depth],center=false);
}

//
// Build Corner Braces
//

// corner at (0,0)
cube(size=[corner_size,corner_size,box_depth-corner_recess]);

// corner at (w,0)
translate( [box_width-corner_size,0,0])
   cube(size=[corner_size,corner_size,box_depth-corner_recess]);

// corner at (0,w)
translate( [0, box_width-corner_size,0])
   cube(size=[corner_size,corner_size,box_depth-corner_recess]);

// corner at (w,w)
translate( [box_width-corner_size, box_width-corner_size,0])
   cube(size=[corner_size,corner_size,box_depth-corner_recess]);
   
//
// Build Middle Braces
//

// middle brace at (0, w/2)
translate( [0, (box_width-corner_size)/2, 0])
   cube(size=[corner_size,corner_size,box_depth-corner_recess]);

// middle brace at (w/2, 0)
translate( [(box_width-corner_size)/2, 0, 0])
   cube(size=[corner_size,corner_size,box_depth-corner_recess]);

// middle brace at (w/2, w)
translate( [(box_width-corner_size)/2, box_width-corner_size, 0])
   cube(size=[corner_size,corner_size,box_depth-corner_recess]);

// middle brace at (w, w/2)
translate( [box_width-corner_size, (box_width-corner_size)/2, 0])
   cube(size=[corner_size,corner_size,box_depth-corner_recess]);

//
// Build Front Panel
//

// use this for panel with no holes
// cube(size=[box_width,box_width,panel_thickness]);

//
// Panel with holes
//
difference()
{
   cube(size=[box_width,box_width,panel_thickness]);
   
   // loop over x and y axis to create grid of holes
   for ( ix = [0 : led_row_count - 1 ] )
   {
      for ( iy = [0 : led_col_count -1 ] )
      {
         translate( [ led_hole_pattern_offset+ix*led_hole_spacing, 
                      led_hole_pattern_offset+iy*led_hole_spacing,
                      -0.5 ] )
         cylinder(h=panel_thickness+1, 
                  r1=led_hole_front_dia/2,
                  r2=led_hole_back_dia/2, 
                  $fn=led_resolution, center=false );
      }
   }
   
   // square holes for objects picts
   for ( iy = [0 : led_row_count - 1 ] )
   {
      translate( [ led_hole_pattern_offset-
                       (object_hole_size+object_grid_seperation), 
                   led_hole_pattern_offset+iy*led_hole_spacing, 
                   panel_thickness/2] )
         cube(size=[object_hole_size,
                    object_hole_size,
                    panel_thickness+2], center=true);
   }

   // place hour numbers across top
   for ( ix = [0 : led_col_count - 1 ] )
   {
      translate( [ 
                   led_hole_pattern_offset+ix*led_hole_spacing,  
                   led_hole_pattern_offset-
                       (object_hole_size+object_grid_seperation),
                   panel_thickness/2] )
         cube(size=[object_hole_size,
                    object_hole_size,
                    panel_thickness+2], center=true);
      
   }
}



