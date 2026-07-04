#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_RELATIONS 10

typedef struct {
    int child_id;
    int parent_id;
    char parent_full_text[256];
} StructureLink;

typedef struct {
    StructureLink relationships[MAX_RELATIONS];
    int count;
} MappingRegistry;

#ifdef _WIN32
    __declspec(dllexport) MappingRegistry* init_registry();
    __declspec(dllexport) void map_hierarchical_bounds(MappingRegistry* mr, int child, int parent, const char* full_text);
    __declspec(dllexport) const char* get_expanded_parent(MappingRegistry* mr, int child);
#endif

MappingRegistry* init_registry() {
    MappingRegistry* mr = (MappingRegistry*)malloc(sizeof(MappingRegistry));
    mr->count = 0;
    return mr;
}

void map_hierarchical_bounds(MappingRegistry* mr, int child, int parent, const char* full_text) {
    if (mr->count < MAX_RELATIONS) {
        int idx = mr->count;
        mr->relationships[idx].child_id = child;
        mr->relationships[idx].parent_id = parent;
        strncpy(mr->relationships[idx].parent_full_text, full_text, sizeof(mr->relationships[idx].parent_full_text) - 1);
        mr->count++;
    }
}

const char* get_expanded_parent(MappingRegistry* mr, int child) {
    for (int i = 0; i < mr->count; i++) {
        if (mr->relationships[i].child_id == child) {
            return mr->relationships[i].parent_full_text;
        }
    }
    return "TARGET_NOT_LINKED";
}
