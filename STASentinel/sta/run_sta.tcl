# OpenSTA signoff-style analysis
read_liberty ../library/stasentinel_cells.lib
read_verilog ../synthesis/synthesized_netlist.v
link_design stasentinel_core
read_sdc ../constraints/timing.sdc
report_clocks
report_checks -path_delay max -digits 3 > ../reports/setup.rpt
report_checks -path_delay min -digits 3 > ../reports/hold.rpt
report_worst_slack -max -digits 3 > ../reports/worst_setup_slack.rpt
report_worst_slack -min -digits 3 > ../reports/worst_hold_slack.rpt
report_tns -max -digits 3 > ../reports/tns_setup.rpt
report_tns -min -digits 3 > ../reports/tns_hold.rpt
