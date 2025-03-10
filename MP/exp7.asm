data segment
msg0 db 0dh, 0ah, "Bhavesh Kukreja 2303080$"
msg1 db 0dh, 0ah, "Enter the string: $"
msg2 db 0dh, 0ah, "Entered string is: $"
msg3 db 0dh, 0ah, "String length: $"
msg4 db 0dh, 0ah, "String in reverse: $"
msg5 db 0dh, 0ah, "Enter the character to search for: $"
msg6 db 0dh, 0ah, "Character found$"
msg7 db 0dh, 0ah, "Character not found$"
msg8 db 0dh, 0ah, "String is palindrome$"
msg9 db 0dh, 0ah, "String is not a palindrome$"
count db ?

data ends

code segment
assume cs:code, ds:data
START:
    mov ax, data
    mov ds, ax

    lea dx, msg0
    mov ah, 09h
    int 21h

    lea dx, msg1
    mov ah, 09h
    int 21h

    mov si, 1000h
    mov di, 2000h

    mov cl, 00h

    up1:
        mov ah, 01h
        int 21h

        mov [si], al
        mov [di], al
        inc si
        inc cl

        cmp al, 0dh
        jnz up1

    dec cl

    lea dx, msg2
    mov ah, 09h
    int 21h

    mov si, 1000h
    mov count, cl

    printstr:
        mov dl, [si]
        mov ah, 02h
        int 21h

        inc si
        inc di
        dec cl

        jnz printstr

    mov cl, count

    mov al, cl

    add al, 30h

    lea dx, msg3
    mov ah, 09h
    int 21h

    mov dl, al
    mov ah, 02h
    int 21h

    ; to print reverse of string
    dec si
    lea dx, msg4
    mov ah, 09h
    int 21h

    mov cl, count
  
    printreverse:
        mov dl, [si]
        mov ah, 02h
        int 21h

        dec si
        

        cmp si, 1000h
        jnz printreverse

    mov dl, [si]
    mov ah, 02h
    int 21h
        
    ; check palindrome
    dec di
    check:
        mov al, [si]
        mov bl, [di]
        inc si
        dec di

        cmp al, bl
        jz check

        cmp di, 1999h
        jz pal


    notpal:
        lea dx, msg9
        mov ah, 09h
        int 21h

        jmp next
        

    pal:
        lea dx, msg8
        mov ah, 09h
        int 21h
        

    next:

    ; check if character entered is there or not




    mov ah, 4ch
    int 21h

    


CODE ENDS
END START
