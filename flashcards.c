#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <sys/stat.h>
#include <string.h>

/** Card structure*/
struct card {
    char* key;
    char* val;
};

/** Global for the home path*/
char home_path[1024];

/** Returns the path where the users flashcard sets will be found*/
char* get_home_path() {
    char* home = getenv("HOME");
    if (home == NULL) {
        return NULL;
    }

    snprintf(home_path, sizeof(home_path), "%s/%s", home, "flashcard_sets");
    return home_path;
}

/** Returns 1 if directory exists, 0 otherwise. */
int dir_exists(char* path){
    struct stat info;
    if (stat(path, &info) == 0 && S_ISDIR(info.st_mode)){
        return 1;
    }

    return 0;
}

int file_exists(char* path){
    struct stat info;
    if (stat(path, &info) == 0 && S_ISREG(info.st_mode)){
        return 1;
    }

    return 0;
}



/** Checks if the home directory for flashcards exists, otherwise creates it. */
void home_checker(){    
    if (dir_exists(get_home_path())){
        printf("The directory exists\n");
    } else {
        mkdir(get_home_path(), 0777);
        //chmod(get_home_path(), 0777);
    }
}

/**Creats new card set */
int make_new_set(char* name){
    char path[1024];
    snprintf(path, sizeof(path), "%s/%s", get_home_path(), name);
    strcat(path, ".csv");

    if (dir_exists(path)){
        printf("Error: set '%s' already exists\n", name);
        return -1;
    } 

    printf("Path: %s\n", path);
    FILE *new_file = fopen(path, "w");
    fclose(new_file);
    return 0;
}

/** Checks if the flashcards set exists, adds key, value pair. */
int add_to_set(char* set_name, char* key, char* value){
    char path[1024];
    snprintf(path, sizeof(path), "%s/%s", get_home_path(), set_name);
    strcat(path, ".csv");

    FILE *file = fopen(path, "a");
    if (file == NULL) {
        perror("fopen failed\n");
        return -1;
    }
    fprintf(file, "%s, %s\n", key, value);
    fclose(file);

    return 0;
}

int main (int argc, char** argv){
    int opt;
    int a = 0, r = 0, c = 0;

    while((opt = getopt(argc, argv, "arc")) != -1){
        switch(opt){
            case 'a':
            a++;
            break;

            case 'r':
            r++;
            break;

            case 'c':
            c++;
            break;

            case '?':
            printf("Error: Unknown flag '-%c' provided\n", optopt);
            return EXIT_FAILURE;
        }
    }

    if (a + r + c > 1){
        printf("Error: Only one option can be selected at a time\n");
        return EXIT_FAILURE;
    }

    home_checker();

    //c for creates
    if (c > 0){
        char* name = strdup(argv[2]);
        make_new_set(name);
        free(name);
    }

    // a for add 
    if (a > 0){
        printf("adding");
        char* set_name = strdup(argv[2]);
        char* key = strdup(argv[3]);
        char* value = strdup(argv[4]);
        add_to_set(set_name, key, value);
        free(set_name);
        free(key);
        free(value);
    }

    // r for remove 
    if (r > 0){

    }

    return EXIT_SUCCESS;
}