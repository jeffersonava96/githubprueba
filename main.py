import sys
import tkinter as tk


def calc(op, a, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return None if b == 0 else a / b
    return None


def console():
    print("Calculadora aritmética: + - * /")
    while True:
        op = input("Operación (q para salir): ").strip()
        if op in ("q", "salir", "exit"):
            break
        if op not in "+-*/":
            print("Operación inválida. Usa +, -, *, /")
            continue
        try:
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
        except ValueError:
            print("Número inválido. Intenta de nuevo.")
            continue
        res = calc(op, a, b)
        if res is None:
            print("Error: división por cero o operación inválida.")
            continue
        print(f"Resultado: {res}")
    print("Adiós.")


def gui():
    root = tk.Tk()
    root.title("Calculadora")

    entry = tk.Entry(root, width=20, font=("Arial", 18), justify="right")
    entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    def press(value):
        entry.insert(tk.END, value)

    def clear():
        entry.delete(0, tk.END)

    def equals():
        expr = entry.get()
        if not set(expr) <= set("0123456789.+-*/"):
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
            return
        try:
            res = eval(expr)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
            return
        entry.delete(0, tk.END)
        entry.insert(0, str(res))

    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ]

    for (text, row, col) in buttons:
        action = equals if text == "=" else clear if text == "C" else lambda t=text: press(t)
        tk.Button(root, text=text, width=5, height=2, command=action).grid(row=row, column=col, padx=2, pady=2)

    tk.Button(root, text="C", width=5, height=2, command=clear).grid(row=5, column=0, columnspan=4, sticky="we", padx=2, pady=2)
    root.mainloop()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "gui":
        gui()
    else:
        console()
