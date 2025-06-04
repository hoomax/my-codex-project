# -*- coding: utf-8 -*-
"""Simple CryptoManager application in Farsi.

This is a minimal Tkinter based application for managing
cryptocurrency transactions. The UI is in Persian and designed
for right-to-left layout.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class CryptoManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("مدیریت دارایی های ارز دیجیتال")
        self.geometry("600x400")

        # Apply a default font (use installed Farsi font if available)
        default_font = ("Vazir", 10)
        self.option_add("*Font", default_font)

        self.create_widgets()
        self.transactions = []

    def create_widgets(self):
        # Menu
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        trans_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="ثبت تراکنش ها", menu=trans_menu)
        trans_menu.add_command(label="تراکنش جدید", command=self.show_form)

        menubar.add_command(label="مجموع هر ارز", command=self.show_totals)

        report_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="گزارشات", menu=report_menu)
        report_menu.add_command(label="لیست تراکنش ها", command=self.show_report)

        self.frame = ttk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.show_form()

    def show_form(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Currency type
        ttk.Label(self.frame, text="نوع ارز دیجیتال:").grid(row=0, column=1, sticky=tk.E, pady=5, padx=5)
        self.currency_var = tk.StringVar()
        currency_list = ["BTC", "ETH", "USDT"]
        ttk.Combobox(self.frame, textvariable=self.currency_var, values=currency_list, width=20).grid(row=0, column=0, pady=5, padx=5)

        # Date
        ttk.Label(self.frame, text="تاریخ تراکنش (YYYY/MM/DD):").grid(row=1, column=1, sticky=tk.E, pady=5, padx=5)
        self.date_var = tk.StringVar()
        ttk.Entry(self.frame, textvariable=self.date_var).grid(row=1, column=0, pady=5, padx=5)

        # Amount
        ttk.Label(self.frame, text="مقدار ارز:").grid(row=2, column=1, sticky=tk.E, pady=5, padx=5)
        self.amount_var = tk.DoubleVar()
        ttk.Entry(self.frame, textvariable=self.amount_var).grid(row=2, column=0, pady=5, padx=5)

        # Unit price (Toman)
        ttk.Label(self.frame, text="قیمت واحد (تومان):").grid(row=3, column=1, sticky=tk.E, pady=5, padx=5)
        self.unit_price_var = tk.DoubleVar()
        ttk.Entry(self.frame, textvariable=self.unit_price_var).grid(row=3, column=0, pady=5, padx=5)

        # Fee in currency
        ttk.Label(self.frame, text="کارمزد (واحد ارز):").grid(row=4, column=1, sticky=tk.E, pady=5, padx=5)
        self.fee_currency_var = tk.DoubleVar()
        ttk.Entry(self.frame, textvariable=self.fee_currency_var).grid(row=4, column=0, pady=5, padx=5)

        # Fee in Toman
        ttk.Label(self.frame, text="کارمزد (تومان):").grid(row=5, column=1, sticky=tk.E, pady=5, padx=5)
        self.fee_toman_var = tk.DoubleVar()
        ttk.Entry(self.frame, textvariable=self.fee_toman_var).grid(row=5, column=0, pady=5, padx=5)

        # Total in Toman
        ttk.Label(self.frame, text="مقدار کل (تومان):").grid(row=6, column=1, sticky=tk.E, pady=5, padx=5)
        self.total_toman_var = tk.DoubleVar()
        ttk.Entry(self.frame, textvariable=self.total_toman_var).grid(row=6, column=0, pady=5, padx=5)

        # Transaction type
        ttk.Label(self.frame, text="نوع تراکنش:").grid(row=7, column=1, sticky=tk.E, pady=5, padx=5)
        self.tx_type_var = tk.StringVar()
        ttk.Combobox(self.frame, textvariable=self.tx_type_var, values=["خرید", "فروش"], width=18).grid(row=7, column=0, pady=5, padx=5)

        # Net total after fee
        ttk.Label(self.frame, text="مقدار کل پس از کسر کارمزد:").grid(row=8, column=1, sticky=tk.E, pady=5, padx=5)
        self.net_total_var = tk.DoubleVar()
        ttk.Entry(self.frame, textvariable=self.net_total_var).grid(row=8, column=0, pady=5, padx=5)

        ttk.Button(self.frame, text="ثبت", command=self.save_transaction).grid(row=9, column=0, pady=20)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=0)

    def save_transaction(self):
        tx = {
            "currency": self.currency_var.get(),
            "date": self.date_var.get(),
            "amount": self.amount_var.get(),
            "unit_price": self.unit_price_var.get(),
            "fee_currency": self.fee_currency_var.get(),
            "fee_toman": self.fee_toman_var.get(),
            "total_toman": self.total_toman_var.get(),
            "type": self.tx_type_var.get(),
            "net_total": self.net_total_var.get(),
        }
        self.transactions.append(tx)
        messagebox.showinfo("ثبت شد", "تراکنش ذخیره شد")
        self.show_form()

    def show_report(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        cols = ("currency", "date", "amount", "unit_price", "fee_currency", "fee_toman", "total_toman", "type", "net_total")
        tree = ttk.Treeview(self.frame, columns=cols, show="headings")
        headings = [
            "ارز", "تاریخ", "مقدار", "قیمت واحد", "کارمزد ارز", "کارمزد تومان", "کل تومان", "نوع", "خالص"
        ]
        for col, head in zip(cols, headings):
            tree.heading(col, text=head)
        for tx in self.transactions:
            tree.insert("", tk.END, values=[tx[c] for c in cols])
        tree.pack(fill=tk.BOTH, expand=True)

    def show_totals(self):
        totals = {}
        for tx in self.transactions:
            totals.setdefault(tx["currency"], 0)
            totals[tx["currency"]] += tx["amount"]

        msg = "\n".join(f"{cur}: {amt}" for cur, amt in totals.items())
        messagebox.showinfo("مجموع هر ارز", msg or "هیچ تراکنشی ثبت نشده است")


if __name__ == "__main__":
    app = CryptoManager()
    app.mainloop()
