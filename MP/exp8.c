#include <stdio.h>
#include <conio.h>

int main() {
	int a, b, gcd;
	clrscr();

	printf("Bhavesh Kukreja 2303080\n");
	printf("Enter a: ");
	scanf("%d", &a);

	printf("Enter b: ");
	scanf("%d", &b);


	asm mov ax, a;
	asm mov bx, b;

	start:
	asm cmp ax, bx;
	asm jc subb;

	suba:
	asm sub ax, bx;
	asm jmp check;

	subb:
	asm sub bx, ax;

	check:
	asm cmp ax, bx;
	asm jnz start;

	asm mov gcd, ax;

	printf("GCD is: %d", gcd);

	getch();
	return 0;
}
