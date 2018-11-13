🥳 Renegade is working
Send file to bot to start upload

You have ${len(services)} services:

% for svc in services:
- ${svc.name} (${svc.mode})
% endfor

% if default_service:
Current default service is ${default_service}.
% else:
You have not set default service, running
/set_default_service to select default upload service.
% endif

<%include file="./bot_commands.mako"/>
