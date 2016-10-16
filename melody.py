import pysynth_e as pse
import random

C_MAJOR_SCALE = ["c3", "d3", "e3", "f3", "g3", "a4", "b4"]

def generateMelody(scale, noteLengths=[2, 4, 8], length=2):
    counter = 0
    melody = []
    
    while(counter < length):
        note = random.choice(scale)
        noteLength = random.choice(noteLengths)
        
        counter += (1.0 / noteLength)
        
        melody.append((note, noteLength))
        
        print "Chose note: " + note + " Length: 1/" + str(noteLength) + " Counter: " + str(counter)
    
    return melody


if __name__=="__main__":
    melody = generateMelody(C_MAJOR_SCALE)
    print melody
    
    pse.make_wav(melody, fn="output.wav", bpm=150)