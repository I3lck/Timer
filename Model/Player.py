from pygame import mixer
import time
from Model.ManagerFiles import ManagerFiles


class SoundPlayer:
    def __init__(self):
        self.current_sound = None
        self.dir_sounds = r'C:\Users\ushko\PycharmProjects\Timer\Sounds'
        self.__soundlist = dict()
        self.update_soundlist()
        self.mixer = mixer
        self.mixer.init()


    def play(self):

        self.mixer.music.load(self.current_sound)
        self.mixer.music.play()

    def stop(self):
        self.mixer.music.stop()

    def update_soundlist(self):
        manager_files = ManagerFiles()
        self.__soundlist = {path_sound.split('\\')[-1]: path_sound for path_sound in manager_files.getPathsFilesWithSuf(self.dir_sounds, '.mp3')}


    def get_soundlist(self):
        return list(self.__soundlist.keys())

    def set_sound(self, sound_name):
        self.current_sound = self.__soundlist[sound_name]


if __name__ == '__main__':
    sound_player = SoundPlayer()
    sound_player.set_sound('CAKEBOY, IROH - НЕРВЫ.mp3')
    sound_player.play()
    print(sound_player.get_soundlist())

    time.sleep(30)
