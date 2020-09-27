#!/usr/bin/env python
#!coding=utf-8
import IPy

ip = IPy.IP('172.27.30.0/24')

for i in ip:
    print(i)
print(ip.len ())

