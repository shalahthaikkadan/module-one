m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))
m4 = int(input("Enter marks for Subject 4: "))
m5 = int(input("Enter marks for Subject 5: "))

def total(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    average = total / 5
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average}")

try:
    total(m1, m2, m3, m4, m5)
except Exception:
    print("Invalid output")
finally:
    print("Marks processing completed.")
