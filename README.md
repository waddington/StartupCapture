# Startup Capture Script

Python script to capture details about the device on startup.

Should the device get stolen, this laptop will hopefully help you recover it should it gain internet access.

## Information

- You will need to run a service on a remote server somewhere, so that the client can "call home".
- You will need to have a script run at startup on the client device; this will periodically try to call home.
