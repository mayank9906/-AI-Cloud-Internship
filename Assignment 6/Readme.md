# Cricket Stats Calculator

## Objective

Analyze cricket player statistics from a JSON dataset using Python and calculate important batting performance metrics.

---

## Dataset

**Dataset Used:** `players.json`

The dataset contains player information such as:

- Player Name
- Matches
- Runs
- Balls Faced
- Outs
- Batting Conditions

---

## Operations Performed

- Read player data from a JSON file
- Calculate Batting Strike Rate
- Calculate Batting Average
- Determine the player's best playing condition
- Identify the most frequent dismissal type
- Display calculated statistics

---

## Performance Metrics

### Strike Rate

Measures how quickly a batsman scores runs.

**Formula**

Strike Rate = (Runs / Balls Faced) × 100

---

### Batting Average

Measures the average number of runs scored before getting out.

**Formula**

Batting Average = Runs / Outs

---

### Better Playing Conditions

Determines whether the player performs better in different match conditions based on the available dataset.

Examples:

- Home
- Away
- Day Match
- Night Match

---

### Frequent Dismissals

Analyzes the dismissal records to determine the most common way a player gets dismissed.

Examples:

- Bowled
- Caught
- LBW
- Run Out
- Stumped

---

## Technologies Used

- Python 3
- JSON
- Basic Mathematics

---

## Files Included

- cricket_stats.py
- players.json
- README.md
- Output.png

---

## Requirements

No external libraries are required.

---

## How to Run

Open Command Prompt in the project folder and execute:

```bash
py -3.14 cricket_stats.py
```

---

## Expected Output

The program displays:

- Player Name
- Strike Rate
- Batting Average
- Best Playing Condition
- Frequent Dismissal Type

---

## Learning Outcomes

- Reading JSON data in Python
- Processing structured datasets
- Performing mathematical calculations
- Working with dictionaries and lists
- Analyzing sports statistics using Python

---

## Author

**Mayank Makhija**  
Step Ahead Internship
