import pysynth_e as pse
import random

C_MAJOR_SCALE3 = ["c3", "d3", "e3", "f3", "g3", "a3", "b3"]
C_MAJOR_SCALE4 = ["c4", "d4", "e4", "f4", "g4", "a4", "b4"]
C_MAJOR_SCALE5 = ["c5", "d5", "e5", "f5", "g5", "a5", "b5"]

C_MINOR_SCALE = ["c3", "d3", "eb3", "f3", "g3", "ab3", "bb3"]

def generateSong(structure="ACCBBCCDDCCCCA", definitions={"A":(C_MAJOR_SCALE3, [1, 2, 4], 2), "B":(C_MAJOR_SCALE4, [2, 4, 8], 2), "C":(C_MAJOR_SCALE5, [4, 8], 2), "D":(C_MAJOR_SCALE4, [2, 4, 8], 4)}):
    songParts = {}
    for name, args in definitions.iteritems():
        songParts[name] = generateMelody(*args)
    
    print songParts
    
    song = []
    
    for key in structure:
        song += songParts[key]
    
    return song



def generateMelody(scale, noteLengths=[2, 4, 8], length=10):
    melody = []
    
    for bar in range(length):
        print "BAR " + str(bar) + ":"
        melody += generateBar(scale, noteLengths)
    
    print "\nGenerated " + str(length) + " bars and " + str(len(melody)) + " notes\n"
    return melody



def generateBar(scale, noteLengths):
    counter = 0
    bar = []

    while(counter < 1):
        note = random.choice(scale)
        
        noteLength = random.choice(noteLengths)
        if(counter + (1.0 / noteLength) > 1):
            noteLength = (1.0 - counter).as_integer_ratio()[1] # caculate the required note length to make the bar the right length

        bar.append((note, noteLength))
        
        counter += (1.0 / noteLength)
        
        print "Chose note: " + note + " Length: 1/" + str(noteLength) + " Counter: " + str(counter)
    
    return bar



if __name__=="__main__":
    song = generateSong()
    print song
    
    pse.make_wav(song, fn="output.wav", bpm=150)
