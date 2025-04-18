#include <stdio.h>
 
	void zeizyaku(){
		printf("hacked\n");
	}
 
	void vuln(){
		char hackme[12];
		scanf("%[^\n]",hackme);
	}
 
	int main(){
		vuln();
		printf("failed\n");
		return 0;
	}
