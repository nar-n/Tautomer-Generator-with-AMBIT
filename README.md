# __Tautomer Generator__

This script automates the generation of tautomers from a CSV file containing SMILES and MoleculeID columns. It utilises the open-source Java library "ambit-tautomers-2.0.0-SNAPSHOT" for tautomer generation.

## __Prerequisites__

Before running this code, ensure you have the following dependencies installed:

1. Java Development Kit (JDK): Ensure you have Java installed on your system.
2. ambit-tautomers-2.0.0-SNAPSHOT.jar: Download the JAR file from the provided link.
3. Pandas
4. RDKit
   
## __Prepare Input__: 
1. Place your input CSV file containing SMILES and MoleculeID. Ensure the CSV file follows the specified format.
2. Download the ambit-tautomers-2.0.0-SNAPSHOT.jar from the provided link (https://sourceforge.net/projects/ambit/files/Ambit2/AMBIT%20applications/tautomers/ambit-tautomers-2.0.0-SNAPSHOT.jar) and ensure you have Java installed on your system.

### __Please note that:__
1. CSV and JAR files location: Ensure both the input CSV file and the ambit-tautomers-2.0.0-SNAPSHOT.jar file are in the same folder as the python script file.
2. Input csv file name: Specify the input csv file name in the script.
3. Tautomers Option: Choose between generating 'all' tautomers or selecting the 'best' tautomer for each molecule based on your requirements.

## __The script generates__ 
1. Tautomers for each molecule in the input CSV file. The tautomers will be saved in the same directory as the input CSV file, as separate SDF files.
2. Additionally, a CSV file named tautomers_output.csv will be generated, summarising the tautomers.
