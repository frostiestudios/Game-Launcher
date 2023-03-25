from appJar import gui
def launchgame():
    print("Launching Game")

app=gui("Game Launcher",useTtk=True)
app.addLabel("T1","Game Launcher")
app.addButton("Launch Game",launchgame)
app.addOptionBox("g1",["Game Title"])
app.go()