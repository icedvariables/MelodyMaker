import pysynth_e as pse
import random

C_MAJOR_SCALE3 = ["c3", "d3", "e3", "f3", "g3", "a3", "b3"]
C_MAJOR_SCALE4 = ["c4", "d4", "e4", "f4", "g4", "a4", "b4"]
C_MAJOR_SCALE5 = ["c5", "d5", "e5", "f5", "g5", "a5", "b5"]

C_MINOR_SCALE = ["c3", "d3", "eb3", "f3", "g3", "ab3", "bb3"]

def generateSong(structure="ABCDCECCF", definitions={"A":(C_MAJOR_SCALE3, [1, 2, 4], 4), "B":(C_MAJOR_SCALE4, [2, 4, 8], 8), "C":(C_MAJOR_SCALE5, [2, 4, 8], 4), "D":(C_MAJOR_SCALE4, [2, 4, 8], 8), "E":(C_MAJOR_SCALE4, [4, 8, 16], 4), "F":(C_MAJOR_SCALE3, [1, 2, 4], 4))
    pass


    melody = []
    
    for bar in range(length):
        print "BAR " + str(bar) + ":"
        melody += generateBar(scale, noteLengths)
    
    print "\n Generated " + str(length) + " bars and " + str(len(melody)) + " notes\n"
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
    melody = generateMelody(C_MINOR_SCALE)
    print melody
    
    pse.make_wav(melody, fn="output.wav", bpm=150)