#!/usr/bin/env python
import os
from lxml import etree as ET
from lxml import objectify
from StringIO import StringIO
import RideSystems_XML
import Create_stop_times
from adj_dirid import get_adj_dirid
from xml.etree import ElementTree

import  xml
from collections import namedtuple
import csv



# ----------------------------------------------------------------------

def create_trip(data, itrip):
    """
    Create an appointment XML element
    """
    trip = objectify.Element(itrip)
    trip2 = objectify.SubElement(trip, itrip)
    trip2.trip_id = data["trip_id"]
    trip2.stop_sequence = data["stop_sequence"]
    trip2.arrival_time = data["arrival_time"]
    trip2.departure_time = data["departure_time"]
    return trip2


# ----------------------------------------------------------------------
def add_string(parent, attr, s):
    if len(attr) == 1:
        setattr(parent, attr[0], s)
    else:
        child = getattr(parent, attr[0], None)
        if child is None:
            child = objectify.SubElement(parent, attr[0])
        add_string(child, attr[1:], s)


# ----------------------------------------------------------------------
def create_xml():
    """
    Create an XML file
    """

    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <root>
    </root>
    '''

    root = objectify.fromstring(xml)
    print os.name
    if os.name == 'posix':
        str_name = '/Users/haroldkurth/Library/Mobile Documents/com~apple~CloudDocs/RideSystems/Source/google_transit/stop_times.txt'
    else:
        str_name = 'C:/Users/hkurth1348/iCloudDrive/RideSystems/Source/google_transit/stop_times.txt'
    name = raw_input("Enter file:")
    if len(name) < 1:
        name = str_name
    handle = open(name)
    current_group = None
    for line in handle:
        line = line.rstrip('\r\n')
        words = line.split(',')
        trip_id = words[0]
        arrival_time = words[1]
        departure_time = words[2]
        stop_id = words[3]
        stop_sequence = words[4]
        stop_headsign = words[5]
        pickup_type = words[6]
        dropoff_type = words[7]
        shape_dist_traveled = words[8]
        if trip_id == 'trip_id':
            continue
        my_trip = root.findall(".//*[@name='root']/trip")
        result = 0
        if current_group is None or trip_id != current_group.get('name'):
            # Start a new group
            current_group = objectify.SubElement(root, 'trip', name=trip_id, text=trip_id)
        # for child in my_trip:
        #     if child.find('trip_id').text == str(trip_id):
        #         result = 1
        # if result == 0:
        #     # add_string(root, ['T'+trip_id, ''], '')
        #     b = objectify.SubElement(root, 'trip', name=trip_id)
        b = current_group
        add_string(b, ['Seq_'+stop_sequence, 'trip_id'], trip_id)
        add_string(b, ['Seq_'+stop_sequence, 'stop_sequence'], stop_sequence)
        add_string(b, ['Seq_'+stop_sequence, 'arrival_time'], arrival_time)
        add_string(b, ['Seq_'+stop_sequence, 'departure_time'], departure_time)
        print trip_id, stop_sequence

    # remove lxml annotation
    objectify.deannotate(root)
    ElementTree.cleanup_namespaces(root)

    # create the xml string
    obj_xml = ElementTree.tostring(root,
                             pretty_print=True,
                             xml_declaration=True)

    try:
        with open("stop_times.xml", "wb") as xml_writer:
            xml_writer.write(obj_xml)
    except IOError:
        pass


def get_rt():
    if os.name == 'posix':
        str_name = '/Users/haroldkurth/Library/Mobile Documents/com~apple~CloudDocs/RideSystems/trips.xml'
    else:
        str_name = 'C:/Users/hkurth1348/iCloudDrive/RideSystems//trips.xml'
    name = raw_input("Enter file:")
    if len(name) < 1:
        name = str_name
    f = open(name)
    xml = f.read()
    f.close()

    tree = etree.parse(StringIO(xml))
    print tree.docinfo.doctype
    context = etree.iterparse(StringIO(xml))
    book_dict = {}
    for action, elem in context:
        if not elem.text:
            text = "None"
        else:
            text = elem.text
        print elem.tag + " => " + text
        book_dict[elem.tag] = text
        if elem.tag == "book":
            if text.beginswith("100"):
                books.append(book_dict)
                book_dict = {}
    print "end"


def parseBookXML(xmlFile):
    """"""

    context = etree.iterparse(xmlFile)
    book_dict = {}
    books = []
    for action, elem in context:
        if not elem.text:
            text = "None"
        else:
            text = elem.text
        print elem.tag + " => " + text
        book_dict[elem.tag] = text
        books.append(book_dict)
        book_dict = {}
    return books


def get_trip_end_time(trip_id):
    tree = etree.parse('stop_times.xml')
    root = tree.getroot()
    x = root.getchildren()
    for content in x:
        my_trip = content.get("name", "0")
        if my_trip == trip_id:
            print content.tag, content.attrib, my_trip
            return
    # for child in root:
    #     name = child.find('name')
    #     print(child.tag, child.attrib, name)

def get_trip_end_time_ret(trip_id):
    tree = ET.parse('stop_times.xml')
    root = tree.getroot()
    x = root.getchildren()
    for content in x:
        my_trip = content.get("name", "0")
        if my_trip == trip_id:
            print content.tag, content.attrib, my_trip
            return my_trip
    # for child in root:
    #     name = child.find('name')
    #     print(child.tag, child.attrib, name)

def get_rt_100(rt_list_2, wkdy, frmdwn):
    document = ElementTree.parse('trips.xml')
    for my_trip in document.findall(rt_list_2):
        # print 'Test:', my_trip.tag, my_trip.text
        # limits = document.find( 'TestLimits/TestLimit/PassLimits' )
        words = [1, 2, 3, 4, 5, 6, 7]
        for node in my_trip.getchildren():
            if node.tag == 'service_id':
                words[0] = node.text
            elif node.tag == 'route_id':
                words[1] = node.text
            elif node.tag == 'shape_id':
                words[2] = node.text
            elif node.tag == 'dir_id':
                words[3] = node.text
            elif node.tag == 'trip_headsign':
                words[4] = node.text
            elif node.tag == 'block_id':
                words[5] = node.text
            elif node.tag == 'trip_id':
                words[6] = node.text
        if words[0] == wkdy and words[3] == frmdwn:
            return words


def get_rt_100list(rt_list2, wkdy, frmdwn):
    mylist = []
    rt_list = namedtuple('rt_list', 'trip_id service_id dir_id')
    document = ElementTree.parse('trips.xml')
    for my_trip in document.findall(rt_list2):
        # print 'Test:', my_trip.tag, my_trip.text
        # mytrip  = my_trip.findall( 'trip_id' )
        mytrip = my_trip.getchildren()
        # for node in mytrip.findall(".//*[@dir_id='" + frmdwn + "']"):
        if mytrip[0].text == str(wkdy) and mytrip[3].text == str(frmdwn):
            # print mytrip[0].attrib, mytrip[0].text, mytrip[3].attrib, mytrip[3].text, mytrip[6].attrib, mytrip[6].text
            node = [mytrip[6].text, mytrip[0].text, mytrip[3].text]
            mylist.append(node)
 
    return mylist


# ----------------------------------------------------------------------
def get_end_time(new_trip):
    doc = ET.parse('stop_times.xml')
    # for my_trip in document.findall(".//*[@name='" + new_trip + "']"):
    root = doc.getroot()
    myend_time = ''
    my_list = []
    my_end_seq = ''
    for departure_time in root.iter('trip'):
        my_attr = departure_time.get("name")
        if my_attr == str(new_trip):
            # print departure_time.tag, departure_time.text
            node = departure_time.iter('departure_time')
            for child in node:
                # print child.tag, child.text
                myend_time = child.text
                for kid in child.iterancestors():
                    if kid.tag.startswith('Seq'):
                        for kid2 in kid.iterchildren():
                            if kid2.tag.startswith('stop'):
                                # print kid.tag, kid.text, kid2.tag, kid2.text
                                my_end_seq = kid2.text
            return new_trip, myend_time, my_end_seq


def get_start_time(new_trip):
    doc = ET.parse('stop_times.xml')
    # for my_trip in document.findall(".//*[@name='" + new_trip + "']"):
    root = doc.getroot()
    mystart_time = ''
    my_start_seq = ''
    my_list = []
    for departure_time in root.iter('trip'):
        my_attr = departure_time.get("name")
        if my_attr == str(new_trip):
            # print departure_time.tag, departure_time.text
            node = departure_time.iter('departure_time')
            for child in node:
                break
            #     gchild = child.getchildren()
            #     # print child.tag, child.text
            #     mystart_time = child.text
            #     # if child.tag == 'Seq_1':
            #     #     gchild = child.iter('departure_time')
            #     #     myend_time = gchild.text
            for kid in child.itersiblings(preceding = True):
                if kid.tag.startswith('stop'):
                    # print kid.tag, kid.text
                    my_start_seq = kid.text
                if kid.tag.startswith('arrival'):
                    # print kid.tag, kid.text
                    mystart_time = kid.text
            return new_trip, mystart_time, my_start_seq

    return new_trip, mystart_time


def get_key(item):
    return item[0]

def create_route_list():
    # get weekday service from downtown
        wkdy = '1'
        frmDwn = '1'
        my_rt_list = ".//*[@name='RT_101']/trip"
        data = get_rt_100(my_rt_list, wkdy, frmDwn)
        for my_str in data:
            print my_str
        end_time = get_end_time(data[6])
        print end_time
        # my_rt_list = ".//*[@name='RT_101']/trip"
        my_list2 = get_rt_100list(my_rt_list, wkdy, frmDwn)
        myroute_from = []
        for line in my_list2:
            end_time2 = get_end_time(line[0])
            print end_time2
            i_sec = end_time2[1].split(':')
            isec = int(i_sec[2]) + (int(i_sec[1]) * 60) + (int(i_sec[0]) * 60 * 60)
            myroute_from.append([isec,line[0],end_time2[1]])
        mylist = get_rt_100list(my_rt_list, wkdy, 0)
        myroute_to = []
        print '--------- start time -------------'
        for line2 in mylist:
            start_time = get_start_time(line2[0])
            # print start_time
            my_sec = start_time[1].split(':')
            mysec = int(my_sec[2]) + (int(my_sec[1]) * 60) + (int(my_sec[0]) * 60 * 60)
            # print mysec
            # if mysec > isec:
            myroute_to.append([mysec, line2[0],start_time[1]])
        srtd_myroute_from =  sorted(myroute_from, key=get_key)
        srtd_myroute_to = sorted(myroute_to, key=get_key)
        print srtd_myroute_from
        print srtd_myroute_to

        # print data[6], my_route[0]
        # equate each outbound route to an inbound route
        cat_rts = []
        for each in srtd_myroute_from:
            for each2 in srtd_myroute_to:
                if int(each2[0]) > int(each[0]):
                    print each[1], '--> ', each2[1]
                    cat_rts.append([each[1], each2[1]])
                    break

        #for entry in cat_rts:
        #    print entry[0], '--> ', entry[1]

        return cat_rts


# ----------------------------------------------------------------------
if __name__ == "__main__":
    for num in range(4,5):
        if num == 1:
            get_adj_dirid()
            RideSystems_XML.get_trip_num()
        elif num == 2:
            create_xml()
        elif num == 3:
            rt_list = create_route_list()
            csv_out = open('rt_list.csv', 'wb')
            mywriter = csv.writer(csv_out)
            for entry in rt_list:
                print entry[0], '--> ', entry[1]
                mywriter.writerow(entry[:2])

            csv_out.close()
        elif num == 4:
            Create_stop_times.proc_rt_list()
        
    print 'program finished'


