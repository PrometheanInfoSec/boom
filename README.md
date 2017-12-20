#Boom

Boom is an entirely digital deadman's switch.
It can be used to execute script(s) from a remote host via a handheld controller.

###Inventory
client.html --> A client page that can be run from any webserver.
relay.py --> A relay server that turns one client to many servers.
server.py --> A listener, armed on the first authenticated message.

###How to
Host client.html somewhere.
Host server.py (as many as you want) somewhere else.
If you have multiple server.py, host relay.py somewhere else.

Edit relay.py to point to all your server.py instances.

Edit server.py to have the commands to execute.. and the proper secret key.

Open client.html in your phone (or other device's browser).  It doesn't matter that it's hosted, because all the code in it runs client side.

Type in the secret key, and set your target (relay.py's url for multiple hosted server.py, or server.py's url for one instance of server.py).

Press down on the button.  If your finger comes off, the code executes.

Happy hunting.
