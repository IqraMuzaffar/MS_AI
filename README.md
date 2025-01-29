# **Ai500 --Foundations of AI**

This repository contains a series of assignments that progressively build expertise in artificial intelligence and machine learning. These assignments cover foundational search algorithms, clustering, decision trees, neural networks, and advanced convolutional neural networks (CNNs) for applications like semantic segmentation and image similarity.

---

## **Table of Contents**
1. [Assignment 1: Search Algorithms](#assignment-1-search-algorithms)
2. [Assignment 2: Clustering and Decision Trees](#assignment-2-clustering-and-decision-trees)
3. [Assignment 3: Custom Neural Networks](#assignment-3-custom-neural-networks)
4. [Assignment 4: Convolutional Neural Networks (CNNs)](#assignment-4-convolutional-neural-networks-cnns)
5. [Manuals and Documentation](#manuals-and-documentation)
6. [How to Run the Code](#how-to-run-the-code)

---

## **Assignment 1: Search Algorithms**
**Directory:** `Search_Algorithms(Assignment-1)/PA1_24240026(Iqra)`

This assignment focuses on the implementation of classical search algorithms essential for solving pathfinding and game tree problems.

### **Implemented Algorithms:**
- **A\* Search Algorithm:**
  - A heuristic-based algorithm for finding the shortest path in a weighted grid.
  - Utilizes the **Manhattan Distance** as the heuristic.
- **Breadth-First Search (BFS):**
  - Explores nodes level by level in a grid.
  - Implements path tracking and maintains an explored path for visualization.
- **Depth-First Search (DFS):**
  - Explores paths deeply using a stack-based approach.
  - Includes detailed tracking of explored paths and visited nodes.
- **Minimax with Alpha-Beta Pruning:**
  - Implements decision-making in adversarial games (e.g., chess).
  - Optimizes game tree traversal by pruning unnecessary branches.

---

## **Assignment 2: Clustering and Decision Trees**
**Directory:** `Algorithms-Implementation(Assignment-2)/Assignment2/AS_2`

This assignment delves into clustering and tree-based classification algorithms.

### **Implemented Algorithms:**
- **DBSCAN (Density-Based Spatial Clustering of Applications with Noise):**
  - Clusters data points based on density.
  - Identifies and excludes outliers.
- **K-Means Clustering:**
  - Groups data into predefined clusters.
  - Visualizes clustering results for different datasets.
- **Decision Trees:**
  - A rule-based supervised learning algorithm for classification tasks.
  - Custom implementation with node-splitting and recursive traversal.

### **Key Features:**
- Visualization of clustering results.
- Evaluation metrics like silhouette scores and decision tree accuracy.

---

## **Assignment 3: Custom Neural Networks**
**Directory:** `Neural_network_custom(Assignment3)`

This assignment demonstrates the implementation of a **feed-forward neural network** from scratch, providing a strong understanding of forward and backward propagation.

### **Features:**
- **Network Architecture:**
  - Supports arbitrary layers and nodes, with fully customizable configurations.
- **Activation Functions:**
  - Implements `Sigmoid`, `ReLU`, and `Leaky ReLU`.
- **Loss Functions:**
  - `Cross-Entropy Loss` for classification tasks.
  - `Mean Squared Error (MSE)` for regression tasks.
- **Optimizers:**
  - Full-Batch Gradient Descent
  - Stochastic Gradient Descent (SGD)
  - Mini-Batch Gradient Descent
- **Flexible Training:**
  - Tracks training and validation loss over epochs.
  - Handles classification and regression experiments.

---

## **Assignment 4: Convolutional Neural Networks (CNNs)**
**Directory:** `Conv_neural_networks(Assignment-4)`

This assignment showcases the application of **CNNs** for advanced computer vision tasks.

### **Tasks:**
- **Semantic Segmentation:**
  - Classifies each pixel in an image into categories (e.g., water-body detection in satellite images).
  - Includes convolutional layers, pooling, and upsampling.
- **Image Similarity Finder:**
  - Extracts image features using CNNs and computes similarity scores.
  - Useful for content-based image retrieval.

### **Key Highlights:**
- Advanced use of CNNs for image processing.
- Integration of feature extraction and similarity metrics.

---

## **Manuals and Documentation**
Detailed manuals for each assignment are available in their respective directories, providing:
- Algorithm explanations.
- Code walkthroughs.
- Usage instructions and examples.

---

## **How to Run the Code**

### **Prerequisites:**
- Install the required Python libraries:
  ```bash
  pip install numpy matplotlib pandas scikit-learn tensorflow
