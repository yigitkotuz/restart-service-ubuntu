#!/bin/bash

remote_user="root"
remote_server="192.168.1.1"
service_name="network"

ssh "$remote_user"@"$remote_server" "/etc/init.d/$service_name restart"
