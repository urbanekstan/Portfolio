////////////////////////////////////////////
// Title: E.Demonstration.h

// Description: Header file that accompanies E.Demonstration.cpp

// Author: Stanley Urbanek

// Date Created: 12/5/17
////////////////////////////////////////////


// Header files
#include <iostream>
#include <vector>
#include <thread>
#include <time.h> 
#include <functional>
#include <unistd.h>

using namespace std;


// Initialize thread values
static const int maxThreads = 5;
thread thrd[maxThreads];

// Initialize other values
static const int sizeOfVectors = 10;

// Class for managing a vector in this demonstrative capacity 
class VectorManager {

 public:

  double sum = 0;      // Sum of the vector population
  vector<int> vctr; // Vector to be operated on
  void summation();

 private:
  double operatedOn;  // Logical for keeping track of what has been operated on

};

