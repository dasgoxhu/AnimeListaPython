class AnimeManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_anime(self, anime):
        with open(self.file_path, 'a') as file:
            file.write(anime + '\n')

    def edit_anime(self, index, new_name):
        animes = self.load_animes()
        if 0 <= index < len(animes):
            animes[index] = new_name
            with open(self.file_path, 'w') as file:
                for anime in animes:
                    file.write(anime + '\n')

    def delete_anime(self, index):
        animes = self.load_animes()
        if 0 <= index < len(animes):
            del animes[index]
            with open(self.file_path, 'w') as file:
                for anime in animes:
                    file.write(anime + '\n')

    def load_animes(self):
        with open(self.file_path, 'r') as file:
            return [anime.strip() for anime in file.readlines()]
