# CN LAB

Computer Networks laboratory record for Experiments 2–11.

Each experiment includes **Aim, Algorithm, Program, Output, and Result**. Experiments with multiple programs keep their parts together in the same folder. Open an experiment below to read the complete record and view its code and output.

| Experiment | Topic | Programs |
| --- | --- | --- |
| [EXP2](EXP2/README.md) | Network addressing and utilities | A–G: hostname, IP addresses, public IP, website IP, DNS, ping, ports |
| [EXP3](EXP3/README.md) | HTTP web client | TCP HTTP client |
| [EXP4](EXP4/README.md) | TCP echo | A: server · B: client |
| [EXP5](EXP5/README.md) | TCP multi-client chat | A: server · B: client |
| [EXP6](EXP6/README.md) | TCP file transfer | A: server · B: client |
| [EXP7](EXP7/README.md) | ARP and RARP | Address-resolution simulation |
| [EXP8](EXP8/README.md) | TCP and UDP in NS2 | Tcl simulation |
| [EXP9](EXP9/README.md) | Distance Vector routing | Tcl simulation |
| [EXP10](EXP10/README.md) | Link State routing | Tcl simulation |
| [EXP11](EXP11/README.md) | Local DNS server hostname and IP address | Supplied local-host program; see experiment note |

## Running the programs

- **Experiments 2–7 and 11:** Python 3. The programs use standard-library modules.
- **Experiments 4–6:** start the server before its client, in separate terminals.
- **Experiments 8–10:** NS2 and NAM. These programs are Tcl scripts and run with `ns filename.tcl`.
- Run commands from the relevant experiment folder. Hostnames, IP addresses, ports, and network output can vary between computers.

## Output and source notes

The record is based on the supplied lab documents and slides. Screenshots are taken from those materials. Added illustrative or expected outputs are labeled. Missing aims, algorithms, and results have been written to match each supplied program.

The Python files passed syntax checks. Local checks covered HTTP responses, echo communication, chat broadcasting, file transfer, and ARP/RARP simulation. The NS2 scripts passed Tcl completeness checks, but NS2/NAM were unavailable for simulation runs.

Experiment 11 retains the supplied title and program, with a note explaining that the program obtains local computer details rather than the configured DNS server’s identity.

## References

- [Python socket documentation](https://docs.python.org/3/library/socket.html)
- [NS2 manual](https://www.isi.edu/websites/nsnam/ns/doc/ns_doc.pdf)
