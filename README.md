# FFT-Analyzer
Python Program that utilizes the Numpy FFT library to identify individual frequency power levels from any sound data leaving a computer without using a microphone.


In order to run FFT_Analyzer.py you will need to follow a few steps:

  1.  First, make sure you have python 3.7 installed on your computer
      - Specifically between 3.7.3 - 3.7.9 (3.7.10 will not work with the libraries you will need) 
  2.  Install Virtual Audio Cable for free from this site: https://vb-audio.com/Cable/
  3.  Install Voice Meter Banana for free from this site: https://vb-audio.com/Voicemeeter/banana.htm
  4.  Open a terminal in the location you wish to save FFT_Analyzer.py and run the following commands:
      - pip install pyaudio
      - pip install numpy
      - pip install matplotlib
      - pip install math
  5. Next, you will need to change the audio input and output for your computer from pc settings:
      - Output will be set to "CABLE input(VB-Audio Virtual Cable)"
      - Input will be set to "CABLE output(VB-Audio Virtual Cable)"
  6. Finally, you will need to change the audio input and output on Voice Meter Banana:
      - Open Voice meter and let the sound engine start (ignore any error messages that pop up)
      - Set “Hardware Input 1” by clicking on the 1 icon and choose CABLE output(VB-Audio Virtual Cable)
      - Set “Hardware Out” by clicking on the A1 icon and choose “WDM: *name of computer speakers*”
  7. Now open the same terminal as before and run “python FTT_Analyzer.py”
  8. Play music from any online or offline source
  9. Completed steps
