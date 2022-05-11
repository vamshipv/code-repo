#include<stdio.h>
#include<string.h>
//int fact(n)
//{
//	int i,m = 1;
//	if(n==0)
//		return 1;
//	else
//		for(i = 1;i<=n;i++)
//		{
//			m = m * i;
//		}
//	return m;
//	
//}
//int main(){
//	int fac, n, m = 1;
//	scanf("%d",&n);
//	fac = fact(n);
//	printf("%d",fac);
//	return 0;
//}

//int main()
//{
//	int a=10,b=11;
////	scanf("%d,%d",&a,&b);
//	a = a+b;
//	b = a-b;
//	a = a-b;
//	printf("%d,%d",a,b);
//	return 0;
//}


//fib without recurresion

//int main()
//{
//	int res,i,n,n1=0,n2=1;
//	scanf("%d",&n);
//	printf("%d,%d",n1,n2);
//	for(i=2;i<=n;i++)
//	{
//		res = n1+n2;
//		printf("%d",res);
//		n1 = n2;
//		n2 = res;
//	}
//return 0;
//}/

//void fib(int n)
//{
//	static res,n1 = 0,n2 = 1;
//	if(n>0){
//		res = n1 + n2;
//		n1 = n2;
//		n2 = res;
//		printf("%d",res);
//		fib(n-1);
//	}
//}
//
//void main()
//{
//	int n;
//	scanf("%d",&n);
//	fib(n-2);
//}



//void main()
//{
//	int n,i,m=0,flag=0;
//	scanf("%d",&n);
//	m = n/2;
//	for(i=2;i<=m;i++)
//	{
//		if(n%i==0)
//		{
//			printf("not prime");
//			flag = 1;
//			break;
//		}
//	}
//	if(flag==0)
//	printf("prime");
//}

//void ispal(char str[])
//{
//	int l = 0;
//	int h = strlen(str) - 1;
//	
//	while(h>1)
//	{
//		printf("%d",l++);
//		if(str[l++] != str[h--])
//		{
//			printf("%s not",str);
//			return;
//		}
//	}
//	printf("%s is",str);
//}
//
//int main()
//{
//	ispal("abba");
//	return 0;
//}


