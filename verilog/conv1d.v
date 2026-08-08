module conv1d(

input signed [15:0] x0,
input signed [15:0] x1,
input signed [15:0] x2,
input signed [15:0] x3,
input signed [15:0] x4,

output signed [31:0] y

);

parameter signed w0 = 16'd3097;
parameter signed w1 = 16'd12185;
parameter signed w2 = -16'd4601;
parameter signed w3 = -16'd8618;
parameter signed w4 = -16'd5184;

assign y =
        x0*w0 +
        x1*w1 +
        x2*w2 +
        x3*w3 +
        x4*w4;

endmodule