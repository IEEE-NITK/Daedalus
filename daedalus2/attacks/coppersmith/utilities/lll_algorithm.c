#include<stdio.h>

void gram_schmidt(int n,int basis[][10],float b_tilde[][10],float u[][10]){
	
	int i,j,k,l;
	int bi_tilde_dot_bi_tilde,bi_tilde_dot_bj;
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			if(i==j)
				u[i][j]=1;
			else
				u[i][j]=0;
		}
	}

	//iterate column-wise
	for(j=0;j<n;j++){
		for(i=0;i<j;i++){
			bi_tilde_dot_bi_tilde=0;
			bi_tilde_dot_bj=0;
			for(k=0;k<n;k++){
				bi_tilde_dot_bi_tilde+=b_tilde[k][i]*b_tilde[k][i];
				bi_tilde_dot_bj+=b_tilde[k][i]*basis[k][j];
			}
			u[i][j]=(float)(bi_tilde_dot_bj)/(bi_tilde_dot_bi_tilde);	
		}

		for(k=0;k<n;k++){
			b_tilde[k][j]=(float)basis[k][j];
			for(i=0;i<j;i++){
				b_tilde[k][j]-=(b_tilde[k][i]*u[i][j]);
			}
		}
	}

}

int round_num(float num){
	float diff=num-(int)num;
	int round_off;
	if(diff<=0.5){
		round_off=(int)num;
	}
	else{
		round_off=((int)num)+1;
	}
	return round_off;
}

void size_reduce(int basis[][10],float u[][10],int index,int n){
	int i,j,k;
	int reduced_basis[10][10];
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			reduced_basis[i][j]=basis[i][j];
		}
	}

	for(j=index-1;j>=0;j--){
		if(u[j][index]>0.5){
			for(i=0;i<n;i++){
				basis[i][index]=basis[i][index]-(round_num(u[j][index])*basis[i][j]);
				u[i][index]=u[i][index]-(round_num(u[j][index])*u[i][j]);
			}
		}
	}

}

float norm_squared(float vector[],int n){
	float norm=0.0;
	int i;
	for(i=0;i<n;i++){
		norm+=(vector[i]*vector[i]);
	}
	return norm;
}

int Lovasz_condition(float orthogonal[][10], float u[][10],int i,int n){
	if(i==-1){
		return 1;
	}
	int j,k;
	float lhs[10],rhs[10];
	for(j=0;j<n;j++){
		lhs[j]=orthogonal[j][i];
		rhs[j]=u[i][i+1]*lhs[j]+orthogonal[j][i+1];
	}
	float norm_lhs=(float)norm_squared(lhs,n);
	float norm_rhs=(float)norm_squared(rhs,n);
	if(0.75*norm_lhs<=norm_rhs){
		return 1;
	}
	return 0;

}

void swap(int basis[][10],int i,int n){
	int j,temp;
	for(j=0;j<n;j++){
		temp=basis[j][i];
		basis[j][i]=basis[j][i+1];
		basis[j][i+1]=temp;
	}
}

void LLL_Algorithm(){
	int n=10,i,j;
	float short_vector[10],initial_vector[10];
	int lovasz_cond;
	float b_tilde[10][10],u[10][10];
	int basis[10][10]={{88,62,15,25,17,90,15,3,85,78},
						{99,18,31,59,97,13,20,42,37,72},
						{22,100,61,34,7,45,51,30,61,89},
						{15,94,8,86,1,8,29,10,77,79},
						{73,35,65,36,13,20,39,77,18,4},
						{46,58,80,53,58,48,96,16,97,47},
						{21,14,23,18,88,71,72,36,49,45},
						{49,12,22,65,63,53,18,85,41,22},
						{65,64,8,83,51,65,60,28,56,72},
						{2,78,52,14,2,32,1,56,50,57}};


	printf("The initial basis is\n");
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			printf("%d\t",basis[i][j]);
		}
		printf("\n");
	}

	for(i=0;i<n;i++){
		initial_vector[i]=basis[i][0];
	}
	printf("\n\nNorm squared of the initial b1 vector is %f\n\n",norm_squared(initial_vector,n));

	while(1==1){
		gram_schmidt(n,basis,b_tilde,u);
		for(i=0;i<n;i++){
			size_reduce(basis,u,i,n);
			lovasz_cond=Lovasz_condition(b_tilde,u,i-1,n);
			if(lovasz_cond==0){
				swap(basis,i-1,n);
				break;
			}
		}
		if(lovasz_cond==1){
			break;
		}	
	}
	printf("The final basis is\n");
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			printf("%d\t",basis[i][j]);
		}
		printf("\n");
	}
	
	for(i=0;i<n;i++){
		short_vector[i]=basis[i][0];
	}
	printf("\n\nNorm squared of the short vector is %f\n\n",norm_squared(short_vector,n));

}

int main(){

	LLL_Algorithm();
	return 0;


}

