#include<stdio.h>
int main()
{
	int temp,pali =0,rem,n;
	printf("enter the number ");
	scanf("%d",&n);
	temp = n;
	while (temp != 0)
	{
		rem = temp%10;
		pali = pali*10 + rem;
		temp = temp/10;
	}
	if (pali == n)
	{
		printf("plai yes");
	}
	else
	{
		printf("plai no");
	}
	return 0;
}


