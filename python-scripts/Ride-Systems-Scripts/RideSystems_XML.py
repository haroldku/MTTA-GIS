import os
from xml.etree import ElementTree


def get_trip_num():
    print os.name
    if os.name == 'posix':
        str_name = '/Users/haroldkurth/Library/Mobile Documents/com~apple~CloudDocs/RideSystems/Source/google_transit/trips.txt'
    else:
        str_name = 'C:/Users/hkurth1348/iCloudDrive/RideSystems/Source/google_transit/trips.txt'
    name = raw_input("Enter file:")
    if len(name) < 1: 
        name = str_name
    handle = open(name)
    root = ElementTree.Element("root")
    rt_100 = ElementTree.SubElement(root, "Route", name = "RT_100")
    rt_101 = ElementTree.SubElement(root, "Route", name = "RT_101")
    rt_105 = ElementTree.SubElement(root, "Route", name = "RT_105")
    rt_111 = ElementTree.SubElement(root, "Route", name = "RT_111")
    rt_112 = ElementTree.SubElement(root, "Route", name = "RT_112")
    rt_114 = ElementTree.SubElement(root, "Route", name = "RT_114")
    rt_117 = ElementTree.SubElement(root, "Route", name = "RT_117")
    rt_118 = ElementTree.SubElement(root, "Route", name = "RT_118")
    rt_203 = ElementTree.SubElement(root, "Route", name = "RT_203")
    rt_210 = ElementTree.SubElement(root, "Route", name = "RT_210")
    rt_215 = ElementTree.SubElement(root, "Route", name = "RT_215")
    rt_221 = ElementTree.SubElement(root, "Route", name = "RT_221")
    rt_222 = ElementTree.SubElement(root, "Route", name = "RT_222")
    rt_251 = ElementTree.SubElement(root, "Route", name = "RT_251")
    rt_306 = ElementTree.SubElement(root, "Route", name = "RT_306")
    rt_318 = ElementTree.SubElement(root, "Route", name = "RT_318")
    rt_471 = ElementTree.SubElement(root, "Route", name = "RT_471")
    rt_508 = ElementTree.SubElement(root, "Route", name = "RT_508")
    rt_902 = ElementTree.SubElement(root, "Route", name = "RT_902")
    rt_909 = ElementTree.SubElement(root, "Route", name = "RT_909")
    # create list for route 100
    route_100 = []
    route_101 = []
    route_105 = []
    route_111 = []
    route_112 = []
    route_114 = []
    route_117 = []
    route_118 = []
    route_203 = []
    route_210 = []
    route_215 = []
    route_221 = []
    route_222 = []
    route_251 = []
    route_306 = []
    route_318 = []
    route_471 = []
    route_508 = []
    route_902 = []
    route_909 = []
    for line in handle:
        line = line.rstrip('\r\n')
        words = line.split(',')
        route_id = words[0]
        service_id = words[1]
        trip_id = words[2]
        trip_headsign = words[3]
        direction_id = words[4]
        block_id = words[5]
        shape_id = words[6]
        if trip_headsign.startswith("100"):
            # chk for route 100
#             if len(route_100) == 0:
#                 route_100.append(shape_id)
#                 #route__100.sElementTree_shapeid(shape_id)
#                 tree = ElementTree.SubElement(rt_100, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_100.count(shape_id) == 0:
                route_100.append(shape_id)
                tree = ElementTree.SubElement(rt_100, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id   
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("101"):
            #chk for route 100
#             if len(route_101) == 0:
#                 route_101.append(shape_id)
#                 tree = ElementTree.SubElement(rt_101, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_101.count(shape_id) == 0:
                route_101.append(shape_id)
                tree = ElementTree.SubElement(rt_101, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("105"):
            #chk for route 100
#             if len(route_105) == 0:
#                 route_105.append(shape_id)
#                 tree = ElementTree.SubElement(rt_105, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_105.count(shape_id) == 0:
                route_105.append(shape_id)
                tree = ElementTree.SubElement(rt_105, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("111"):
            #chk for route 100
#             if len(route_111) == 0:
#                 route_111.append(shape_id)
#                 tree = ElementTree.SubElement(rt_111, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_111.count(shape_id) == 0:
                route_111.append(shape_id)
                tree = ElementTree.SubElement(rt_111, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("112"):
            #chk for route 100
#             if len(route_112) == 0:
#                 route_112.append(shape_id)
#                 tree = ElementTree.SubElement(rt_112, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_112.count(shape_id) == 0:
                route_112.append(shape_id)
                tree = ElementTree.SubElement(rt_112, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("114"):
            #chk for route 100
#             if len(route_114) == 0:
#                 route_114.append(shape_id)
#                 tree = ElementTree.SubElement(rt_114, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_114.count(shape_id) == 0:
                route_114.append(shape_id)
                tree = ElementTree.SubElement(rt_114, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("117"):
            #chk for route 100
#             if len(route_117) == 0:
#                 route_117.append(shape_id)
#                 tree = ElementTree.SubElement(rt_117, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_117.count(shape_id) == 0:
                route_117.append(shape_id)
                tree = ElementTree.SubElement(rt_117, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("118"):
            #chk for route 100
#             if len(route_118) == 0:
#                 route_118.append(shape_id)
#                 tree = ElementTree.SubElement(rt_118, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_118.count(shape_id) == 0:
                route_118.append(shape_id)
                tree = ElementTree.SubElement(rt_118, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("203"):
            #chk for route 100
#             if len(route_203) == 0:
#                 route_203.append(shape_id)
#                 tree = ElementTree.SubElement(rt_203, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_203.count(shape_id) == 0:
                route_203.append(shape_id)
                tree = ElementTree.SubElement(rt_203, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("210"):
            #chk for route 100
#             if len(route_210) == 0:
#                 route_210.append(shape_id)
#                 tree = ElementTree.SubElement(rt_210, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_210.count(shape_id) == 0:
                route_210.append(shape_id)
                tree = ElementTree.SubElement(rt_210, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("215"):
            #chk for route 100
#             if len(route_215) == 0:
#                 route_215.append(shape_id)
#                 tree = ElementTree.SubElement(rt_215, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_215.count(shape_id) == 0:
                route_215.append(shape_id)
                tree = ElementTree.SubElement(rt_215, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("221"):
            #chk for route 100
#             if len(route_221) == 0:
#                 route_221.append(shape_id)
#                 tree = ElementTree.SubElement(rt_221, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_221.count(shape_id) == 0:
                route_221.append(shape_id)
                tree = ElementTree.SubElement(rt_221, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("222"):
            #chk for route 100
#             if len(route_222) == 0:
#                 tree = ElementTree.SubElement(rt_222, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#                 route_222.append(shape_id)
#             elif route_222.count(shape_id) == 0:
                route_222.append(shape_id) 
                tree = ElementTree.SubElement(rt_222, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("251"):
            #chk for route 100
#             if len(route_251) == 0:
#                 route_251.append(shape_id)
#                 tree = ElementTree.SubElement(rt_251, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_251.count(shape_id) == 0:
                route_251.append(shape_id)  
                tree = ElementTree.SubElement(rt_251, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("306"):
            #chk for route 100
#             if len(route_306) == 0:
#                 route_306.append(shape_id)
#                 tree = ElementTree.SubElement(rt_306, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_306.count(shape_id) == 0:
                route_306.append(shape_id)   
                tree = ElementTree.SubElement(rt_306, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("318"):
            #chk for route 100
#             if len(route_318) == 0:
#                 route_318.append(shape_id)
#                 tree = ElementTree.SubElement(rt_318, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_318.count(shape_id) == 0:
                route_318.append(shape_id)  
                tree = ElementTree.SubElement(rt_318, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("471"):
            #chk for route 100
#             if len(route_471) == 0:
#                 route_471.append(shape_id)
#                 tree = ElementTree.SubElement(rt_471, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_471.count(shape_id) == 0:
                route_471.append(shape_id)
                tree = ElementTree.SubElement(rt_471, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("508"):
            #chk for route 100
#             if len(route_508) == 0:
#                 route_508.append(shape_id)
#                 tree = ElementTree.SubElement(rt_508, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_508.count(shape_id) == 0:
                route_508.append(shape_id)
                tree = ElementTree.SubElement(rt_508, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("902"):
            #chk for route 100
#             if len(route_902) == 0:
#                 route_902.append(shape_id)
#                 tree = ElementTree.SubElement(rt_902, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_902.count(shape_id) == 0:
                route_508.append(shape_id)                                 
                tree = ElementTree.SubElement(rt_902, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
        if trip_headsign.startswith("909"):
            #chk for route 100
#             if len(route_909) == 0:
#                 route_909.append(shape_id)
#                 tree = ElementTree.SubElement(rt_909, 'T'+ shape_id)
#                 ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
#                 ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
#                 ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
#                 ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
#                 ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
#                 ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
#                 ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id
#             elif route_909.count(shape_id) == 0:
                route_909.append(shape_id)                                 
                tree = ElementTree.SubElement(rt_909, "trip", name=trip_id)
                ElementTree.SubElement(tree, "service_id", name="service_id").text = service_id
                ElementTree.SubElement(tree, "route_id", name="route_id").text = route_id
                ElementTree.SubElement(tree, "shape_id", name="shape_id").text = shape_id
                ElementTree.SubElement(tree, "dir_id", name="dir_id").text = direction_id
                ElementTree.SubElement(tree, "trip_headsign", name="trip_headsign").text = trip_headsign
                ElementTree.SubElement(tree, "block_id", name="block_id").text = block_id
                ElementTree.SubElement(tree, "trip_id", name="trip_id").text = trip_id        
    print '100', route_100 
    print '101', route_101
    print '105', route_105
    print '111', route_111
    print '112', route_112
    print '114', route_114
    print '117', route_117
    print '118', route_118
    print '203', route_203
    print '210', route_210
    print '221', route_221
    print '222', route_222
    print '251', route_251
    print '306', route_306
    print '318', route_318
    print '471', route_471
    print '508', route_508
    print '902', route_902
    print '909', route_909
    tree = ElementTree.ElementTree(root)
    tree.write("trips.xml")


def main():
    print "main"
    get_trip_num()

if __name__ == "__main__":
    main()
