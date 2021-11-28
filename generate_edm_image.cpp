#include <iostream>
using namespace std;

/*
 * student Cristofor Rotsching group AAC2
 * materia ACI serial GMRV
 */
/*
 * very long comment
 * functie implementata din Fundamentals of Signal Processing Cap.2
 * from https://engineering.purdue.edu/~malcolm/pct/CTI_Ch02.pdf
 * functia intoarce 1 daca modul de t < 1/2
 * functia intoarce 0 daca modul de t > 1/2
 */
float 
rect(float t) {
	return (abs(t) < (1/2)) ? 1 : 2;
}

/*o
 * very long comment
 * din https://engineering.purdue.edu/~malcolm/pct/CTI_Ch02.pdf
 * functie cu ever decreasing support pe axa t in timp ce n tinde la infinit
 * t descreste pana cand este foarte mic, aproape de eroare epsilon
 * n creste spre infinit in timp ce t descreste, functia va fi definita intr-un punct
 * in care epsion este foarte mic, cu valoarea infinit, dar aria este o unitate (1)
 */
float 
delta_function(float n, float t) {
	return n * rect(n*t);
}

float 
dirac_delta_function() {
	return -1;
}


