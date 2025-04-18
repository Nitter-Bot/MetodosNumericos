/*	Linear Interpolation
*	Find a solution for f(x) = 0 given a continuos function f on 
*	the interval [a,b], where f(a) and f(b) have opposite signs, but 
*	makes lines from f(a) to f(b) and int the middle point makes a secant to f
*	making less iterations than bisection
*
*	f(x)
*		evaluates the function on a given x
*	calc_mid(ld,ld,ld,ld)
*		calc de mid point on the line from a,b
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
	return powl(x,3)+(4*x*x)-10;
}

ld calc_mid(ld &xa,ld &ya,ld &xb,ld &yb){
	return (-ya)*(xb-xa)/(yb-ya) + xa;
}

void log_data(ofstream &file,ld &a,ld &b ,ld &c,ld &fa,ld &fb, ld &fc,ld &error){
	file << a << "," << b << ","  << c << ","  << fa << ","<< fb << ","<< fc << "," << error << '\n';
}

int main(){
	const ld TOL = 1e-5;//Tolerance
	int it = 200;//Max number ot iteration
	ofstream file("../data/secant_output.csv");
	file << "xa,xb,xc,ya,yb,yc,error\n";
	ld a,b,c,fa,fb,fc;
	a = 1,b = 2;
	fa = f(a);
	fb = f(b);

	for(int i=1;i<=it;i++){
		c = calc_mid(a,fa,b,fb);
		fc = f(c);
		ld error = fc;
		log_data(file,a,b,c,fa,fb,fc,error);
		if(fc == 0 || abs(error) < TOL){
			cout << "Found Solution !!!\n";
			cout << c << " : " << fc << '\n';
			file.close();
			return 0;
		}
		if(fa*fc < 0){
			b = c;
			fb = fc;
		}else{
			a = c;
			fa = fc;
		}
	}
	
	file.close();
	cout << "Method failed\n";
	return 0;
}
