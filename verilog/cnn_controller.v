module cnn_controller(

input clk,

output reg conv1_en,
output reg conv2_en,
output reg conv3_en,
output reg conv4_en

);

reg [2:0] state = 0;

always @(posedge clk)

begin

case(state)

0:

begin

conv1_en <= 1;
conv2_en <= 0;
conv3_en <= 0;
conv4_en <= 0;

state <= 1;

end

1:

begin

conv1_en <= 0;
conv2_en <= 1;

state <= 2;

end

2:

begin

conv2_en <= 0;
conv3_en <= 1;

state <= 3;

end

3:

begin

conv3_en <= 0;
conv4_en <= 1;

state <= 0;

end

endcase

end

endmodule