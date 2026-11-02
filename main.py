Web VPython 3.2
airplain = box(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6BhoAXCd3G5bZFzborXqBr-FAU5jQJj-qfaNadgkOZAQAvbj-FkwRFcA&s=10", size=vec(1, 1, 0.0001), pos = vec(0,-1,0))
while True :
    rate(100)
    k = keysdown()
    if 'a'in k :
        airplain.pos.x = airplain.pos.x - 0.1
    if 'd'in k :
        airplain.pos.x = airplain.pos.x + 0.1
    if airplain.pos.x > 10 :
        airplain.pos.x = airplain.pos.x - 0.1
    if airplain.pos.x < -10 :
        airplain.pos.x = airplain.pos.x + 0.1
    dt = 1
    if ' ' in k :
        ball = sphere(pos(airplain.pos.x, -1, 0), )
        ball.pos.x = ball.pos.x + 
