import os
import subprocess
import pandas as pd
from rdkit import Chem

def generate_tautomers(input_sdf, output_sdf, tautomers_option):
    # Generate tautomers for the input SDF file
    java_command = f"java -jar ambit-tautomers-2.0.0-SNAPSHOT.jar -f {input_sdf} -o {output_sdf} -t {tautomers_option}"
    subprocess.run(java_command, shell=True)

def process_molecules(csv_file, output_tautomers, tautomers_option, chunk_size):
    # Read the input CSV file
    data = pd.read_csv(csv_file)

    # Create output folder if it doesn't exist
    os.makedirs(output_tautomers, exist_ok=True)

    # Counter to track molecules processed
    mol_count = 0

    # List to store molecules in the current chunk
    chunk_molecules = []

    # Process each row in the CSV file
    for index, row in data.iterrows():
        smiles = row['SMILES']
        mol_id = row['MoleculeID']

        # Convert SMILES to RDKit molecule
        mol = Chem.MolFromSmiles(smiles)

        if mol is not None:
            # Add the molecule to the current chunk
            chunk_molecules.append((mol, mol_id))

            # Increment molecule count
            mol_count += 1

            # If the chunk size is reached or at the end of the file, process the current chunk
            if mol_count % chunk_size == 0 or index == len(data) - 1:
                # Create a temporary SDF file for the current chunk
                temp_sdf = os.path.join(output_tautomers, f"temp_{mol_count - 1}.sdf")  # Fix index
                writer = Chem.SDWriter(temp_sdf)
                for chunk_mol, chunk_mol_id in chunk_molecules:
                    # Write the RDKit molecule to the SDF file
                    writer.write(chunk_mol, confId=-1)
                writer.close()

                # Generate tautomers for the current chunk
                output_chunk_sdf = os.path.join(output_tautomers, f"output_{mol_count - 1}.sdf")  # Fix index
                generate_tautomers(temp_sdf, output_chunk_sdf, tautomers_option)

                # Clear the chunk for the next iteration
                chunk_molecules = []

    print(f"Tautomers generated successfully. Output folder: {output_tautomers}")

def create_tautomers_csv(output_tautomers, tautomers_option):
    # List all the SDF files in the output folder
    sdf_files = [f for f in os.listdir(output_tautomers) if f.startswith("output_") and f.endswith(".sdf")]

    # Create a list to store DataFrames
    dfs = []

    # Iterate through each SDF file and extract tautomers
    for sdf_file in sdf_files:
        input_sdf = os.path.join(output_tautomers, sdf_file)

        # Read the SDF file
        suppl = Chem.SDMolSupplier(input_sdf)

        # Extract information and append to the list of DataFrames
        df_list = []
        for index, mol in enumerate(suppl):
            if mol is not None:
                smiles = Chem.MolToSmiles(mol)
                mol_id = f"{sdf_file}_{index}"
                tautomer_info = mol.GetProp("_Name")

                # Split tautomer_info and handle if not enough values are present
                tautomer_info_parts = tautomer_info.split("\t")
                if len(tautomer_info_parts) == 3:
                    tautomer_smiles, tautomer_rank, tautomer_id = tautomer_info_parts
                else:
                    # Set default values if not enough values are present
                    tautomer_smiles, tautomer_rank, tautomer_id = "", "", ""

                df_list.append({
                    'SMILES': smiles,
                    'MoleculeID': mol_id,
                    'Tautomer_SMILES': tautomer_smiles,
                    'Tautomer_Rank': tautomer_rank,
                    'TautomerID': tautomer_id
                })

        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(df_list)
        dfs.append(df)

    # Concatenate all DataFrames in the list
    results_df = pd.concat(dfs, ignore_index=True)

    # Save the DataFrame to a CSV file
    output_csv = os.path.join(output_tautomers, 'tautomers_output.csv')
    results_df.to_csv(output_csv, index=False)

    print(f"Tautomers CSV file generated successfully: {output_csv}")

def main():
    # Replace 'your_input_file.csv' with your actual CSV file name
    csv_file = 'test.csv'
    tautomers_option = 'all'  # Specify 'all' or 'best' based on your requirements

    # Specify the output folder path
    output_tautomers = 'output_tautomers'

    # Specify the chunk size
    chunk_size = 1

    # Print information before processing the molecules
    print(f"Processing the CSV file: {csv_file}")

    # Call the function to process molecules
    process_molecules(csv_file, output_tautomers, tautomers_option, chunk_size)

    # Calculate tautomers for each molecule in the output folder
    create_tautomers_csv(output_tautomers, tautomers_option)

if __name__ == "__main__":
    main()
