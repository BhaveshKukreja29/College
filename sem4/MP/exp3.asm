data Segment
a db ?
b db ?
msg db 0Dh,0Ah,"Enter the 1st number $"
msg1 db 0Dh,0Ah, "Enter the 2nd number $"
msg2 db 0Dh,0Ah,"The result of the addition Bhavesh 2303080: $"
msg3 db 0D,0Ah, "The result of substraction Bhavesh 2303080: $"
data Ends

code Segment
assume cs:code,ds:data
start:
mov ax,data
mov ds,ax

mov dx,OFFSET msg
mov ah,09h
int 21h

call input
mov a,bl

mov dx,OFFSET msg1
mov ah,09h
int 21h

call input
mov b,bl

mov dx,OFFSET msg2
mov ah,09h
int 21h

mov cl,00

add bl,a
JNC l3
inc cl

l3:   
        mov dh,bl
        mov bl,cl
        and bl,0Fh
        call convert
        mov dl,bl
        mov ah,02h
        int 21h

        mov bl,dh
        and bl,0F0h
        ror bl,04h

        call convert
        mov dl,bl
        mov ah,02h
        int 21h

        mov bl,dh
        and bl,0Fh
        call convert

        mov dl,bl
        mov ah,02h
        int 21h


mov dx, OFFSET msg3
mov ah, 09h
int 21h

mov bl, a
mov cl, 00h
sub bl, b

JNC l4
inc cl

l4:   
        mov dh,bl
        mov bl,cl
        and bl,0Fh
        call convert
        mov dl,bl
        mov ah,02h
        int 21h

        mov bl,dh
        and bl,0F0h
        ror bl,04h

        call convert
        mov dl,bl
        mov ah,02h
        int 21h

        mov bl,dh
        and bl,0Fh
        call convert

        mov dl,bl
        mov ah,02h
        int 21h



mov ah,4ch
int 21h

input proc
mov ah,01h
int 21h

call ascii2hex
mov bl,al
rol bl,4

mov ah,01h
int 21h
call ascii2hex
add bl,al
ret
endp

ascii2hex proc
cmp al,41h
jc num
sub al,07h
num: sub al,30h
ret
endp

convert proc
cmp bl,0Ah
jc l1
add bl,37h
jmp l2
        l1:add bl,30h
                l2:ret
endp
code Ends
end start
