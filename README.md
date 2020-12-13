# Wanze der Müllroboter


Pulsweitenmodulation ist aktuell mit RPi.GPIO realisiert. Gibt aber auch noch die library pigppio, die angeblich ein genaueres PWM Signal generiert. Da wir aber sowieso mehrere Motoren über eine
externe Motorsteuerung ansteuern müssen, kann es sein, dass wir die library der Motorsteuerung nutzen müssen, welche das PWM Signal generiert. Das ist vermutlich genauer als jedes PWM Signal, das 
der Pi generieren kann. 