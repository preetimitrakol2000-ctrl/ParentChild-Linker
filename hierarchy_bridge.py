import ctypes
import os
import sys

class HierarchyBridge:
    def __init__(self):
        if not os.path.exists("./libhierarchy.so") and not os.path.exists("./libhierarchy.dll"):
            if sys.platform.startswith("win"):
                os.system("gcc -shared -o libhierarchy.dll parent_child_map.c")
                lib_path = "./libhierarchy.dll"
            else:
                os.system("gcc -shared -fPIC -o libhierarchy.so parent_child_map.c")
                lib_path = "./libhierarchy.so"
        else:
            lib_path = "./libhierarchy.dll" if sys.platform.startswith("win") else "./libhierarchy.so"

        self.lib = ctypes.CDLL(lib_path)
        self.lib.init_registry.restype = ctypes.c_void_p
        self.lib.map_hierarchical_bounds.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
        self.lib.get_expanded_parent.argtypes = [ctypes.c_void_p, ctypes.c_int]
        self.lib.get_expanded_parent.restype = ctypes.c_char_p
        
        self.registry_ptr = self.lib.init_registry()

    def bind_structures(self, child_id: int, parent_id: int, parent_raw_text: str):
        self.lib.map_hierarchical_bounds(self.registry_ptr, child_id, parent_id, parent_raw_text.encode('utf-8'))

    def expand_context_window(self, matched_child_id: int) -> str:
        return self.lib.get_expanded_parent(self.registry_ptr, matched_child_id).decode('utf-8')
