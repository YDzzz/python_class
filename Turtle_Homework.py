import turtle

turtle.setup(720, 480, 200, 200)

# 绘制六边形
for i in range(50):
    turtle.fd((i+1)*2)
    turtle.left(60)

turtle.reset()
turtle.penup()
turtle.bk(100)
turtle.pendown()

# 绘制星型
for i in range(4):
    turtle.circle(100, 90)
    turtle.right(180)
