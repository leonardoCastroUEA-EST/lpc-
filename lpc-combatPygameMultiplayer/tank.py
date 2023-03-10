from config import *


class Tank:
    def __init__(self, photo, color: tuple, x: int, y: int, point: int, speed: int, angle: int, ide: int):
        self.__x_position = x
        self.__y_position = y
        self.__x_origin = x
        self.__y_origin = y
        self.__movement = False
        self.__spin_left = False
        self.__spin_right = False
        self.__shoot = False
        self.__photo = photo
        self.__surface = pygame.Surface((self.__photo.get_width(), self.__photo.get_height()))
        rect = (0, 0, self.__photo.get_width(), self.__photo.get_height())
        pygame.draw.rect(self.__surface, color, rect)
        self.__surface.blit(self.__photo, (0, 0))
        self.__point = point
        self.__vector = pygame.Vector2(0, -speed)
        self.__angle = angle
        self.__speed_angle = abs(speed)
        self.__id = ide
        self.__time_to_recharge = 0
        self.__time_of_visibility = 0
        self.__time_of_animation = 0
        self.__time_sound_walk = 0

    def move(self, counter, sound) -> None:
        if self.__movement:
            self.__x_position += self.__vector[0]
            self.__y_position += self.__vector[1]
            if counter - self.__time_sound_walk > Config.time_sound * 1000:
                sound.play()
                self.__time_sound_walk = pygame.time.get_ticks()
        if not self.__movement:
            sound.stop()

    def spin_right(self) -> None:
        if self.__spin_right:
            self.__angle += -self.__speed_angle
            if self.__angle <= -360:
                self.__angle = 0
            self.__photo = pygame.transform.rotate(self.__surface, self.__angle)
            self.__vector = self.__vector.rotate(self.__speed_angle)

    def spin_left(self) -> None:
        if self.__spin_left:
            self.__angle += self.__speed_angle
            if self.__angle >= 360:
                self.__angle = 0
            self.__photo = pygame.transform.rotate(self.__surface, self.__angle)
            self.__vector = self.__vector.rotate(-self.__speed_angle)

    def respawn(self, speed) -> None:
        self.__x_position = self.__x_origin
        self.__y_position = self.__y_origin
        self.__angle = 0
        self.__photo = pygame.transform.rotate(self.__surface, self.__angle)
        self.__vector = pygame.Vector2(0, -speed)

    def spin_death(self, counter, surface, rect) -> None:
        if counter - self.__time_of_animation < Config.animation_time * 1000:
            self.__angle += 20
            self.__photo = pygame.transform.rotate(self.__surface, self.__angle)
            surface.blit(self.__photo, rect)

    def get_id(self) -> int:
        return self.__id

    def get_vector(self):
        return self.__vector

    def get_x(self) -> float:
        return self.__x_position

    def get_y(self) -> float:
        return self.__y_position

    def set_x(self, x) -> None:
        self.__x_position = x

    def set_y(self, y) -> None:
        self.__y_position = y

    def get_movement(self) -> bool:
        return self.__movement

    def set_movement(self, movement) -> None:
        self.__movement = movement

    def get_spin_l(self) -> bool:
        return self.__spin_left

    def set_spin_l(self, spin) -> None:
        self.__spin_left = spin

    def get_spin_r(self) -> bool:
        return self.__spin_right

    def set_spin_r(self, spin) -> None:
        self.__spin_right = spin

    def get_shoot(self) -> bool:
        return self.__shoot

    def set_shoot(self, shoot) -> None:
        self.__shoot = shoot

    def get_time_to_recharge(self):
        return self.__time_to_recharge

    def set_time_to_recharge(self):
        self.__time_to_recharge = pygame.time.get_ticks()

    def get_point(self) -> int:
        return self.__point

    def ad_point(self) -> None:
        self.__point += 1

    def get_invisibility(self) -> int:
        return self.__time_of_visibility

    def get_photo(self):
        return self.__photo

    def get_surface(self):
        return self.__surface

    def get_rect(self):
        return self.__photo.get_rect()

    def set_time_of_animation(self) -> None:
        self.__time_of_animation = pygame.time.get_ticks()

    def get_time_of_animation(self) -> int:
        return self.__time_of_animation


class Ball:
    def __init__(self, photo, x, y, x_speed, y_speed, life, id):
        self.photo = photo
        self.rect = self.photo.get_rect()
        self.surface = pygame.Surface((self.photo.get_width(), self.photo.get_height()))
        self.x_position = x
        self.y_position = y
        self.speed_x = x_speed
        self.speed_y = y_speed
        self.life = life
        self.__id = id

    def move(self):
        self.x_position += self.speed_x
        self.y_position += self.speed_y

    def get_id(self):
        return self.__id
