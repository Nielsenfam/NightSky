use <pibase.scad>
use <ledmatrix.scad>

small = 0.1;

board_x = 85.0;
board_y = 56.0;

clearance = 2.0;
base_thickness = 1.0;
floor_thickness = 1.4;
base_x = board_x + base_thickness*2 + clearance*2;
base_y = 70.0;
base_z = 28.0;

board_dx = base_thickness + clearance;
board_dy = (base_y-board_y)/2;
board_dz = 4.0+2.0;

$fa = 1;
$fs = 1;

module base_volume()
{
  cube([base_x,base_y,base_z]);
}

module wall(length)
{
  cube([length, base_thickness, base_z]);
}


module floor()
{
  width = 7.0;
  tab();
  translate([0,base_y+tab_y,0]) tab();
  difference() {
    cube([base_x, base_y, floor_thickness]);
    translate([width,width,-small]) {
      cube([base_x-width*2, base_y-width*2, floor_thickness+small*2]);
    }
  }
}

module walls()
{
   // wall(base_x);        

    rotate([0,0,180]) {
     translate([-base_x,-base_y,0]) {
     wall(base_x);
     }
   }


   side_thickness = peg_or*1.2;
   rotate([0,0,90]) {
   translate([side_thickness*0.5,-(base_x+side_thickness*0.5),0]) {
     cube([base_y-side_thickness,side_thickness,base_z]);
    }
  }

  rotate([0,0,270]) {
   translate([-(base_y-side_thickness*0.5),-side_thickness*0.5,0]) {
      cube([base_y-side_thickness,side_thickness,base_z]);
    }
  }
}

peg_or = 3.6;
peg_ir = peg_or-0.7;
peg_cap = 5;
peg_pilot_ir = 1;
peg_pilot = 6;

module peg()
{
  cylinder(h=base_z, r=peg_or);
}

module peg_negative()
{
  translate([0,0,-small]) {
    cylinder(h=base_z-peg_cap+small, r=peg_ir);
  }
  translate([0,0,base_z-peg_pilot]) {
    cylinder(h=peg_pilot+small, r=peg_pilot_ir);
  }
}

module pegs()
{
  translate([0,peg_or,0]) peg();
  translate([base_x,peg_or,0]) peg();
  translate([0,base_y-peg_or,0]) peg();
  translate([base_x,base_y-peg_or,0]) peg();
}

module pegs_negative()
{
  translate([0,peg_or,0]) peg_negative();
  translate([base_x,peg_or,0]) peg_negative();
  translate([0,base_y-peg_or,0]) peg_negative();
  translate([base_x,base_y-peg_or,0]) peg_negative();
}

module base()
{
  translate([board_dx,board_dy,board_dz]) pibase();
  floor();
  difference() 
  {
    walls();
    translate([board_dx,board_dy,board_dz]) board();
  }
}

difference() 
{
  union() 
  {
    translate([board_dx, board_dy, board_dz]) %board();
    base();
    //%base_volume();
    pegs();
     translate([-peg_or,69,base_z+2.5])
       rotate([110,0,0])
          %led_matrix();
  }
  pegs_negative();
}

