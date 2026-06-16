import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    "data/x2L.xlsx",
    sheet_name=0, #change sheet_name number for different charges
    header=None
)

# Skip the title and units rows
df = df.iloc[2:]

zimag = pd.to_numeric(df[0], errors="coerce")
zreal = pd.to_numeric(df[1], errors="coerce")

plt.xlabel("Z' (Ω)")
plt.ylabel("-Z'' (Ω)")
plt.title("x2L Nyquist Plot")
plt.grid(True)

plt.plot(zimag,zreal)
plt.grid(True)

plt.savefig("x2L_nyquist.png", dpi=300)#rename based on which sheet you're looking at

print("Plot saved!")
