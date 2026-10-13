# Experiment 9 — Distance Vector routing using NS2

[Back to experiment index](../README.md)

Run this Tcl script with NS2. Output below describes the expected behavior rather than a recorded simulation run.

## Aim

To simulate Distance Vector routing and observe route changes after link failure and recovery.

## Algorithm

1. Create an NS2 simulator and enable DV routing.
2. Open packet and NAM trace files.
3. Create eight nodes connected in a ring.
4. Attach UDP/CBR traffic to the source and a Null sink to the destination.
5. Start traffic at 0.5 seconds.
6. Bring the link between n3 and n4 down at one second and restore it at two seconds.
7. Stop traffic at 4.5 seconds.
8. Finish at five seconds, close the trace files, and open NAM.

## Program

Source file: [distance_vector.tcl](distance_vector.tcl)

Run from this experiment folder:

```bash
ns distance_vector.tcl
```

Requires NS2 and NAM. The script generates `out.nam` and `trace.tr`.

```tcl
# Create simulator
set ns [new Simulator]

# Enable Distance Vector routing
$ns rtproto DV

# Trace files
set nf [open out.nam w]
$ns namtrace-all $nf

set nt [open trace.tr w]
$ns trace-all $nt

# Finish procedure
proc finish {} {
    global ns nf nt
    $ns flush-trace
    close $nf
    close $nt
    exec nam -a out.nam &
    exit 0
}

# Create nodes
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]
set n7 [$ns node]
set n8 [$ns node]

# Create links
$ns duplex-link $n1 $n2 1Mb 10ms DropTail
$ns duplex-link $n2 $n3 1Mb 10ms DropTail
$ns duplex-link $n3 $n4 1Mb 10ms DropTail
$ns duplex-link $n4 $n5 1Mb 10ms DropTail
$ns duplex-link $n5 $n6 1Mb 10ms DropTail
$ns duplex-link $n6 $n7 1Mb 10ms DropTail
$ns duplex-link $n7 $n8 1Mb 10ms DropTail
$ns duplex-link $n8 $n1 1Mb 10ms DropTail

# Link orientation (for NAM)
$ns duplex-link-op $n1 $n2 orient left-up
$ns duplex-link-op $n2 $n3 orient up
$ns duplex-link-op $n3 $n4 orient right-up
$ns duplex-link-op $n4 $n5 orient right
$ns duplex-link-op $n5 $n6 orient right-down
$ns duplex-link-op $n6 $n7 orient down
$ns duplex-link-op $n7 $n8 orient left-down
$ns duplex-link-op $n8 $n1 orient left

# UDP Agent
set udp0 [new Agent/UDP]
$ns attach-agent $n1 $udp0

# CBR Traffic
set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 500
$cbr0 set interval_ 0.005
$cbr0 attach-agent $udp0

# Null Agent (Sink)
set null0 [new Agent/Null]
$ns attach-agent $n4 $null0

# Connect UDP to Null
$ns connect $udp0 $null0

# Labels
$ns at 0.0 "$n1 label Source"
$ns at 0.0 "$n4 label Destination"

# Start traffic
$ns at 0.5 "$cbr0 start"

# Link failure and recovery
$ns rtmodel-at 1.0 down $n3 $n4
$ns rtmodel-at 2.0 up $n3 $n4

# Stop traffic
$ns at 4.5 "$cbr0 stop"

# End simulation
$ns at 5.0 "finish"

# Run simulation
$ns run
```

## Output

Expected output; the supplied document contains no output screenshot, and NS2 is unavailable here:

- NAM displays an eight-node ring with the source and destination labeled.
- Traffic initially follows the shorter route `n1 → n2 → n3 → n4`.
- The `n3–n4` link fails at 1.0 s, triggering routing updates.
- After DV convergence, traffic can use `n1 → n8 → n7 → n6 → n5 → n4`.
- The failed link recovers at 2.0 s; later routing updates can restore the shorter route.
- The simulation finishes at 5.0 s.

The Tcl variables are named `n1`–`n8`, while NS2 assigns node IDs starting at 0. Timing of convergence and any packet loss should be observed in NAM and the trace.

## Result

The experiment demonstrates how Distance Vector routing exchanges distance information and adapts routes after a topology change. Confirm the route transitions by running the simulation.
