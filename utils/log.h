#include <pthread.h>
#include <stdio.h>

static pthread_mutex_t log_mtx = PTHREAD_MUTEX_INITIALIZER;

#define LOG(...)                  \
    do {                           \
        pthread_mutex_lock(&log_mtx);                      \
        fprintf(stdout, "%s: ", __func__); \
        fprintf(stdout, __VA_ARGS__);\
        fprintf(stdout, "\n");\
        pthread_mutex_unlock(&log_mtx); \
    } while (0)

#define DLOG(...) LOG("[DEBUG]: " __VA_ARGS__)
