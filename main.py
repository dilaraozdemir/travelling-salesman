# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 17:38:07 2021

@author: rhaen
"""
#%% Kütüphanelerin tanımlanması.
import pygame,sys
import time
import random
import os
# Oluşturduğumuz diğer dosyadan Point sınıfını alıyoruz.
from points import Point

#%% pygame için gerekli ayarlamaların yapılması
distance_matrix = [ [0,	2,	6,	7,	8,	9,	4,	7,	9,	2,],
                    [2,	0,	4,	6,	8,	2,	3,	7,	8,	3,],
                    [6,	4,	0,	4,	7,	1,	9,	3,	6,	2,],
                    [7,	6,	4,	0,	9,	4,	7,	1,	2,	5,],
                    [8,	8,	7,	9,	0,	8,	3,	6,	8,	1,],
                    [9,	2,	1,	4,	8,	0,	6,	2,	7,	3,],
                    [4,	3,	9,	7,	3,	6,	0,	2,	8,	1,],
                    [7,	7,	3,	1,	6,	2,	2,	0,	3,	6,],
                    [9,	8,	6,	2,	8,	7,	8,	3,	0,	7,],
                    [2,	3,	2,	5,	1,	3,	1,	6,	7,	0,],
                    ]
# pygame ekranını ortaya yerleştirmek için.
os.environ["SDL_VIDEO_CENTERED"]='1'

# Ekranın boyutu için kullanılacak yükseklikler
width, height = 700, 700
# Görselleştirme için kullanacağımız renkleri ayarlıyoruz.
black= (0,0,0)
white = (255,255,255)
green = (0,255,25)

# pygame ayarları yapılıyor.
pygame.init()
pygame.display.set_caption("Gezgin Satici Problemi")
pygame.display.set_mode((width,height))
screen = pygame.display.set_mode((width,height))

#%% değişkenler tanımlanıyor.
# 
points = []
offset_screen = 50
smallest_path = []
record_distance = 0
number_of_points = 10

#%%
# Rastgele noktaları ekranda gösterme.
for n in range(number_of_points):
    x = random.randint(offset_screen,width-offset_screen)
    y = random.randint(offset_screen,height-offset_screen)  
    
    point = Point(x,y)
    points.append(point)

#%%
# Noktaların yerlerini karıştırma işlemi.
def shuffle(a,b,c):
    temp = a[b]
    a[b] = a[c]
    a[c] = temp

#%%
# pythagorean teoremine göre uzaklık hesaplama (distance_matrix kullanıldığı için bu fonksiyon kullanılmamıştır.)
def calculate_distance(points_list):
    total =  0
    for n in range(len(points)-1):
        distance = ((points[n].x - points[n+1].x) ** 2 + (points[n].y - points[+1].y) ** 2) ** 0.5
        total += distance
    return total
#%%
# distance_matrix içerisinden uzaklıkları alma işlemi.
def get_distance(point_list,distance_matrix):
    total = 0
    #i = 0 olduğunda a noktası demektir.
    for i in range(len(point_list)-1):
        for j in range(len(distance_matrix)-1):
            distance = distance_matrix[i][j]
            total += distance
    return total

dist = get_distance(points,distance_matrix)

# record_distance = en kısa yol için kullanılacak değişken
record_distance = dist

smallest_path = points.copy()

# pygame çalıştırılıyor.
run = True

while run:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    # Noktaları ve çizgileri  /// Burası koordinatlara göre değiştirilecek
    for n in range(len(points)):
        pygame.draw.circle(screen,white, (points[n].x , points[n].y ),10)
        
    a = random.randint(0,len(points)-1)
    b = random.randint(0,len(points)-1)
    
    shuffle(points, a, b)
    dist = get_distance(points, distance_matrix)
    
    if dist< record_distance:
        record_distance = dist
        smallest_path = points.copy()
    for m in range(len(points)-1):
        pygame.draw.line(screen,white,(points[m].x, points[m].y),(points[m+1].x, points[m+1].y),3)
    
    for m in range(len(smallest_path)-1):
        pygame.draw.line(screen,green,(smallest_path[m].x, smallest_path[m].y),(smallest_path[m+1].x, smallest_path[m+1].y))
        
        
    pygame.display.update()
    
    
print("En kısa yol:", record_distance)
pygame.quit()