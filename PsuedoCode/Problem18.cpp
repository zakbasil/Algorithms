#include <iostream> 
using namespace std; 
  
class Demo{ 
   int a, b; 
    public: 
    Demo()
    { 
        cout << "Default Constructor" << endl; 
    } 

    Demo(int a, int b):a(a),b(b)
    { 
cout << "parameterized constructor -values" <<a<< " "<<b<< endl; 
    } 
      
}dwehbfiwhyb(1,2); 
  
  
int main() { 
    return 0; 
}