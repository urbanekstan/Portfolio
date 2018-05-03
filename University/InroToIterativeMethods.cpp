///////////////////////////////////////
// File: introToIterativeMethods.cpp

// Description: For HW1 on Numerical Methods
//              Intro to Jacobian, Gauss-Seidel methods

// Author: Stanley Urbanek

// Date: 2/3/15
/////////////////////////////////////

#include <iostream>
#include <cmath>

using namespace std;    

int main()
{
  
  // initialize variable
  int i, j, k, n, N;
  float x[10], A[10][10], b[10], s[10],XO[10];
  
  // prompt the user to enter number of unknowns
  cout<<"\nEnter the value of n: \n";
  cin>>n;
  
  // prompt user to enter number of iterations
  cout <<"\nEnter the number of iterations: \n";
  cin>>N;
  
  // prompt user to enter b vector components
  cout<<"\nEnter the right hand side coefficients: \n";
  for (i=0;i<n;i++) {
    cin>>b[i];
  }
  
  // prompt user to enter A matrix components
  cout<<"\nEnter the coefficients row wise: \n";
  for (i=0;i<n;i++) {
    x[i] = 0;
    XO[i] = 0;
    for (j=0;j<n;j++) {
      cin>>A[i][j];
    }
  }
  
  //set up counter for iterations
  k = 1;
  
  //compute summations for x guesses
  while (k <= N) {
    for (i=0;i<n;i++) {
      s[i] = b[i];
      for (j=0;j<n;j++) {
        if (i!=j) {
          s[i] = s[i] - A[i][j]*XO[j];
        }
      } 
    }
    
    // compute x guess using above summation
    for (i=0;i<n;i++) {
      x[i] = s[i]/A[i][i];
    }
    
    // increase iteration coutner
    k++;
    
    // reset old guesses with new ones
    for (i=0;i<n;i++) {
      XO[i] = x[i];
    }
  }
  
  // print jacobian answers 
  cout << "\nJacobi Method Answers \n";
  for (i=0;i<n;i++) {
    cout <<"x"<<i+1<<"= "<<XO[i]<<"\n";
  }
  
  // compute gauss seidel answers
  // initalize new variables for GS method
  float xg[10], XOG[10], sg[10], cg[10];
  int kg;
  double errorG, tol1, tol2;
  tol1 = pow(10,-6);
  tol2 = pow(10,-8);
  bool flag1;
  flag1 = false;

  // intialize coutner for GS method
  kg = 1;
  
  //fill in initial guesses 
  for (i=0;i<n;i++) {
    XOG[i] = 0;
    xg[i] = 0;
  }
  
  // compute summations for x guesses
  while (kg<= N) { 
    for (i=0; i<n; i++) {
      sg[i] = b[i];
      for (j=0;j<n;j++) {
        if (j<i) {
          sg[i] = sg[i] - A[i][j]*xg[j];
        }
        if (j>i) {
          sg[i] = sg[i] - A[i][j]*XOG[j];
        }
	
      //update new guess using summations
      xg[i] = sg[i]/A[i][i];
      }
    }
    
    // compute norm 
    errorG = 0;
    for (i=0;i<n;i++) {
      cg[i] = pow(xg[i]-XOG[i], 2);
    }
    for (i=0; i<n;i++) {
      errorG = errorG + cg[i];
    }
    errorG = sqrt(errorG);
      
    // add to iteration counter
    kg++;

    // reset old guesses with new ones
    for (i=0;i<n;i++) {
      XOG[i] = xg[i];
    }
  }
  
  // print Gauss-Seidel output
  cout<<"\nGauss-Seidel Method Answers \n";
  for (i=0;i<n;i++) {
    cout <<"x"<<i+1<<"= "<< XOG[i]<<"\n";
  }
  
}
