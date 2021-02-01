import Zielzustand


class Bewegungsablaeufe():
    
    def joystick_linker_arm_nach_oben(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (100,1,1)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (100,1,1)
        
    def joystick_rechter_arm_nach_oben(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (100,1,1)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts'] = (100,1,1)

    def joystick_linker_arm_nach_unten(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (0,1,2)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_links'] = (0,1,2)
        
    def joystick_rechter_arm_nach_unten(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (0,1,2)
        Zielzustand.ZIELZUSTAENDE['schulter_servo_rechts'] = (0,1,2)

    def joystick_rechter_ellbogen_nach_oben(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (100,1,1)

    def joystick_linker_ellbogen_nach_oben(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (100,1,1)
    
    def joystick_linker_ellbogen_nach_unten(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_links'] = (0,1,2)
        
    def joystick_rechter_ellbogen_nach_unten(self):
        Zielzustand.ZIELZUSTAENDE['ellbogen_servo_rechts'] = (0,1,2)
        
    
    


