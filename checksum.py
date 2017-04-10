#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        checksum.py
#
# Author:      Grant Curell
#
# Created:     16 Sept 2012
#
# Description: Calculates the checksum for an IP header
#-------------------------------------------------------------------------------
    
    
def ip_checksum(ip_header, size):
    
    cksum = 0
    pointer = 0
    
    while size > 1:
        cksum += int(((ip_header[pointer][0]) << 8)+(ip_header[pointer+1][0]))
        
        #cksum += int((str("%02x" % (ip_header[pointer],)) + 
        #              str("%02x" % (ip_header[pointer+1],))), 16)
        # print cksum
        # print size
        size -= 2
        pointer += 2
    if size: #This accounts for a situation where the header is odd
        cksum += ip_header[pointer][0]
    cksum = (cksum >> 16) + (cksum & 0xffff)
    cksum += (cksum >>16)
    
    return (~cksum) & 0xFFFF