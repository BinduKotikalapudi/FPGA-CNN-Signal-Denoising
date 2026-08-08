module conv_layer3(

input clk,

input signed [31:0] in_data,

output signed [31:0] y

);

reg [11:0] addr;

wire signed [15:0] weight;

blk_mem_gen_2 conv3_weights(

.clka(clk),

.addra(addr),

.douta(weight)

);

wire signed [15:0] x;

assign x = in_data[31:16];

conv1d CONV(

.x0(x),
.x1(x),
.x2(x),
.x3(x),
.x4(x),

.y(y)

);

endmodule