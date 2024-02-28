
import pgzrun
WIDTH=600
HEIGHT=600
score=0
ship=Actor("ship")
ship.x=300
ship.y=400
bullets=[]
bugs=[]
for i in range(7):
    bug=Actor("bug")
    bug.x=70+(50*i)
    bug.y=200
    bugs.append(bug)
    
ship.dead=False
def draw():
    screen.fill("slate gray")
    if ship.dead==False:
        ship.draw()
    else:
        screen.draw.text("game over!",(300,300),color="red")

    for b in bullets:
        b.draw()
    for bug in bugs:
        bug.draw()
    screen.draw.text (str(score),(15,15),color=  "deep sky blue")
def update():
    global score
    for b in bullets:
        b.y=b.y-5
    if keyboard.w:
        ship.y-=10
    if keyboard.s:
        ship.y+=10
    if keyboard.d:
        ship.x+=10
    if keyboard.a:
        ship.x-=10
    if keyboard.space:
        bullet=Actor("bullet")
        bullet.x=ship.x
        bullet.y=ship.y-150
        bullets.append(bullet)
    for b in bugs:
        b.y+=0.5
        for bullet in bullets:
            if bullet.colliderect(b):
                bullets.remove(bullet)
                bugs.remove(b)
                score=score+1
    
        if ship.colliderect(b):
            ship.dead=True
           
