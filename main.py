Web VPython 3.2
airplain = box(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6BhoAXCd3G5bZFzborXqBr-FAU5jQJj-qfaNadgkOZAQAvbj-FkwRFcA&s=10", size=vec(1, 1, 0.0001), pos = vec(0,-5,0))

dt = 0.01
ta = []
en = []

while True :
    rate(100)
    k = keysdown()
    posx = airplain.pos.x
    if 'a'in k :
        airplain.pos.x = airplain.pos.x - 0.1
    if 'd'in k :
        airplain.pos.x = airplain.pos.x + 0.1
    if airplain.pos.x > 5 :
        airplain.pos.x = airplain.pos.x - 0.1
    if airplain.pos.x < -5 :
        airplain.pos.x = airplain.pos.x + 0.1
    enemy = box(texture = "https://raw.githubusercontent.com/Junhwi0325/2026-vpython-project/refs/heads/main/IMG_20261110_152944_362.jpg", size=vec(1, 1, 0.0001), pos = vec(0,5,0), v= vec(0,-5, 0))
    while enemy.pos.y >= -5 :
        rate(100)
        enemy.pos = enemy.pos + enemy.v*dt
        
    
    if ' ' in k :
        ball = sphere(pos = vec(airplain.pos.x, -1, 0), radius = 0.05, v= vec(0, 50, 0))
        tan
        while ball.pos.y <= 5 :
            rate(100)
            ball.pos = ball.pos + ball.v*dt
           
        del ball
