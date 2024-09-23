import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Simulation functions
def simulate_market_share(price_A, price_B, elasticity):
    attractiveness_A = 1 / (price_A ** elasticity)
    attractiveness_B = 1 / (price_B ** elasticity)
    total_attractiveness = attractiveness_A + attractiveness_B
    market_share_A = attractiveness_A / total_attractiveness
    market_share_B = attractiveness_B / total_attractiveness
    return market_share_A, market_share_B

def calculate_profit(market_share, price, cost_per_litre, total_customers):
    sales = total_customers * market_share
    revenue = sales * price
    cost = sales * cost_per_litre
    profit = revenue - cost
    return profit

# GUI application
class MarketSimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gas Station Market Simulation")

        # Initial Parameters
        self.price_A = tk.DoubleVar(value=1.50)
        self.price_B = tk.DoubleVar(value=1.50)
        self.elasticity = tk.DoubleVar(value=1.5)
        self.total_customers = tk.IntVar(value=1000)
        self.price_drop_A = tk.DoubleVar(value=0.10)  # Price drop for Station A
        self.slight_discount_B = tk.DoubleVar(value=0.05)  # Slight discount for Station B
        self.cost_A = tk.DoubleVar(value=1.20)  # Cost per litre for Station A
        self.cost_B = tk.DoubleVar(value=1.20)  # Cost per litre for Station B

        # Create input fields and labels
        self.create_widgets()

        # Create Text widget for results display
        self.results_text = tk.Text(self.root, wrap='none', height=10, width=80)
        self.results_text.grid(column=0, row=9, columnspan=2, padx=5, pady=5)

        # Create a placeholder for the plot
        self.figure, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.canvas.get_tk_widget().grid(column=2, row=0, rowspan=10, padx=5, pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)


    def create_widgets(self):
        # Price of Station A
        ttk.Label(self.root, text="Initial Price of Station A:").grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.price_A).grid(column=1, row=0, padx=5, pady=5)

        # Price of Station B
        ttk.Label(self.root, text="Initial Price of Station B:").grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.price_B).grid(column=1, row=1, padx=5, pady=5)

        # Price Elasticity
        ttk.Label(self.root, text="Price Elasticity:").grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.elasticity).grid(column=1, row=2, padx=5, pady=5)

        # Total Customers
        ttk.Label(self.root, text="Total Customers:").grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.total_customers).grid(column=1, row=3, padx=5, pady=5)

        # Price Drop for Station A
        ttk.Label(self.root, text="Price Drop for Station A:").grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.price_drop_A).grid(column=1, row=4, padx=5, pady=5)

        # Slight Discount for Station B
        ttk.Label(self.root, text="Slight Discount for Station B:").grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.slight_discount_B).grid(column=1, row=5, padx=5, pady=5)

        # Cost per litre for Station A
        ttk.Label(self.root, text="Cost per litre for Station A:").grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.cost_A).grid(column=1, row=6, padx=5, pady=5)

        # Cost per litre for Station B
        ttk.Label(self.root, text="Cost per litre for Station B:").grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.cost_B).grid(column=1, row=7, padx=5, pady=5)

        # Run Simulation Button
        ttk.Button(self.root, text="Run Simulation", command=self.run_simulation).grid(column=0, row=8, columnspan=2, padx=5, pady=5)

    def run_simulation(self):
        # Get values from input fields
        price_A = self.price_A.get()
        price_B = self.price_B.get()
        elasticity = self.elasticity.get()
        total_customers = self.total_customers.get()
        price_drop_A = self.price_drop_A.get()
        slight_discount_B = self.slight_discount_B.get()
        cost_A = self.cost_A.get()
        cost_B = self.cost_B.get()

        # Strategy Scenarios for Station B
        strategies = {
            "Maintain Price": price_B,
            "Match Price Drop": price_A - price_drop_A,
            "Slight Discount": price_B - slight_discount_B
        }

        results = []
        for strategy, new_price_B in strategies.items():
            market_share_A, market_share_B = simulate_market_share(price_A - price_drop_A, new_price_B, elasticity)
            profit_A = calculate_profit(market_share_A, price_A - price_drop_A, cost_A, total_customers)
            profit_B = calculate_profit(market_share_B, new_price_B, cost_B, total_customers)
            results.append({
                "Strategy": strategy,
                "Price_B": new_price_B,
                "Market Share A": market_share_A,
                "Market Share B": market_share_B,
                "Profit A": profit_A,
                "Profit B": profit_B
            })

        # Convert results to DataFrame
        results_df = pd.DataFrame(results)
        self.display_results(results_df)

    def display_results(self, results_df):
        # Clear the previous results
        self.results_text.delete(1.0, tk.END)
        
        # Display the new results in the Text widget
        self.results_text.insert(tk.END, results_df.to_string(index=False))

        # Update the plot with new data
        self.update_plot(results_df)

    def update_plot(self, results_df):
        # Clear the previous plot
        self.ax.clear()

        # Plotting profits for each strategy
        for strategy in results_df['Strategy']:
            strategy_data = results_df[results_df["Strategy"] == strategy]
            self.ax.bar(strategy_data["Strategy"], strategy_data["Profit B"], label=f"{strategy} - Profit B")

        self.ax.set_xlabel('Strategy of Station B')
        self.ax.set_ylabel('Profit')
        self.ax.set_title('Profit of Station B for Different Strategies')
        self.ax.legend()

        # Refresh the canvas
        self.canvas.draw()
        
    def on_closing(self):
        """Handle window close event"""
        self.root.destroy()  # Destroy the window to release resources
        self.root.quit()  # Stop the main loop
        


# Create the main window
root = tk.Tk()
app = MarketSimulationApp(root)
root.mainloop()