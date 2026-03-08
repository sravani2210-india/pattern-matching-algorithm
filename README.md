# Pattern Matching Algorithm in Python

This project demonstrates a simple pattern matching algorithm that searches for a substring inside a larger text.

## Problem Statement
The goal of this project is to detect whether a specific pattern exists within a given text and determine its starting index.

## Technologies Used
- Python

## Approach
The algorithm scans the text and compares each substring of the same length as the pattern.  
If a match is found, it reports the starting index of the pattern in the text.

## Example 1

Input  
Text: artificial intelligence  
Pattern: intelligence  

Output  
Pattern found at index: 11

## Example 2

Input  
Text: i love myself and proud of me  
Pattern: love  

Output  
Pattern found at index: 2

## How to Run the Program

Run the following command in the terminal:

python pattern_matching.py

## Future Improvements
- Implement the Knuth–Morris–Pratt (KMP) algorithm for efficient pattern matching
- Extend the system to support multiple pattern searches
