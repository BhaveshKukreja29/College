DATA SEGMENT
msg DB 0dh, 0ah, "-- -- -- --  OF DF IF TF SF ZF -- AF -- PF -- CF $"
newl DB 0dh, 0ah, "$"
flag DW ?
Data ENDS

Code SEGMENT
ASSUME CS: Code, DS: Data
start:
 mov ax, Data
 mov DS, ax

 mov dx, OFFSET msg
 mov ah, 09h
 int 21h

 mov dx, offset newl
 mov ah, 09h
 int 21h

 pushf

 pop bx

 mov flag, bx

 mov cx, 10h
 mov bx, 8000h

loops:
 mov ax, flag
 and ax, bx
 jz zero
 mov dl, 31h
 mov ah, 02h
 int 21h
 jmp space

zero: mov dl, 30h
 mov ah, 02h
 int 21h

space: mov dl, ' '
 mov ah, 02h
 int 21h

 mov ah, 02h
 int 21h

 ror bx, 1

 loop loops

 mov ah, 4ch

 int 21h

Code ENDS
END start
