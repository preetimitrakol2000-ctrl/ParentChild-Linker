#ifndef PARENT_CHILD_MAP_H
#define PARENT_CHILD_MAP_H

typedef struct StructureLink StructureLink;
typedef struct MappingRegistry MappingRegistry;
MappingRegistry* init_registry();
void map_hierarchical_bounds(MappingRegistry* mr, int child, int parent, const char* full_text);
const char* get_expanded_parent(MappingRegistry* mr, int child);

#endif
