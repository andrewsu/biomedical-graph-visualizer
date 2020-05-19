#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from .templates import *

### PATHS
QUERIES_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(QUERIES_DIR, "download")
GRAPH_PICKLE_PATH = os.path.join(QUERIES_DIR, "BGV_Graph.pkl")

### CORE CONCEPTS
DRUG = "Drug"
DRUG_ID = "Q8386"
CHEMICAL_COMPOUND = "Chemical Compound"
CHEMICAL_COMPOUND_ID = "Q11173"
GENE = "Gene"
GENE_ID = "Q7187"
PROTEIN = "Protein"
PROTEIN_ID = "Q8054"
DISEASE = "Diseases"
DISEASE_ID = "Q12136"
SYMPTOM = "Symptom"
SYMPTOM_ID = "Q169872"

### PERIPHERAL CONCEPTS
MOLECULAR_FUNCTION = "Molecular Function"
MOLECULAR_FUNCTION_ID = "Q14860489"
BIOLOGICAL_PROCESS = "Biological Process"
BIOLOGICAL_PROCESS_ID = "Q2996394" 
CHEMICAL_COMPOUND = "Chemical Compound"
CHEMICAL_COMPOUND_ID = "Q11173"
MEDICAL_SPECIALTY = "Medical Specialty"
MEDICAL_SPECIALTY_ID = "Q930752"
CAUSE = "Symptom Cause"
CAUSE_ID = "CAUSEID"
ICD10 = "ICD10"
ICD10_ID = "ICD10ID"
PROTEIN_FAMILY = "Protein Family"
PROTEIN_FAMILY_ID = "Q417841"
PROTEIN_SUPERFAMILY = "Protein Superfamily"
PROTEIN_SUPERFAMILY_ID = "Q7251477"
PROTEIN_DOMAIN = "Protein Domain"
PROTEIN_DOMAIN_ID = "Q7251502"
GO = "Gene Ontology ID"
GO_ID = "GOID"
CHROMOSOME = "Chromosome"
CHROMOSOME_ID = "Q37748"
#CHROMOSOME_STRAND = "Chromosome Strand"
#CHROMOSOME_STRAND_ID = ["Q22809680","Q22809711"]
DRUG_FUNCTION = "Drug Function"
DRUG_FUNCTION_ID = "DRUGFUNCTIONID"
PHARMACEUTICAL_PRODUCT = "Pharmaceutical Product"
PHARMACEUTICAL_PRODUCT_ID = "Q288851002"

## RELATIONSHIPS
HAS_GO = "has gene ontology ID"
HAS_GO_ID = "P686"
PART_OF = "part of"
PART_OF_ID = "P361"
HAS_PART = "has part"
HAS_PART_ID = "P527"
GENETIC_ASSOCIATION = "genetic association"
GENETIC_ASSOCIATION_ID = "P2293"
ENCODES = "encodes"
ENCODES_ID = "P688"
ENCODED_BY = "encoded by"
ENCODED_BY_ID = "P702"
INFLUENCED_BY = "influenced by"
INFLUENCED_BY_ID = "P737"
RELATED_MOLECULAR_FUNCTION = "related molecular function" # actually named ‘molecular function’
RELATED_MOLECULAR_FUNCTION_ID = "P680"
RELATED_BIOLOGICAL_PROCESS = "related biological process" # actually named ‘biological process’
RELATED_BIOLOGICAL_PROCESS_ID = "P682"

IN_CHROMOSOME = "in chromosome" # actually named “chromosome”
IN_CHROMOSOME_ID = "P1057"
STRAND_ORIENTATION = "strand orientation"
STRAND_ORIENTATION_ID = "P2548"
#GENE_SUBSTITUTION_ASSOCIATION_WITH = "gene substitution association with"
#GENE_SUBSTITUTION_ASSOCIATION_WITH_ID = "P1916"
GENETIC_ASSOCIATION = "genetic association"
GENETIC_ASSOCIATION_ID = "P2293"
DRUG_USED_FOR_TREATMENT = "drug used for treatment"
DRUG_USED_FOR_TREATMENT_ID = "P2176"
HAS_CAUSE = "has cause"
HAS_CAUSE_ID = "P828"
HEALTH_SPECIALTY = "health specialty"
HEALTH_SPECIALTY_ID = "P1995"
HAS_ICD10 = "has ICD10 code"
HAS_ICD10_ID = "P494"
SUBCLASS = "subclass of"
SUBCLASS_ID = "P279"
HAS_ACTIVE_INGREDIENT = "has active ingredient"
HAS_ACTIVE_INGREDIENT_ID = "P2781"
ACTIVE_INGREDIENT_IN = "active ingredient in"
ACTIVE_INGREDIENT_IN_ID = "P3780"
MEDICAL_CONDITION_TREATED = "medical condition treated"
MEDICAL_CONDITION_TREATED_ID = "P2175"
ACTIVATOR_OF = "activator of"
ACTIVATOR_OF_ID = "P3771"
PHYSICALLY_INTERACTS_WITH = "physically interacts with"
PHYSICALLY_INTERACTS_WITH_ID = "P129"
SIGNIFICANT_DRUG_INTERACTION = "significant drug interaction"
SIGNIFICANT_DRUG_INTERACTION_ID = "P769"
SUBJECT_HAS_ROLE = "subject has role" 
SUBJECT_HAS_ROLE_ID = "P2868"

# MAPPINGS
CORE_CONCEPT_LABEL_ID_DICT = {
	DRUG:DRUG_ID,
	CHEMICAL_COMPOUND:CHEMICAL_COMPOUND_ID,
	GENE:GENE_ID,
	PROTEIN:PROTEIN_ID,
	DISEASE:DISEASE_ID,
	SYMPTOM:SYMPTOM_ID,
}

PERIPHERAL_CONCEPT_LABEL_ID_DICT = {
	MOLECULAR_FUNCTION: MOLECULAR_FUNCTION_ID,
	BIOLOGICAL_PROCESS: BIOLOGICAL_PROCESS_ID,
	CHEMICAL_COMPOUND: CHEMICAL_COMPOUND_ID,
	MEDICAL_SPECIALTY: MEDICAL_SPECIALTY_ID,
	ICD10: ICD10_ID,
	PROTEIN_FAMILY: PROTEIN_FAMILY_ID,
	PROTEIN_SUPERFAMILY: PROTEIN_SUPERFAMILY_ID,
	PROTEIN_DOMAIN: PROTEIN_DOMAIN_ID,
	GO: GO_ID,
	CHROMOSOME: CHROMOSOME_ID,
	#CHROMOSOME_STRAND: CHROMOSOME_STRAND_ID,
	DRUG_FUNCTION: DRUG_FUNCTION_ID,
	PHARMACEUTICAL_PRODUCT: PHARMACEUTICAL_PRODUCT_ID,
	CAUSE: CAUSE_ID,
	HEALTH_SPECIALTY: HEALTH_SPECIALTY_ID,
}

CONCEPT_LABEL_ID_DICT = dict()
CONCEPT_LABEL_ID_DICT.update(CORE_CONCEPT_LABEL_ID_DICT)
CONCEPT_LABEL_ID_DICT.update(PERIPHERAL_CONCEPT_LABEL_ID_DICT)

CORE_CONCEPT_ID_LABEL_DICT = {v: k for k, v in CORE_CONCEPT_LABEL_ID_DICT.items()}
PERIPHERAL_CONCEPT_ID_LABEL_DICT = {v: k for k, v in PERIPHERAL_CONCEPT_LABEL_ID_DICT.items()}
CONCEPT_ID_LABEL_DICT = {v: k for k, v in CONCEPT_LABEL_ID_DICT.items()}


RELATION_LABEL_ID_DICT = {
	HAS_GO: HAS_GO_ID,
	PART_OF: PART_OF_ID,
	HAS_PART: HAS_PART_ID,
	GENETIC_ASSOCIATION: GENETIC_ASSOCIATION_ID,
	ENCODES: ENCODES_ID,
	ENCODED_BY: ENCODED_BY_ID,
	INFLUENCED_BY: INFLUENCED_BY_ID,
	RELATED_MOLECULAR_FUNCTION: RELATED_MOLECULAR_FUNCTION_ID,
	RELATED_BIOLOGICAL_PROCESS: RELATED_BIOLOGICAL_PROCESS_ID,
	IN_CHROMOSOME: IN_CHROMOSOME_ID,
	STRAND_ORIENTATION: STRAND_ORIENTATION_ID,
	GENETIC_ASSOCIATION: GENETIC_ASSOCIATION_ID,
	DRUG_USED_FOR_TREATMENT: DRUG_USED_FOR_TREATMENT_ID,
	HAS_CAUSE: HAS_CAUSE_ID,
	HEALTH_SPECIALTY: HEALTH_SPECIALTY_ID,
	HAS_ICD10: HAS_ICD10_ID,
	SUBCLASS: SUBCLASS_ID,
	HAS_ACTIVE_INGREDIENT: HAS_ACTIVE_INGREDIENT_ID,
	ACTIVE_INGREDIENT_IN: ACTIVE_INGREDIENT_IN_ID,
	MEDICAL_CONDITION_TREATED: MEDICAL_CONDITION_TREATED_ID,
	ACTIVATOR_OF: ACTIVATOR_OF_ID,
	PHYSICALLY_INTERACTS_WITH: PHYSICALLY_INTERACTS_WITH_ID,
	SIGNIFICANT_DRUG_INTERACTION: SIGNIFICANT_DRUG_INTERACTION_ID,
	SUBJECT_HAS_ROLE: SUBJECT_HAS_ROLE_ID,
}

RELATION_ID_LABEL_DICT = {v: k for k, v in RELATION_LABEL_ID_DICT.items()}

TAXON, NO_TAXON, WILDCARD = (query_template_taxon, query_template_no_taxon, query_template_wildcard)

EDGES_DICT = {
	(GENE, DISEASE): (GENETIC_ASSOCIATION, TAXON),
	#(GENE, DISEASE): (GENE_SUBSTITUTION_ASSOCIATION_WITH, TAXON),
	(GENE, PROTEIN): (ENCODES, TAXON),
	(GENE, CHROMOSOME): (IN_CHROMOSOME, TAXON),
	#(GENE, STRAND): (STRAND_ORIENTATION, TAXON),

	(SYMPTOM, CAUSE): (HAS_CAUSE, NO_TAXON),
	(SYMPTOM, DRUG): (DRUG_USED_FOR_TREATMENT, NO_TAXON),
	(SYMPTOM, ICD10): (HAS_ICD10, NO_TAXON),
	(SYMPTOM, HEALTH_SPECIALTY): (HEALTH_SPECIALTY, NO_TAXON),

	(PROTEIN, GENE): (ENCODED_BY, TAXON),
	(PROTEIN, MOLECULAR_FUNCTION): (RELATED_MOLECULAR_FUNCTION, TAXON),
	(PROTEIN, BIOLOGICAL_PROCESS): (RELATED_BIOLOGICAL_PROCESS, TAXON),
	(PROTEIN, PROTEIN_FAMILY): (PART_OF, TAXON),
	# (PROTEIN, PROTEIN_SUPERFAMILY): (PART_OF, TAXON),  # TODO: can SPARQL differentiate between family and superfamily?
	(PROTEIN, PROTEIN_DOMAIN): (HAS_PART, TAXON),

	(MOLECULAR_FUNCTION, GO): (HAS_GO, NO_TAXON),
	(MOLECULAR_FUNCTION, BIOLOGICAL_PROCESS): (PART_OF, NO_TAXON),

	(DRUG, PROTEIN): (INFLUENCED_BY, WILDCARD),
	(DRUG, GENE): (ACTIVATOR_OF, WILDCARD),
	(DRUG, DISEASE): (MEDICAL_CONDITION_TREATED, WILDCARD),
	(DRUG, DRUG_FUNCTION): (SUBJECT_HAS_ROLE, WILDCARD),
	(DRUG, PHARMACEUTICAL_PRODUCT): (ACTIVE_INGREDIENT_IN, WILDCARD)
}

# Nearest Neighbors
NN_ALGORITHMS = ['cosine_similarity', 'ball_tree', 'kd_tree', 'brute', 'auto']