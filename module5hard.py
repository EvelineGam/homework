import time

class User: # класс User, принимающий на вход nickname(строку), password(в хэшированном виде), age(число)
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

class Video: # класс Video, принимающий на вход title(строку), duration(число, секунды), time_now, adult_mode
    def __init__(self, title: str, duration: int, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube: # класс UrTube

    def __init__(self):
        self.users = [] # список объектов класса User
        self.videos = [] # список объектов класс Video
        self.current_user = None

    def log_in(self, nickname: str, password: str): # метод авторизации
        for user in self.users:
            if nickname == user.nickname and user.password == hash(password):
                self.current_user = user
        return self.current_user

    def register(self, nickname: str, password: str, age: int): # метод регистрации нового пользователя
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, hash(password), age)
        self.users.append(new_user)
        self.log_in(nickname, password)

    def log_out(self): # метод выхода
        self.current_user = None
        return self.current_user

    def add(self, *videos): # метод добавления видео
        for new_video in videos:
            if new_video not in self.videos:
                self.videos.append(new_video)
        return self.videos

    def get_videos(self, word:str):
        video_list = []
        for video in self.videos:
            if word.upper() in video.title.upper():
                video_list.append(video.title)
        return video_list

    def watch_video(self, title:str):
        if not self.current_user:
            print('Пожалуйста, войдите в аккаунт для просмотра видео')
            return
        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return
                for sec in range(1,video.duration + 1):
                    print(sec, end=' ')
                    time.sleep(1)
                    video.time_now += 1
                video.time_now = 0
                print('Конец видео')
                return video.time_now

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
    ur.add(v1, v2)

# Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

# Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')










