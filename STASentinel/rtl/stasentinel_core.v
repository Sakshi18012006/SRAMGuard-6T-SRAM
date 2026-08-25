// STASentinel educational RTL
module stasentinel_core (
    input wire clk,
    input wire rst_n,
    input wire [3:0] a,
    input wire [3:0] b,
    output reg [3:0] y
);
    reg [3:0] r1;
    reg [3:0] r2;
    wire [3:0] n1, n2, n3, n4;
    assign n1 = ~(r1 & b);
    assign n2 = ~n1;
    assign n3 = ~(n2 | a);
    assign n4 = ~n3;
    always @(posedge clk) begin
        if (!rst_n) begin r1 <= 4'b0; r2 <= 4'b0; y <= 4'b0; end
        else begin r1 <= a; r2 <= n4; y <= r2; end
    end
endmodule
