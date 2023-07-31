import socket
import pygame

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Настраиваем сокет
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # Отключаем пакетирование
sock.connect(("localhost", 10000))

while True:
   sock.send("Мороз и солнце, день чудесный, еще ты дремлешь друг прелестный)".encode())

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))