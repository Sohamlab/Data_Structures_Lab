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


#include <iostream>
using namespace std;

struct node{
    string name;
    int prn;
    node *next;
};

typedef struct node node;

class club{
     
    public:
      node *pres;
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
      void reverse(node *pres);

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
    int ct = 0;


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

void club::reverse(node *tp){

    
    if(tp->next != NULL){
        
        reverse(tp->next);
    }
    cout<<tp->prn<<"\t";
    cout<<tp->name<<"\t\n";
    

}


int main(){
    club p;
    p.create_club();
    p.display_club();
    node *tp = p.pres;
    p.del_pres();
    p.display_club();
    p.del_sec();
    p.display_club();
    p.del_mem();
    p.display_club();
    p.add_pres();
    p.display_club();
    p.add_sec();
    p.display_club();
    p.add_mem();
    p.display_club();
    p.count();
    club q;
    q.create_club();
    p.concat(q);
    p.display_club();
    cout<<"|PRN\t|"<<"NAME\t|\n";
    cout<<"--------------------------------\n";
    p.reverse(tp);
    
    
    

 
    return 0;
}
(base) comp5@comp5-HP-Pro-SFF-280-G9-Desktop-PC:~/Desktop$ g++ linkedsoham.cpp
(base) comp5@comp5-HP-Pro-SFF-280-G9-Desktop-PC:~/Desktop$ ./a.out
Enter the President Details: Enter Name: sk
Enter PRN: 1
Enter Number of Members: 2
Enter Member Details: Enter Name: a
Enter PRN: 2
Enter Name: b
Enter PRN: 3
Enter the Secretary Details: Enter Name: ss
Enter PRN: 4
Club Details Entered Succesfully!!
|PRN	|NAME	|
--------------------------------
1	sk	
2	a	
3	b	
4	ss	
President Changed!!
|PRN	|NAME	|
--------------------------------
2	a	
3	b	
4	ss	
Secretary Changes!!
|PRN	|NAME	|
--------------------------------
2	a	
3	b	
Enter PRN number of Member to be Deleted: 2
Member Deleted!!
|PRN	|NAME	|
--------------------------------
2	a	
3	b	
Enter the President Details: Enter Name: newpres
Enter PRN: 10
New President Added!!
|PRN	|NAME	|
--------------------------------
10	newpres	
2	a	
3	b	
Enter the Secretary Details: Enter Name: newsec
Enter PRN: 20
New Secretary Added!!
|PRN	|NAME	|
--------------------------------
10	newpres	
2	a	
3	b	
20	newsec	
Enter Member Details: Enter Name: newmem
Enter PRN: 30
|PRN	|NAME	|
--------------------------------
10	newpres	
30	newmem	
2	a	
3	b	
20	newsec	
The Total Number of Members = 5Enter the President Details: Enter Name: xx 
Enter PRN: 1
Enter Number of Members: 2
Enter Member Details: Enter Name: y
Enter PRN: 2
Enter Name: z
Enter PRN: 3
Enter the Secretary Details: Enter Name: zz
Enter PRN: 4
Club Details Entered Succesfully!!
|PRN	|NAME	|
--------------------------------
10	newpres	
30	newmem	
2	a	
3	b	
20	newsec	
1	xx	
2	y	
3	z	
4	zz	
|PRN	|NAME	|
--------------------------------
4	zz	
3	z	
2	y	
1	xx	
20	newsec	
3	b	
2	a	
1	sk	

