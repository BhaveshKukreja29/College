#include <stdio.h>
#include <conio.h>

int main() {
	int choice;
	int count = 1;
	clrscr();

	printf("Bhavesh Kukreja 2303080\n");

	do {
		printf("Enter 1 to increment, 2 to decrement, 3 to disable \n");
		printf("Enter choice: ");
		scanf("%d", &choice);
		switch(choice) {

		case 1:
		if (count >= 4) {
			printf("Cannot increase more\n");
			break;
		}
		count++;
		asm mov cx, count;
		asm mov ah, 01h;
		asm int 10h;
		break;

		case 2:
		if (count <= 0) {
			printf("Cannot decrease further\n");
			break;
		}
		count--;
		asm mov cx, count;
		asm mov ah, 01h;
		asm int 10h;
		break;

		case 3:
		asm mov cl, 20h;
		asm mov ah, 01h;
		asm int 10h;
		break;

		case 4:
		break;

		default:
		printf("Invalid choice.\n");
		}

	} while(choice != 4);

	getch();
	return 0;
}
