DATA SEGMENT
MSG1 DB 10, 13, "ARRAY LIMIT IS 10: $"
MSG2 DB 10, 13, "ENTER THE NUMBER: $"
MSG3 DB 10, 13, "THE SORTED ARRAY IS: $"
MSG4 DB 10, 13, "$"
COUNT DB ?
TEMP DB ?
DATA ENDS

CODE SEGMENT
ASSUME DS:DATA,CS:CODE
START:
    MOV AX, DATA
    MOV DS, AX

    LEA DX, MSG1
    MOV AH, 09h
    INT 21H

    MOV SI, 4000H
    MOV CX, 10

    LABEL1:

    LEA DX, MSG2
    MOV AH, 09H
    INT 21H

    MOV AH, 01H
    INT 21H
    CALL INPUT
    ROL AL, 04H
    MOV BL, AL

    MOV AH, 01H
    INT 21H
    CALL INPUT
    MOV AH, 00H
    ADD BL, AL

    MOV [SI], BL
    INC SI
    LEA DX, MSG4
    MOV AH, 09H
    INT 21H

    LOOP LABEL1

    MOV CX, 9
    MOV BX, 0000H

    LABEL2:

    MOV SI, 4000H
    MOV BL, [SI]
    INC SI
    MOV BH, 9

    LABEL3:

    DEC BH
    CMP BL, [SI]
    JC LABEL4
    MOV DL, BL
    MOV BL, [SI]
    DEC SI
    MOV [SI], BL
    INC SI
    MOV [SI], DL

    LABEL4:
    MOV BL, [SI]
    INC SI
    CMP BH, 00H
    JNZ LABEL3

    LOOP LABEL2

    MOV SI, 4000H
    MOV CX, 10

    d:
    LEA DX, MSG3
    MOV AH, 09H
    INT 21H

    MOV BL, 00H
    MOV BL, [SI]
    AND BL, 0F0H
    ROR BL, 04H
    CALL OUTPUT
    MOV BL, [SI]
    AND BL, 0FH
    CALL OUTPUT
    INC SI
    LOOP d

    MOV AH, 4CH
    INT 21H

    INPUT PROC
        CMP AL, 41H
        JC LABEL6
        SUB AL, 07H
    LABEL6:
        SUB AL, 30H

        RET
        ENDP

    OUTPUT PROC
        CMP BL, 04AH
        JC LABEL7
        ADD BL, 07H
    LABEL7:
        ADD BL, 30H
        MOV DL, BL
        MOV AH, 02H

    INT 21H

    RET
    ENDP

CODE ENDS
END START
