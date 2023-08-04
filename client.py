import socket
import math
import pygame

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Настраиваем сокет
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # Отключаем пакетирование
sock.connect(("localhost", 10000))
pygame.init()
width = 800
height = 600
cc = (width//2, height//2)
old = (0, 0)
radius = 50

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bacteries')



run = True
while run:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run =False
      elif pygame.mouse.get_focused():
         pos = pygame.mouse.get_pos()
         vector = pos[0] - cc[0], pos[1] - cc[1]
         lenv = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
         vector = vector[0]/lenv, vector[1]/lenv
         if lenv <= radius:
            vector = 0, 0

         elif vector != old:
            old = vector
            msg = f"<{vector[0]},{vector[1]}>"
            sock.send(msg.encode())


   data = sock.recv(1024).decode()
   print('Получмл', data)

   screen.fill('gray')
   pygame.draw.circle(screen, (255, 0, 0), cc, radius)
   font_style = pygame.font.SysFont('serif', radius//2)
   mes = font_style.render('Romas', True, (0, 0, 0))
   screen.blit(mes, (cc[0]-32, cc[1]-10))
   pygame.display.update()

pygame.quit()