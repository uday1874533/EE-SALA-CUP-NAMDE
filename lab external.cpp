#include<stdio.h>
int main()
{
	int a[50],n,j,i,temp;
	printf("enter the size of array\n");
	scanf("%d",&n);
	printf("enter the array elements\n");
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	for(i=1;i<n;i++)
	{
		temp=a[i];
		j=i-1;
		while(j>=0 && a[j]>temp)
		{
			a[j+1]=a[j];
			j--;
		}
		a[j+1]=temp;
		}
		printf("elements after insertion sort\n");
		for(i=0;i<n;i++)
		printf("%d\t",a[i]);
	}

