# 🔷 Hasse Diagram Visualizer

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)

A Python tool to visualize the **Hasse diagram** of a partially ordered set (poset). This tool performs a transitive reduction, checks for structural validity, and draws a clean, level-based diagram using `networkx` and `matplotlib`.

---

## 📚 What Is a Hasse Diagram?

A **Hasse diagram** is a simplified drawing of a partially ordered set (poset), where:

- Only the **essential order relations** are shown (i.e., transitive and reflexive relations are omitted).
- Edges are drawn **upward** to represent the partial order.
- The diagram is **layered**, showing elements by level of dependency.

---

## 📂 Project structure

```bash
hasse-diagram/
│
├── LICENSE             # License
├── README.md           # Documentation
├── hasse.py            # Main module with all functionality
├── example.py          # Example script to test the library
├── images/
│   └── example_diagram.png  # Output example
```

---

## ✨ Features

- Automatically performs **transitive reduction** to eliminate redundant relations  
- Validates that the input is a **valid poset** according to the definition
- Dynamically adjusts **node size** and **layout** based on input size  
- Supports **custom node colors** (classic colors like `red`, `green`, `blue`, etc.)  
- Clean, level-based layout using `matplotlib` and `networkx`

---

## 📦 Installation

Make sure you have Python 3.7+ installed. Then install the required packages:

```bash
pip install matplotlib networkx
```

---

## 🛠️ Usage

Import the package

```bash
from hasse import display_hasse_diagram
```

Define your poset (reflexive pairs are optional)

```bash
poset = [
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 10), (1, 12), (1, 15), (1, 20), (1, 30), (1, 60),
    (2, 2), (2, 4), (2, 6), (2, 10), (2, 12), (2, 20), (2, 30), (2, 60),
    (3, 3), (3, 6), (3, 12), (3, 15), (3, 30), (3, 60),
    (4, 4), (4, 12), (4, 20), (4, 60),
    (5, 5), (5, 10), (5, 15), (5, 20), (5, 30), (5, 60),
    (6, 6), (6, 12), (6, 30), (6, 60),
    (10, 10), (10, 20), (10, 30), (10, 60),
    (12, 12), (12, 60),
    (15, 15), (15, 30), (15, 60),
    (20, 20), (20, 60),
    (30, 30), (30, 60),
    (60, 60)
]
```

Set a title and node color, then display the diagram

```bash
display_hasse_diagram(poset, title="My Poset", node_color="skyblue")
```

Example diagram

![Example Hasse Diagram](images/example_diagram.png)

---

## 📄 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this software with proper attribution.

---

## 🤝 Contributions

Contributions are welcome!

If you have ideas for improvement, bug reports, or would like to add new features:

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

Please ensure your code is clean, documented, and tested. Thank you!