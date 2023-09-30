def molecular_weight(seq):
    pass


def three_letter_code(seq):
    pass


def show_length(seq):
    pass


def folding(seq):
    '''
    Counts the number of amino acids characteristic separately for alpha helixes and beta sheets,
    and gives out what will be the structure of the protein more.
    This function has been tested on proteins such as 2M3X, 6DT4 (PDB ID) and MHC, CRP. The obtained results corresponded to reality.
        Parameters:
            seq (str): amino acid sequence
        Returns:
            (str): overcoming structure ('alfa_helix', 'beta_sheet', 'equally')
    '''
    alfa_helix = ['A', 'E', 'L', 'M', 'G', 'Y', 'S', 'a', 'e', 'l', 'm', 'g', 'y', 's']
    beta_sheet = ['Y', 'F', 'W', 'T', 'V', 'I', 'y', 'f', 'w', 't', 'v', 'i']
    alfa_helix_counts = 0
    beta_sheet_counts = 0
    for amino_acid in seq:
        if amino_acid in alfa_helix:
            alfa_helix_counts += 1
        elif amino_acid in beta_sheet:
            beta_sheet_counts += 1
    if alfa_helix_counts > beta_sheet_counts:
        return 'alfa_helix'
    elif alfa_helix_counts < beta_sheet_counts:
        return 'beta_sheet'
    elif alfa_helix_counts == beta_sheet_counts:
        return 'equally'


def function(seq):
    pass


def aminoacid_seqs_only(seqs):
    '''
    Leaves only the amino acid sequences from the fed into the function.
        Parameters:
            seqs (list): amino acid sequence list
        Returns:
            aminoacid_seqs (list): amino acid sequence list without non amino acid sequence
    '''
    aminoacid_seqs = []
    for seq in seqs:
        unique_chars = set(seq)
        amino_acid = set('ARNDVHGQEILKMPSYTWFOUCarndvhgqeilkmpsytwfouc')
        if unique_chars <= amino_acid:
            aminoacid_seqs.append(seq)
    return aminoacid_seqs


def amino_acid_tools(*args):
    '''
    Performs functions for working with protein sequences.
    
        Parameters:
            The function must accept an unlimited number of protein sequences (str) as input,
            the last  variable must be the function (str) you want to execute.
            The amino acid sequence can consist of both uppercase and lowercase letters.
            Input example:
    	        amino_acid_tools('PLPKVEL','VDviRIkLQ','PPDFGKT','folding')
    	    Function:
    	        molecular_weight:
    	        three_letter_code:
    	        show_length:
    	        folding: 
    	        function: counts the number of amino acids characteristic separately for alpha helixes and beta sheets,
    	                  and gives out what will be the structure of the protein more
    	        
        Returns:
            If one sequence is supplied, a string with the result is returned.
            If several are submitted, a list of strings is returned.
    	    Depending on the function performed, the following returns will occur:
    	        molecular_weight (int) or (list): amino acid sequence molecular weight number or list of numbers
    	        three_letter_code (str) or (list):
    	        show_length (int) or (list):
    	        folding (str) or (list): 'alpha_helix', if there are more alpha helices
    	                                 'beta_sheet', if there are more beta sheets
    	                                 'equally', if the probability of alpha spirals and beta sheets are the same
    	        function (str) or (list):
    '''
    *seqs, function = args
    d_of_functions = {'molecular_weight': molecular_weight, 
                      'three_letter_code': three_letter_code,
                      'show_length': show_length,
                      'folding': folding,
                      'function': function
                     }
    answer = []
    aminoacid_seqs = aminoacid_seqs_only(seqs)
    for sequence in aminoacid_seqs:
        answer.append(d_of_functions[function](sequence))
    if len(answer) == 1:
        return answer[0]
    else:
        return answer
