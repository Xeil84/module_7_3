import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __eq__(self, other):
        return self.password == other.password

    def __hash__(self):
        return hash(self.password)

    def __repr__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode = False, time_now=0):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                return

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        self.users.append(User(nickname, password, age))
        self.current_user = User(nickname, password, age)

    def log_out(self):
        self.current_user = None

    def add(self,*videos):
        for video in videos:
            if video.title not in (v.title == video.title for v in self.videos):
                self.videos.append(video)
            else:
                pass

    def get_videos(self, search):
        name_video = []
        for i in self.videos:
            if search.lower() in i.title.lower():
                name_video.append(i.title)
        return name_video

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        else:
            for i in self.videos:
                if title.lower() == i.title.lower():
                    if i.adult_mode == True and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        for j in range(i.duration):
                            print(j+1)
                            time.sleep(1)
                        print('Конец видео')
                else:
                    pass

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