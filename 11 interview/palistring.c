#include <stdio.h> 
#include <string.h>

void palindrome(char S[])
{
	int l = 0;
	int h = strlen(S) - 1;
	
	while (h>1)
	{
		if (S[l++] != S[h--])
		{
			printf("%s not",S);
			return;
		}
	}
	printf("%s is palindrome",S);
}
	
int  main()
{	
	char *S;
	scanf("%s",&S);
	palindrome(S);
	return 0;
}
