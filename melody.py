import pysynth_e as pse
import random

C_MAJOR_SCALE = ["c3", "d3", "e3", "f3", "g3", "a4", "b4"]

def generateMelody(scale, noteLengths=[2, 4, 8], length=2):
    melody = []
    
    for bar in range(length):
        print "BAR " + str(bar) + ":"
        melody += generateBar(scale, noteLengths)
    
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
    melody = generateMelody(C_MAJOR_SCALE)
    print melody
    
    pse.make_wav(melody, fn="output.wav", bpm=150)