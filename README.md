__Tautomer Generator__

This script automates the generation of tautomers from a CSV file containing SMILES and molecule IDs. It utilises the open-source Java library "ambit-tautomers-2.0.0-SNAPSHOT" for tautomer generation.

Prerequisites
Before running this code, ensure you have the following dependencies installed:

1. Java Development Kit (JDK): Ensure you have Java installed on your system.
2. ambit-tautomers-2.0.0-SNAPSHOT.jar: Download the JAR file from the provided link.
3. Pandas
4. RDKit
   
Prepare Input: Place your input CSV file containing SMILES and MoleculeID. Ensure the CSV file follows the specified format.
Download the ambit-tautomers-2.0.0-SNAPSHOT.jar from the provided link (https://sourceforge.net/projects/ambit/files/Ambit2/AMBIT%20applications/tautomers/ambit-tautomers-2.0.0-SNAPSHOT.jar) and ensure you have Java installed on your system.

Ensure you have a CSV file containing SMILES and MoleculeID columns.
Download the ambit-tautomers-2.0.0-SNAPSHOT.jar file from the provided link .

Please note that:
1. CSV and JAR Location: Ensure both the input CSV file and the ambit-tautomers-2.0.0-SNAPSHOT.jar file are in the same folder as the tautomer_generator.py script.
2. Input csv file name: Specify the input csv file name in the script.
3. Chunk Size: The script processes molecules in chunks to manage memory usage. You can adjust the chunk size based on your system's capabilities and the size of your input data.
4. Tautomers Option: Choose between generating 'all' tautomers or selecting the 'best' tautomer for each molecule based on your requirements.

The script will generate tautomers for each molecule in the input CSV file. The tautomers will be saved in the same directory as the input CSV file, as separate SDF files. Additionally, a CSV file named tautomers_output.csv will be generated, summarizing the tautomers.
