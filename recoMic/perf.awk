BEGIN {
  cputime = 0.0;
  xrealtime = 0.0;
  walltime = 0.0;
  xwall = 0.0;
  utterances = 0;
}
( $3 == "TOTAL" && $6 == "CPU") { 
  cputime+=$5;
  xrealtime +=$7 } 
( $3 == "TOTAL" && $6 == "wall") {
  walltime+=$5;
  xwall+=$7; }
( $3 == "Utterance" ) {
  utterances += 1;
} 
END {
 print "Utterances=" utterances;
 print "CpuTime=" cputime " seconds";
 print "CPU xRealTime=" xrealtime " or " xrealtime*100 "% of one core"
 print "Actual Speech=" cputime/xrealtime " seconds";
 print "Utterances=" walltime " seconds total";
 printf "%.0f%s of utterances were speech \n", 100/xwall, "%";

}

