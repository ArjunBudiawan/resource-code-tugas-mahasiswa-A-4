nilaiBarangNim4digit = {"B001": 10, "B002": 5}

nilaiBarangNim4digit["B003"] = 8
nilaiBarangNim4digit["B002"] = 7
terhapusNim4digit = nilaiBarangNim4digit.pop("B001")

print("Dictionary akhir:", nilaiBarangNim4digit)
print("Value yang dikembalikan pop():", terhapusNim4digit)