from haversine import haversine

def coords_parser(line:str) -> dict[str:float]:
    line = line.split('"')
    coords = {"lat":float(line[1]), "lon":float(line[3])}
    return coords

def logs_parser(raw_logs:list[list[str]]) -> dict[str:str]:
    found = False
    log = {}
    for raw_log in raw_logs:
        for line in raw_log:
            if "<groundspeak:type>Found it" in line or "<groundspeak:type>Attended" in line or "<groundspeak:type>Webcam Photo Taken" in line:
                found = True
            if "<groundspeak:log id=" in line:
                log["id"] = line.split('"')[1]
            if "<groundspeak:date>" in line:
                log["date"] = line.strip()[18:28]
        if found:
            return(log)
    print("Could not find Found It log")
            

def cache_parser(raw_cache:list[str]) -> dict[str:str|tuple[float]]:
    cache_info = {}
    coords = coords_parser(raw_cache[0])
    cache_info["coords"] = (coords["lat"], coords["lon"])

    raw_logs = []
    in_log = False
    log = []
    for line in raw_cache:
        if "<type>" in line:
            cache_info["type"] = line.strip()[6:-7].split('|')[1]
        if "<name>" in line:
            cache_info["gc_code"] = line.strip()[6:-7]
        if "<groundspeak:log id" in line:
            in_log = True
        if in_log:
            log.append(line)
        if "</groundspeak:log>" in line:
            in_log = False
            raw_logs.append(log)
            log = []
    #print(cache_info["gc_code"])
    found_log = logs_parser(raw_logs)
    cache_info["log_date_id"] = found_log["date"] + found_log["id"]          

    return cache_info

raw_caches = []

with open('My_finds.gpx', 'r', encoding='utf-8') as gpx:
    cache = []
    in_cache = False
    for line in gpx.readlines():
        if '<wpt' in line:
            in_cache = True
        if in_cache:
            cache.append(line)
        if '</wpt' in line:
            in_cache = False
            raw_caches.append(cache)
            cache = []

#print(cache_parser(raw_caches[0]))

parsed_caches = []
for raw_cache in raw_caches:
    parsed = cache_parser(raw_cache)
    if "Locationless" not in parsed["type"]:
        parsed_caches.append(parsed)

parsed_caches = sorted(parsed_caches, key=lambda d: d['log_date_id'])

dist = 0
code_printed = False
for i in range(len(parsed_caches)-1):
    dist += haversine(parsed_caches[i]["coords"], parsed_caches[i+1]["coords"])
    if dist > 37026 and not code_printed:
        print(parsed_caches[i+1]["gc_code"])
        code_printed = True

if not code_printed:
    print("Il semble que vous ne validez pas le challenge...")

#print(len(parsed_caches))
#print(parsed_caches[0])
#print(dist)