__author__ = 'haroldkurth'
import csv
import os
import shutil


def get_adj_dirid():
    if os.name == 'posix':
        str_name = '/Users/haroldkurth/Library/Mobile Documents/com~apple~CloudDocs/RideSystems/Source/google_transit/trips.txt'
        out_name = '/Users/haroldkurth/Library/Mobile Documents/com~apple~CloudDocs/RideSystems/Source/google_transit/test.csv'
        old_name = '/Users/haroldkurth/Library/Mobile Documents/com~apple~CloudDocs/RideSystems/Source/google_transit/trips.txt.old'
    else:
        str_name = 'C:/Users/hkurth1348/iCloudDrive/RideSystems/Source/google_transit/trips.txt'
        out_name = 'C:/Users/hkurth1348/iCloudDrive/RideSystems/Source/google_transit/test.csv'
        old_name = 'C:/Users/hkurth1348/iCloudDrive/RideSystems/Source/google_transit/trips.txt.old'
    name = raw_input("Enter file:")
    if len(name) < 1:
        name = str_name
    handle = open(name)
    csv_out = open(out_name, 'wb')
    # words = [1,2,3,4,5,6]
    mywriter = csv.writer(csv_out)
    for line in handle :
        line = line.rstrip('\r\n')

        words = line.split(',')
        if words[0].startswith ('route_id'):
            words[0] = 'route_id'
            words[1] = 'service_id'
            words[2] = 'trip_id'
            words[3] = 'trip_headsign'
            words[4] = 'direction_id'
            words[5] = 'block_id'
            words[6] = 'shape_id'
        else:
            words2 = words[3].split(' ')
            # words[0] = words[0]
            # words[1] = words[1]
            # words[2] = words[2]
            # words[3] = words[3]
            # words[4] = words[5]
            # words[5] = words[6]
            # words[6] = words[7]
            if words[3].endswith('TO DOWNTOWN'):
                words[4] = '0'
            elif words[3].endswith('NORTHBOUND'):
                words[4] = '0'
            elif words[3].endswith('CLOCKWISE'):
                words[4] = '0'
                if words[3].startswith('508'):
                    if words[3].endswith('COUNTERCLOCKWISE'):
                        words[4] = '1'
                    else:
                        words[4] = '0'
            elif words[3].endswith('EASTBOUND'):
                words[4] = '0'
            else:
                words[4] = '1'

        print words[:7]
        mywriter.writerow(words[:7])

    csv_out.close()
    handle.close()
    shutil.copy2(str_name, old_name)
    shutil.copy2(out_name, str_name)


def main():
    print os.name
    get_adj_dirid()


if __name__ == "__main__":
    main()