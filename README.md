# Snake
game 3 fases  (senes )
    display menu 
    display game 
    display highscore 

class snake (senes game)
 bevat blokjes voor de snake zijn lichaam. Dit is gebaseerd op aantal gegeten appels

class apple (sprite) 
    er word een random appel op het scherm geplakt, wanneer de slang de appel oppakt word de slang langer en komt er een nieuwe appel op het scherm. 
    de appel is een afbeelding van een appel 

class movement (snake)
    up down left right 

class scherm
    het scherm is verdeeld is een gelijk aantal blokken.


class game win / game over 
    waneer de slang zich zelf raakt is het game over. Ook als de slang de zij kant raakt. 
    wanneer de slang het scherm heeft gevuld IE even groot is als de blokken van het scherm. dan wint de speler!

class geluid    
    geluid speeld af wanneer;
        de slang een appel pakt 
        waneer de slang zich zelf eet 
        waneer de slang de muur eet
        start spel 
        win !