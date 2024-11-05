import csv

def is_in_dict(key, dictionary):
    if key not in dictionary:
        return 1
    return dictionary[key] + 1

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
album_release_date = header.index("album_release_date")

danceability_sum = 0
liveness_sum = 0
count = 0

album_release_year = {}
artist_tracks = {}

for line in lines:
    danceability_sum += float(line[danceability])

    if float(line[energy]) > 0.5:
        liveness_sum += float(line[liveness])
        count += 1

    artist_tracks[line[artist_name]] = is_in_dict(line[artist_name], artist_tracks)
    album_release_year[line[album_release_date][:4]] = is_in_dict(line[album_release_date][:4], album_release_year)

danceability_avg = danceability_sum / len(lines)
liveness_avg = liveness_sum / count

artists_sorted = sorted(artist_tracks.items(), key = lambda x: x[1], reverse=True)
artist_top_num_tracks = []
artist_top = []
for artist in artists_sorted:
    if len(artist_top_num_tracks) < 3 and artist[1] not in artist_top_num_tracks:
        artist_top_num_tracks.append(artist[1])
        artist_top.append(artist[0])
    elif artist[1] in artist_top_num_tracks:
        artist_top.append(artist[0])

top_year = sorted(album_release_year.items(), key = lambda x: x[1], reverse=True)[0][0]

print(f"{danceability_avg}\n{liveness_avg}\n{artist_top}\n{top_year}")
