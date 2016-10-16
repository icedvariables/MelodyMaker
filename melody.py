import pysynth_s as pss
import random

C_MAJOR_SCALE = ["c4", "d4", "e4", "f4", "g4", "a5", "b5"]

def generateMelody(scale, noteLengths=[1, 2, 4, 8], length=2):
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
    
    pss.make_wav(melody, fn="output.wav", bpm=150)