#include <iostream>
#include <fstream>
#include <math.h>

// setting maximum number of timesteps (2^27)
#define MAX 134217728

using namespace std;

float dt;
int steps;

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

void run(float (&t)[MAX], float (&x)[MAX]){
    // initial state of time and position
    t[0]=0;
    x[0]=1;

    // running Euler integration
    for(int i=1;i<steps;i++){
        t[i]=t[i-1]+dt;
        x[i]=(1-3*dt)*x[i-1];
    }
    return;
}

void saveFile(float t[MAX], float x[MAX], string fileName){
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

int main(){
    readFile("params.dat");
    // calculating number of steps in 9 seconds
    steps=int(9/dt);
    // creating arrays for time and position
    float t[MAX];
    float x[MAX];
    run(t,x);




    return 0;
}