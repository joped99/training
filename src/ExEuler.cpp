#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

void readFile(string fileName){
    // creating input stream
    ifstream fin(fileName);
    if (fin.fail()){
        cout << "FAILED TO READ FILE" << endl;
        return;
    }

    // reading data
    float dt;
    float MAX;
    fin >> dt >> MAX;

    // closing file
    fin.close();
}

int main(){
    readFile("params.dat");



    return 0;
}