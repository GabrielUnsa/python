#include <iostream>

using namespace std;

long long int H( long long int );
long int fn( long int );
long int fac_n( long int );
void f_index( int );
long long int f_index2( int );
long long f_20( int );
long long int f_20R( long long int );
long long int f_index3( int );
long long int f_index4( int );

long int fac_n( long int n ){
	if ( n == 0 ) return 1;
	else return ( n * fac_n ( n - 1 ) );
}

long int fn( long int n ){
	long int n1 = 1;
	int i;
	for( i = 2 ; i <= n ; i++ ){
		n1 = n1 * i;
	}
	return n1;
}

long long int H(long long int n){
	if ( n <= 2 ) return (2*n+1);
	else return ( ( 1 + H( n-1 ) ) * ( 2 + H( n-3 ) ) );
}

void f_index( int n ){
	long long int* H = new long long int[n];
	long long int result;
	int i;
	H[0] = 1; H[1] = 3; H[2] = 5;
	for( i = 3 ; i <= n ; i++){
		H[i] = ( 1 + H[i-1] ) * ( 2 + H[i-3] );
	}
	result = H[n];
	cout<<"F_index Resultado: "<<result;
	return;
}

long long f_index2( int n ){
	long long  h0=1; /* n - 3 */
	long long  h1=3; /* n - 2 */
	long long  h2=5; /* n - 1 */
	long long  hn;
	int i;
	if ( n <= 2 ) return ( 2 * n + 1 );
	for( i = 3 ; i <= n ; i++ ){
		hn = ( 1 + h2 ) * ( 2 + h0 );
		h0 = h1;
		h1 = h2;
		h2 = hn;
	}
	return hn;
}


long long int f_index3( int n ){
	int i; long long int f1 = 4; long long int fn;
	if ( n < 3 ) return 4;
	for( i = 2 ; i <= n ; i++ ){
		fn = f1 - ( 3 / ( i * ( i - 1 ) ) );
		f1 = fn;
	}
	return fn;
}

long long int f_index4( int n ){
	int i; 
	long long int f0 = 1; 
	long long int f1 = 2;
	long long int fn;
	if ( n < 3 ) return 4;
	for( i = 2 ; i <= n ; i++ ){
		fn = ( 2 * n * f0 ) - ( ( i - 2 ) * f1 ); 
		f0 = f1;
		f1 = fn;
	}
	return f1;
}

long long int f_20( int n ){
	long long int f1 = 1; /*n-2*/
	long long int f2 = 2; /*n-1*/
	long long int fn;
	int i;
	if ( n < 3 && n > 0) return n;
	for( i = 3 ; i <= n ; i++){
		fn = f1 - n * f2;
		f1 = f2;
		f2 = fn;
	}
	return fn;
}

long long int f_20R( long long int n ){
	if ( n < 3 ) return n;
	else return f_20R( n - 2 ) - n * f_20R( n - 1 );
}

int main(int argc, char *argv[]) {
	//	cout<<"Funcion H : "<<H(8);
	//	cout<<"\n";
	//	f_index(8);
	//	cout<<"\n";
	//	cout<<"Funcion ITER: "<<f_index2(8);
	//	cout<<"\nFuncion Fac_N : "<<fac_n(4);
	//	cout<<"\nFuncion FN : "<<fn(4);
	cout<<"Funcion Recuersiva: "<<f_20R(10000)<<"\n";
	cout<<"Funcion iterativa: "<<f_20(10000)<<"\n";
	return 0;
}
