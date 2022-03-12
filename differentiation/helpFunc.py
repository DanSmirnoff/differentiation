def founder(string, part):             #founds part in string and returns it indexes
    places = []
    for i in range(len(string)):
        if string[i] == part[0] and i+len(part) <= len(string):
            if string[i:i + len(part)] == part:
                places.append(i)
    return places

def replacer(string, part1, part2, exceptions):     #part1 - what to replace, part2 - what to replace with
    places = founder(string, part1)
    if len(exceptions) != 0:
        for index in exceptions:
            if index in places:
                places.remove(index)
    i = 0
    k = 0
    while i < len(places):
        k = places[i]
        string = string[:k] + part2 + string[k+len(part1):]   
        for j in range(len(places)):
            places[j] -= len(part1) - len(part2)
        i += 1
    return string