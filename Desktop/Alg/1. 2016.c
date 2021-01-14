#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int a, int b) {
	char *week[7] = { "THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED" };
	int month[13] = { 0,31,29,31,30,31,30,31,31,30,31,30,31 };
	int i;
	int sum = 0;

	for (i = 0; i < a; i++) {
		sum += month[i];
	}
	sum += b;

	char* answer = (char*)malloc(sizeof(char));
	answer = week[sum % 7];
	return answer;
}
int main() {
	int a, b;
	printf("Enter the date(a/b): ");
	scanf("%d/%d", &a, &b);
	printf("Day of the week of that date is %s\n", solution(a, b));
	return 0;
}