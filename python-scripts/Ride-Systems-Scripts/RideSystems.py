import os

class Route_Trips:
    def __init__(self, route, route_id):
            self.route = route
            self.route_id = route_id
            self.service_id = ''
            self.trip_id = ''
            self.trip_headsign = ''
            self.direction_id = ''
            self.block_id = ''
            self.shape_id = '0'
            
    def set_shapeid(self, shape_id):
        self.shape_id = shape_id
        
def get_trip_num():
    print os.name
    if (os.name == 'posix'):
        str_name = '/Users/haroldkurth/Library/Mobile Documents/com~apple~CloudDocs/RideSystems/Source/google_transit/trips.txt'
    else:
        str_name = 'C:/Users/hkurth1348/iCloudDrive/RideSystems/Source/google_transit/trips.txt'
    name = raw_input("Enter file:")
    if len(name) < 1 : name = str_name
    handle = open(name)
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
            #chk for route 100
            if len(route_100) == 0:
                route_100.append(shape_id)
                route__100 = Route_Trips("100", route_id)
                #route__100.set_shapeid(shape_id)
                setattr(route__100, 'shape_id', str(shape_id))
                print(route__100)
            elif route_100.count(shape_id) == 0:
                route_100.append(shape_id)
                route__100 = Route_Trips("100", route_id)
                print (route__100.route, route__100.route_id, route__100.shape_id)
        if trip_headsign.startswith("101"):
            #chk for route 100
            if len(route_101) == 0:
                route_101.append(shape_id)
            elif route_101.count(shape_id) == 0:
                route_101.append(shape_id)
        if trip_headsign.startswith("105"):
            #chk for route 100
            if len(route_105) == 0:
                route_105.append(shape_id)
            elif route_105.count(shape_id) == 0:
                route_105.append(shape_id)
        if trip_headsign.startswith("111"):
            #chk for route 100
            if len(route_111) == 0:
                route_111.append(shape_id)
            elif route_111.count(shape_id) == 0:
                route_111.append(shape_id)
        if trip_headsign.startswith("112"):
            #chk for route 100
            if len(route_112) == 0:
                route_112.append(shape_id)
            elif route_112.count(shape_id) == 0:
                route_112.append(shape_id)
        if trip_headsign.startswith("114"):
            #chk for route 100
            if len(route_114) == 0:
                route_114.append(shape_id)
            elif route_114.count(shape_id) == 0:
                route_114.append(shape_id)
        if trip_headsign.startswith("117"):
            #chk for route 100
            if len(route_117) == 0:
                route_117.append(shape_id)
            elif route_117.count(shape_id) == 0:
                route_117.append(shape_id)
        if trip_headsign.startswith("118"):
            #chk for route 100
            if len(route_118) == 0:
                route_118.append(shape_id)
            elif route_118.count(shape_id) == 0:
                route_118.append(shape_id)
        if trip_headsign.startswith("203"):
            #chk for route 100
            if len(route_203) == 0:
                route_203.append(shape_id)
            elif route_203.count(shape_id) == 0:
                route_203.append(shape_id) 
        if trip_headsign.startswith("210"):
            #chk for route 100
            if len(route_210) == 0:
                route_210.append(shape_id)
            elif route_210.count(shape_id) == 0:
                route_210.append(shape_id)  
        if trip_headsign.startswith("215"):
            #chk for route 100
            if len(route_215) == 0:
                route_215.append(shape_id)
            elif route_215.count(shape_id) == 0:
                route_215.append(shape_id)
        if trip_headsign.startswith("221"):
            #chk for route 100
            if len(route_221) == 0:
                route_221.append(shape_id)
            elif route_221.count(shape_id) == 0:
                route_221.append(shape_id)
        if trip_headsign.startswith("222"):
            #chk for route 100
            if len(route_222) == 0:
                route_222.append(shape_id)
            elif route_222.count(shape_id) == 0:
                route_222.append(shape_id) 
        if trip_headsign.startswith("251"):
            #chk for route 100
            if len(route_251) == 0:
                route_251.append(shape_id)
            elif route_251.count(shape_id) == 0:
                route_251.append(shape_id)  
        if trip_headsign.startswith("306"):
            #chk for route 100
            if len(route_306) == 0:
                route_306.append(shape_id)
            elif route_306.count(shape_id) == 0:
                route_306.append(shape_id)   
        if trip_headsign.startswith("318"):
            #chk for route 100
            if len(route_318) == 0:
                route_318.append(shape_id)
            elif route_318.count(shape_id) == 0:
                route_318.append(shape_id)  
        if trip_headsign.startswith("471"):
            #chk for route 100
            if len(route_471) == 0:
                route_471.append(shape_id)
            elif route_471.count(shape_id) == 0:
                route_471.append(shape_id)
        if trip_headsign.startswith("508"):
            #chk for route 100
            if len(route_508) == 0:
                route_508.append(shape_id)
            elif route_508.count(shape_id) == 0:
                route_508.append(shape_id)                                 
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
def main():
    print "main"
    get_trip_num()

if __name__ == "__main__":
    main()
    
    
    