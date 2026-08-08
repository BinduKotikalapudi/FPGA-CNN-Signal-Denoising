module conv_layer1(

input clk,

input signed [15:0] x0,x1,x2,x3,x4,

output signed [31:0] y

);

reg [6:0] addr;

wire signed [15:0] weight;

blk_mem_gen_0 conv1_weights(

.clka(clk),

.addra(addr),

.douta(weight)

);

reg signed [15:0] w0,w1,w2,w3,w4;

reg [2:0] state = 0;

always @(posedge clk)

begin

case(state)

0: begin addr<=0; state<=1; end
1: begin w0<=weight; addr<=1; state<=2; end
2: begin w1<=weight; addr<=2; state<=3; end
3: begin w2<=weight; addr<=3; state<=4; end
4: begin w3<=weight; addr<=4; state<=5; end
5: begin w4<=weight; state<=6; end

endcase

end

conv1d CONV(

.x0(x0),
.x1(x1),
.x2(x2),
.x3(x3),
.x4(x4),

.y(y)

);

endmodule