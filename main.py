Web VPython 3.2
airplain = box(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6BhoAXCd3G5bZFzborXqBr-FAU5jQJj-qfaNadgkOZAQAvbj-FkwRFcA&s=10", size=vec(1, 1, 0.0001), pos = vec(0,-5,0))
back = box(texture = "https://raw.githubusercontent.com/Junhwi0325/2026-vpython-project/5647d77a4dd7e809f4b6eca37bcf568a0acee326/1794897378797.jpg", size= vec(20, 30, 0.0001), pos= vec(0, 0, -1))
scene.camera.pos = vector(0, 0, 10)
import random
dt = 0.01
ta = []
en = []
t1 = 0
t2 = 0
t3 = 0
t4 = 0

while True :
   
     
    rate(100)
    k = keysdown()
    
   
   
    if 'a'in k :
        airplain.pos.x = airplain.pos.x - 0.1
    if 'd'in k :
        airplain.pos.x = airplain.pos.x + 0.1
       
    if airplain.pos.x > 5 :
        airplain.pos.x = airplain.pos.x - 0.1
    if airplain.pos.x < -5 :
        airplain.pos.x = airplain.pos.x + 0.1
       
    t1 = t1 + dt
    t2 = t2 + dt
    t3 = t3 + dt
    t4 = t4 + dt
    if t1 >= 1 :
            enemy = box(texture = "https://raw.githubusercontent.com/Junhwi0325/2026-vpython-project/refs/heads/main/IMG_20261110_152944_362.jpg", size=vec(1, 1, 0.0001), pos = vec(random.randint(-4, 4),5,0), v= vec(0,-5, 0))
            t1 = 0
            en.append(enemy)
    
    if t3 >= 3 :
            enemy = box(texture = "https://raw.githubusercontent.com/Junhwi0325/2026-vpython-project/ff4cb25d57d5e883ba5172c41f3b05971673c0c9/IMG_20261116_141815_163.jpg", size=vec(1, 1, 0.0001), pos = vec(random.randint(-4, 4),5,0), v= vec(0,-5, 0))
            t3 = 0
            en.append(enemy)
    if t4 >= 4 :
            enemy = box(texture = "https://raw.githubusercontent.com/Junhwi0325/2026-vpython-project/f817759776a607c82fc9dcf8b87db43c7ed81dcc/IMG_20261116_141817_966.jpg", size=vec(1, 1, 0.0001), pos = vec(random.randint(-4, 4),5,0), v= vec(0,-5, 0))
            t4 = 0
            en.append(enemy)
    for enemy in en :
        enemy.pos = enemy.pos + enemy.v*dt
        if enemy.pos.y <= -6 :
            en.remove(enemy)
            enemy.visible = False

   
       
   
    if ' ' in k and  t2 >= 0.3 :
        ball = sphere(pos = vec(airplain.pos.x, -5, 0), radius = 0.1, v= vec(0, 50, 0), color = color.red)
        ta.append(ball)
        t2 = 0
    for ball in ta :
            ball.pos = ball.pos + ball.v*dt
            if ball.pos.y >= 6 :
                ta.remove(ball)
                ball.visible = False
    for enemy in en :
        for ball in ta :
           
            
            if abs(ball.pos.y - enemy.pos.y) < 0.7 and abs(ball.pos.x - enemy.pos.x) < 0.7  :
                en.remove(enemy)
                enemy.visible = False
                ta.remove(ball)
                ball.visible = False
    for enemy in en :
        if abs(airplain.pos.y - enemy.pos.y) < 1 and abs(airplain.pos.x - enemy.pos.x) < 1  :
            airplain.visible = False
