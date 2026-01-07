<h1 align="center">WGUPS Routing: A Study in Greedy Heuristics</h1>

<p align="center">
  An exploration of the Traveling Salesman Problem (TSP) through custom data structures and algorithmic optimization.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB" />
  <img src="https://img.shields.io/badge/Algorithm-Nearest_Neighbor-red" />
  <img src="https://img.shields.io/badge/Data_Structure-Custom_Hash_Map-orange" />
  <img src="https://img.shields.io/badge/Academic-WGU_C950-blue" />
</p>

**DeliveryRouter** serves as a technical demonstration of solving complex logistical constraints without the use of high-level library abstractions. By implementing a custom Hash Table and a Greedy heuristic, this project explores the balance between **computational complexity** and **operational efficiency** in a simulated environment.

<br />

## 🧠 Academic Objectives

The goal of this implementation was to satisfy several high-level data structure and algorithm requirements:
- **Optimization**: Deliver all packages within a 140-mile limit for a three-truck fleet.
- **Self-Sufficiency**: Avoid Python’s built-in `dict` to demonstrate an understanding of hash functions and collision resolution.
- **Deterministic State**: Provide a point-in-time status for any package, requiring a simulation engine that accounts for speed, distance, and time.

<br />

## 🚀 Algorithmic Analysis (Nearest Neighbor)

The core routing logic utilizes the **Nearest Neighbor** heuristic. At each delivery point, the algorithm performs a local search to find the mathematically closest address for the next delivery.


### Computational Complexity
- **Time Complexity**: $O(n^2)$ due to the nested iteration where each package ($n$) is compared against all remaining packages ($n$) to find the minimum distance.
- **Space Complexity**: $O(n)$ to maintain the package state and truck queues.

### The "Greedy" Trade-off
While Nearest Neighbor is computationally inexpensive and easy to implement, it is a **Greedy Algorithm**, meaning it makes the best local choice at each step. This can sometimes lead to sub-optimal global routes, but for the scope of a 40-package dataset, it successfully achieves the mileage target.

<br />


## 🏗️ Data Structure: Custom Chaining Hash Table

A central requirement was the manual creation of a Hash Table to manage package data.

- **Hashing Logic**: Uses a simple modulo operator on the package ID to determine bucket placement: `hash(key) % len(self.table)`.
- **Collision Resolution**: Utilizes **Chaining** via Python lists. This prevents data overwriting when multiple IDs map to the same index.
- **Access Time**: Achieves **$O(1)$ average-case lookup** time, allowing the simulation to query package details (like delivery time and current status) instantly.

<br />

## 📊 Performance Metrics

The simulation successfully satisfies all operational parameters:
- **Total Miles**: Delivered 40 packages in ~102 miles (well under the 140-mile limit).
- **Efficiency**: All packages met their specific delivery deadlines (e.g., 9:00 AM, 10:30 AM).
- **Data Integrity**: Handled "Package 9" dynamic address update at 10:20 AM without interrupting the simulation flow.

<br />

## 🚦 Getting Started

### Installation
```bash
git clone https://github.com/ronbodnar/deliveryrouter-cli.git
cd deliveryrouter-cli
```

### Execution
```bash
# Run the main simulation and CLI reporting tool
python main.py
```

<br />

## 📫 Connect
**Ronald Bodnar**
- Student ID: 011194327
- LinkedIn: [linkedin.com/in/ronbodnar](https://linkedin.com/in/ronbodnar)
- Portfolio: [ronbodnar.com](https://ronbodnar.com)

<br />

## ⚖️ License
MIT License. Created for WGU C950.
