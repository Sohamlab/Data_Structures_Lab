#include <iostream>
using namespace std;

struct node{
    string name;
    int prn;
    node *next;
};

typedef struct node node;

class club{
    private:
      node *pres;

    public:
      void create_club();
      void display_club();
      void add_pres();
      void add_sec();
      void add_mem();
      void del_pres();
      void del_sec();
      void del_mem();
      void count();
      void concat(club &cn);
      void reverse();

};

void club::create_club(){
    node *presnode;
    node *secnode;
    node *newnode;
    node *temp;
    int n,i;

    presnode = new node;
    pres = presnode;
    cout<<"Enter the President Details: ";
    cout<<"Enter Name: ";
    cin>>presnode->name;
    cout<<"Enter PRN: ";
    cin>>presnode->prn;
    temp = presnode;

    cout<<"Enter Number of Members: ";
    cin>>n;
    cout<<"Enter Member Details: ";
    for (i=1;i<=n;i++){
        newnode = new node;
        cout<<"Enter Name: ";
        cin>>newnode->name;
        cout<<"Enter PRN: ";
        cin>>newnode->prn;
        newnode->next = NULL;
        temp->next = newnode;
        temp = newnode;
    }

    secnode = new node;
    cout<<"Enter the Secretary Details: ";
    cout<<"Enter Name: ";
    cin>>secnode->name;
    cout<<"Enter PRN: ";
    cin>>secnode->prn;
    secnode->next = NULL;
    temp->next = secnode;

    cout<<"Club Details Entered Succesfully!!\n";
}

void club::display_club(){
    node *temp;
    temp = pres;
    cout<<"|PRN\t|"<<"NAME\t|\n";
    cout<<"--------------------------------\n";
    while (temp != NULL){
        cout<<temp->prn<<"\t";
        cout<<temp->name<<"\t\n";
        temp = temp->next;
    }


}

void club::add_pres(){
    node *temp;
    node *presnode;
    temp = pres;
    presnode = new node;
    pres = presnode;
    cout<<"Enter the President Details: ";
    cout<<"Enter Name: ";
    cin>>presnode->name;
    cout<<"Enter PRN: ";
    cin>>presnode->prn;
    presnode->next = temp;
    cout<<"New President Added!!\n";
}

void club::add_sec(){
    node *temp;
    node *secnode;
    temp = pres;
    while (temp->next != NULL){
        temp = temp->next;
    }
    secnode = new node;
    cout<<"Enter the Secretary Details: ";
    cout<<"Enter Name: ";
    cin>>secnode->name;
    cout<<"Enter PRN: ";
    cin>>secnode->prn;
    secnode->next = NULL;
    temp->next = secnode;
    cout<<"New Secretary Added!!\n";
}

void club::add_mem(){
    node *temp1;
    node *temp2;
    node *newnode;
    temp1 = pres;
    temp2 = temp1->next;
   
    cout<<"Enter Member Details: ";
    newnode = new node;
    cout<<"Enter Name: ";
    cin>>newnode->name;
    cout<<"Enter PRN: ";
    cin>>newnode->prn;
    newnode->next = temp2;
    temp1->next = newnode;
}

void club::del_pres(){
    node *temp;
    temp = pres->next;
    pres = temp;
    cout<<"President Changed!!\n";
}

void club::del_sec(){
    node *temp;
    node *prev;
    temp = pres;
    while (temp->next !=NULL){
        prev = temp;
        temp = temp->next;
    }
    prev->next = NULL;
    delete temp;
    cout<<"Secretary Changes!!\n";  
}

void club::del_mem(){
    int prn;
    node *temp;
    node *prev;
    cout<<"Enter PRN number of Member to be Deleted: ";
    cin>>prn;
    temp = pres;
    prev = pres;
    while(temp->next != NULL){
        if (temp->prn == prn){
            prev->next = temp->next;
            break;
        }
        prev = temp;
        temp = temp->next;
    }
    cout<<"Member Deleted!!\n";
}

void club::count(){
    int ct = 0;
    node *temp;
    temp = pres;
    while (temp != NULL){
        ct+=1;
        temp = temp->next;
    }
    cout<<"The Total Number of Members = "<<ct;
}

void club::concat(club &cn){
    node *temp;
    temp = pres;
    while(temp->next != NULL){
        temp = temp->next;
    }
    temp->next = cn.pres;
}

void club::reverse(){
    node *temp;
    temp = pres;
    while(temp->next != NULL){
        temp = temp->next;
        reverse();
    }
    cout<<"|PRN\t|"<<"NAME\t|\n";
    cout<<"--------------------------------\n";
    cout<<temp->prn<<"\t";
    cout<<temp->name<<"\t\n";
    

}


int main(){
    club p;
    p.create_club();
    p.display_club();

 
    return 0;
}
