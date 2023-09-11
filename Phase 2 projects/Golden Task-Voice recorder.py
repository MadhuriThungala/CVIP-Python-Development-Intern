import sounddevice
from scipy.io.wavfile import write
seconds=int(input("Enter number of seconds you want to record:"))
print("Your audio is being recording")
audiorecording=sounddevice.rec((seconds*44100),channels=2)
sounddevice.wait()
name_of_the_file=input("Enter the name of your file:")
write(name_of_the_file,44100,audiorecording)
print("Your recording has been finished")

