#include<bits/stdc++.h>
using namespace std;

struct node{
  int data;
  node *left;
  node *right;
};
typedef struct node node;

class bst{
  private:
    node *root;
    
  public: 
    bst(){
      root = NULL;
    }
    void insert(int data);
    void display(node *curr);
    void display();
    
    

};

void bst::insert(int data){
      node *newnode,*temp,*parent;
      newnode = new node;
      newnode->data = data;
      newnode->left = NULL;
      newnode->right = NULL;
      if(root == NULL){
        root = newnode;
        return;
      }
      else{
        temp = root;
        parent = NULL;
        while(temp != NULL){
          parent = temp;
          if(data < temp->data){
            temp = temp->left;
          }
          else{
            temp = temp->right;
          }
        }
        if(data < parent->data){
          parent->left = newnode;
        }
        else{
          parent->right = newnode;
        }
        cout<<"Node Inserted Succesfully!!";
      }
    }

void bst::display(node *curr){
  if(curr != NULL){
    display(curr->left);
    cout<<curr->data<<" ";
    display(curr->right);
  }
 }
 
void bst::display(){
  display(root);
}


int main(){
  bst t1;
  int option,data;
  bool Flag = true;
  while(Flag){
  cout<<"1. Insert Data to tree. "<<endl;
  cout<<"2. Display Data (Inorder) "<<endl;
  cout<<"3. EXIT "<<endl;
  cin>>option;
  switch(option){
    case 1:
       cout<<"Enter Data: "<<endl;
       cin>>data;
       t1.insert(data);
       break;
    case 2:
       cout<<"THe TREE is as follows: "<<endl;
       t1.display();
       break;
    case 3:
       Flag = false;
       break;       
  }
 }
  return 0;
}
