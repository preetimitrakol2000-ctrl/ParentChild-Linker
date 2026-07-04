from hierarchy_bridge import HierarchyBridge

if __name__ == "__main__":
    linker = HierarchyBridge()

    # Link microscopic text fragments (children) to full contextual master documents (parents)
    linker.bind_structures(child_id=99, parent_id=900, parent_raw_text="Master Security Policy: Database connections must use encrypted SSL channels on port 5432.")

    # Vector search yields small chunk ID 99
    simulated_vector_hit = 99
    
    # Expand child reference to parent block instantly via memory mappings
    context_expansion = linker.expand_context_window(simulated_vector_hit)

    print("=== PARENTCHILD-LINKER GRANULAR EXPANSION LAYER ===")
    print(f"[*] Search Hit Identified Child Fragment: {simulated_vector_hit}")
    print(f"[*] Expanded Core Master Context Passed to Model Prompt:\n -> {context_expansion}")
