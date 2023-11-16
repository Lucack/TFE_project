import wave
import struct
import sys
import csv
import numpy 
from scipy.io import wavfile
from scipy.signal import resample

def write_wav(data, filename, framerate, amplitude):
    wavfile = wave.open(filename, 'w')
    nchannels = 1
    sampwidth = 2
    framerate = framerate
    nframes = len(data)
    comptype = "NONE"
    compname = "not compressed"
    wavfile.setparams((nchannels,
                        sampwidth,
                        framerate,
                        nframes,
                        comptype,
                        compname))
    frames = []
    for s in data:
        mul = int(s * amplitude)
        frames.append(struct.pack('h', mul))

    frames = ''.join(frames)
    wavfile.writeframes(frames)
    wavfile.close()
    print("%s written" % (filename)) 

if __name__ == "__main":
    # Ler os dados do arquivo CSV (teste.csv)
    data = []
    with open("Modificados\\Dia 3\\Modified_pressao 5 fora caixa.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            try:
                data.append(float(row[1]))  # Supondo que a segunda coluna contém os dados de áudio
            except ValueError:
                pass  # Ignorar erros de valor

    arr = numpy.array(data)  # Organizar todas as amostras em um array

    # Normalizar os dados
    arr /= numpy.max(numpy.abs(data))  # Dividir todas as amostras pelo valor máximo da amostra

    # Gravar o arquivo WAV
    write_wav(arr, 'rec.wav', 16000, 32767)  # 16000 é a taxa de amostragem e 32767 é a amplitude máxima
    print("Arquivo WAV gravado com sucesso!")

filename = "Modificados\\Dia 3\\Modified_pressao 5 fora caixa.csv"
framerate = 
amplitude = 
write_wav(data, filename, framerate, amplitude)