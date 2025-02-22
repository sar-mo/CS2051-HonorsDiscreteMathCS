# CS 2051 Spring 2023 - HW9 Supplement Parts 2-3: Context-Free Grammars and Syntatical Structures
# instructor: Gerandy Brito
# creator - Sarthak Mohanty

# author - your name here
# collaborators - N/A

# NOTE: Use [] to describe the empty string

def generate_cfg_example() -> list:
    """Generates a CFG for the language {0^n 1^n : n \in N}"""
    cfg = []
    # S generates 0S1
    cfg.append(('S', ['0', 'S', '1']))
    # S generates the empty string
    cfg.append(('S', []))
    return cfg

def generate_cfg_binary() -> list:
    """Generates a CFG for the language {s : s has the same number of 1s and 0s}"""
    raise NotImplementedError

def generate_cfg_union() -> list:
    """Generates a CFG for the language {a^i b^j c^k : i, j, k \in N and (i = j or i = k)}"""
    raise NotImplementedError

def generate_cfg_rna() -> list:
    """Generates a CFG for the language {s : s is a valid stem loop rna sequence}"""
    raise NotImplementedError

def generate_cfg_tricky() -> list:
    """Generates a CFG for the language {1^i 0^j : 2i != 3j + 1}"""
    raise NotImplementedError

def generate_cfg_logic(atoms : set) -> list:
    """Generates a CFG for the language {s : s is a valid logical expression}
        The alphabet is the set of atoms, and the operators are "|", "&", "!", "=>", "<=>", "(", ")", "T", and "F"
        
        Parameters:
            atoms - the set of atomic propositions in the language. Assume atoms is a subset of the lowercase alphabet"""
    raise NotImplementedError

def generate_cfg_english(parts_of_speech : dict) -> list:
    """Generates a CFG for (some subset of) the language {s : s is a valid english sentence}

        Parameters:
            parts_of_speech - a dictionary mapping parts of speech to lists of words of that part of speech.
            See test cases for examples of parts_of_speech"""
    raise NotImplementedError