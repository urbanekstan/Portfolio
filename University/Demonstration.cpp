//////////////////////////////////////////
// Title: E.Demonstration.cpp

// Description: Simple script to demonstrate working knowledge
//              of software design principles (classes, multithreading,
//              organization).

//              Script creates simples vector manager class to manipulate.

// Author: Stanley Urbanek

// Date Created: 12/5/17
//////////////////////////////////////////

// Header File
#include "E.Demonstration.h"


// Defining summation function for VectorManager class
void VectorManager::summation() {
  for (int i = 0; i < sizeOfVectors; i++) {
    VectorManager::sum = VectorManager::sum + VectorManager::vctr[i];
  }
  return;
 
}

// Main function
int main() {
  
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

  // Thread through vectors and add
  thrd[0] = thread(std::bind(&VectorManager::summation, aVec));
  thrd[1] = thread(std::bind(&VectorManager::summation, bVec));
  thrd[2] = thread(std::bind(&VectorManager::summation, cVec));
  thrd[3] = thread(std::bind(&VectorManager::summation, dVec));
  thrd[4] = thread(std::bind(&VectorManager::summation, eVec));

  usleep(1000000);
  // Join the threads with main thread
  for (int i = 0; i < sizeOfVectors; i++) {
    thrd[i].join();
  }

  return 0;
}
