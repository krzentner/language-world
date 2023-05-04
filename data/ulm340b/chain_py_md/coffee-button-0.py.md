

and continue it. If you are finished with an implementation, you can click the check button to check if your program is correct.
"""
[eod] [code]from tkinter import ttk, messagebox


class Table():
    def __init__(self, root):
        self.root = root

        # Creating table header
        self._table_header = ttk.Frame(root, padding=10)

        self._table_columns_name = ["Item", "Cost", "Quantity"]
        self._table_columns_width = [100, 100, 100]

        for i in range(len(self._table_columns_name)):
            ttk.Label(self._table_header, text=self._table_columns_name[i]).grid(row=1, column=i, sticky=tk.W)

        ttk.Separator(self._table_header, orient=tk.HORIZONTAL).grid(row=0, column=0, columnspan=len(self._table_columns_name), sticky=tk.EW)
        ttk.Separator(self._table_header, orient=tk.HORIZONTAL).grid(row=2, column=0, columnspan=len(self._table_columns_name), sticky=tk.EW)

        ttk.Label(self._table_header, text="Total Cost: 0").grid(row=3, column=0, columnspan=len(self._table_columns_name), sticky=tk.E)

        # Creating table footer
        self._table_footer = ttk.Frame(root)

        self._clear_all_button = ttk.Button(self._table_footer, text="Clear All", command=self.clear_all_items)
        self._clear_all_button.grid(row=0, column=0, sticky=tk.W + tk.N)
        self._calculate_total_button = ttk.Button(self._table_footer, text="Calculate", command=self.calculate_total_price)
        self._calculate_total_button.grid(row=0, column=1, sticky=tk.E + tk.N)

        ttk.Separator(self._table_footer, orient=tk.HORIZONTAL).grid(row=1, column=0, columnspan=len(self._table_columns_name), sticky=tk.EW)

        self._table_columns = {}
        for i in range(len(self._table_columns_name)):
            