#include<stdio.h>
#include<stdlib.h>
#define CHAR_SIZE sizeof(char)


int str_to_int(char str[]){
	int i=0;
	int num=0;
	while(str[i]){
		num=(10*num)+str[i]-'0';
		i++;
	}	
	return num;
}

void add(char *a,char *b,char *sum,int N){
    int i,j=0,carry=0;
    for(i=N-1;i>=0;i--){
        sum[j]=a[i]-'0'+b[i]-'0'+carry;
        carry=sum[j]/10;
        sum[j]=sum[j]%10;
        j++;
    }
    sum[j]=carry;
    while(sum[j]==0){
        j--;
    }
    printf("\nSum is\n");
	for(j;j>=0;j--){
        printf("%d",sum[j]);
    }
    printf("\n");
}

void multiply(char *a,char *b,char *prod,int N){
    int i,j,k,l,carry,p;
    for(i=N-1;i>=0;i--){
        l=k;
        carry=0;
        for(j=N-1;j>=0;j--){
            p=(a[i]-'0')*(b[j]-'0');
            prod[l]+=(p+carry);
            carry=prod[l]/10;
            prod[l]=prod[l]%10;
            l++;
        }
        prod[l]=carry;
        k++;
    }
	printf("\nProduct is \n");
    while(prod[l]==0)
        l--;
    for(;l>=0;l--)
        printf("%d",prod[l]);
    printf("\n");

}


int main(int argc,char *argv[]){
	if(argc!=5){
		printf("Format is %s <sizeof_num1> <sizeof_num2> <num1> <num2>\n",argv[0]);
	}
	else{
		int N,m,n,i;
        char *a,*b;
    
		m=str_to_int(argv[1]);
		n=str_to_int(argv[2]);
        if(m>n){
            N=m;
        }else{
            N=n;
        }
        char *prod,*sum;
        a=(char *)calloc(N,CHAR_SIZE);
        b=(char *)calloc(N,CHAR_SIZE);
        prod=(char *)calloc(m+n,CHAR_SIZE);
        sum=(char *)calloc(N+1,CHAR_SIZE);
        
        
        char *e=argv[3];
        char *f=argv[4];
        if(m>n){
            for(i=0;e[i];i++){
                a[i]=e[i];
            }
            for(i=0;i<m-n;i++){
                b[i]='0';
            }
            for(i=0;f[i];i++){
                 b[i+m-n]=f[i];
            }
        }
        else{
            for(i=0;i<n-m;i++){
                a[i]='0';
            }
            for(i=0;e[i];i++){
                a[i+n-m]=e[i];
            }
            for(i=0;f[i];i++){
                b[i]=f[i];
            }
        }
        multiply(a,b,prod,N);
        add(a,b,sum,N);
    }
	return 0;
}
