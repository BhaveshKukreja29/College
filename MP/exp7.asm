Data SEGMENT

Arr DB 01h,05h,03h,02h,04h

min DB ?

max DB ?

msg2 db 0dh,0ah, "Minimum is $"

msg3 db 0dh,0ah, "Maximum is $"

Data ends

Code SEGMENT

ASSUME CS:Code,DS:Data

START:

MOV AX,Data

MOV DS,AX

MOV CL,04H

LEA SI,Arr

MOV AL,[SI]

MOV min,AL

MOV max,AL

L2:

INC SI

MOV AL,[SI]

CMP min,AL

JC L1

MOV min,AL

L1:

DEC SI

JNC L2

MOV DX,offset msg2

MOV AH,09H

INT 21H

MOV DL,min

ADD DL,30H

MOV AH,02H

INT 21H

MOV CL,04H

LEA SI,Arr

MOV AL,[SI]

MOV min,AL

MOV max,AL

L3:

INC SI

MOV AL,[SI]

CMP max,AL

JC L4

MOV Al,max

L4:

DEC SI

JNC L3

MOV DX,offset msg3

MOV AH,09H
INT 21H

MOV DL,AL

ADD DL,30H

MOV AH,02H

INT 21H

MOV AH,4CH

INT 21H

Code ends

end START
