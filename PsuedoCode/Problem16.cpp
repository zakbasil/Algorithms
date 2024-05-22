using namespace std;    
class Test 
{ 
  public:
  static int i; 
  int j; 

  Test(){
    i++;
  }
};

int Test::i = 0;

int main() 
{ 
    cout<<Test::i<<endl;
    Test t1;
    cout<<Test::i<<endl;
    Test t2;
    cout<<Test::i<<endl;
    return 0; 
} 