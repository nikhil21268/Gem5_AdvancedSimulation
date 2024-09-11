#include "sim/maths_operations.hh"
#include <iostream>
#include <base/trace.hh>
#include <debug/FIBONACCISEQUENCE.hh>
#include <debug/FIBONACCINUMBER.hh>
#include <debug/PRIMECHECK.hh>  
#include <debug/GCDRESULT.hh>
#include <debug/GCDNUMBER.hh>

namespace gem5 {

MathsOperations::MathsOperations(const MathsOperationsParams &params) :
    SimObject(params), 
    event([this]{processEvent();}, name()), 
    fibEvent([this]{processEvent1();}, name()), 
    primeEvent([this]{processEvent2();}, name()), 
    gcdEvent([this]{processEvent3();}, name())
{
    std::cout << "Hello World! From a SimObject!" << std::endl;
}

void
MathsOperations::processEvent()
{
    DPRINTF(FIBONACCISEQUENCE, "Hello world! Processing the event!\n");
}

void
MathsOperations::processEvent1()
{
    int n = 5;
    DPRINTF(FIBONACCISEQUENCE, "Generating Fibonacci sequence for number: %d\n", n);
    int a = 0, b = 1, c;
    for (int i = 0; i < n; ++i) {
        DPRINTF(FIBONACCISEQUENCE, "%d ", a);
        c = a + b;
        a = b;
        b = c;
    }
    std::cout << std::endl;
    DPRINTF(FIBONACCINUMBER, "Final Fibonacci number: %d\n", n);
}

void
MathsOperations::processEvent2()
{
    int num = 7;
    DPRINTF(PRIMECHECK, "Checking if number is prime: %d\n", num);
    if (num <= 1) {
        DPRINTF(PRIMECHECK, "%d is not prime (less than or equal to 1).\n", num);
        // std::cout << num << " is not prime." << std::endl;
    }
    for (int i = 2; i * i <= num; ++i) {
        if (num % i == 0) {
            DPRINTF(PRIMECHECK, "%d is not prime (divisible by %d).\n", num, i);
            // std::cout << num << " is not prime." << std::endl;
        }
    }
    DPRINTF(PRIMECHECK, "%d is prime.\n", num);
    // std::cout << num << " is prime." << std::endl;
}

void
MathsOperations::processEvent3()
{
    int a = 12, b = 18;
    DPRINTF(GCDNUMBER, "Calculating GCD for numbers: %d, %d\n", a, b);
    while (b != 0) {
        int t = b;
        b = a % b;
        a = t;
        DPRINTF(GCDRESULT, "Intermediate GCD results: %d, %d\n", a, b);
    }
    DPRINTF(GCDRESULT, "Final GCD is: %d\n", a);
    // std::cout << "GCD " << "is " << a << std::endl;
}


void
MathsOperations::startup()
{
    schedule(event, 10);
    schedule(fibEvent, 100);
    schedule(primeEvent, 1000);
    schedule(gcdEvent, 10000);
}

} // namespace gem5


