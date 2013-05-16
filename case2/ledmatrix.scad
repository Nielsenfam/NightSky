led_radius = 2.6;
led_separation = 2*led_radius + 3.5;

// Distance from the boarder to the first led.
boarder = 16;
boarder_bottom = boarder+4.0;

// General meterial thickness
thickness = 2.0;

led_distance_height = 4.0;
led_distance_thickness = 0.75;

// Frame parameters
frame_thickness = 2.0;
frame_height = 8.0;

// Number of leds in each direction
grid_x = 8;
grid_y = 8;

stand_width = 7;
stand_angle = 20;

board_depth = 66.0;
board_height = 2.55;


$fn=50;

// End config
width = led_separation*(grid_x-1) + 2*led_radius + boarder*2;
height = led_separation*(grid_y-1) + 2*led_radius + boarder + boarder_bottom;

echo("Width: ", width); 
echo("Height: ", height);


module _led_grid() {
	difference() {
		union() {
			cube([width, height, thickness]);

			translate([boarder + led_radius, boarder_bottom + led_radius, 0])
			for(r = [0:grid_x-1]) {
				for(c = [0:grid_y-1]) {
					translate([r*led_separation, c*led_separation, 0])
					cylinder(r=led_radius+led_distance_thickness, h=led_distance_height);
				}
			}
		}

		translate([boarder + led_radius, boarder_bottom + led_radius, 0])
		for(r = [0:grid_x-1]) {
			for(c = [0:grid_y-1]) {
				translate([r*led_separation, c*led_separation, -1])
				cylinder(r=led_radius, h=led_distance_height+2);
			}
		}

		
	}
}

module _frame() {
	difference() {
		cube([width, height, frame_height]);
	
		translate([frame_thickness, frame_thickness, -1])
		cube([width-2*frame_thickness, height-2*frame_thickness, frame_height+2]);
	}
}

module _stand() {
	difference() {
	translate([0, -tan(stand_angle)*frame_height,0])
	rotate([90-stand_angle, 0, 0])
	translate([0,0, -(2*thickness+board_height)])
	difference() {
		union() {
			cube([stand_width, board_depth+2*thickness, thickness*2+board_height]);

			translate([width-stand_width, 0, 0])
			cube([stand_width, board_depth+2*thickness, thickness*2+board_height]);
		}

		translate([thickness, thickness, thickness-3])
		  cube([width-2*thickness, board_depth+4, board_height+3 ]);
        
        translate([width-3.5, (69.95-3.6), 2])
          cylinder(r=1,h=thickness*4);

        translate([3.6, (69.95-3.6), 0])
          cylinder(r=1,h=thickness*4);

        translate([3.6, 3.6, 0])
          cylinder(r=1,h=thickness*4);

       translate([width-3.5, 3.6, 2])
          cylinder(r=1,h=thickness*4); 

	}


	translate([-width/2, -height/2, -frame_height*2])
	cube([width*2, height*2, frame_height*2]);
	}
}

module led_matrix() {
	union() {
		_led_grid();
		_frame();
		_stand();
	}
}

led_matrix();








