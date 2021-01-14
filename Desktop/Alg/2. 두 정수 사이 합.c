#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
	long long answer = 0;
	if (a == b) {
		answer = a;
		return answer;
	}
	if (a < b) {
		for (int i = a; i <= b; i++) {
			answer += i;
		}
	}
	else {
		for (int i = b; i <= a; i++) {
			answer += i;
		}
	}
	return answer;
}
int main() {
	int a, b;
	printf("Enter A: ");
	scanf("%d", &a);
	printf("Enter B: ");
	scanf("%d", &b);
	printf("The sum of integers between A and B is %lld\n", solution(a, b));
	return 0;
}