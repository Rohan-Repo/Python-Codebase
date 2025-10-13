from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

def print_zones(dt1, dt2):
    zone1 = dt1.tzinfo.key if dt1.tzinfo else "Unknown"
    zone2 = dt2.tzinfo.key if dt2.tzinfo else "Unknown"

    if zone1 != zone2:
        print(f"Time Difference between: {zone1} and {zone2}")
    else:
        print("The Time Difference is:")


def print_time_difference(dt1, dt2):
    # Convert both to their LOCAL (naive) clock times, just like Java's LocalDateTime.from()
    dt1_local = dt1.replace(tzinfo=None)
    dt2_local = dt2.replace(tzinfo=None)

    delta = dt1_local - dt2_local
    total_seconds = abs(int(delta.total_seconds()))

    days = total_seconds // (24 * 3600)
    hours = (total_seconds % (24 * 3600)) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    parts = []
    if days:
        parts.append(f"Days: {days}")
    if hours:
        parts.append(f"Hours: {hours}")
    if minutes:
        parts.append(f"Minutes: {minutes}")
    if seconds or not parts:
        parts.append(f"Seconds: {seconds}")

    print("\t" + "\t".join(parts) + "\n")


def main():
    curr_dt = datetime.now(ZoneInfo("America/Toronto"))

    zones = {
        "Vancouver/San-Francisco": ZoneInfo("Canada/Pacific"),
        "Atlantic Canada": ZoneInfo("Canada/Atlantic"),
        "UAE (Dubai/Abu-Dhabi)": ZoneInfo("Asia/Dubai"),
        "India": ZoneInfo("Asia/Kolkata"),
        "Newfoundland": ZoneInfo("Canada/Newfoundland"),
    }

    fmt = "%Y-%b-%d %H:%M:%S %Z"

    print("\n -- Time Information -- ")
    print(f"Time in Toronto/New York : {curr_dt.strftime(fmt)}")

    zone_times = {}
    for name, zone in zones.items():
        local_time = curr_dt.astimezone(zone)
        zone_times[name] = local_time
        print(f"Time in {name} : {local_time.strftime(fmt)}")

    print("\n -- Time Difference Information -- ")

    # Now calculate clock differences (Java-style)
    print_zones(zone_times["Vancouver/San-Francisco"], curr_dt)
    print_time_difference(zone_times["Vancouver/San-Francisco"], curr_dt)

    print_zones(zone_times["India"], curr_dt)
    print_time_difference(zone_times["India"], curr_dt)

    print_zones(curr_dt, zone_times["UAE (Dubai/Abu-Dhabi)"])
    print_time_difference(curr_dt, zone_times["UAE (Dubai/Abu-Dhabi)"])

    print_zones(zone_times["Atlantic Canada"], zone_times["India"])
    print_time_difference(zone_times["Atlantic Canada"], zone_times["India"])

    print_zones(zone_times["Newfoundland"], zone_times["Atlantic Canada"])
    print_time_difference(zone_times["Newfoundland"], zone_times["Atlantic Canada"])

    time_minus_30s = curr_dt - timedelta(seconds=30)
    print_zones(curr_dt, time_minus_30s)
    print_time_difference(curr_dt, time_minus_30s)

    print_zones(zone_times["Vancouver/San-Francisco"], zone_times["India"])
    print_time_difference(zone_times["Vancouver/San-Francisco"], zone_times["India"])


if __name__ == "__main__":
    main()
