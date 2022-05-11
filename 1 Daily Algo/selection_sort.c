#include<stdio.h>
int main()
{
    int arr[] = {64, 25, 12, 22, 11}; 
	int n = sizeof(arr)/sizeof(arr[0]); 
    printf("%d",n);
    return 0;
}