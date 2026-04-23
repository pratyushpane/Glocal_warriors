def parse_line(line):
    data = {}

    if "ALT:" in line:
        data["altitude"] = int(line.split(":")[1])

    elif "STATUS:" in line:
        data["status"] = line.split(":")[1]

    elif "DEPLOY:" in line:
        data["deploy"] = line.split(":")[1]

    return data