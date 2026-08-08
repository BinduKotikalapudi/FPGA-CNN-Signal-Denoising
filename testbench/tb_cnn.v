`timescale 1ns/1ps

module tb_cnn;

reg clk;

reg rst;

reg [15:0] ecg_in;

reg [15:0] key;

wire [15:0] ecg_out;

cnn_top DUT(

.clk(clk),

.rst(rst),

.ecg_in(ecg_in),

.key(key),

.ecg_out(ecg_out)

);

always #5 clk = ~clk;

initial

begin

clk = 0;

rst = 1;

key = 16'h55AA;

ecg_in = 0;

#20;

rst = 0;

#100 ecg_in = 120;

#100 ecg_in = 210;

#100 ecg_in = 180;

#100 ecg_in = 320;

#100 ecg_in = 280;

#100 ecg_in = 420;

#100 ecg_in = 360;

#200;

$finish;

end

endmodule