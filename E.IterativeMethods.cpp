/////////////////////////////
// File: iterativeMethods.cpp

// Description: For HW2 on iterative methods
// 		Includes Jacobi, Gauss-Seidel, SOR methods

// Author: Stanley Urbanek

// Date: 2/5/15
///////////////////////////////

#include <iostream>
#include <cmath>
#include <vector>

#define _USE_MATH_DEFINES

using namespace std;
typedef vector<double> Vec;
typedef vector<vector<double> > DVec;

// get_max returns largest value in vector
double get_max(Vec vector, int n) 
{
  int i;
  double maxVal;
  maxVal = 0;
  for (i=0;i<n;i++) {
    if (vector[i] >= maxVal) {
      maxVal = vector[i];
    }
  }
  return maxVal;
}

// computes jacobi when iterations is a constraint
void Jacobi (int N,int n,DVec A,Vec b, Vec XO)
{
  //initialize variables
  int i,j,k;

  //set up counter for iterations
  k = 1;

  //initialize vectors for approximations
  Vec x,s;

  // create vectors with zeros to use for approximations
  for (i=0;i<n;i++) {
    x.push_back(0);
    s.push_back(0);
  }  

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
  cout <<"Number of iterations: "<<k-1<<"\n";
}

//computes jacobi when iterations is a constraint
void JacobiTol (double TOL,int n,DVec A,Vec b, Vec XO)
{
  //initialize variables
  int i,j,k;
  double d;
  Vec normDif;

  //set up counter for iterations
  k = 1;
  double norm = 1;
  
  //initialize vectors for approximations
  Vec x,s;
  // create vectors with zeros to use for approximations
  for (i=0;i<n;i++) {
    x.push_back(0);
    s.push_back(0);
  }  

  //compute summations for x guesses
  while (norm > TOL) {
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

    //compute new norm
    for (i=0;i<n;i++) {
      d = abs (x[i] - XO[i]);
      normDif.push_back(d);
    }
    norm = get_max(normDif, n);
    normDif.clear();   //clear the vector    
    

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
  cout <<"Number of iterations: "<<k-1<<"\n";
  cout<<"Tolerance is "<<TOL<<"\n";
}

//computes GS when iterations is a constraint
void GaussSeidel (int N,int n,DVec A,Vec b, Vec XO)
{
  //initialize variables
  int i,j,k;
  // intialize coutner for GS method
   k = 1;

  //initialize vectors for approximations
  Vec x,s;
  // create vectors with zeros to use for approximations
  for (i=0;i<n;i++) {
    x.push_back(0);
    s.push_back(0);
  }  
  
  // compute summations for x guesses
  while (k<= N) { 
    for (i=0; i<n; i++) {
      s[i] = b[i];
      for (j=0;j<n;j++) {
        if (j<i) {
          s[i] = s[i] - A[i][j]*x[j];
        }
        if (j>i) {
          s[i] = s[i] - A[i][j]*XO[j];
        }
      //update new guess using summations
      x[i] = s[i]/A[i][i];
      }
    }
    // add to iteration counter
    k++;

    // reset old guesses with new ones
    for (i=0;i<n;i++) {
      XO[i] = x[i];
    }
  }
  // print Gauss-Seidel output
  cout<<"\nGauss-Seidel Method Answers \n";
  for (i=0;i<n;i++) {
    cout <<"x"<<i+1<<"= "<< XO[i]<<"\n";
  }
  cout <<"Number of iterations: "<<k-1<<"\n";
}

//computes GS when tolerance level is a constraint
void GaussSeidelTol (double TOL,int n,DVec A,Vec b, Vec XO)
{
  //initialize variables
  int i,j,k;
  double d;
  Vec normDif;

  // intialize coutner for GS method
   k = 1;
   double norm = 1;
  
   //initialize vectors for approximations
  Vec x,s;
  // create vectors with zeros to use for approximations
  for (i=0;i<n;i++) {
    x.push_back(0);
    s.push_back(0);
  }  
 
  // compute summations for x guesses
  while (norm > TOL) { 
    for (i=0; i<n; i++) {
      s[i] = b[i];
      for (j=0;j<n;j++) {
        if (j<i) {
          s[i] = s[i] - A[i][j]*x[j];
        }
        if (j>i) {
          s[i] = s[i] - A[i][j]*XO[j];
        }
      //update new guess using summations
      x[i] = s[i]/A[i][i];
      }
    }
   
    //compute new norm
    for (i=0;i<n;i++) {
      d = abs (x[i] - XO[i]);
      normDif.push_back(d);
    }
    norm = get_max(normDif, n);
    normDif.clear();   //clear the vector    

    
    // add to iteration counter
    k++;

    // reset old guesses with new ones
    for (i=0;i<n;i++) {
      XO[i] = x[i];
    }
  }
  // print Gauss-Seidel output
  cout<<"\nGauss-Seidel Method Answers \n";
  for (i=0;i<n;i++) {
    cout <<"x"<<i+1<<"= "<< XO[i]<<"\n";
  }
  cout <<"Number of iterations: "<<k-1<<"\n";
  cout<<"Tolerance is "<<TOL<<"\n";
}

// computes SOR when # iterations is a restraint
void SOR (int N,int n,int omega,DVec A,Vec b, Vec XO) 
{
  //initialize variables
  int i,j,k;
  
  // intialize coutner for GS method
  k = 1;

  //initialize vectors for approximations
  Vec x,s;
  // create vectors with zeros to use for approximations
  for (i=0;i<n;i++) {
    x.push_back(0);
    s.push_back(0);
  }   
 
  // compute summations for x guesses
  while (k <= N) { 
    for (i=0; i<n; i++) {
      s[i] = b[i];
      for (j=0;j<n;j++) {
        if (j<i) {
          s[i] = s[i] - A[i][j]*x[j];
        }
        if (j>i) {
          s[i] = s[i] - A[i][j]*XO[j];
        }
      //update new guess using summations
      x[i] = (1-omega)*XO[i] + (omega*s[i])/A[i][i];
      }
    }

    // add to iteration counter
    k++;

    // reset old guesses with new ones
    for (i=0;i<n;i++) {
      XO[i] = x[i];
    }
  }
  // print SOR output
  cout<<"\nSOR Method Answers \n";
  for (i=0;i<n;i++) {
    cout <<"x"<<i+1<<"= "<< XO[i]<<"\n";
  }
  cout <<"Number of iterations: "<<k-1<<"\n";
  cout<<"Omega is "<<omega<<"\n";
}

//computes SOR approx when TOL is a restraint
void SORTol (double TOL,int n,double omega,DVec A,Vec b, Vec XO) 
{
  //initialize variables
  int i,j,k;
  double d;
  Vec normDif;
    
  // intialize coutner for GS method
  k = 1;
  double norm = 1;

  //initialize vectors for approximations
  Vec x,s;
  // create vectors with zeros to use for approximations
  for (i=0;i<n;i++) {
    x.push_back(0);
    s.push_back(0);
  }  

  // compute summations for x guesses
  while (norm > TOL) { 
    for (i=0; i<n; i++) {
      s[i] = b[i];
      for (j=0;j<n;j++) {
        if (j<i) {
          s[i] = s[i] - A[i][j]*x[j];
        }
        if (j>i) {
          s[i] = s[i] - A[i][j]*XO[j];
        }
      //update new guess using summations
      x[i] = (1-omega)*XO[i] + (omega*s[i])/A[i][i];
      }
    }

    //compute new norm
    for (i=0;i<n;i++) {
      d = abs (x[i] - XO[i]);
      normDif.push_back(d);
    }
    norm = get_max(normDif, n);
    normDif.clear();   //clear the vector

    // add to iteration counter
    k++;

    // reset old guesses with new ones
    for (i=0;i<n;i++) {
      XO[i] = x[i];
    }
  }
  // print SOR output
  cout<<"\nSOR Method Answers\n";
  for (i=0;i<n;i++) {
    cout <<"x"<<i+1<<"= "<< XO[i]<<"\n";
  }
  cout <<"Number of iterations: "<<k-1<<"\n";
  cout<<"Omega is "<<omega<<"\n";
  cout<<"Tolerance level is "<<TOL<<"\n";
}

int main()
{
  //initialize variables for for loops
  int i,j;
  
 //problem 9b
  double A9[3][3] = {{2,-1,1},{2,2,2},{-1,-1,2}};
  double b9[3] = {-1,4,-5};
  
  Vec XO9;  //initialize vectors 

  Vec b_9;
  DVec A_9;

  //create the matrixes into vectors
  for (int i = 0; i < 3; i++) {
    Vec row9; // Create an empty row
    b_9.push_back(b9[i]);
    for (int j = 0; j < 3; j++) {
        row9.push_back(A9[i][j]); // Add an element (column) to the row
    }
    A_9.push_back(row9); // Add the row to the main vector
  }

  // create vectors with initial guesses
  for (i=0;i<3;i++) {
    XO9.push_back(0);
  }  

  cout<<"Problem 9b\n";
  Jacobi (25,3,A_9,b_9,XO9);

 
  cout<<"\nProblem 9d\n";
  GaussSeidelTol(pow(10,-5),3,A_9,b_9,XO9);


  //problem 18
  cout<<"\nProblem 18\n";

  DVec A_18;
  Vec b_18,XO18;

  // create vector with initial guesses
  for (i=0;i<8;i++) {
    XO18.push_back(0);
  }  
   
  double y = sqrt(2)/2;
  double z = sqrt(3)/2;
  double A18[8][8] = {{-1,0,0,y,1,0,0,0},{0,-1,0,y,0,0,0,0},{0,0,-1,0,0,0,.5,0},{0,0,0,-y,0,-1,-.5,0},{0,0,0,0,-1,0,0,1},{0,0,0,0,0,1,0,0},{0,0,0,-y,0,0,z,0},{0,0,0,0,0,0,-z,-1}};
  double b18[8] = {0,0,0,0,0,10000,0,0};

  //create the matrixes into vectors
  for (int i = 0; i < 8; i++) {
    Vec row18; // Create an empty row
    b_18.push_back(b18[i]);
    for (int j = 0; j < 8; j++) {
        row18.push_back(A18[i][j]); // Add an element (column) to the row
    }
    A_18.push_back(row18); // Add the row to the main vector
  }

  //compute approximations
  JacobiTol(pow(10,-2),8,A_18,b_18,XO18);
  GaussSeidelTol(pow(10,-2),8,A_18,b_18,XO18);

  //problem 15
  cout<<"\nProblem 15\n";
  double b15[80] = {};
  double A15[80][80] = { { } };
  for (i=1;i<=80;i++) {
    b15[i] = 3.14159265359;
    for (j=1;j<=80;j++) {
        if (j==i) {
            A15[i-1][j-1] = 2*i;
        }
        else if (i<=78 && j == i+2) {
            A15[i-1][j-1] = .5*i;
        }
        else if (i>=3 && j == i-2) {
            A15[i-1][j-1] = .5*i;
        }
        else if  (i<=76 && j==i+4) {
            A15[i-1][j-1] = .25*i;
        }
        else if (i>=5 && j== i-4)  {
            A15[i-1][j-1] = .25*i;
        }
        else {
            A15[i-1][j-1] = 0;
        }
    }
  }  
   
  DVec A_15;
  Vec b_15,XO15;

  // create vector to use for initial guesses
  for (i=0;i<80;i++) {
    XO15.push_back(0);
  }  
 
  //create the matrixes into vectors
  for (int i = 0; i < 80; i++) {
    Vec row15; // Create an empty row
    b_15.push_back(b15[i]);
    for (int j = 0; j < 80; j++) {
        row15.push_back(A15[i][j]); // Add an element (column) to the row
    }
    A_15.push_back(row15); // Add the row to the main vector
  }
  
  //Compute approximations
  JacobiTol (pow(10,-5),80,A_15,b_15,XO15);
  GaussSeidelTol (pow(10,-5),80,A_15,b_15,XO15);
                    
            

  //matrices for 1,3,5,7
  double A1a[3][3] = {{3,-1,1},{3,6,2},{3,3,7}};
  double b1a[3] = {1,0,4};

  DVec A_1a;
  Vec b_1a,XO1a;

  // create vectors with zeros to use for approximations
  for (i=0;i<3;i++) {
    XO1a.push_back(0);
  }   

    //create the matrixes into vectors
  for (int i = 0; i < 3; i++) {
    Vec row1a; // Create an empty row
    b_1a.push_back(b1a[i]);
    for (int j = 0; j < 3; j++) {
        row1a.push_back(A1a[i][j]); // Add an element (column) to the row
    }
    A_1a.push_back(row1a); // Add the row to the main vector
  }

  DVec A_1b;
  Vec b_1b,XO1b;

  // create vectors with zeros to use for approximations
  for (i=0;i<3;i++) {
    XO1b.push_back(0);
  }  

  double A1b[3][3] = {{10,-1,0},{-1,10,-2},{0,-2,10}};
  double b1b[3] = {9,7,6};

   //create the matrixes into vectors
  for (int i = 0; i < 3; i++) {
    Vec row1b; // Create an empty row
    b_1b.push_back(b1b[i]);
    for (int j = 0; j < 3; j++) {
        row1b.push_back(A1b[i][j]); // Add an element (column) to the row
    }
    A_1b.push_back(row1b); // Add the row to the main vector
  }

  DVec A_1c;
  Vec b_1c,XO1c;

  // create vectors with zeros to use for approximations
  for (i=0;i<4;i++) {
    XO1c.push_back(0);
  }  
  
  double A1c[4][4] = {{10,5,0,0},{5,10,-4,0},{0,-4,8,1},{0,0,-1,5}};
  double b1c[4] = {6,25,-11,-11};

   //create the matrixes into vectors
  for (int i = 0; i < 4; i++) {
    Vec row1c; // Create an empty row
    b_1c.push_back(b1c[i]);
    for (int j = 0; j < 4; j++) {
        row1c.push_back(A1c[i][j]); // Add an element (column) to the row
    }
    A_1c.push_back(row1c); // Add the row to the main vector
  }

  DVec A_1d;
  Vec b_1d,XO1d;

  // create vectors with zeros to use for approximations
  for (i=0;i<5;i++) {
    XO1d.push_back(0);
  }  

  double A1d[5][5] = {{4,1,1,0,1},{-1,-3,1,1,0},{2,1,5,-1,-1},{-1,-1,-1,4,0},{0,2,-1,1,4}};
  double b1d[5] = {6,6,6,6,6};

   //create the matrixes into vectors
  for (int i = 0; i < 5; i++) {
    Vec row1d; // Create an empty row
    b_1d.push_back(b1d[i]);
    for (int j = 0; j < 5; j++) {
        row1d.push_back(A1d[i][j]); // Add an element (column) to the row
    }
    A_1d.push_back(row1d); // Add the row to the main vector
  }

  //matrices for 2,4,6,8

  DVec A_2a;
  Vec b_2a,XO2a;

   // create vectors with initial guesses
  for (i=0;i<3;i++) {
    XO2a.push_back(0);
  } 

  double A2a[3][3] = {{4,1,-1},{-1,3,1},{2,2,5}};
  double b2a[3] = {5,-4,1};
  
   //create the matrixes into vectors
  for (int i = 0; i < 3; i++) {
    Vec row2a; // Create an empty row
    b_2a.push_back(b2a[i]);
    for (int j = 0; j < 3; j++) {
        row2a.push_back(A2a[i][j]); // Add an element (column) to the row
    }
    A_2a.push_back(row2a); // Add the row to the main vector
  }

  DVec A_2b;
  Vec b_2b,XO2b;

   // create vectors with initial guesses
  for (i=0;i<3;i++) {
    XO2b.push_back(0);
  }   

  double A2b[3][3] = {{-2,1,1/2},{1,-2,-1/2},{0,1,2}};
  double b2b[3] = {4,-4,0};

    //create the matrixes into vectors
  for (int i = 0; i < 3; i++) {
    Vec row2b; // Create an empty row
    b_2b.push_back(b2b[i]);
    for (int j = 0; j < 3; j++) {
        row2b.push_back(A2b[i][j]); // Add an element (column) to the row
    }
    A_2b.push_back(row2b); // Add the row to the main vector
  }

  DVec A_2c;
  Vec b_2c,XO2c;

   // create vectors with initial guesses
  for (i=0;i<4;i++) {
    XO2c.push_back(0);
  } 

  double A2c[4][4] = {{4,1,-1,1},{1,4,-1,-1},{-1,-1,5,1},{1,-1,1,3}};
  double b2c[4] = {-2,1,0,1};

    //create the matrixes into vectors
  for (int i = 0; i < 4; i++) {
    Vec row2c; // Create an empty row
    b_2c.push_back(b2c[i]);
    for (int j = 0; j < 4; j++) {
        row2c.push_back(A2c[i][j]); // Add an element (column) to the row
    }
    A_2c.push_back(row2c); // Add the row to the main vector
  }

  DVec A_2d;
  Vec b_2d,XO2d;
  
 // create vectors with initial guesses
  for (i=0;i<6;i++) {
    XO2d.push_back(0);
  } 

  double A2d[6][6] = {{4,-1,0,0,0,0},{-1,4,-1,0,0,0},{0,-1,4,0,0,0},{0,0,0,4,-1,0},{0,0,0,-1,4,-1},{0,0,0,0,-1,4}};
  double b2d[6] = {0,5,0,6,-2,6};

    //create the matrixes into vectors
  for (int i = 0; i < 6; i++) {
    Vec row2d; // Create an empty row
    b_2d.push_back(b2d[i]);
    for (int j = 0; j < 6; j++) {
        row2d.push_back(A2d[i][j]); // Add an element (column) to the row
    }
    A_2d.push_back(row2d); // Add the row to the main vector
  }

  //problem 1
  cout<<"\nProblem 1a\n";
  SOR(2,3,1.1,A_1a,b_1a,XO1a);
  
  cout<<"\nProblem 1b\n";
  SOR(2,3,1.1,A_1b,b_1b,XO1b);

  cout<<"\nProblem 1c\n";
  SOR(2,4,1.1,A_1c,b_1c,XO1c);

  cout<<"\nProblem 1d\n";
  SOR(2,5,1.1,A_1d,b_1d,XO1d);

  // problem 2
  cout<<"\nProblem 2a\n";
  SOR(2,3,1.1,A_2a,b_2a,XO2a);

  cout<<"\nProblem 2b\n";
  SOR(2,3,1.1,A_2b,b_2b,XO2b);
 
  cout<<"\nProblem 2c\n";
  SOR(2,4,1.1,A_2c,b_2c,XO2c);

  cout<<"\nProblem 2d\n";
  SOR(2,6,1.1,A_2d,b_2d,XO2d);  
  
  //Problem 3
  cout<<"\nProblem 3a\n";
  SOR(2,3,1.3,A_1a,b_1a,XO1a);
  
  cout<<"\nProblem 3b\n";
  SOR(2,3,1.3,A_1b,b_1b,XO1b);

  cout<<"\nProblem 3c\n";
  SOR(2,4,1.3,A_1c,b_1c,XO1c);

  cout<<"\nProblem 3d\n";
  SOR(2,5,1.3,A_1d,b_1d,XO1d);

  //problem 4
  cout<<"\nProblem 4a\n";
  SOR(2,3,1.3,A_2a,b_2a,XO2a);

  cout<<"\nProblem 4b\n";
  SOR(2,3,1.3,A_2b,b_2b,XO2b);
 
  cout<<"\nProblem 4c\n";
  SOR(2,4,1.3,A_2c,b_2c,XO2c);

  cout<<"\nProblem 4d\n";
  SOR(2,6,1.3,A_2d,b_2d,XO2d);  

  // problem 5
  cout<<"\nProblem 5a\n";
  SORTol(pow(10,-3),3,1.2,A_1a,b_1a,XO1a);
  
  cout<<"\nProblem 5b\n";
  SORTol(pow(10,-3),3,1.2,A_1b,b_1b,XO1b);

  cout<<"\nProblem 5c\n";
  SORTol(pow(10,-3),4,1.2,A_1c,b_1c,XO1c);

  cout<<"\nProblem 5d\n";
  SORTol(pow(10,-3),5,1.2,A_1d,b_1d,XO1d);

  //problem 6
  cout<<"\nProblem 6a\n";
  SORTol(pow(10,-3),3,1.2,A_2a,b_2a,XO2a);
  
  cout<<"\nProblem 6b\n";
  SORTol(pow(10,-3),3,1.2,A_2b,b_2b,XO2b);

  cout<<"\nProblem 6c\n";
  SORTol(pow(10,-3),4,1.2,A_2c,b_2c,XO2c);

  cout<<"\nProblem 6d\n";
  SORTol(pow(10,-3),5,1.2,A_2d,b_2d,XO2d); 

  //Problem 7b 
  cout<<"\nProblem 7b\n";
  SOR(2,3,1.0128,A_1b,b_1b,XO1b);

  //Problem 7c
  cout<<"\nProblem 7c\n";
  SOR(2,4,1.1535,A_1c,b_1c,XO1c);

  //Problem 8d
  cout<<"\nProblem 8d\n";
  SOR(2,6,1.0334,A_2d,b_2d,XO2d);

  //problem 10

  DVec A_10;
  Vec b_10,XO10; 
  
   // create vectors with initial guesses
  for (i=0;i<8;i++) {
    XO10.push_back(0);
  } 

  //create the matrixes into vectors using array from problem 18 
  for (int i = 0; i < 8; i++) {
    Vec row10; // Create an empty row
    b_10.push_back(b18[i]);
    for (int j = 0; j < 8; j++) {
        row10.push_back(A18[i][j]); // Add an element (column) to the row
    }
    A_10.push_back(row10); // Add the row to the main vector
  }
  
  //compute approximation
  cout<<"\nProblem 10\n";
  SORTol (pow(10,-2),8,1.25,A_10,b_10,XO10);
 
  //problem 11
   
  DVec A_11;
  Vec b_11,XO11;

   // create vectors with initial guesses
  for (i=0;i<80;i++) {
    XO11.push_back(0);
  } 
 
  //create the matrixes into vectors use matrices from problem 15
  for (int i = 0; i < 80; i++) {
    Vec row11; // Create an empty row
    b_11.push_back(b15[i]);
    for (int j = 0; j < 80; j++) {
        row11.push_back(A15[i][j]); // Add an element (column) to the row
    }
    A_11.push_back(row11); // Add the row to the main vector
  }
  
  //Compute approximations
  cout<<"\nProblem 11\n";
  SORTol(pow(10,-5),80,1,A_11,b_11,XO11);
}

