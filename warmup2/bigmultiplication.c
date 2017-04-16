#include<stdio.h>
#include<string.h>
#define MAX(a,b) (((a)>(b))?(a):(b))
void main()
{
int c[200],car,i,j,k,l,r,s,a,flag=0;
char n[100],m[100];
printf("\nEnter the first number");
scanf("%s",m);
printf("\nEnter the second number");
scanf("%s",n);
k=strlen(m)-1;
l=strlen(n)-1;
r=2*MAX(k,l)+2;
for(i=0;i<200;i++)
    c[i]=0;
s=r;
for(j=l;j>=0;j--)
{
    s--;
    a=0;
    car=0;
    for(i=k;i>=0;i--)
    {
        c[s-a-1]+=(c[s-a]/10);
        c[s-a]%=10;
        c[s-a]+=(((int)(m[i]-'0')*(int)(n[j]-'0')+car)%10);
        car=((int)(m[i]-'0')*(int)(n[j]-'0')+car)/10;
        c[s-a-1]+=(c[s-a]/10);
        c[s-a]%=10;
        a++;
    }
    c[s-a]+=car;
}
printf("\nThe product is : ");
for(i=0;i<r;i++)
{
    if(c[i]!=0&&flag==0)
        flag=1;
    if(flag==1)
        printf("%d",c[i]);
}
}


