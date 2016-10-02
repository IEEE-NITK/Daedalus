#include <stdlib.h>
#include <stdio.h>

int* add(int* n1, int c1, int* n2, int c2);
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
	for(i=0;i<c;i++){
		printf("%d",n[i]);
	}
	printf("\n");
	
	//Multiplying the numbers 
	int j,k,l=0;
	c=c1+c2;
	int product[c];
	for(i=0;i<c;i++){
		product[i]=0;
	}
	for(i=c1-1;i>=0;i--,l++){
		for(j=c2-1,k=c-l-1;j>=0;j--,k--){
			int sum=product[k]+n1[i]*n2[j];
			product[k]=sum%10;
			product[k-1]+=sum/10;
		}
	}
	for(i=0;i<c;i++){
		printf("%d",product[i]);
	}
	printf("\n");

	//Implement muliplication using gauss trick 
	//
	//
	
	return 0;
}
