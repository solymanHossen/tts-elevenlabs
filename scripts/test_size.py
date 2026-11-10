def check(words, turns):
    est_sec = (words / 138.0) * 60.0 + turns * 0.28 + 14.0
    return est_sec / 60.0

print("3100 words, 140 turns:", check(3100, 140), "mins")
print("3300 words, 150 turns:", check(3300, 150), "mins")
print("3500 words, 160 turns:", check(3500, 160), "mins")
