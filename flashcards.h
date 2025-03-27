#ifndef FLASHCARDS_H
#define FLASHCARDS_H

#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <sys/stat.h>
#include <string.h>

/** Card structure */
struct card {
    char* key;
    char* val;
};

/** Function prototypes */
char* get_home_path();
int dir_exists(char* path);
int file_exists(char* path);
void home_checker();
int make_new_set(char* name);
int add_to_set(char* set_name, char* key, char* value);
int remove_from_set(char* set_name, int num);
int delete_set(char* set_name);

#endif // FLASHCARDS_H
