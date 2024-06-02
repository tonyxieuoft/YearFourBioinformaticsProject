import os
from After_BLAST.concatenate_exons import concatenate_exons


def concatenate_gene_results(exon_pull_path, blast_path, save_path):

    for gene in os.listdir(exon_pull_path):
        gene_file = open(save_path + "\\" + gene + ".fas", "a")
        gene_path = exon_pull_path + "\\" + gene
        for taxa in os.listdir(gene_path):
            taxa_path = gene_path + "\\" + taxa
            for species in os.listdir(taxa_path):
                species_path = taxa_path + "\\" + species
                for file in os.listdir(species_path):
                    to_write = concatenate_exons(species_path + "\\" + file)
                    gene_file.write(to_write)

        gene_file.close()

    for gene in os.listdir(blast_path):
        gene_file = open(save_path + "\\" + gene + ".fas", "a")
        gene_path = blast_path + "\\" + gene
        for taxa in os.listdir(gene_path):
            taxa_path = gene_path + "\\" + taxa
            for species in os.listdir(taxa_path):
                species_path = taxa_path + "\\" + species
                for file in os.listdir(species_path):
                    to_write = concatenate_exons(species_path + "\\" + file)
                    gene_file.write(to_write)

        gene_file.close()

if __name__ == "__main__":

    exon_pull_path = r"C:\Users\tonyx\Downloads\NCBI_exon_pull_results (2)"
    blast_path = r"C:\Users\tonyx\Downloads\blast_test_again4"
    save_path = r"C:\Users\tonyx\Downloads\alignments (2)"
    concatenate_gene_results(exon_pull_path, blast_path, save_path)
