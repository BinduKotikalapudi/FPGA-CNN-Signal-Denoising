module xor_encrypt(

input [15:0] data_in,
input [15:0] key,

output [15:0] data_out

);

assign data_out = data_in ^ key;

endmodule