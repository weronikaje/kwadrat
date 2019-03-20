
def setup():
    frameRate(60)
    size(700,300)
    krotkaKolorow=((255,0,0),(0,255,0),(0,0,255))
    strokeWeight(2)
    stroke(*krotkaKolorow[2])
    
    global wspolrzedna1
    global wspolrzedna2
    global szerokosc
    global wysokosc
    global szybkosc 
    global kierunek 
    
    wspolrzedna1 = 0
    wspolrzedna2 = 0
    szerokosc = 100
    wysokosc = 100
    szybkosc = 5
    kierunek = 1
    
def draw():
    global wspolrzedna1,wspolrzedna2,b,szerokosc,d,szybkosc,kierunek
    background(10)
    rgb=[0,0,0]
    rgb[0] = random(0,255)
    rgb[1] = random(0,255)
    rgb[2] = random(0,255)
    fill(rgb[0], rgb[1], rgb[2])
    
    rect(wspolrzedna1,wspolrzedna2, szerokosc, wysokosc)
    
    
    if(wspolrzedna1 == 610):
        kierunek = 0
        
        
    if(wspolrzedna1 == 0):
          kierunek = 1
     
    if(kierunek == 1 ):
        wspolrzedna1 = wspolrzedna1 + szybkosc
    else:
        wspolrzedna1 = wspolrzedna1 - szybkosc    
                              
          
                     

  
