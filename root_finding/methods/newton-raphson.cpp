/*	The Newton-Raphson method
*	Find a solution for f(x) = 0 given a continuos function f on an open interval
*	
*	f(x)
*		evaluates the function on a given x
*	df(x)
*		evaluates the derivate of the function on the given x
*	log_data(ofstream &, ld &,ld &,ld &)
*		this function writes on an csv file the data of x_n,x_n+1
*		and the relative error in every iteration
*	main()
*		method with the starting point near the root
*/


#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

ld f(ld x){
	return 230*powl(x,4)+18*powl(x,3) + 9*x*x - 221*x-9;
}
ld df(ld x){
	return 920*powl(x,3)+54*x*x+18*x-221;
}

void log_data(ofstream &file,ld &a,ld &b,ld &error){
	file << a << "," << b << ","<< error << '\n';
}

int main(){
	const ld TOL = 1e-6;//Tolerance
	int it = 200;//Max number ot iteration
	ofstream file("../data/newton-raphson_output.csv");
	file << "xn,xn1,error\n";
	ld x_0 = 3;

	for(int i=1;i<=it;i++){
		ld x_i = x_0-(f(x_0)/df(x_0));
		ld error = abs(x_0-x_i);
		log_data(file,x_0,x_i,error);
		if(error < TOL){
			cout << "Found Solution !!!\n";
			cout << x_i << " : " << f(x_i) << '\n';
			file.close();
			return 0;
		}
		x_0 = x_i;
	}
	
	file.close();
	cout << "Method failed\n";
	return 0;
}
