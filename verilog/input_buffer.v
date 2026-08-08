module input_buffer(

input clk,
input rst,

input signed [15:0] sample_in,

output reg signed [15:0] x0,
output reg signed [15:0] x1,
output reg signed [15:0] x2,
output reg signed [15:0] x3,
output reg signed [15:0] x4

);

always @(posedge clk or posedge rst)

begin

    if(rst)

    begin

        x0 <= 0;
        x1 <= 0;
        x2 <= 0;
        x3 <= 0;
        x4 <= 0;

    end

    else

    begin

        x4 <= x3;
        x3 <= x2;
        x2 <= x1;
        x1 <= x0;
        x0 <= sample_in;

    end

end

endmodule