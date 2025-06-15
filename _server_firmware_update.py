#!/usr/bin/python3

import requests, sqlite3, os, py7zr, time, hashlib, json, shutil
device_list = "https://api.ipsw.me/v4/devices"

class DatabaseInit():
    
    def iOSInit(self):
        print("[+] Preparing iOS")
        if os.path.isfile('ios_devices.db'):
            os.remove('ios_devices.db')
            
        conn = sqlite3.connect('ios_devices.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE devices (DEVICE_NAME, IDENTIFIER, SIGNED, IOS_VERSION, BUILDID, SHA1SUM, FILESIZE, URL, RELEASEDATE)")

        new_get = requests.get(device_list)
        for each_device in new_get.json():
            if 'iPhone' in each_device['identifier']:
                nUrl = f"https://api.ipsw.me/v4/device/{each_device['identifier']}?type=ipsw"
                data = requests.get(nUrl)

                for device_ids in data.json()['firmwares']:
                    cur.execute('''INSERT INTO devices VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
                        data.json()['name'],
                        device_ids['identifier'],
                        device_ids['signed'],
                        device_ids['version'],
                        device_ids['buildid'],
                        device_ids['sha1sum'],
                        device_ids['filesize'],
                        device_ids['url'],
                        device_ids['releasedate'],
                    ))
                    
        conn.commit()
        conn.close()

    def iPadInit(self):
        print("[+] Preparing iPadOS")
        if os.path.isfile('ipad_devices.db'):
                os.remove('ipad_devices.db')
            
        conn = sqlite3.connect('ipad_devices.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE devices (DEVICE_NAME, IDENTIFIER, SIGNED, IOS_VERSION, BUILDID, SHA1SUM, FILESIZE, URL, RELEASEDATE)")

        new_get = requests.get(device_list)
        for each_device in new_get.json():
            if 'iPad' in each_device['identifier']:
                nUrl = f"https://api.ipsw.me/v4/device/{each_device['identifier']}?type=ipsw"
                data = requests.get(nUrl)
                for device_ids in data.json()['firmwares']:
                    cur.execute('''INSERT INTO devices VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
                        data.json()['name'],
                        device_ids['identifier'],
                        device_ids['signed'],
                        device_ids['version'],
                        device_ids['buildid'],
                        device_ids['sha1sum'],
                        device_ids['filesize'],
                        device_ids['url'],
                        device_ids['releasedate'],
                    ))
                    
        conn.commit()
        conn.close()

    def iPodInit(self):
        print("[+] Preparing iPod")
        if os.path.isfile('ipod_devices.db'):
                os.remove('ipod_devices.db')
            
        conn = sqlite3.connect('ipod_devices.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE devices (DEVICE_NAME, IDENTIFIER, SIGNED, IOS_VERSION, BUILDID, SHA1SUM, FILESIZE, URL, RELEASEDATE)")

        new_get = requests.get(device_list)
        for each_device in new_get.json():
            if 'iPod' in each_device['identifier']:
                nUrl = f"https://api.ipsw.me/v4/device/{each_device['identifier']}?type=ipsw"
                data = requests.get(nUrl)
                for device_ids in data.json()['firmwares']:
                    cur.execute('''INSERT INTO devices VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
                        data.json()['name'],
                        device_ids['identifier'],
                        device_ids['signed'],
                        device_ids['version'],
                        device_ids['buildid'],
                        device_ids['sha1sum'],
                        device_ids['filesize'],
                        device_ids['url'],
                        device_ids['releasedate'],
                    ))
                    
        conn.commit()
        conn.close()

    def iTunesInit(self):
        print("[+] Preparing iTunes")
        if os.path.isfile('iTunes.db'):
                os.remove('iTunes.db')
            
        conn = sqlite3.connect('iTunes.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE devices (PLATFORM, _VERSION, DATEFOUND, URL32, URL64, RELEASEDATE)")
        nURL = "https://api.ipsw.me/v4/itunes/windows"
        new_get = requests.get(nURL)
        for data in new_get.json():
                cur.execute('''INSERT INTO devices VALUES (?, ?, ?, ?, ?, ?)''', (
                    data['platform'],
                    data['version'],
                    data['datefound'],
                    data['url'],
                    data['64biturl'],
                    data['releasedate']
                ))
                    
        conn.commit()
        conn.close()

    def MacBookInit(self):
        print("[+] Preparing MacBook")
        if os.path.isfile('macbook_devices.db'):
                os.remove('macbook_devices.db')
        
        conn = sqlite3.connect('macbook_devices.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE devices (DEVICE_NAME, IDENTIFIER, SIGNED, IOS_VERSION, BUILDID, SHA1SUM, FILESIZE, URL, RELEASEDATE)")
        new_get = requests.get(device_list)

        macs = ['Macmini', 'MacBook']
        for each_device in new_get.json():
                for other_dev in macs:
                        if other_dev in each_device['identifier']:
                                nUrl = f"https://api.ipsw.me/v4/device/{each_device['identifier']}?type=ipsw"
                                data = requests.get(nUrl)
                                if data.json()['firmwares']:
                                        for device_ids in data.json()['firmwares']:
                                                cur.execute('''INSERT INTO devices VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
                                                data.json()['name'],
                                                device_ids['identifier'],
                                                device_ids['signed'],
                                                device_ids['version'],
                                                device_ids['buildid'],
                                                device_ids['sha1sum'],
                                                device_ids['filesize'],
                                                device_ids['url'],
                                                device_ids['releasedate'],
                                        ))

        conn.commit()
        conn.close()

    def OtherInit(self):
        print("[+] Preparing Other")
        if os.path.isfile('other.db'):
           os.remove('other.db')
        
        conn = sqlite3.connect('other.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE devices (DEVICE_NAME, IDENTIFIER, SIGNED, IOS_VERSION, BUILDID, SHA1SUM, FILESIZE, URL, RELEASEDATE)")
        new_get = requests.get(device_list)

        other = ['AudioAccessory', 'iBridge', 'AppleTV']
        for each_device in new_get.json():
            for other_dev in other:
                if other_dev in each_device['identifier']:
                        nUrl = f"https://api.ipsw.me/v4/device/{each_device['identifier']}?type=ipsw"
                        data = requests.get(nUrl)
                        if data.json()['firmwares']:
                            for device_ids in data.json()['firmwares']:
                                cur.execute('''INSERT INTO devices VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
                                        data.json()['name'],
                                        device_ids['identifier'],
                                        device_ids['signed'],
                                        device_ids['version'],
                                        device_ids['buildid'],
                                        device_ids['sha1sum'],
                                        device_ids['filesize'],
                                        device_ids['url'],
                                        device_ids['releasedate'],
                                ))
        conn.commit()
        conn.close()

if __name__ == '__main__':
    print("[+] Info: SCRIPT VERSION - 2.0")
    print("[+] Info: SCRIPT DATE - 06-26-2021")

    print("[+] Cleaning...")
    if os.path.isfile('DBs.7z'):
        os.remove('DBs.7z')

    if os.path.exists('iFTK-Updates/updates'):
         shutil.rmtree('iFTK-Updates/updates')
    
    os.mkdir('iFTK-Updates/updates')

    get_dbs = os.listdir('.')
    if get_dbs:
        for each in get_dbs:
            if each[-3::] == '.db':
                os.remove(each)

    db = DatabaseInit()
    db.iOSInit()
    db.iPadInit()
    db.iPodInit()
    db.iTunesInit()
    db.OtherInit()
    db.MacBookInit()

    print("[+] Zipping files...")
    get_dbs = os.listdir('.')
    with py7zr.SevenZipFile('DBs.7z', 'w') as file:
        for each in get_dbs:
            if each[-3::] == '.db':
                file.writeall(each)

    print("[+] Updating verval.txt")
    with open('iFTK-Updates/updates/verval.txt', 'w') as file:
        json.dump({
            "date": f"{time.strftime('%m%d%Y')}", 
            "relevant": "17"
            }, file)

    sha256 = hashlib.sha256()
    print("[+] Hashing file...")
    with open('iFTK-Updates/updates/sha25sum.txt', 'w') as file:
        with open('DBs.7z', 'rb') as hash_it:
            sha256.update(hash_it.read())
        
        file.write(sha256.hexdigest())

    print("[+] Copying file...")
    shutil.move('DBs.7z', 'iFTK-Updates/updates')
    print("[+] Cleaning up...")
    get_dbs = os.listdir('.')
    if get_dbs:
        for each in get_dbs:
            if each[-3::] == '.db':
                os.remove(each)

    os.chdir('iFTK-Updates')
    os.system('git add . && git commit -m "Updates" && git push')
    print("[+] All set.")

