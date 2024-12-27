class FormatException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class AudioFile:

    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise FormatException("Invalid file format")
        self.filename = filename


class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print("playing {} as mp3".format(self.filename))


class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print("playing {} as wav".format(self.filename))


class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print("playing {} as ogg".format(self.filename))


class FlacFile:
    def __init__(self, filename):
        if not filename.endwith(".flac"):
            raise FormatException("Invalid format")
        self.filename = filename

    def play(self):
        print("playing {} as flac".format(self.filename))


class MyException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


if __name__ == "__main__":
    ogg = OggFile("myfile.ogg")
    ogg.play()
    mp3 = MP3File("myfile.mp3")
    mp3.play()

    try:
        not_an_mp3 = MP3File("myfile.org")
        not_an_falc = FlacFile("a.mp3")
        raise MyException("MyException occured")
    except FormatException as e:
        print(e.args)

    try:
        raise MyException("my exception")
        not_an_mp3 = MP3File("myfile.org")
        not_an_ogg = OggFile("file.mp3")
        raise MyException
    except FormatException as e:
        # print(e.args)
        print(e)

    except MyException as e:
        print(e.args)
