#include <iostream>
using namespace std;

/*
 * student Cristofor Rotsching group AAC2
 * materia ACI serial GMRV
 */
//function implemented from https://engineering.purdue.edu/~malcolm/pct/CTI_Ch02.pdf
int rect(int t) {
	return (abs(t) < (1/2)) ? 0 : 1;
}
