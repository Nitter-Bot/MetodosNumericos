/*	The bisection method
*	Find a solution for f(x) = 0 given a continuos function f on 
*	the interval [a,b], where f(a) and f(b) have opposite signs
*
*	f(x)
*		evaluates the function on a given x
*	log_data(ofstream &, ld &,ld &,ld &,ld &,ld &, ld & , ld&)
*		this function writes on an csv file the data of a,b,c, f(a), f(b), f(c)
*		and the relative error in every iteration
*
*	main()
*		given a,b applies the method with the tolerance and 
*		max number of iterations
*/


#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

ld f(ld x){
	return x-powl(2,-x);
}

void log_data(ofstream &file,ld &a,ld &b ,ld &c,ld &fa,ld &fb, ld &fc,ld &error){
	file << a << "," << b << ","  << c << ","  << fa << ","<< fb << ","<< fc << "," << error << '\n';
}

int main(){
	const ld TOL = 1e-5;//Tolerance
	int it = 200;//Max number ot iteration
	ofstream file("../data/bisection_output.csv");
	file << "a,b,c,fa,fb,fc,error\n";
	ld a,b;
	a = 0,b = 1;
	ld c,fa,fb,fc;
	fa = f(a);
	fb = f(b);

	for(int i=1;i<=it;i++){
		c = a+(b-a)/2;
		fc = f(c);
		ld error = (b-a)/2;
		log_data(file,a,b,c,fa,fb,fc,error);
		if(fc == 0 || error < TOL){
			cout << "Found Solution !!!\n";
			cout << c << " : " << fc << '\n';
			file.close();
			return 0;
		}
		if(fa*fc > 0){
			a = c;
			fa = fc;
		}else{
			b = c;
			fb = fc;
		}
	}
	
	file.close();
	cout << "Method failed\n";
	return 0;
}
