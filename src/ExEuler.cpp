#include <iostream>
#include <fstream>
#include <climits>
#include <math.h>

// setting maximum number of timesteps (2^27)
#define MAX 134217728

using namespace std;

// creating global variables
float dt;
int steps;

void readFile(string fileName);

void run(double* &t, double* &x);

void saveFile(double t[MAX], double x[MAX], string fileName);

int main(){
    string inputFile = "../data/params.dat";
    readFile(inputFile);

    // calculating number of steps in 9 seconds
    steps=int(9/dt);

    // creating arrays for time and position
    double* t;
    double* x;

    t = new double[MAX];
    x = new double[MAX];

    run(t,x);

    string outputFile = "../data/output.dat";
    saveFile(t,x,outputFile);

    return 0;
}

void readFile(string fileName){
    // creating input stream
    ifstream fin(fileName);
    if (fin.fail()){ // reporting failed read
        cout << "FAILED TO READ FILE" << endl;
        return;
    }

    // reading data
    fin >> dt;

    // closing file
    fin.close();

    return;
}

void run(double* &t, double* &x){
    // initial state of time and position
    t[0]=0.0;
    x[0]=1.0;

    // running Euler integration
    for(int i=1;i<steps;i++){
        t[i]=t[i-1]+dt;
        x[i]=(1-3*dt)*x[i-1];
    }

    return;
}

void saveFile(double t[MAX], double x[MAX], string fileName){
    // creating output stream
    ofstream fout(fileName);
    if (fout.fail()){ // reporting failed write
        cout << "FAILED TO WRITE FILE" << endl;
        return;
    }

    // writing data
    for(int i=0;i<steps;i++){
        fout << t[i] << " " << x[i] << endl;
    }

    return;
}