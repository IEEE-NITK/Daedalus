#include <stdlib.h>
#include <stdio.h>

int* multiply(int* n1, int c1, int* n2, int c2);
int* add(int* n1, int c1, int* n2, int c2);
int count_digits(int number);
int main(int argc, char** argv){
	if(argc!=3){
		printf("Usage- %s <number1> <number2>\n",argv[0]);
		exit(0);
	}

	FILE* file1;
	FILE* file2;
	int c1,c2,d1,d2;
	file1=fopen(argv[1],"r");
	file2=fopen(argv[2],"r");
	fscanf(file1,"%d\n",&d1);
	fscanf(file2,"%d\n",&d2);

	printf("Length of the first number- %d\n",d1);
	printf("Length of the second number- %d\n",d2);
	if(d1<d2){
		c1=d2;
		c2=d2;
	}
	else{
		c2=d1;
		c1=d1;
	}
	//printf("%d\n%d\n",c1,c2);
	
	//Storing and printing the numbers
	int n1[c1],n2[c2],i;
	printf("Number1- \t");
	for(i=0;i<c1;i++){
		if(i>=c1-d1){
			char c;
			fscanf(file1,"%c",&c);
			n1[i]=(int)(c-'0');
			printf("%d",n1[i]);
		}
		else{
			n1[i]=0;
		}
	}
	printf("\n");
	printf("Number2- \t");
	for(i=0;i<c2;i++){
		if(i>=c2-d2){
			char c;
			fscanf(file2,"%c",&c);
			n2[i]=(int)(c-'0');
			printf("%d",n2[i]);
		}
		else{
			n2[i]=0;
		}

	}
	printf("\n");

	//Adding the numbers
	int c=c1+1; 
	int n[c];
	for(i=0;i<c;i++){
		n[i]=0;
	}
	for(i=c-1;i>=0;i--){
		int sum=n[i]+n1[i-1]+n2[i-1];
		n[i]=sum%10;
		n[i-1]=sum/10;
	}
	printf("Sum-\t");
	for(i=0;i<c;i++){
		printf("%d",n[i]);
	}
	printf("\n");
	int *n3=multiply(n1,c1,n2,c2);
	c=c1+c2;
	printf("Product-\t");
	for(i=0;i<c;i++){
		printf("%d",*(n3+i));
	}
	printf("\n");
	return 0;
}
int* multiply(int* n1, int c1, int* n2, int c2){
	int c3, *product;
	c3=c1+c2;
	product=(int *)malloc(sizeof(int)*c3);
	int i,j,k,l=0;
	for(i=0;i<c3;i++){
		*(product+i)=0;
	}
	for(i=c1-1;i>=0;i--,l++){
		for(j=c2-1,k=c3-l-1;j>=0;j--,k--){
			int p1=*(n1+i);
			int p2=*(n2+j);
			int sum=*(product+k)+p1*p2;
			*(product+k)=sum%10;
			*(product+k-1)=*(product+k-1)+sum/10;
		}
	}
	return product;
}
