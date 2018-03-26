#!/bin/bash

systemctl $2 $1 | grep Active: > /var/www/html/cgi-bin/status.txt
