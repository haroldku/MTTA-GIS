#!/usr/bin/env python
import os
import StopTimes_XML

def add_stops_2_stoptimes(outbound, inbound):
    x = []
    y = []
    # print 'baa'
    # need to access xml for outbound
    # add trip_id,arrival_time,departure_time,stop_id,stop_sequence,stop_headsign,pickup_type,drop_off_type,shape_dist_traveled
    # add from xml file
    # to stop_times_new.txt
    x = StopTimes_XML.get_end_time(outbound)
    # now join entries for inbound
    y = StopTimes_XML.get_start_time(inbound)
    print x
    print y
    
def proc_rt_list():
    print 'proc_rt_list'
    if os.name == 'posix':
        str_name = '/Users/haroldkurth/Library/Mobile Documents/com~apple~CloudDocs/RideSystems/rt_list.csv'
    else:
        str_name = 'C:/Users/hkurth1348/iCloudDrive/RideSystems/rt_list.csv'
    handle = open(str_name)
    for line in handle:
        line = line.rstrip('\r\n')
        words = line.split(',')
        outbound = words[0]
        inbound = words[1]
        print outbound, ': ', inbound
        add_stops_2_stoptimes(outbound, inbound)
        # temporarily terminate for loop
        break
    
if __name__ == "__main__":
    proc_rt_list()