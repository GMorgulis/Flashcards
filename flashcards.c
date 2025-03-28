#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <sys/stat.h>
#include <string.h>

/** Returns the path where the users flashcard sets will be found*/
char* sets_hub() {
    return "flashcard_sets";
}

/** Returns 1 if directory exists, 0 otherwise. */
int dir_exists(char* path){
    struct stat info;
    if (stat(path, &info) == 0 && S_ISDIR(info.st_mode)){
        return 1;
    }

    return 0;
}

/** Checks if a file exists at the given path */
int file_exists(char* path){
    struct stat info;
    if (stat(path, &info) == 0 && S_ISREG(info.st_mode)){
        return 1;
    }

    return 0;
}

/** Checks if the home directory for flashcards exists, otherwise creates it. */
void home_checker(){
    if (!dir_exists(get_home_path())){
        mkdir(get_home_path(), 0777);
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
    // add error handeling 
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
        //perror("fopen failed\n");
        return -1;
    }
    fprintf(file, "%s, %s\n", key, value);
    fclose(file);

    return 0;
}

/** Removes flashcards with give number for set */
int remove_from_set(char* set_name, int num){
    char src[1024];
    snprintf(src, sizeof(src), "%s/%s", get_home_path(), set_name);
    strcat(src, ".csv");

    char dest[1024];
    snprintf(dest, sizeof(dest), "%s/%s", get_home_path(), "txzf123");
    strcat(dest, ".csv");

    FILE *src_file = fopen(src, "r");
    FILE *dest_file = fopen(dest, "w");

    if (src_file == NULL){
        printf("Error: Could not open the scource file\n");
        return -1;
    }

    if (dest_file == NULL){
        printf("Erro : Could not open the destination file\n");
        return -1;
    }

    int count = 0;
    char buffer[1024];  
    while (fgets(buffer, sizeof(buffer), src_file)) {
        if (num != count){
            fputs(buffer, dest_file);
        }
        count++;
    }

    fclose(src_file);
    fclose(dest_file);

    remove(src);
    strcat(set_name, ".csv");
    rename(dest, src);

    return 0;
}

/** Removes set of flashcards. */
int delete_set(char* set_name){
    char src[1024];
    snprintf(src, sizeof(src), "%s/%s", get_home_path(), set_name);
    strcat(src, ".csv");
    remove(src);
    return 0;
}

int main (int argc, char** argv){
    int opt;
    int a = 0, r = 0, c = 0, d = 0;

    while((opt = getopt(argc, argv, "arcd")) != -1){
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

            case'd':
            d++;
            break;

            case '?':
            printf("Error: Unknown flag '-%c' provided\n", optopt);
            return EXIT_FAILURE;
        }
    }

    // only one flag at a time
    if (a + r + c + d > 1){
        printf("Error: Only one option can be selected at a time\n");
        return EXIT_FAILURE;
    }

    home_checker();

    if (c > 0){
        char* name = strdup(argv[2]);
        make_new_set(name);
        free(name);
    }

    if (a > 0){
        char* set_name = strdup(argv[2]);
        char* key = strdup(argv[3]);
        char* value = strdup(argv[4]);
        add_to_set(set_name, key, value);
        free(set_name);
        free(key);
        free(value);
    }

    if (r > 0){
        char* set_name = strdup(argv[2]);
        int position = atoi(argv[3]);
        remove_from_set(set_name, position);
        free(set_name);
    }

    if (d > 0){
        char* set_name = strdup(argv[2]);
        delete_set(set_name);
        free(set_name);
    }

    return EXIT_SUCCESS;
}