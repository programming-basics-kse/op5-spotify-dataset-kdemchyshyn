import csv

lines = []
with open("top_50_2023.csv", 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    header = next(csv_reader)
    for line in csv_reader:
         lines.append(line)

danceability = header.index("danceability")
liveness = header.index("liveness")
energy = header.index("energy")
artist_name = header.index("artist_name")

danceability_sum = 0
liveness_sum = 0
count = 0

artist_tracks = {}

for line in lines:
    danceability_sum += float(line[danceability])
    if float(line[energy]) > 0.5:
        liveness_sum += float(line[liveness])
        count += 1
    if line[artist_name] not in artist_tracks:
        artist_tracks[line[artist_name]] = 1
    else:
        artist_tracks[line[artist_name]] += 1

danceability_avg = danceability_sum / len(lines)
liveness_avg = liveness_sum / count
top_three = sorted(artist_tracks.items(), key = lambda x: x[1], reverse=True)

print(danceability_avg, liveness_avg, top_three[:3])
