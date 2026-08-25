# STASentinel SDC constraints
create_clock -name CLK -period 1.00 -waveform {0.00 0.50} [get_ports clk]
set_clock_uncertainty -setup 0.05 [get_clocks CLK]
set_clock_uncertainty -hold 0.03 [get_clocks CLK]
set_input_delay 0.10 -clock CLK [get_ports {a[*] b[*]}]
set_output_delay 0.10 -clock CLK [get_ports {y[*]}]
set_input_transition 0.05 [get_ports {a[*] b[*]}]
set_load 0.02 [get_ports {y[*]}]
set_false_path -from [get_ports rst_n]
# Example only; enable only when functionally justified:
# set_multicycle_path 2 -setup -from [get_clocks CLK] -to [get_clocks CLK]
# set_multicycle_path 1 -hold -from [get_clocks CLK] -to [get_clocks CLK]
