import os
import pandas as pd
import matplotlib.pyplot as plt

# Create results directory if it doesn't exist
os.makedirs("results", exist_ok=True)

excel_file = "data/x2L.xlsx" #change file name for other excel sheets

# Get all sheet names
xls = pd.ExcelFile(excel_file)

for sheet_name in xls.sheet_names:

    print(f"\nLoading sheet: {sheet_name}")

    try:
        df = pd.read_excel(
            excel_file,
            sheet_name=sheet_name,
            header=None
        )

        print("Original shape:", df.shape)

        # Skip empty sheets
        if df.empty:
            print("Sheet is empty. Skipping.")
            continue

        # Need at least 2 columns for Zimag and Zreal
        if df.shape[1] < 2:
            print("Not enough columns. Skipping.")
            continue

        # Remove title and units rows
        df = df.iloc[2:, :]

        print("Data shape:", df.shape)

        # First impedance pair
        zreal = pd.to_numeric(
            df.iloc[:, 0],
            errors="coerce"
        )

        zimag = pd.to_numeric(
            df.iloc[:, 1],
            errors="coerce"
        )

        # Remove NaNs
        mask = (
            zreal.notna()
            & zimag.notna()
        )

        zreal = zreal[mask]
        zimag = zimag[mask]

        # Skip if no valid data
        if len(zreal) == 0:
            print("No valid impedance data. Skipping.")
            continue

        plt.figure(figsize=(6, 5))

        plt.plot(
            zreal,
            zimag,
            'o-',
            linewidth=1
        )

        plt.xlabel("Z' (Ω)")
        plt.ylabel("-Z'' (Ω)")
        plt.title(f"Nyquist Plot - {sheet_name}")
        plt.grid(True)

        # Uncomment if you want mirrored orientation
        # plt.gca().invert_xaxis()

        safe_name = str(sheet_name).replace("/", "_")

        plt.savefig(
            f"results/{safe_name}.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        print(f"Saved: results/{safe_name}.png")

    except Exception as e:
        print(f"Error processing {sheet_name}:")
        print(e)

print("\nFinished processing.")
~
