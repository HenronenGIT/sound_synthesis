import audiere

d = audiere.open_device()
t = d.create_tone(17000)
t.play()
time.sleep(5)
t.stop()