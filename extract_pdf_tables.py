import tabula.io as tabula
import pandas as pd
import sys

def extract_tables(file_path, excel_file_path):
    # Extract tables from all pages
    df_list = tabula.read_pdf(file_path, pages='all', multiple_tables=True)

    # Check if the df_list is not empty
    if df_list:
        # Write each DataFrame to a separate sheet in the Excel file
        with pd.ExcelWriter(excel_file_path) as writer:
            for idx, df in enumerate(df_list, start=1):
                # Ensure df is not empty
                if not df.empty:
                    df.to_excel(writer, sheet_name=f'Sheet{idx}', index=False)
        print(f"Tables have been successfully saved to {excel_file_path}")
    else:
        print("No tables found in the PDF.")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python extract_pdf_tables.py <input_pdf_path> <output_excel_path>")
    else:
        input_pdf_path = sys.argv[1]
        output_excel_path = sys.argv[2]
        extract_tables(input_pdf_path, output_excel_path)
