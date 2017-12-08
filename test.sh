#!/bin/bash
curl --dump-header - "127.0.0.1:8090/nextbus/agencylist/"
curl --dump-header - "127.0.0.1:8090/nextbus/routelist/?a=sf-muni"
curl --dump-header - "127.0.0.1:8090/nextbus/routeconfig/?a=sf-muni&r=N"
curl --dump-header - "127.0.0.1:8090/nextbus/predictions/?a=sf-muni&r=N&s=5205&useShortTitles=true"
curl --dump-header - "127.0.0.1:8090/api/v1/stats/"
curl --dump-header - "127.0.0.1:8090/nextbus/agencylist/"
