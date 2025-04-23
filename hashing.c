#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>


//implement hash table in C

//functionalities to include
//insert, delete, find
//expected time complexity is O(1)
//also handle collisions using a linked list

//create linked list for hashtable
#define TABLE_SIZE 100

typedef struct node{
    int val;
    int key;
    struct node* next;
}node;

typedef struct table{
    node** buckets;
    int table_size;

}table;


table* create_table(){
    table* hash_table = malloc(sizeof(table));
    hash_table->buckets= calloc(TABLE_SIZE, sizeof(node*));
    hash_table->table_size = TABLE_SIZE;
    return hash_table;

}


// int hash(int table_size, )

void insert(table* hashAddr,int data, int key){
    int index = hash(key);
    node* nodeAddr = malloc(sizeof(node));

    nodeAddr->key = key;
    nodeAddr->val = data;
    nodeAddr->next = hashAddr->buckets[index];

    hashAddr->buckets[index]= nodeAddr;
    return;   
}
int *get(table* ht, int key){
    int index = hash(key);
    node* curr = ht->buckets[index];
    while(curr){
        if(curr->key ==key){
            return &curr->val;
        }
        curr = curr->next;
    }
    return NULL;
}

void delete(table* ht, int key){
    int index = hash(key);
    node* curr = ht->buckets[index];
    node* prev = NULL;
    while(curr){
        if(curr->key == key){
            if(prev){
                prev->next= curr->next;
            }
            else{
                ht->buckets[index]= curr->next;
            }
            free(curr);
            return;
        }
        prev = curr;
        curr = curr->next;
    }
    return ;

}
