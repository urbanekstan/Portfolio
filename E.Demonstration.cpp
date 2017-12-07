//////////////////////////////////////////
// Title: E.Demonstration.cpp

// Description: Simple script to demonstrate working knowledge
//              of classes, multithreading, pointers, and organization.

//              Script creates simples vector manager class to manipulate.

// Author: Stanley Urbanek

// Date Created: 12/5/17

// References: http://www.cplusplus.com/reference/ctime/time/
//////////////////////////////////////////

// Header File
#include "E.Demonstration.h"

// Defining summation function for VectorManager class
void VectorManager::summation() {
  for (int i = 0; i < sizeOfVectors; i++) {
    cout << "inside \n" ;
    VectorManager::sum = VectorManager::sum + VectorManager::vctr[i];
  }
  
  return VectorManager::sum;
}

// Main function
int main() {

  // User input: Run script using threads or not?
  int threadLogical;
  cout << "\nHow to run script? (0) Using multithreading (1) Not using multithreading\nEnter Option: ";
  cin >> threadLogical;
  
  // Initialize vectors and their values
  VectorManager aVec, bVec, cVec, dVec, eVec;
  aVec.vctr.resize(sizeOfVectors);
  bVec.vctr.resize(sizeOfVectors);
  cVec.vctr.resize(sizeOfVectors);
  dVec.vctr.resize(sizeOfVectors);
  eVec.vctr.resize(sizeOfVectors);

  // Populate all vectors with integers sequentially allotted
  for (int i = 0; i < sizeOfVectors; i++) {
    aVec.vctr[i] = i;
  }

  aVec.summation();
  cout << aVec.sum << '\n';

  for(int n = 0; n < aVec.vctr.size(); n++) {
    cout << n << ' ';
  }

  // Thread through vectors and add
  thrd(VectorManager::summation, summation());
  //thrd[2] = thread(bVec.summation());

  return 0;
}
