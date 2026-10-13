# Additional exercises

Questions supplied with the lab material. These are optional extensions to the main experiment.

Scenario 1: Chat Room System
Situation
A university wants to create multiple chat rooms such as:
Computer Networks
Operating Systems
Cyber Security
Students should only see messages from the room they joined.
Task
Enhance the chat server to support multiple chat rooms.
Questions
What new data structure is required to store chat rooms?
How can the server track which client belongs to which room?
What change is needed in the broadcast function?
How will clients select a room after connecting?
Scenario 2: Limiting Maximum Clients
Situation
The server should only allow 10 clients at a time to prevent overload.
Task
Modify the server so that if the maximum number of clients is reached, new users will receive the message:
Server is full. Try again later.
Questions
Where does the server accept new client connections?
How can the server check the number of connected clients?
What message should be sent before closing the connection?
Why do real servers limit connections?
Scenario 3: Internet-Based Chat Server
Situation
Currently, the chat server runs only on localhost. Students from different computers in the lab cannot connect.
Task
Modify the program so that the chat server can run on a LAN network.
Questions
Which IP address should replace 127.0.0.1?
How will clients know the server’s IP address?
What network issues may occur in real environments?
Why is port configuration important in networking?
Scenario 4: Private Messaging Feature
Situation
In the current chat system, every message is broadcast to all clients. In real messaging applications, users can send private messages.
Task
Modify the chat system so that a user can send a private message using the format:
@username message
Example:
@Bob Hello Bob!
 Questions
How can the server identify the target user from the message?
What modification is required in the broadcast() function?
How should the server search for the correct client socket?
What should happen if the username does not exist?
