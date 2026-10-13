# Additional exercises

Questions supplied with the lab material. These are optional extensions to the main experiment.

Scenario 1: Network Troubleshooting in a College Lab
Situation
The college internet is working, but some websites are not loading in browsers like Google Chrome.
The network administrator asks you to verify whether the issue is:
DNS problem
Port blocking
Server-side issue
You must test connectivity using the given Python socket client.

Tasks
Modify hostname:
"example.com"
"google.com"
"nonexistentdomain.xyz"
Change port:
80
81
443 (without SSL)
Record:
Output
Error messages
Response time
Scenario 2: Web Server Response Analysis
Situation
The IT department wants to analyze how web servers respond to different resource requests.
You are asked to test server behavior using manual HTTP requests.

Tasks
Change path variable to:
/
/index.html
/abcxyz
/robots.txt

 Questions
Identify status codes returned:
200
404
301
Extract:
Content-Type
Server
Date
What happens if you remove:
Host: {hostname}

Additional Task
Split headers and body using:
header, body = response.split("\r\n\r\n", 1)


Scenario 3: Performance Testing of Web Servers
Situation
The college wants to compare response time of different servers to choose a reliable hosting provider.
You are asked to measure latency using the socket client.

Tasks
Add:
import time
Measure response time for:
example.com
github.com
google.com
(HTTP only, port 80)
Scenario 4: Secure Communication Investigation
Situation
Students noticed that most websites use HTTPS instead of HTTP.
You are asked to investigate why your program fails with secure websites.

Tasks
Try:
hostname = "google.com"
port = 443
Observe output.
Modify program using SSL wrapper.
Compare HTTP vs HTTPS behavior.
