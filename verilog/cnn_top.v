module cnn_top(

input clk,
input rst,

input [15:0] ecg_in,
input [15:0] key,

output [15:0] ecg_out

);

wire [15:0] encrypted;
wire [15:0] decrypted;

wire signed [15:0] x0,x1,x2,x3,x4;

wire signed [31:0] conv1_out;
wire signed [31:0] relu1_out;

wire signed [31:0] conv2_out;
wire signed [31:0] relu2_out;

wire signed [31:0] conv3_out;
wire signed [31:0] relu3_out;

wire signed [31:0] conv4_out;

wire signed [31:0] y;


/* Encryption */

xor_encrypt ENC(

.data_in(ecg_in),
.key(key),
.data_out(encrypted)

);


/* Input Buffer */

input_buffer BUF1(

.clk(clk),
.rst(rst),

.sample_in(encrypted),

.x0(x0),
.x1(x1),
.x2(x2),
.x3(x3),
.x4(x4)

);


/* Layer 1 */

conv1d C1(

.x0(x0),
.x1(x1),
.x2(x2),
.x3(x3),
.x4(x4),

.y(conv1_out)

);

relu R1(

.data_in(conv1_out),

.data_out(relu1_out)

);


/* Buffer 2 */

wire signed [15:0] b1_0,b1_1,b1_2,b1_3,b1_4;

input_buffer BUF2(

.clk(clk),
.rst(rst),

.sample_in(relu1_out[31:16]),

.x0(b1_0),
.x1(b1_1),
.x2(b1_2),
.x3(b1_3),
.x4(b1_4)

);


/* Layer 2 */

conv1d C2(

.x0(b1_0),
.x1(b1_1),
.x2(b1_2),
.x3(b1_3),
.x4(b1_4),

.y(conv2_out)

);

relu R2(

.data_in(conv2_out),

.data_out(relu2_out)

);


/* Buffer 3 */

wire signed [15:0] b2_0,b2_1,b2_2,b2_3,b2_4;

input_buffer BUF3(

.clk(clk),
.rst(rst),

.sample_in(relu2_out[31:16]),

.x0(b2_0),
.x1(b2_1),
.x2(b2_2),
.x3(b2_3),
.x4(b2_4)

);


/* Layer 3 */

conv1d C3(

.x0(b2_0),
.x1(b2_1),
.x2(b2_2),
.x3(b2_3),
.x4(b2_4),

.y(conv3_out)

);

relu R3(

.data_in(conv3_out),

.data_out(relu3_out)

);


/* Buffer 4 */

wire signed [15:0] b3_0,b3_1,b3_2,b3_3,b3_4;

input_buffer BUF4(

.clk(clk),
.rst(rst),

.sample_in(relu3_out[31:16]),

.x0(b3_0),
.x1(b3_1),
.x2(b3_2),
.x3(b3_3),
.x4(b3_4)

);


/* Layer 4 */

conv1d C4(

.x0(b3_0),
.x1(b3_1),
.x2(b3_2),
.x3(b3_3),
.x4(b3_4),

.y(conv4_out)

);

assign y = conv4_out;


/* Decryption */

xor_encrypt DEC(

.data_in(y[31:16]),
.key(key),

.data_out(decrypted)

);

assign ecg_out = decrypted;

endmodule