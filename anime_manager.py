class AnimeManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_anime(self, anime):
        with open(self.file_path, 'a') as file:
            file.write(anime + '\n')

    def load_animes(self):
        with open(self.file_path, 'r') as file:
            return [anime.strip() for anime in file.readlines()]
