attr = input()
attrsplit = attr.split()
songs = []
indices = {}
for i in range(len(attrsplit)):
    indices[attrsplit[i]] = i

for j in range(int(input())):
    songs.append(input().split())

for k in range(int(input())):
    if(k > 0):
        print("")
    line = input()
    songs = sorted(songs, key = lambda song:song[indices.get(line)])
    print(attr)
    for song in songs:
        print(song[0],end="")
        for elem in song[1:]:
            print(" ",end="")
            print(elem,end="")
        print("")
