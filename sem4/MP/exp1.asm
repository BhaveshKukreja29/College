data segment
num1 db 23h
num2 db 12h
data ends

code segment
assume cs:code, ds:data
start:  mov ax, data
        mov ds, ax

        mov al, num1
        mov bl, num2

        add al, bl

        mov ah, 4ch
        int 21h

code ends
end start
